# Auto-Research & Agentic AI

Running log of papers on automated scientific discovery, AI scientist systems, LLM-driven experiment loops, and multi-agent research pipelines.

---

## 2026-05-26 (manually reviewed)

### karpathy/autoresearch
**Link:** https://github.com/karpathy/autoresearch (~83k★)
**Authors:** Andrej Karpathy

Proof-of-concept autonomous ML research loop. An LLM agent iteratively edits a single-file nanoGPT training script (`train.py`), runs a fixed 5-minute training experiment, measures `val_bpb` (bits per byte — vocabulary-size-independent quality metric), keeps the change if it improves the metric and reverts otherwise, then repeats indefinitely. Research direction is steered via a natural-language `program.md` file. Key design insights: fixed time budget makes experiments directly comparable across runs; `val_bpb` prevents tokenizer changes from gaming the metric; persistent experiment log carries all history forward.

---

### Accelerating Scientific Discovery with Co-Scientist
**Link:** https://doi.org/10.1038/s41586-026-10644-y | **Local:** `projects/agent/Accelerating_scientific_discovery_with_Co-Scientist.pdf`
**Authors:** Gottweis, Weng, Daryin, Tu et al. (Google DeepMind / Google Research)
**Venue:** Nature 2026

Multi-agent AI system built on Gemini for structured scientific hypothesis generation. Core mechanism: agents independently generate hypotheses, then engage in pairwise self-play scientific debate, producing win/loss records used to evolve and refine hypotheses through a tournament process. More test-time compute → more tournament rounds → better hypotheses (validated across 15 expert-curated scientific goals; outperforms GPT-4o and Gemini 2.0 Deep Research). Validated in three biomedical domains including drug repurposing for AML (confirmed in vitro) and independently rediscovering unpublished findings in antimicrobial resistance.

---

### A Multi-Agent System for Automating Scientific Discovery (Robin)
**Link:** https://doi.org/10.1038/s41586-026-10652-y | **Local:** `projects/agent/A_multi-agent_system_for_automating_scientific_discovery.pdf`
**Authors:** Ghareeb, Chang, Mitchener, Yiu et al. (FutureHouse)
**Venue:** Nature 2026

Robin is the first system to close the full scientific loop from hypothesis generation through experimental data analysis and back to refined hypotheses, without requiring human involvement in the experiment execution step. Three specialized agents: Crow (concise literature search), Falcon (deep literature search), Finch (data analysis — RNA-seq, flow cytometry). Applied to dry AMD drug discovery: analyzed 551 papers in 30 minutes (200x faster than humans), proposed ripasudil (a ROCK inhibitor never previously proposed for dAMD), confirmed efficacy in vitro, then autonomously designed and analyzed a follow-up RNA-seq experiment identifying ABCA1 as a novel target.

---

### Agentic Artificial Intelligence (book)
**Local:** `projects/agent/agentic_artifical_intelligence.pdf`
**Authors:** Pascal Bornet, Jochen Wirtz, Thomas H. Davenport et al.
**Venue:** Book (2025), Forbes "Top 10 Must-Read Tech Book"

Practitioner/business-oriented guide to AI agents co-authored by 27 industry and academic contributors. Covers a 5-level autonomy framework (automation → full autonomy), the three pillars of agents (action, reasoning, memory), a practical guide to building and deploying agents in enterprises, and future-of-work implications. Not technically deep; more useful for the action/reasoning/memory framing as a design vocabulary for speccing out agent components.

---

