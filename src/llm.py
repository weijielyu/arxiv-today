"""Claude-backed scoring and summarization.

Scoring uses structured outputs (json_schema) so we get a validated, parseable
result. The stable rubric+profile lives in the system prompt with a cache
breakpoint, so repeated scoring calls in one run can hit the prompt cache.
"""
from __future__ import annotations

import asyncio
import json

from anthropic import AsyncAnthropic

from .config import settings
from .models import Paper
from .prompts import (
    SCORE_SCHEMA,
    SCORING_SYSTEM,
    SCORING_USER,
    SUMMARY_SYSTEM,
    SUMMARY_USER,
)

# Lazily constructed so importing this module doesn't require ANTHROPIC_API_KEY
# (needed only when scoring/summarizing actually runs).
_client_singleton: AsyncAnthropic | None = None


def _client() -> AsyncAnthropic:
    global _client_singleton
    if _client_singleton is None:
        _client_singleton = AsyncAnthropic()  # reads ANTHROPIC_API_KEY from env
    return _client_singleton

# System prompt for scoring is identical across all papers in a run -> cache it.
_SCORING_SYSTEM_BLOCKS = [
    {
        "type": "text",
        "text": SCORING_SYSTEM.format(profile=settings.user_profile),
        "cache_control": {"type": "ephemeral"},
    }
]
_SUMMARY_SYSTEM_BLOCKS = [
    {"type": "text", "text": SUMMARY_SYSTEM, "cache_control": {"type": "ephemeral"}}
]


async def score_paper(paper: Paper) -> None:
    """Score a paper in place from its title/abstract/authors."""
    user = SCORING_USER.format(
        title=paper.title,
        categories=", ".join(paper.categories),
        authors=paper.author_str(limit=12),
        abstract=paper.abstract,
    )
    try:
        resp = await _client().messages.create(
            model=settings.model,
            max_tokens=600,
            system=_SCORING_SYSTEM_BLOCKS,
            messages=[{"role": "user", "content": user}],
            output_config={"format": {"type": "json_schema", "schema": SCORE_SCHEMA}},
        )
        text = next(b.text for b in resp.content if b.type == "text")
        data = json.loads(text)
        paper.relevance = int(data.get("relevance", 0))
        paper.novelty = int(data.get("novelty", 0))
        paper.clarity = int(data.get("clarity", 0))
        paper.score = max(0, min(100, int(data.get("score", 0))))
        paper.risk_flags = list(data.get("risk_flags", []) or [])
        paper.reason = (data.get("one_line_reason") or "").strip()
    except Exception as exc:  # a single failure shouldn't sink the run
        paper.score = 0
        paper.reason = f"[scoring failed: {exc}]"


async def summarize_paper(paper: Paper, full_text: str) -> None:
    """Generate a structured markdown briefing for a top pick, in place."""
    user = SUMMARY_USER.format(
        title=paper.title,
        authors=paper.author_str(limit=12),
        arxiv_id=paper.id,
        full_text=full_text,
    )
    try:
        resp = await _client().messages.create(
            model=settings.model,
            max_tokens=2048,
            system=_SUMMARY_SYSTEM_BLOCKS,
            messages=[{"role": "user", "content": user}],
        )
        paper.summary = "".join(b.text for b in resp.content if b.type == "text").strip()
    except Exception as exc:
        paper.summary = f"_(summary generation failed: {exc})_"


async def score_all(papers: list[Paper]) -> None:
    """Score every paper, bounded by the configured concurrency."""
    sem = asyncio.Semaphore(settings.concurrency)

    async def _one(p: Paper) -> None:
        async with sem:
            await score_paper(p)

    await asyncio.gather(*(_one(p) for p in papers))


async def summarize_all(papers_with_text: list[tuple[Paper, str]]) -> None:
    sem = asyncio.Semaphore(settings.concurrency)

    async def _one(p: Paper, text: str) -> None:
        async with sem:
            await summarize_paper(p, text)

    await asyncio.gather(*(_one(p, t) for p, t in papers_with_text))
