"""Slack notification of the day's top picks.

Posts a substantive digest (not just titles): each top pick carries its score,
authors, a link, and a TL;DR pulled from the structured summary.
"""
from __future__ import annotations

import json
import re
import urllib.request

from .config import settings
from .models import Paper

_REPORT_URL = "https://github.com/weijielyu/arxiv-today/blob/main/reports/daily/{date}.md"


def extract_tldr(summary: str) -> str:
    """Pull the text under the '## TL;DR' heading from a structured summary."""
    if not summary:
        return ""
    match = re.search(r"##\s*TL;DR\s*\n(.+?)(?:\n##\s|\Z)", summary, re.S | re.I)
    if not match:
        # Fall back to the first non-empty line.
        for line in summary.splitlines():
            if line.strip() and not line.strip().startswith("#"):
                return line.strip()
        return ""
    return re.sub(r"\s+", " ", match.group(1)).strip()


def build_message(date: str, total: int, top_picks: list[Paper]) -> str:
    lines = [
        f"*:rolled_up_newspaper: arXiv CS.CV Daily — {date}*  ·  _{total} new submissions_",
        "",
        "*⭐ Top Picks*",
    ]
    for p in top_picks:
        tldr = extract_tldr(p.summary) or p.reason
        lines.append(
            f"\n*{p.score}/100 · <{p.abs_url}|{p.title}>*  ({p.author_str(limit=4)})"
        )
        if tldr:
            lines.append(tldr)
    lines.append(
        f"\n:page_facing_up: Full report: <{_REPORT_URL.format(date=date)}|reports/daily/{date}.md>"
    )
    return "\n".join(lines)


def _post(webhook: str, text: str) -> bool:
    body = json.dumps({"text": text}).encode()
    req = urllib.request.Request(
        webhook, data=body, headers={"Content-Type": "application/json"}
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return resp.read().decode().strip() == "ok"
    except Exception as exc:
        print(f"  Slack post failed: {exc}")
        return False


def notify(date: str, total: int, top_picks: list[Paper]) -> None:
    if not settings.slack_webhooks:
        print("  No Slack webhooks configured; skipping notification.")
        return
    if not top_picks:
        print("  No top picks; skipping Slack notification.")
        return
    text = build_message(date, total, top_picks)
    for hook in settings.slack_webhooks:
        ok = _post(hook, text)
        print(f"  Slack post -> {'ok' if ok else 'FAILED'}")
