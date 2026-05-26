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

### 3. Score & curate — assign a relevance score (1–10)
Give every paper that passes the filter a **relevance score from 1 to 10** that reflects how worth-reading it is *for Weijie specifically*. Score holistically against these anchors, then apply the modifiers, then clamp to 1–10:

**Base relevance (interest area + quality):**
- **9–10** — Squarely in a priority-1/2 area (**video generation** or **image generation**) *and* a clear, novel contribution from a notable group; or a strong, on-topic paper from a close collaborator. A must-read.
- **7–8** — Solid paper with a clear contribution in any of the four interest areas; or a priority-3/4 area (**3D**, **human/face**) paper from a strong group.
- **5–6** — Relevant to an interest area but incremental, narrow in scope, or from an unknown group.
- **3–4** — Only tangentially related; borderline.
- **1–2** — Off-topic or in an excluded area.

**Priority weighting** (when otherwise comparable): video generation > image generation > 3D ≈ human/face. Nudge scores accordingly.

**Modifiers** (apply, then clamp to 1–10):
- **+2** — a close collaborator is an author (Ming-Hsuan Yang, Zhixin Shu, Xiangtai Li, Yujing Wang, Xueting Li, Yi-Hsuan Tsai, Lu Jiang) *and* the paper is at least loosely on-topic. This is how collaborator papers get surfaced even when borderline.
- **+1** — notable group lead / top-tier lab (e.g., **Ziwei Liu**, **Kaiming He**) with a clearly novel contribution.
- **−2** — in an excluded area (medical imaging, remote sensing, autonomous driving unless 3D-relevant, action recognition, NLP benchmarks, agricultural/satellite) even if it trips a keyword.

**Tiers (drive the report from the score):**
- **≥ 8 → ⭐ Top Pick.** Take the 3–5 highest; if more than 5 qualify, keep the top 5 (break ties by collaborator presence, then priority area). If fewer than 3 reach 8, fill Top Picks with the next-highest down to a floor of 7.
- **5–7 → include** in the category table.
- **< 5 → exclude** from the report.

Quality over quantity still governs: prefer well-known groups/top venues, abstracts that clearly state a novel contribution, and papers likely to be discussed. The score makes that judgment explicit and sortable.

### 4. Write reports

**Daily report format** (`reports/daily/YYYY-MM-DD.md`):
- Header with date and total new submission count
- **Top Picks** section — the 3–5 highest-scored papers, ordered by score (descending), each with its score and a 2–3 sentence explanation of why
- Tables per category: **Score**, Paper, arXiv ID (linked), authors, one-line highlight — sort rows by score descending

**Category report format** (`reports/categories/<topic>.md`):
- Appended entries per day (newest at top within a date section)
- Each entry: score, arXiv ID, title, authors, 2–3 sentence summary of contribution

**Formatting conventions** (follow the existing reports exactly):
- arXiv IDs use the date-based scheme `YYMM.NNNNN` (e.g., `2605.22818`); link as `[2605.22818](https://arxiv.org/abs/2605.22818)`
- Show the relevance score as **`N/10`**. In daily Top Picks put it on its own line (`**Score:** 9/10`); in category tables it's the leading **Score** column; in category reports prefix the entry title (e.g., `**9/10** · MotiMotion: …`)
- **Bold** author names for both close collaborators *and* notable group leads (e.g., `**Ming-Hsuan Yang**`, `**Ziwei Liu**`); end the summary with a `Notable: …` callout when a collaborator is an author
- Tag each paper with a subcategory using `→` (e.g., `Video Generation → Motion Control`)
- In category reports, prefix entries that were daily Top Picks with `⭐`
- Daily reports use blockquote (`>`) for the per-paper rationale; lines end with two trailing spaces for hard breaks

After writing reports, sync with git so other machines stay current:
```bash
git add reports/ && git commit -m "daily: $(date +%Y-%m-%d)" && git push
```

---

## MCP Server

`arxiv-mcp-server` (2763★, blazickjp/arxiv-mcp-server) is configured in `.mcp.json`.
- Install: `uv tool install --python 3.12 arxiv-mcp-server` (v0.5.0+ requires Python ≥3.11; without `--python`, uv may silently fall back to the broken 0.1.0 if the default interpreter is older)
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