### The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery
**arXiv:** [2408.06292](https://arxiv.org/abs/2408.06292)
**Authors:** Chris Lu, Cong Lu, Robert Tjarko Lange, Jakob Foerster, Jeff Clune, David Ha (Sakana AI)
**Venue:** arXiv 2024

Landmark paper for end-to-end autonomous ML research. Full pipeline: idea generation → code writing → experiment execution → result visualization → paper writing → automated peer review. Applied to three ML subfields (diffusion modeling, transformer language modeling, learning dynamics). ~$15 per paper. One paper exceeded the acceptance threshold of their automated reviewer. Open-sourced at https://github.com/SakanaAI/AI-Scientist. Limitation: requires human-authored code templates per research domain; evaluated only in narrow ML settings.

---

### The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree Search
**arXiv:** [2504.08066](https://arxiv.org/abs/2504.08066)
**Authors:** Yutaro Yamada, Robert Tjarko Lange, Cong Lu et al. (Sakana AI)
**Venue:** arXiv 2025

Extends v1 by eliminating reliance on human-authored code templates and introducing **progressive agentic tree search** — explores multiple experiment branches in parallel, managed by a dedicated experiment manager agent that prunes unpromising branches. Also adds a VLM feedback loop for iterative figure refinement. One out of three submitted manuscripts was accepted at an ICLR 2025 workshop — the first fully AI-generated peer-review-accepted paper. Open-sourced at https://github.com/SakanaAI/AI-Scientist-v2.

---

### Jr. AI Scientist and Its Risk Report
**arXiv:** [2511.04583](https://arxiv.org/abs/2511.04583)
**Authors:** Atsuyuki Miyai, Mashiro Toyooka, Takashi Otonari et al.
**Venue:** arXiv 2025

Given a baseline paper from a human mentor, the system analyzes its limitations, formulates improvement hypotheses, iteratively experiments until improvements are achieved, and writes a paper. Unlike Sakana's AI Scientist, handles complex multi-file codebases using modern coding agents and follows a well-defined research workflow modeled on a novice student researcher. Successfully produced new papers building on real NeurIPS, IJCV, and ICLR works. Also includes a comprehensive risk report identifying failure modes and limitations — valuable for anyone building similar systems.

---

### AutoML-Agent: A Multi-Agent LLM Framework for Full-Pipeline AutoML
**arXiv:** [2410.02958](https://arxiv.org/abs/2410.02958)
**Authors:** Patara Trirat, Wonyong Jeong, Sung Ju Hwang
**Venue:** arXiv 2024

Full-pipeline AutoML using LLM agents, from data retrieval to model deployment. Key contribution: **retrieval-augmented planning** — instead of generating a single plan, the agent retrieves past successful plans via RAG and generates multiple candidate plans, then selects the best. Each plan is decomposed into parallel sub-tasks solved by specialized agents concurrently. Validated across 7 downstream tasks on 14 datasets. The RAG-augmented multi-plan approach and parallel sub-task decomposition are directly applicable to the research agent design.

---

### AI Scientists Fail Without Strong Implementation Capability
**arXiv:** [2506.01372](https://arxiv.org/abs/2506.01372)
**Authors:** Minjun Zhu, Qiujie Xie, Yixuan Weng et al.
**Venue:** arXiv 2025

Position paper arguing that the fundamental bottleneck in current AI scientist systems is not hypothesis quality but **execution capability**: the ability to implement rigorous experiments and produce valid scientific papers. Evaluated 28 papers generated by 5 AI scientist systems; found that systems frequently fail at the verification/implementation step. Critical reading before building any agentic research system — the code-writing agent must be robust with self-debugging before the research loop is useful.

---

### How Far Are AI Scientists from Changing the World?
**arXiv:** [2507.23276](https://arxiv.org/abs/2507.23276)
**Authors:** Qiujie Xie, Yixuan Weng, Minjun Zhu et al.
**Venue:** arXiv 2025

Survey of current AI scientist systems. Comprehensively analyzes achievements, identifies key bottlenecks, and describes the critical components needed for an AI scientist capable of producing groundbreaking discoveries. Good entry point for understanding where the field is and what is missing. Complements the "AI Scientists Fail" paper with broader scope.

---

### Agentic AI Scientists Are Not Built For Autonomous Scientific Discovery
**arXiv:** [2605.08956](https://arxiv.org/abs/2605.08956)
**Authors:** Harshit Bisht, Vinay Kumar, Kevin Maik Jablonka, Mausam, N. M. Anoop Krishnan
**Venue:** arXiv 2026

Position paper identifying four fundamental challenges in building autonomous AI scientists: (1) problem selection biased toward easily measurable proxies (McNamara fallacy); (2) LLM training corpora lack tacit procedural and failure knowledge from lab practice; (3) post-training preference optimization compresses output diversity toward consensus; (4) benchmarks measure single-turn prediction, not iterative experimental feedback. Recommends using scientific simulations as verifiers, designing persistent world models, and pre-registering AI-generated hypotheses. Useful for understanding what the field is missing.

---

## 2026-05-29

### GenClaw: Code-Driven Agentic Image Generation
**arXiv:** [2605.30248](https://arxiv.org/abs/2605.30248)
**Authors:** Junyan Ye, Jun He, Zilong Huang, Dongzhi Jiang, Xuan Yang
**Score:** 85

Proposes using executable code (SVG, HTML, Three.js) as a structured intermediate "canvas" in an agentic image generation pipeline — Conceptualize (search + reasoning) → Sketch (code execution for layout) → Color (image model for textures). Addresses the fundamental bottleneck of existing image-gen agents that are trapped in prompt-rewriting loops with no direct canvas control. Demonstrates improved compositional control, text rendering, physics-assisted simulation, and layered editing. Directly relevant as an example of LLM code agents applied to creative visual generation, establishing a debuggable and interpretable agentic framework where each pipeline stage has a clear failure mode.

---

### WorldMemArena: Evaluating Multimodal Agent Memory Through Action-World Interaction
**arXiv:** [2605.29341](https://arxiv.org/abs/2605.29341)
**Authors:** Chengzhi Liu, Yuzhe Yang, Sophia Xiao Pu, Yepeng Liu, Lin Long
**Score:** 80

New benchmark decomposing multimodal agent memory into four distinct operations: write, maintain, retrieve, and use — evaluated through interactive world environment tasks where agents must track an evolving state, revise stale information, and surface the right evidence at decision time. Unlike existing benchmarks that collapse memory into end-of-task accuracy, WorldMemArena localizes failures to specific memory operations, enabling principled comparison of memory designs (hand-crafted vs. agent-authored). Directly useful for understanding which memory mechanisms are the bottleneck in long-horizon multimodal agents.

---

### AgentCVR: Active Multi-Agent Cross-Video Reasoning via Script-Simulated Reinforcement Learning
**arXiv:** [2605.29643](https://arxiv.org/abs/2605.29643)
**Authors:** Yilun Qiu, Jiahe Wang, Cilin Yan, Jiayin Cai, Xiaolong Jiang
**Score:** 73

Multi-agent framework for cross-video reasoning that treats evidence acquisition as an active task: a Master Agent iteratively coordinates specialized Visual and Audio agents to retrieve and aggregate evidence distributed across multiple videos. Trained via script-simulated RL, avoiding the cost of human annotation. Outperforms single-pass MLLM strategies that compress all video context into a shared context window. Relevant as a multi-agent pattern (active coordinator + specialized sub-agents with RL training) applicable to evidence-gathering in research pipelines.

---

### STAMP: Training Explicit Memory for Mobile GUI Agents in Controllable and Scalable Virtual Environments
**arXiv:** [2605.29324](https://arxiv.org/abs/2605.29324)
**Authors:** Junyang Wang, Haiyang Xu, Xi Zhang, Zhaoqing Zhu et al.
**Score:** 70

Trains GUI agents to explicitly memorize task-relevant transient information during long-horizon tasks — addressing the context-window vs. screenshot-heavy history conflict that causes reactive agents to lose critical state. Uses scalable virtual environments to generate what-and-when-to-memorize training signals that static datasets cannot provide. Relevant as a memory training paradigm: the insight that agents need explicit training to know *when* to write to memory (not just how) applies directly to research agents that must selectively log experiment results across long sessions.

---

## 2026-05-27

### GenEvolve: Self-Evolving Image Generation Agents via Tool-Orchestrated Visual Experience Distillation
**arXiv:** [2605.21605](https://arxiv.org/abs/2605.21605)
**Authors:** Sixiang Chen, Zhaohu Xing, Tian Ye, Xinyu Geng
**Score:** 73

Self-evolving framework for image generation agents that improves through experience rather than fixed training. Each generation attempt is modeled as a tool-orchestrated trajectory; the agent distills successful visual experiences into its policy via a feedback loop over tool use and output quality. Relevant to the auto-research theme: demonstrates how an agent can accumulate skill from trial-and-error trajectories rather than requiring curated supervised data, analogous to how a research agent should learn from its experiment history.

---
