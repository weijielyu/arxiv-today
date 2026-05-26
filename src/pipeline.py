"""End-to-end daily pipeline: fetch -> score -> summarize top picks -> report + notify."""
from __future__ import annotations

import asyncio
import datetime as _dt

from . import arxiv_client, llm, notifier, report
from .config import settings
from .models import Paper
from .pdf_service import fetch_full_text


def _dedupe(papers: list[Paper]) -> list[Paper]:
    seen: set[str] = set()
    out: list[Paper] = []
    for p in papers:
        if p.id not in seen:
            seen.add(p.id)
            out.append(p)
    return out


async def run() -> None:
    date = _dt.datetime.now(_dt.timezone.utc).strftime("%Y-%m-%d")
    print(f"arXiv-today — {date} (model: {settings.model})")

    # 1. Fetch today's new submissions across configured categories.
    papers: list[Paper] = []
    for category in settings.categories:
        fetched = arxiv_client.fetch_today(category, settings.max_results)
        print(f"  {category}: {len(fetched)} new submissions")
        papers.extend(fetched)
    papers = _dedupe(papers)
    total = len(papers)

    if total == 0:
        print("  No new submissions today (weekend/holiday). Nothing to do.")
        return

    # 2. Score every paper.
    print(f"  Scoring {total} papers (concurrency={settings.concurrency})...")
    await llm.score_all(papers)

    # 3. Filter + rank.
    kept = [p for p in papers if (p.score or 0) >= settings.score_threshold]
    kept.sort(key=lambda p: (p.score or 0), reverse=True)
    top_picks = [p for p in kept if (p.score or 0) >= settings.top_pick_min]
    if settings.max_top_picks > 0:  # 0 = no cap (quality-driven count)
        top_picks = top_picks[: settings.max_top_picks]
    print(f"  {len(kept)} kept (>= {settings.score_threshold}); {len(top_picks)} top picks")

    # 4. Deep-read + summarize top picks (full text, not just abstract).
    if top_picks:
        print("  Fetching full text + summarizing top picks...")
        loop = asyncio.get_running_loop()
        texts = await asyncio.gather(
            *(loop.run_in_executor(None, fetch_full_text, p) for p in top_picks)
        )
        await llm.summarize_all(list(zip(top_picks, texts)))

    # 5. Write the markdown report.
    path = report.write_report(date, total, kept, top_picks)
    print(f"  Wrote {path}")

    # 6. Notify Slack.
    notifier.notify(date, total, top_picks)
    print("  Done.")


def main() -> None:
    asyncio.run(run())


if __name__ == "__main__":
    main()
