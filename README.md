# 📄 arXiv Today

> A Claude-powered daily arXiv digest for CS.CV — fetch, **score**, **summarize**, and notify.

Every run pulls the day's new [cs.CV](https://arxiv.org/list/cs.CV/recent) submissions, scores each one (0–100) against a researcher profile with **Claude (Sonnet 4.6)**, writes a deep structured summary for the top picks from their full text, saves a markdown report, and pushes the top picks to Slack.

The architecture is ported from [HarborYuan/paper_agent](https://github.com/HarborYuan/paper_agent), with OpenAI replaced by the **Anthropic Claude API**. It's a backend pipeline — no web UI, no database, nothing to host 24/7.

---

## What it does

| Stage | Detail |
|-------|--------|
| 🔎 **Fetch** | New submissions from the category recent listing (cross-lists excluded); metadata via the arXiv API. |
| 🤖 **Score** | Every paper scored **0–100** by Claude with structured outputs — `relevance·10 + novelty·5 + clarity·5`, plus collaborator/notable boosts and risk-flag penalties. |
| 📝 **Summarize** | Top picks get a structured briefing (TL;DR · Problem · Contributions · Method · Results · Why It Matters) generated from the **full paper text**. |
| 📬 **Notify** | Top picks pushed to Slack with score, authors, TL;DR, and a link to the full report. |
| 🗂️ **Archive** | A markdown report is written to [`reports/daily/`](reports/daily/) and committed to git. |

---

## Setup

```bash
git clone https://github.com/weijielyu/arxiv-today.git
cd arxiv-today

uv sync                 # install deps (Python ≥ 3.11)
cp .env.example .env    # fill in ANTHROPIC_API_KEY (+ optional Slack webhooks)
```

Then run the daily pipeline:

```bash
uv run python -m src
```

### Configuration

All via environment / `.env` (see [`.env.example`](.env.example)):

| Variable | Default | Purpose |
|----------|---------|---------|
| `ANTHROPIC_API_KEY` | — | **Required.** Claude API key. |
| `ARXIV_MODEL` | `claude-sonnet-4-6` | Model for scoring + summarization. |
| `ARXIV_CATEGORIES` | `cs.CV` | Comma-separated categories to scan. |
| `ARXIV_SCORE_THRESHOLD` | `50` | Minimum score to appear in the report. |
| `ARXIV_TOP_PICK_MIN` | `70` | Minimum score to earn a full PDF summary. |
| `ARXIV_MAX_TOP_PICKS` | `5` | Cap on deep-summarized top picks. |
| `ARXIV_CONCURRENCY` | `6` | Concurrent scoring requests. |
| `SLACK_WEBHOOK_URL`, `SLACK_WEBHOOK_URL_2` | — | Slack incoming webhooks (second is optional). |

---

## Scheduling

The pipeline is stateless, so any scheduler works as long as it provides the env vars: cron on a host, a CI cron job, or a [Claude Code routine](https://claude.ai/code/routines) running `uv run python -m src`. There's no server to keep alive.

```bash
# Sync the report after each run
git add reports/ && git commit -m "daily: $(date +%Y-%m-%d)" && git push
```

---

*Built with [Claude Code](https://claude.com/claude-code) · scoring & summaries by Claude Sonnet 4.6*
