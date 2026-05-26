"""Fetch today's new arXiv submissions and their metadata.

Two-step, mirroring the proven manual workflow:
  1. Scrape the category "recent" listing for the IDs of NEW submissions
     (cross-lists and replacements that follow are excluded).
  2. Pull clean metadata (title, abstract, authors) for those IDs from the
     arXiv Atom API in batches.
"""
from __future__ import annotations

import re
import time

import feedparser
import httpx

from .models import Paper

RECENT_URL = "https://arxiv.org/list/{cat}/recent?skip=0&show={n}"
API_URL = "https://export.arxiv.org/api/query"
_ID_RE = re.compile(r"/abs/(\d{4}\.\d{4,5})")
_CROSS_RE = re.compile(r"Cross[\s-]?(?:lists|submissions)", re.I)
_USER_AGENT = "arxiv-today/0.1 (https://github.com/weijielyu/arxiv-today)"


def fetch_new_submission_ids(category: str, n: int = 250) -> list[str]:
    """Return the arXiv IDs of NEW submissions on the category's recent page, in order."""
    url = RECENT_URL.format(cat=category, n=n)
    resp = httpx.get(url, timeout=30, follow_redirects=True, headers={"User-Agent": _USER_AGENT})
    resp.raise_for_status()
    html = resp.text

    # New submissions appear before the "Cross-lists" / "Cross submissions" heading.
    cut = _CROSS_RE.search(html)
    region = html[: cut.start()] if cut else html

    ids: list[str] = []
    seen: set[str] = set()
    for match in _ID_RE.finditer(region):
        pid = match.group(1)
        if pid not in seen:
            seen.add(pid)
            ids.append(pid)
    return ids


def _chunks(items: list[str], size: int):
    for i in range(0, len(items), size):
        yield items[i : i + size]


def fetch_metadata(ids: list[str], batch_size: int = 100) -> list[Paper]:
    """Fetch title/abstract/authors/categories for the given IDs via the arXiv API."""
    papers: list[Paper] = []
    for batch in _chunks(ids, batch_size):
        params = {"id_list": ",".join(batch), "max_results": str(len(batch))}
        resp = httpx.get(
            API_URL, params=params, timeout=60, headers={"User-Agent": _USER_AGENT}
        )
        resp.raise_for_status()
        feed = feedparser.parse(resp.text)
        for entry in feed.entries:
            raw_id = entry.id.split("/abs/")[-1]
            pid = re.sub(r"v\d+$", "", raw_id)
            papers.append(
                Paper(
                    id=pid,
                    title=re.sub(r"\s+", " ", entry.title).strip(),
                    abstract=re.sub(r"\s+", " ", entry.summary).strip(),
                    authors=[a.name for a in getattr(entry, "authors", [])],
                    categories=[t.term for t in getattr(entry, "tags", [])],
                )
            )
        time.sleep(0.5)  # be polite to the API between batches
    return papers


def fetch_today(category: str, n: int = 250) -> list[Paper]:
    ids = fetch_new_submission_ids(category, n)
    if not ids:
        return []
    return fetch_metadata(ids)
