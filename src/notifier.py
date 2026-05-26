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


def _extract_section(summary: str, heading: str) -> str:
    """Pull the text under a '## <heading>' section from a structured summary."""
    if not summary:
        return ""
    match = re.search(
        rf"##\s*{re.escape(heading)}\s*\n(.+?)(?:\n##\s|\Z)", summary, re.S | re.I
    )
    return match.group(1).strip() if match else ""


def extract_tldr(summary: str) -> str:
    tldr = _extract_section(summary, "TL;DR")
    if tldr:
        return re.sub(r"\s+", " ", tldr).strip()
    for line in summary.splitlines():  # fallback: first non-heading line
        if line.strip() and not line.strip().startswith("#"):
            return line.strip()
    return ""


def extract_contributions(summary: str, limit: int = 3) -> list[str]:
    """Return up to `limit` Key Contributions bullets, cleaned to one line each."""
    section = _extract_section(summary, "Key Contributions")
    bullets: list[str] = []
    for line in section.splitlines():
        line = line.strip()
        if line.startswith(("-", "*", "•")):
            text = re.sub(r"\s+", " ", line.lstrip("-*• ").strip())
            if text:
                bullets.append(text)
    return bullets[:limit]


def build_message(date: str, total: int, top_picks: list[Paper]) -> str:
    lines = [
        f"*:rolled_up_newspaper: arXiv CS.CV Daily — {date}*  ·  _{total} papers_",
        "",
        "*⭐ Top Picks*",
    ]
    for p in top_picks:
        lines.append(f"\n*{p.score}/100 · <{p.abs_url}|{p.title}>*")
        lines.append(f"_{p.author_str(limit=5)}_")
        tldr = extract_tldr(p.summary) or p.reason
        if tldr:
            lines.append(f"TL;DR: {tldr}")
        contribs = extract_contributions(p.summary)
        if contribs:
            lines.append("Key contributions:")
            lines.extend(f"• {c}" for c in contribs)
    lines.append(
        f"\n:page_facing_up: <{_REPORT_URL.format(date=date)}|Full report ({total} scanned)>"
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
