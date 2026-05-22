# arXiv Daily — Claude Code Project

## Purpose

Daily arXiv CS.CV paper monitor. Each session, fetch today's new submissions, filter to relevant papers, and update two sets of reports:
1. **Daily reports** — `reports/daily/YYYY-MM-DD.md` — one file per day, all relevant papers with abstracts and a top-picks section
2. **Category reports** — `reports/categories/*.md` — running cumulative lists organized by topic

---

## Researcher Profile

**Weijie Lyu** — 3rd-year EECS PhD at UC Merced (advisor: Prof. Ming-Hsuan Yang). Currently Research Scientist Intern at Apple (May 2026–, advisor: Dr. Lu Jiang).

**Research interests, in priority order:**
1. **Video generation** — especially autoregressive video generation, camera-controlled video, motion-controlled video, text/image-to-video
2. **Image generation** — controllable generation, diffusion models (DiT, flow matching), text-to-image
3. **3D reconstruction & generation** — Gaussian Splatting, NeRF, feed-forward 3D models, dynamic 3D, scene reconstruction
4. **Human video & reconstruction** — face generation, face reconstruction, talking head, portrait video, full-body avatars

**Close collaborators** (flag papers from these people even if outside the main areas):
- Ming-Hsuan Yang (advisor, UC Merced)
- Zhixin Shu (Adobe Research)
- Xiangtai Li, Yujing Wang (ByteDance)
- Xueting Li, Yi-Hsuan Tsai (Adobe)
- Lu Jiang (Apple, current internship)

---

## Daily Workflow

### 1. Fetch today's papers
```
https://arxiv.org/list/cs.CV/recent?skip=0&show=250
```
- Parse with Python (HTML uses single-quote attributes: `class='list-title mathjax'`)
- The page shows how many new submissions: "showing N of N"
- New submissions come first; cross-lists follow — treat only new submissions as today's papers
- Use the arXiv API for abstracts: `https://export.arxiv.org/api/query?id_list=ID1,ID2,...`

### 2. Filter for relevant papers
Scan title + abstract for keywords across these areas:
- **Video gen:** video generation, video diffusion, text-to-video, image-to-video, autoregressive video, video editing, motion control, camera control, camera trajectory, novel view synthesis
- **Image gen:** image generation, diffusion model, text-to-image, image editing, controllable generation, DiT, flow matching
- **3D:** 3D reconstruction, 3D generation, Gaussian splatting, NeRF, neural radiance, point cloud, novel view, feed-forward 3D, dynamic 3D
- **Human/face:** face generation, face reconstruction, talking head, portrait, avatar, human video, human reconstruction, facial, full-body

**Exclude by default:** medical imaging, remote sensing, autonomous driving (unless 3D-relevant), action recognition, NLP benchmarks, agricultural/satellite tasks.

### 3. Curate — quality over quantity
Not every matched paper is worth reporting. Prefer:
- Papers from well-known research groups / top venues
- Papers where the abstract clearly states a novel contribution
- Papers that are likely to be discussed in the community

Flag papers from the user's close collaborators even if borderline.

### 4. Write reports

**Daily report format** (`reports/daily/YYYY-MM-DD.md`):
- Header with date and total new submission count
- **Top Picks** section — 3–5 papers most worth reading, with 2–3 sentence explanations of why
- Tables per category: arXiv ID (linked), authors, one-line highlight

**Category report format** (`reports/categories/<topic>.md`):
- Appended entries per day (newest at top within a date section)
- Each entry: arXiv ID, title, authors, 2–3 sentence summary of contribution

---

## MCP Server

`arxiv-mcp-server` (2763★, blazickjp/arxiv-mcp-server) is configured in `.mcp.json`.
- Install: `uv tool install arxiv-mcp-server`
- Paper storage: `~/.arxiv-mcp-server/papers` (default, local to each machine)
- Tools: `search_papers`, `download_paper`, `read_paper`, `list_papers`, `watch_topic`, `check_alerts`

---

## Repository Structure

```
arxiv_today/
├── CLAUDE.md                    ← this file
├── .mcp.json                    ← arxiv-mcp-server config
├── .gitignore
└── reports/
    ├── daily/
    │   └── YYYY-MM-DD.md
    └── categories/
        ├── video_generation.md
        ├── image_generation.md
        ├── 3d_reconstruction.md
        └── human_reconstruction.md
```
