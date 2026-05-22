# 📄 arXiv Today

> A personal daily arXiv digest for CS.CV — curated by Claude Code, organized by topic.

Every day, Claude Code fetches all new [cs.CV](https://arxiv.org/list/cs.CV/recent) submissions, filters them by research interest, reads the abstracts, and writes two sets of reports:

- **Daily reports** — top picks with explanations + full tables by category
- **Category logs** — running cumulative lists so you can track any topic over time

---

## Research Areas Covered

| Category | Topics |
|----------|--------|
| 🎬 Video Generation | Autoregressive video, camera control, motion control, text/image-to-video |
| 🖼️ Image Generation | Diffusion models, DiT, flow matching, text-to-image, controllable generation |
| 🧊 3D Reconstruction & Generation | Gaussian Splatting, NeRF, feed-forward 3D, dynamic 3D, scene reconstruction |
| 🧑 Human Video & Face | Face generation/reconstruction, talking head, portrait video, full-body avatars |

---

## Reports

### By Date
Browse [`reports/daily/`](reports/daily/) for day-by-day digests.

Each daily report has:
- **⭐ Top Picks** — 3–5 papers most worth reading, with a paragraph on why
- **Category tables** — all relevant papers with authors and a one-line highlight

### By Topic
Browse [`reports/categories/`](reports/categories/) for running topic logs.

| File | Covers |
|------|--------|
| [video_generation.md](reports/categories/video_generation.md) | Video gen, motion/camera control |
| [image_generation.md](reports/categories/image_generation.md) | Image gen, diffusion, DiT |
| [3d_reconstruction.md](reports/categories/3d_reconstruction.md) | 3D reconstruction & generation |
| [human_reconstruction.md](reports/categories/human_reconstruction.md) | Human video, face, avatars |

---

## Setup

### Requirements
- [Claude Code](https://claude.ai/code)
- [uv](https://docs.astral.sh/uv/) — Python package manager

### Installation

```bash
git clone https://github.com/weijielyu/arxiv-today.git
cd arxiv-today

# Install the arXiv MCP server (blazickjp/arxiv-mcp-server, 2700+★)
uv tool install arxiv-mcp-server
```

Then open the folder in Claude Code:

```bash
claude .
```

Claude Code will detect `.mcp.json` and wire up the `arxiv-mcp-server` automatically (one-time trust prompt). From there, just ask Claude to fetch today's papers.

### Syncing across machines

```bash
# After each session
git add reports/ && git commit -m "daily: $(date +%Y-%m-%d)" && git push

# On another machine before starting
git pull
```

---

## How It Works

1. **Fetch** — downloads the full day's cs.CV listing from arXiv (`show=250`)
2. **Filter** — scans titles against topic keywords; fetches abstracts via the arXiv API for candidates
3. **Curate** — reads abstracts, applies quality judgment (known groups, clear contributions, community relevance)
4. **Write** — updates the daily report and appends to the relevant category logs

The full workflow and curation rules live in [`CLAUDE.md`](CLAUDE.md), which Claude Code reads automatically on every session.

---

## MCP Server

This project uses [`arxiv-mcp-server`](https://github.com/blazickjp/arxiv-mcp-server) (2700+★) configured in [`.mcp.json`](.mcp.json). It exposes tools for searching arXiv, downloading papers, reading full text, and setting up topic alerts — all directly accessible within Claude Code.

---

*Built with [Claude Code](https://claude.ai/code)*
