# arXiv Today — Claude Code Project

## Purpose

A **Claude-powered daily arXiv digest** (CS.CV by default). Each run fetches the day's new submissions, **scores every one** against the researcher's interests, writes deep structured summaries for the high-scoring papers, saves a markdown report, and pushes the top picks to Slack. Methodology is ported from [HarborYuan/paper_agent](https://github.com/HarborYuan/paper_agent).

## Two execution paths

This repo supports the same methodology two ways:

1. **Scheduled routine (PRIMARY, no API key)** — a Claude Code routine runs daily on the user's **Max subscription**. The agent does the scoring and summarization *itself, in-session* — no Anthropic API key, no per-token cost. This is the engine that actually runs day-to-day. See "Routine methodology" below.
2. **Python pipeline (reference, needs API key)** — `src/` is a standalone backend that does the same thing via the **Anthropic Claude API** (Sonnet 4.6). It requires a paid `ANTHROPIC_API_KEY` from console.anthropic.com (separate from a Claude.ai subscription), so it's kept as a clean reference / for anyone with API access — not the default runner.

**No keyword filtering.** Both paths score *every* new submission against the profile rather than pre-filtering by keyword — this is deliberate (keyword gates were missing relevant papers). Relevance comes entirely from the LLM's judgment against the profile.

---

## Researcher Profile

**Weijie Lyu** — EECS PhD at UC Merced (advisor: Prof. Ming-Hsuan Yang), Research Scientist Intern at Apple (advisor: Dr. Lu Jiang).

**Interests, in priority order** (drives the scoring rubric): (1) **agentic AI research & automated scientific discovery** (AI scientist systems, autonomous research agents, LLM-driven experiment loops, multi-agent research pipelines), (2) **video generation**, (3) **image generation**, (4) **3D reconstruction & generation**, (5) **human video & face**. Close collaborators (boosted in scoring): Ming-Hsuan Yang, Zhixin Shu, Xiangtai Li, Yujing Wang, Xueting Li, Yi-Hsuan Tsai, Lu Jiang.

The canonical, machine-read copy of this profile lives in `USER_PROFILE` in [src/config.py](src/config.py) — edit it there; this section is the human summary.

---

## Architecture

```
src/
├── config.py        ← settings (model, categories, thresholds, Slack webhooks) + USER_PROFILE
├── models.py        ← Paper dataclass (carries scores + summary through the pipeline)
├── arxiv_client.py  ← fetch new-submission IDs from the recent listing, metadata via arXiv API
├── pdf_service.py   ← full-text extraction (arXiv HTML → PDF → abstract fallback)
├── prompts.py       ← scoring rubric + summarization prompt + JSON score schema
├── llm.py           ← Claude scoring (structured outputs) + summarization, async + bounded
├── notifier.py      ← Slack digest (substantive: score + authors + TL;DR + report link)
├── report.py        ← writes reports/daily/YYYY-MM-DD.md
└── pipeline.py      ← orchestration: fetch → score → summarize top picks → report + notify
reports/daily/       ← generated markdown archive (git-synced)
```

**Pipeline stages** ([src/pipeline.py](src/pipeline.py)):
1. **Fetch** — all arXiv IDs in the most recent day-section of `arxiv.org/list/<cat>/recent` (new submissions **plus** cross-lists; `show=2000` so a busy day isn't truncated), metadata from the arXiv Atom API.
2. **Score** — every paper scored 0–100 by Claude with structured outputs, concurrently (bounded by `ARXIV_CONCURRENCY`). The score is **holistic** (a precise integer 0–100), informed by relevance/novelty/clarity sub-signals plus collaborator/notable boosts, a **+10 bonus when the paper has a project webpage** (URL / GitHub repo / demo cited in the abstract), and risk-flag penalties — deliberately *not* a rigid `10r+5n+5c` formula, which would snap every score to a multiple of 5 (see `SCORING_SYSTEM` in [src/prompts.py](src/prompts.py)).
3. **Filter/rank** — keep ≥ `ARXIV_SCORE_THRESHOLD`; top picks = ≥ `ARXIV_TOP_PICK_MIN`, capped at `ARXIV_MAX_TOP_PICKS`.
4. **Summarize top picks** — fetch full text and write a structured briefing (TL;DR / Problem / Key Contributions / Method / Results / Why It Matters).
5. **Report + notify** — write the daily markdown report and post top picks to Slack.

---

## Running

Requires [uv](https://docs.astral.sh/uv/). Install Python ≥ 3.11 deps and run:

```bash
uv sync                       # install dependencies
cp .env.example .env          # then fill in ANTHROPIC_API_KEY (+ Slack webhooks)
uv run python -m src          # run the daily pipeline
```

Key environment variables (see [.env.example](.env.example)): `ANTHROPIC_API_KEY` (required), `ARXIV_MODEL` (default `claude-sonnet-4-6`), `ARXIV_CATEGORIES`, `ARXIV_SCORE_THRESHOLD`, `ARXIV_TOP_PICK_MIN`, `ARXIV_MAX_TOP_PICKS`, `ARXIV_CONCURRENCY`, `SLACK_WEBHOOK_URL`, `SLACK_WEBHOOK_URL_2`.

After a run, sync reports so other machines stay current:
```bash
git add reports/ && git commit -m "daily: $(date +%Y-%m-%d)" && git push
```

---

## Claude API conventions (for anyone editing src/llm.py)

- Use the official **Anthropic Python SDK** (`anthropic`), never an OpenAI-compatible shim.
- Default model is **`claude-sonnet-4-6`** for both scoring and summarization (`ARXIV_MODEL`). Do not silently change models.
- **Scoring** uses structured outputs (`output_config={"format": {"type": "json_schema", "schema": SCORE_SCHEMA}}`) — keep the schema within the supported subset (no numeric min/max; `additionalProperties: false`).
- **Prompt caching:** the scoring rubric + profile is a stable system-prompt prefix with a `cache_control` breakpoint — keep volatile per-paper content in the user message so the prefix stays cacheable.
- Scoring/summarization run concurrently via `AsyncAnthropic` bounded by a semaphore; the SDK auto-retries 429/5xx.

---

## Routine methodology (the path that actually runs)

The daily routine is a Claude Code cloud session on the user's Max subscription (model: Sonnet 4.6 — faster/lighter than Opus for scoring the full day's list in one session). Its prompt instructs the agent to, in one session:

1. **Fetch** all papers announced today from the recent listing's first day-section (new submissions **plus** cross-lists, `show=2000`) for **cs.CV**; pull title/abstract/authors via the arXiv API.
2. **Score every paper** with a holistic integer 0–100 against the profile (relevance/novelty/clarity as signals, plus collaborator/notable boosts and risk-flag penalties — a precise score like 87 or 93, not a multiple-of-5 formula). **No keyword filtering.**
3. **Summarize by quality, not a fixed count** — every paper scoring **≥ 80** gets a full-text structured summary (fetch `arxiv.org/html/<id>`; TL;DR / Problem / Key Contributions / Method / Why It Matters — *no Results section: "better than baselines" claims aren't useful*). Some days that's 3 papers, some days 15.
4. **Write** `reports/daily/YYYY-MM-DD.md` (full summaries for ≥80; scored table for the rest ≥ threshold). Append any auto_research papers scoring ≥70 to `reports/categories/auto_research.md` (date header + arXiv ID, title, authors, 2–3 sentence summary). Then `git add reports/ && commit && push`.
5. **Notify Slack** — post the ≥80 picks (each: score + title link + authors + TL;DR + 2–3 Key Contributions bullets) plus a link to the full report, to `SLACK_WEBHOOK_URL` / `SLACK_WEBHOOK_URL_2` (read from the environment; treat as secret).

The routine needs **no `ANTHROPIC_API_KEY`** (the agent is Claude, on the subscription); it only needs the Slack webhook env vars set in the cloud environment, and GitHub access for clone/push.

## Scheduling / hosting (Python path)

The Python pipeline is stateless, so with an `ANTHROPIC_API_KEY` + Slack webhooks in the environment it can be driven by cron, CI, or a routine running `uv run python -m src`. There is no long-running server to host. For the day-to-day no-key path, use the routine above instead.

---

## Reports

`reports/daily/YYYY-MM-DD.md` — Top Picks (with full structured summaries) + a scored table of other relevant papers. Earlier dates use the legacy hand-curated format; the pipeline now generates this automatically.
