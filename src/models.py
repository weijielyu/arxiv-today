"""Data model for a single paper as it moves through the pipeline."""
from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Paper:
    id: str            # date-based arXiv id, e.g. "2605.22818" (no version suffix)
    title: str
    abstract: str
    authors: list[str] = field(default_factory=list)
    categories: list[str] = field(default_factory=list)

    # Filled in by the scoring pass.
    score: int | None = None
    relevance: int | None = None
    novelty: int | None = None
    clarity: int | None = None
    risk_flags: list[str] = field(default_factory=list)
    reason: str = ""

    # Filled in for top picks by the summarization pass (structured markdown).
    summary: str = ""

    @property
    def abs_url(self) -> str:
        return f"https://arxiv.org/abs/{self.id}"

    @property
    def pdf_url(self) -> str:
        return f"https://arxiv.org/pdf/{self.id}"

    @property
    def html_url(self) -> str:
        return f"https://arxiv.org/html/{self.id}"

    def author_str(self, limit: int = 6) -> str:
        if len(self.authors) <= limit:
            return ", ".join(self.authors)
        return ", ".join(self.authors[:limit]) + ", et al."
