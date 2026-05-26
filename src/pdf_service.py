"""Full-text extraction for top-pick papers.

Tries the arXiv HTML rendering first (clean, fast); falls back to the PDF via
pypdf; falls back to the abstract if neither is reachable.
"""
from __future__ import annotations

import html as _html
import io
import re

import httpx

from .models import Paper

_USER_AGENT = "arxiv-today/0.1 (https://github.com/weijielyu/arxiv-today)"
_DEFAULT_LIMIT = 200_000  # chars; keeps the summarization prompt within context


def _strip_html(raw: str) -> str:
    raw = re.sub(r"(?is)<script.*?</script>", " ", raw)
    raw = re.sub(r"(?is)<style.*?</style>", " ", raw)
    text = re.sub(r"(?s)<[^>]+>", " ", raw)
    text = _html.unescape(text)
    return re.sub(r"\s+", " ", text).strip()


def fetch_full_text(paper: Paper, limit: int = _DEFAULT_LIMIT) -> str:
    headers = {"User-Agent": _USER_AGENT}

    # 1. arXiv HTML rendering (not every paper has one).
    try:
        resp = httpx.get(paper.html_url, timeout=60, follow_redirects=True, headers=headers)
        if resp.status_code == 200 and "<html" in resp.text.lower():
            text = _strip_html(resp.text)
            if len(text) > 1000:
                return text[:limit]
    except Exception:
        pass

    # 2. PDF via pypdf.
    try:
        resp = httpx.get(paper.pdf_url, timeout=120, follow_redirects=True, headers=headers)
        if resp.status_code == 200 and resp.content:
            from pypdf import PdfReader

            reader = PdfReader(io.BytesIO(resp.content))
            text = "\n".join(page.extract_text() or "" for page in reader.pages)
            text = text.strip()
            if len(text) > 500:
                return text[:limit]
    except Exception:
        pass

    # 3. Give up — use the abstract.
    return paper.abstract
