"""Write the daily markdown report to reports/daily/YYYY-MM-DD.md."""
from __future__ import annotations

from pathlib import Path

from .models import Paper

_REPORTS_DIR = Path(__file__).resolve().parent.parent / "reports" / "daily"


def _bold_score(score: int | None) -> str:
    return f"{score}/100" if score is not None else "—"


def build_report(date: str, total: int, kept: list[Paper], top_picks: list[Paper]) -> str:
    top_ids = {p.id for p in top_picks}
    lines: list[str] = [
        f"# arXiv CS.CV Daily Report — {date}",
        "",
        f"> **{total} new submissions** scanned. "
        f"{len(kept)} scored at or above threshold; {len(top_picks)} deep-summarized top picks.",
        "",
        "---",
        "",
        "## ⭐ Top Picks",
        "",
    ]

    for i, p in enumerate(top_picks, 1):
        lines += [
            f"### {i}. {p.title}",
            f"**Score:** {p.score}/100 · **arXiv:** [{p.id}]({p.abs_url})  ",
            f"**Authors:** {p.author_str(limit=10)}  ",
            "",
            p.summary or f"> {p.reason}",
            "",
            "---",
            "",
        ]

    # Everything else that cleared the threshold, as a scored table.
    rest = [p for p in kept if p.id not in top_ids]
    if rest:
        lines += [
            "## Other Relevant Papers",
            "",
            "| Score | Paper | arXiv | Why |",
            "|-------|-------|-------|-----|",
        ]
        for p in rest:
            title = p.title.replace("|", "\\|")
            reason = (p.reason or "").replace("|", "\\|")
            lines.append(
                f"| {_bold_score(p.score)} | {title} | [{p.id}]({p.abs_url}) | {reason} |"
            )
        lines.append("")

    lines += ["---", "", f"*Generated on {date} · {total} new cs.CV submissions scanned*", ""]
    return "\n".join(lines)


def write_report(date: str, total: int, kept: list[Paper], top_picks: list[Paper]) -> Path:
    _REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    path = _REPORTS_DIR / f"{date}.md"
    path.write_text(build_report(date, total, kept, top_picks))
    return path
