"""Runtime configuration, loaded from environment variables.

A minimal .env loader is included so `python -m src` works without extra deps;
real secrets (ANTHROPIC_API_KEY, Slack webhooks) should come from the environment
in production.
"""
from __future__ import annotations

import os
from dataclasses import dataclass, field
from pathlib import Path

# The researcher this digest is curated for. Drives the scoring rubric — keep in
# sync with CLAUDE.md.
USER_PROFILE = """\
Weijie Lyu — EECS PhD (UC Merced, advisor Ming-Hsuan Yang), Research Scientist Intern at Apple (advisor Lu Jiang).

Research interests, in PRIORITY order (higher = score relevance higher):
1. Agentic AI research & automated scientific discovery — AI scientist systems, autonomous research agents, LLM-driven experiment loops, automated hypothesis generation, multi-agent research pipelines, agentic ML optimization.
2. Video generation — autoregressive video, camera-controlled video, motion-controlled video, text/image-to-video, video diffusion, video editing.
3. Image generation — controllable generation, diffusion models (DiT, flow matching), text-to-image, image editing.
4. 3D reconstruction & generation — Gaussian Splatting, NeRF, feed-forward 3D, dynamic/4D, scene reconstruction, novel view synthesis.
5. Human video & reconstruction — face generation/reconstruction, talking head, portrait video, full-body avatars.

Close collaborators (treat their papers as high-relevance even if borderline): Ming-Hsuan Yang, Zhixin Shu, Xiangtai Li, Yujing Wang, Xueting Li, Yi-Hsuan Tsai, Lu Jiang.

Avoid (score low / flag domain_mismatch): medical imaging, remote sensing, autonomous driving (unless 3D-relevant), action recognition, NLP benchmarks, agricultural/satellite tasks.
"""


def _load_dotenv() -> None:
    """Populate os.environ from a local .env file if present (does not override real env)."""
    path = Path(__file__).resolve().parent.parent / ".env"
    if not path.exists():
        return
    for line in path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        os.environ.setdefault(key, value)


_load_dotenv()


@dataclass
class Settings:
    model: str = os.getenv("ARXIV_MODEL", "claude-sonnet-4-6")
    categories: list[str] = field(
        default_factory=lambda: [
            c.strip() for c in os.getenv("ARXIV_CATEGORIES", "cs.CV").split(",") if c.strip()
        ]
    )
    max_results: int = int(os.getenv("ARXIV_MAX", "250"))
    score_threshold: int = int(os.getenv("ARXIV_SCORE_THRESHOLD", "50"))
    top_pick_min: int = int(os.getenv("ARXIV_TOP_PICK_MIN", "85"))
    # 0 = no cap: summarize every paper at/above top_pick_min (quality-driven, not a fixed count).
    max_top_picks: int = int(os.getenv("ARXIV_MAX_TOP_PICKS", "0"))
    concurrency: int = int(os.getenv("ARXIV_CONCURRENCY", "6"))
    user_profile: str = USER_PROFILE
    slack_webhooks: list[str] = field(
        default_factory=lambda: [
            u
            for u in (os.getenv("SLACK_WEBHOOK_URL"), os.getenv("SLACK_WEBHOOK_URL_2"))
            if u
        ]
    )


settings = Settings()
