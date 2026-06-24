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

## 2026-06-01

### Crafter: A Multi-Agent Harness for Editable Scientific Figure Generation from Diverse Inputs
**arXiv:** [2605.30611](https://arxiv.org/abs/2605.30611)
**Authors:** Haozhe Zhao, Shuzheng Si, Zhenhailong Wang, Zheng Wang, Liang Chen, Xiaotong Li, Zhixiang Liang, Maosong Sun, Minjia Zhang
**Score:** 83

Multi-agent harness for scientific figure generation that solves the root failure mode of AI-generated structured visuals: five cooperating agents (intent reasoner, plan generator, critic, specification refiner, convergence judge) share an evolving structured figure specification as persistent pipeline memory, enabling typed targeted correction of localized errors (garbled labels, misaligned connectors) across diverse figure types and input modalities. Companion system CraftEditor converts raster outputs to locally editable SVGs via iterative assembly; CraftBench benchmark spans 3 figure types and 4 input conditions. Directly relevant to automated research pipelines: the harness abstraction (structured spec as memory, verify-then-refine loop, directive diagnostics) generalizes to any structured scientific content generation task.

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

## 2026-06-02

### Reasmory: 3D Reconstruction as Explicit Memory for VLMs Spatial Reasoning
**arXiv:** [2606.00963](https://arxiv.org/abs/2606.00963)
**Authors:** Jixuan He, Xueting Li, Chieh Hubert Lin, Ming-Hsuan Yang
**Score:** 93

Reasmory builds explicit 3D point-cloud memory from multi-view images or video and constrains VLM interaction with that memory via a validated domain-specific language (DSL), achieving 6–18% gains over GPT-5-mini and Gemini-3-flash on spatial reasoning benchmarks. Semantic 3D object instances augment the point cloud, and generated DSL programs are syntactically validated before execution — preventing the errors common with unconstrained free-form tool use. Demonstrates that structured, validated access to explicit spatial memory dramatically outperforms unconstrained tool calls for VLM reasoning tasks.

---

### OpenWebRL: Demystifying Online Multi-turn Reinforcement Learning for Visual Web Agents
**arXiv:** [2606.02031](https://arxiv.org/abs/2606.02031)
**Authors:** Rui Yang, Qianhui Wu, Yuxi Chen, Hao Bai, Wenlin Yao, Hao Cheng, Baolin Peng, Huan Zhang, Tong Zhang, Jianfeng Gao
**Score:** 83

OpenWebRL is the first fully open-source framework for training visual web agents with online multi-turn RL on real websites, using only 0.4K initialization trajectories versus the 278K required by supervised baselines. Core contribution is MM-GRPO (Multimodal Multi-turn GRPO), extending GRPO to live browser interaction with trajectory-level outcome rewards judged by OpenWebRL-Judge-8B. OpenWebRL-4B achieves 67.0% on Online-Mind2Web and 64.0% on DeepShop — competitive with proprietary systems like OpenAI CUA at 650× less training data.

---

### Thinking in Blender: Staged Executable Inverse Graphics with Vision-Language Models
**arXiv:** [2606.02580](https://arxiv.org/abs/2606.02580)
**Authors:** Guangzhao He, Rundong Luo, Wei-Chiu Ma, Hadar Averbuch-Elor
**Score:** 81

SEIG (Staged Executable Inverse Graphics) reconstructs editable 3D Blender scenes from single images by decomposing reconstruction into sequential stages (geometry → materials → composition → lighting), each with a generator-verifier loop where a pretrained VLM writes executable Blender Python code and visually inspects rendered output before proceeding. No specialized 3D models or differentiable rendering pipelines are required. Shows that agentic VLMs can perform complex 3D reconstruction through structured code generation and staged verification — the finding that task decomposition matters more than toolkit richness is broadly applicable to agentic AI design.

---

### VESTA: Visual Exploration with Statistical Tool Agents
**arXiv:** [2606.00384](https://arxiv.org/abs/2606.00384)
**Authors:** William Rudman, Abhishek Divekar, Kanishk Jain, Sebastian Joseph, Stella S. R. Offner, Matthew Lease, Kyle Mahowald, Greg Durrett, Junyi Jessy Li
**Score:** 80

VESTA equips VLMs with a dynamically growing toolkit of visual diagnostic tools (data transformations, hypothesis-driven visualizations, statistical tests) to iteratively fit statistical models to data, including real-world astronomy tasks (gravitational-wave chirp signals, initial mass functions). Unlike prior systems that rely on iterative text critique alone, tools accumulate in context across refinement rounds and are reused; dynamically generated tools outperform expert-written static tool sets, especially on complex domain-specific tasks. Demonstrates automated scientific discovery at the level of statistical model fitting — one of the most expertise-intensive steps in research pipelines — directly relevant to AI scientist systems.

---

### APE: Agentic Prompt Enhancer for Image Generation and Editing
**arXiv:** [2606.00204](https://arxiv.org/abs/2606.00204)
**Authors:** Zijian Huang, Jay Zhangjie Wu, Zian Wang, Tianshi Cao, Jiasi Chen, Sanja Fidler, Huan Ling, Xuanchi Ren
**Score:** 78

APE post-trains small language models (SLMs) as lightweight prompt-enhancement agents for image generation and editing, eliminating dependence on proprietary LLMs like ChatGPT or Gemini for prompt rewriting. Two variants: SAPE for single-pass rewriting and MAPE, a multi-agent router→rewriter→composer pipeline handling compositional constraints over objects, attributes, spatial relations, and edits. With task-aware RL rewards, APE outperforms base SLMs and narrows the gap to closed-source prompt enhancers without modifying the downstream visual model.

---

### 3DCodeBench: Benchmarking Agentic Procedural 3D Modeling Via Code
**arXiv:** [2606.01057](https://arxiv.org/abs/2606.01057)
**Authors:** Yipeng Gao, Lei Shu, Genzhi Ye, Xi Xiong, Ameesh Makadia, Meiqi Guo, Laurent Itti, Jindong Chen
**Score:** 77

3DCodeBench evaluates 12 advanced VLMs as agentic procedural 3D modelers, testing their ability to translate text and image references into procedural code for 3D modeling software — a paradigm offering deterministic, engine-ready, precisely editable assets that neural 3D generators lack. Key findings: failures mostly arise from API mismatches, and test-time scaling (higher thinking budgets, multi-turn refinement) consistently improves performance. Includes 3DCodeArena, a pairwise human-preference ranking platform, highlighting the need for high-quality procedural coding data and robust execution environments for iterative VLM refinement.

---

### Agent Skills Should Go Beyond Text: The Case for Visual Skills
**arXiv:** [2606.01414](https://arxiv.org/abs/2606.01414)
**Authors:** Binxiao Xu, Ruichuan An, Bocheng Zou, Hang Hua
**Score:** 75

Argues that text-only skill paradigms (instructions, reasoning traces, summarized trajectories) create a fundamental bottleneck for visual-centric agents, where reusable knowledge depends on spatial layout, visual grounding, and localized state changes. Proposes three multimodal skill forms: static priors for stable conventions, dynamic priors for in-situ visual working memory, and interleaved visual skills binding text steps to source frames and page regions. An automatic system converts agent trajectories into these multimodal skills; experiments on GUI tasks show visual skills consistently outperform text-only skills on tasks requiring spatial correspondence and visual verification.

---

### DeepLatent: Think with Images via Parallel Latent Visual Reasoning
**arXiv:** [2606.00562](https://arxiv.org/abs/2606.00562)
**Authors:** Dongchen Lu, Zhimo Li, Mao Shu, Huo Cao
**Score:** 75

DeepLatent introduces a parallel latent visual reasoning framework where VLMs embed explicit visual states into intermediate reasoning steps, combining the flexibility of tool-assisted methods with lower latency. LatentFormer uses learnable 2D tokens to generate context-conditioned latent states in parallel — anchored to original image features — while a continuous-space RL algorithm optimizes latent modulation parameters directly in embedding space, improving representation quality beyond what knowledge distillation alone achieves. Achieves state-of-the-art performance across multiple benchmarks while avoiding the sequential bottleneck of autoregressive latent-token approaches.

---

### Do Multimodal Agents Really Benefit from Tool Use? A Systematic Study
**arXiv:** [2606.02357](https://arxiv.org/abs/2606.02357)
**Authors:** Garvin Guo, Donglei Yu, Yu Chen, Xiang Wang, Shuai Li, Xinpei Zhao, Huaxing Liu, Qinghao Wang, Minpeng Liao
**Score:** 74

Challenges the common interpretation that strong benchmark gains from tool-augmented agents prove tool utility: 93–96% of tool-solved problems in two representative agents (Thyme, DeepEyesV2) are also solved by non-tool settings, and tool access yields little consistent aggregate improvement or token-cost reduction. Mechanism ablations show agents learn tool-calling patterns more reliably than tool-contributed capabilities — raising the possibility that benchmark gains come from structured output formatting rather than actual tool benefit. Recommends evaluation designs that distinguish tool availability from whether tools actually expand what agents can solve.

---

### Sandboxed Coding Agents are Competitive Omni-modal Task Solvers
**arXiv:** [2606.00579](https://arxiv.org/abs/2606.00579)
**Authors:** Dongping Chen, Xuanao Huang, Zhihan Hu, Qingyuan Shi, Dianqi Li, Tianyi Zhou
**Score:** 73

Shows that coding agents with only text+image access and sandboxed tool use can match or outperform state-of-the-art native omnimodal models on video and audio benchmarks by converting omnimodal tasks into retrieval and code-driven information-processing problems. Their strength comes from writing code to extract evidence from transcripts, frames, and modality signals rather than ingesting entire media streams. Introduces Code-X (training recipe + OmniCoding trajectory dataset with verifiable reward) and TerminalBench-O for process-level omnimodal benchmarking.

---

### Diversity Over Frequency: Rethinking Tool Use in Visual Chain-of-Thought Agents
**arXiv:** [2606.00096](https://arxiv.org/abs/2606.00096)
**Authors:** Dong-Hee Kim, Reuben Tan, Donghyun Kim
**Score:** 72

Identifies a "tool-use collapse" phenomenon in visual chain-of-thought agents: models progressively stop using tools during training while still achieving higher accuracy, revealing an asymmetry where eliminating tools hurts but incentivizing tool use yields only marginal gains. Both standard training and tool-use encouragement reduce rollout diversity — explaining why higher tool frequency does not yield stronger reasoning — while entropy regularization promoting diverse rollout exploration achieves best performance despite declining tool usage. Reframes tools as training-time scaffolding rather than inference-time necessities, with important implications for agent training curricula.

---

## 2026-06-03

### MUSE: A Unified Agentic Harness for MLLMs
**arXiv:** [2606.03005](https://arxiv.org/abs/2606.03005)
**Authors:** Jianglin Lu, Hailing Wang, Xu Ma, Qihua Dong, Mingyuan Zhang et al.
**Score:** 73

MUSE investigates how much capability can be elicited from a frozen MLLM purely through improved execution scaffolding — without any weight updates. It introduces a unified agentic harness with learnable interface modules (structured perception, action decomposition, iterative verification loops) that wrap a frozen MLLM and handle tasks like grid maze navigation or multi-step puzzle solving that the base model fails at. The key finding is that the execution scaffold matters as much as model capacity: a frozen medium-sized MLLM with a well-designed harness outperforms a larger bare model. Directly relevant as a design template for wrapping any MLLM with an agentic layer for research tasks.

---

### JAVEDIT: Joint Audio-Visual Instruction-Guided Video Editing with Agentic Data Curation
**arXiv:** [2606.03168](https://arxiv.org/abs/2606.03168)
**Authors:** Yinan Chen, Chuming Lin, Zhennan Chen, Yuxiang Zeng, Junwei Zhu et al.
**Score:** 78

JAVEDIT introduces JAVEdit-100k, the first large-scale dataset (100K clips) for instruction-guided joint audio-visual video editing, built entirely via an agentic data curation pipeline that automatically filters, annotates, and pairs raw video clips with editing instructions without human labeling. The agentic pipeline demonstrates how LLM-driven automation can replace manual dataset construction for multimodal tasks — a pattern directly applicable to building training data for research agent systems. The accompanying editing model supports simultaneous instruction-guided modification of both visual and audio streams in human-centric videos.

---

## 2026-06-08

### Skill-3D: Evolving Scene-Aware Skills for Agentic 3D Spatial Reasoning
**arXiv:** [2606.07436](https://arxiv.org/abs/2606.07436)
**Authors:** Haoyuan Li, Zhengdong Hu, Jun Wang, Hehe Fan, Yi Yang
**Score:** 76

Identifies a core failure mode in agentic 3D spatial reasoning: MLLM agents apply a uniform tool-use strategy regardless of scene, missing that 3D tasks are heterogeneous across environments. Skill-3D addresses this with a self-evolving Scene Memory: successful tool-use trajectories from similar scenes are distilled into reusable scene-aware skills, while failures are attached as lessons. The co-evolution loop between memory and skill library drives tool utilization from 39% to 78% on VSI-Bench and boosts Gemini-3-Flash by 67% on MMSI-Bench. Relevant as a framework for adapting agentic tool use to domain-specific task distributions.

---

### MemDreamer: Decoupling Perception and Reasoning for Long Video Understanding via Hierarchical Graph Memory and Agentic Retrieval Mechanism
**arXiv:** [2606.07512](https://arxiv.org/abs/2606.07512)
**Authors:** Cong Chen, Guo Gan, Kaixiang Ji, ChaoYang Zhang, Zhen Yang, Guangming Yao, Hao Chen, Jingdong Chen, Yi Yuan, Chunhua Shen
**Score:** 72

MemDreamer shifts long-video understanding into an agentic exploration paradigm by decoupling perception from reasoning: streaming video builds a Hierarchical Graph Memory (three-tier semantic abstraction with spatiotemporal/causal edges), while inference uses an Observation-Reason-Action loop to navigate the graph and retrieve only what is needed. Constraining the reasoning context to 2% of full-context input still yields a 12.5-point accuracy gain. The finding of a strong positive linear correlation between logic reasoning capability and long-video understanding suggests agentic capability scaling as a new training paradigm — relevant to any LLM-driven retrieval and multi-step reasoning agent.

---

### GOPAgen: Motion-Aware and Efficient Agentic Long-Video Understanding with Structural Memory and Hierarchical Reasoning
**arXiv:** [2606.06532](https://arxiv.org/abs/2606.06532)
**Authors:** Haozhe Chi, Yang Jin, Yadong Mu
**Score:** 71

GOPAgen integrates video codec structure into agentic video understanding: a motion agent trained on Groups of Pictures (GOPs) captures detailed local motion, a GOP tree reasoning algorithm provides hierarchical navigation, and a structural memory with coarse-to-fine zoom-in enables efficient retrieval. A motion vector database supports multi-granularity retrieval. Achieves state-of-the-art on MotionBench and Egoschema. The codec-native memory architecture is a concrete example of incorporating domain-specific efficient representations into an agentic framework.

---

---

## 2026-06-09

### VideoWeaver: Evaluating and Evolving Skills for Agentic Long Video Generation
**arXiv:** 2606.08091 | **Authors:** Jianhui Wei, Jie Tan, Hengchuan Zhu, Xiaotian Zhang, Yan Zhang, Ziyi Chen, Daoan Zhang, Wei Xu, Zuozhu Liu

The first systematic study of whether general-purpose coding agent frameworks (Claude Code, Codex, OpenClaw) can handle long video generation as a long-horizon multimodal task. Introduces VideoWeaver, a benchmark (16 categories, 285 cases) and agent harness where agents compose and evolve their own skill workflows rather than following fixed pipelines, plus an agent-as-judge that evaluates both execution traces and final videos. Skill evolution via agent feedback meaningfully improves long video quality, and the framework establishes a research agenda at the intersection of agentic AI and video generation.

---

### Crayotter: Traceable Multi-Agent Workflows for Long-Form Video Editing
**arXiv:** 2606.07636 | **Authors:** Lecheng Yan, Yichong Zhang, Ben Pan, Xiaoyu Zheng, Jiawei Qian, Anqi Wu, Wenxi Li, Chenyang Lyu

Open-source multi-agent system for prompt-driven long-form video editing with three phases (material preparation → editing research → timeline execution), each externalizing inspectable artifacts for diagnostic replay. Agents can selectively revise failed segments without restarting, and a trajectory-level RLVR design prepares these workflows for future policy optimization. Scores 3.40/5 vs 2.44 and 1.70 for competing baselines in human evaluation on 23 editing themes.

---

### ViMax: Agentic Video Generation
**arXiv:** 2606.07649 | **Authors:** Lingxuan Huang, Sizhe He, Hengji Zhou, Liqiang Nie, Lianghao Xia, Chao Huang

Multi-agent video generation framework that addresses long-form narrative video creation through hierarchical narrative planning with retrieval-augmented generation and a dependency-aware visual consistency mechanism tracking character and environment states. Specialized VLM-guided agents coordinate narrative decisions, visual continuity, and production quality; spatial coherence is maintained through transition videos between scenes. Directly addresses "catastrophic semantic forgetting" in current video generators via principled multi-agent coordination.

---

### Struct-Searcher: Agentic Structural Thinking Advances Multimodal Deep Information Seeking
**arXiv:** 2606.07689 | **Authors:** Fan Zhang, Vireo Zhang, Shengju Qian, Haoxuan Li et al.

Plug-and-play agentic workflow grounded in belief revision theory that maintains an evolving multimodal structural graph throughout deep information seeking, enabling conflict-aware resolution when text and visual evidence contradict each other. Unlike evidence accumulation agents that linearly aggregate information, Struct-Searcher explicitly detects and resolves contradictions via graph updates grounded in formal belief revision. Achieves +17.2% average relative accuracy improvement on BrowseComp-VL across five backbone models without retraining.

---

### SceneConductor: 3D Scene Generation from Single Image with Multi-Agent Orchestration
**arXiv:** 2606.08402 | **Authors:** Jeonghwan Kim, Yushi Lan, Yongwei Chen, Hieu Trung Nguyen, Chuanyu Pan, Xingang Pan

Multi-agent orchestration framework for single-image 3D scene generation with three stages: initialization, environment construction, and multi-agent refinement where a planner agent routes simple fixes directly and dispatches specialist agents for complex localized revisions. Demonstrates that agent-based decomposition outperforms holistic or weakly-decomposed pipelines on geometric accuracy and perceptual realism on standard benchmarks. The specialist-agent routing pattern is a scalable solution to the complexity-growth problem in 3D scene generation.

---

### A Case Study of Evaluating AI Agents on a Neuroscience Data-to-Discovery Pipeline
**arXiv:** 2606.07718 | **Authors:** Kai A. Horstmann, Ethan Lin, Alice A. Robie, Jennifer J. Sun et al.

Empirical evaluation of general-purpose coding agents on a real fly optogenetics data-to-discovery pipeline with datasets orders of magnitude larger than typical benchmarks and domain-expert-grounded evaluation criteria. Agents can handle individual pipeline stages but fail end-to-end; the key failure mode is when no predefined iteration criterion exists and agents must apply scientific judgment to assess their own intermediate outputs. Distills principles for constructing scientific agent benchmarks and identifies computational resource management and visual self-evaluation as critical open challenges for AI scientist systems.

---

### PhysAgent: Automating Physics-Based 4D Synthesis via Trajectory-Grounded Multi-Agent Feedback
**arXiv:** 2606.08688 | **Authors:** Chunji Lv, Jiaxi Ye, Yuchen Jiang, Rexar Lin, Changsheng Li

First simulator-in-the-loop multi-agent framework for automated physics-based 4D synthesis, using a Semantic Agent for force field initialization and Trajectory-Grounded Refine Agents that extract dense point trajectories from rendered frames and use LLM reasoning for zero-shot force field optimization. Eliminates the manual configuration bottleneck in physics-based 4D synthesis by fully decoupling material properties from extrinsic force fields and closing the optimization loop through physical simulation feedback. Significantly outperforms existing baselines in generation diversity and physical accuracy.

---

### IEA: Amateur-Friendly Conversational Image Editing Agent
**arXiv:** 2606.08016 | **Authors:** Zichen Zhu, Yuheng Sun, Mingxuan Zhu, Wenjie Ma et al.

Conversational image editing agent designed for non-expert users via three-stage multitask alignment: intent understanding, edit planning, and instruction-following execution. Bridges the gap between user intent and generative model outputs by making the editing process interactive and transparent, explaining why edits were applied. Demonstrates that conversational agentic interaction significantly reduces artifacts and stylistic drift compared to single-round generation.

---

### Visual Para-Thinker++: Single-Policy Multi-Agent Framework for Visual Reasoning
**arXiv:** 2606.09290 | **Authors:** Haoran Xu, Hongyu Wang, Yifei Gao, Jiaze Li et al.

Single shared MLLM policy instantiated as multiple parallel reasoning agents that integrate visual evidence from different regions, attributes, and relations, avoiding early perceptual commitment and hallucination in single-chain reasoning. Each agent explores a different reasoning path simultaneously, and a consensus mechanism aggregates the parallel evidence streams. Demonstrates consistent improvement over single-chain baselines on visual reasoning benchmarks.

---

### Claude Code-Driving Scenario Mining for the Argoverse 2 Challenge
**arXiv:** 2606.09180 | **Authors:** Wei Deng, Caoshengzhe Xue, Shuaikun Liu, Zhaohong Liu et al.

CVPR 2026 challenge system submission using a Claude Code agent for autonomous code generation in a four-stage pipeline: iterative code generation → training set screening → dataset extension → evaluation. Demonstrates that a coding agent can autonomously navigate the full scenario mining pipeline with iterative self-improvement via threshold-based curation. Provides a practical case study of Claude Code-style agents for data-curation automation in autonomous driving research.

---

## 2026-06-10

### Data Journalist Agent: Transforming Data into Verifiable Multimodal Stories
**arXiv:** [2606.11176](https://arxiv.org/abs/2606.11176)
**Authors:** Kevin Qinghong Lin, Batu EI, Yuhong Shi, Pan Lu, Philip Torr, James Zou
**Score:** 82

Data2Story is a 7-agent virtual newsroom (Detective, Analyst, Editor, Designer, Programmer, Auditor, Inspector) that takes a raw dataset and produces an interactive multimedia news article where every claim is traceable back to executable code or a source URL. The Inspector agent is the key innovation: it binds each published HTML fragment to the exact code line or external reference that generated it, achieving claim-level auditability that even carefully crafted human articles rarely provide. A human study (53 participants, 18 articles) finds Data2Story competitive with professional journalists on transparency and verifiability while human articles retain an edge in editorial angle and design.

---

### A History-Aware Visually Grounded Critic for Computer Use Agents
**arXiv:** [2606.11078](https://arxiv.org/abs/2606.11078)
**Authors:** Jaewoo Lee, Zaid Khan, Archiki Prasad, Justin Chih-Yao Chen, Supriyo Chakraborty, Kartik Balasubramaniam
**Score:** 81

HiViG is a test-time critic for Computer Use Agents that addresses two overlooked failure modes in existing critic models: short-sighted planning (forgetting earlier actions) and lack of visual grounding (approving logically correct but spatially misaligned actions). The critic is trained on 52K GUI trajectory samples and at test time recursively compresses past interactions into macro-action histories while visually verifying proposed action coordinates against a rendered marker on the screenshot. HiViG improves Gemini-3-Flash on WebArenaLitev2 by 15% absolute (30.5%→45.5%) and outperforms all baseline critics by 9% average across web, mobile, and desktop — a notable result for long-horizon GUI automation.

---

### 3D-CoS: A New 3D Reconstruction Paradigm Based on VLM Code Synthesis
**arXiv:** [2606.10478](https://arxiv.org/abs/2606.10478)
**Authors:** Yuhao Wang, Puyi Wang, Linjie Li, Zhengyuan Yang, Kevin Qinghong Lin, Yu Cheng
**Score:** 74

3D-CoS proposes constructing 3D assets as executable Blender code rather than neural representations (NeRF, point clouds, meshes) — a programmatic medium that is interpretable, controllable, and directly editable at the part level. The paper systematically evaluates VLMs on code-based 3D reconstruction across four synthesis workflows: blueprint-based planning, RAG over Blender API documentation, few-shot geometric demonstrations, and a component-level agent workflow for part-wise code generation. Code-based 3D representation shows strong edit fidelity and locality for targeted text-driven modifications, establishing a new direction at the intersection of VLM code synthesis and 3D generation.

---

## 2026-06-11

### InternVideo3: Agentify Foundation Models with Multimodal Contextual Reasoning
**arXiv:** [2606.12195](https://arxiv.org/abs/2606.12195)
**Authors:** Ziang Yan, Sheng Xia, Jiashuo Yu, Yue Wu, Tianxiang Jiang, Songze Li, Kanghui Tian, Yicheng Xu, Yinan He, Kai Chen, Limin Wang, Yu Qiao, Yi Wang
**Score:** 85

InternVideo3 introduces Multimodal Contextual Reasoning (MCR), a closed-loop formulation where multimodal observations, instructions, intermediate reasoning, tool actions, feedback, and memory all share one evolving context — treating long-video understanding as iterative evidence accumulation and belief revision rather than single-pass prediction. Complementing MCR, M²LA (Multimodal Multi-head Latent Attention) compresses KV-cache states via RoPE-aware positional aggregation and low-rank latent factorization, enabling efficient long-horizon rollouts without discarding full token streams. A staged training recipe (continued pretraining → short-to-long SFT → rule-based RL → on-policy distillation) yields strong results on Video-MME, MLVU, and EgoSchema, and a video agent instantiation demonstrates how recursive multimodal reasoning supports robust evidence-grounded tool use.

---

### DIRECT: When and Where Should You Allocate Test-Time Compute in Embodied Planners?
**arXiv:** [2606.12402](https://arxiv.org/abs/2606.12402)
**Authors:** Jadelynn Dao, Milan Ganai, Yasmina Abukhadra, Ajay Sridhar, Mozhgan Nasr Azadani, Katie Luo, Clark Barrett, Jiajun Wu, Chelsea Finn, Marco Pavone
**Score:** 80

DIRECT shows that the three dominant test-time compute axes for embodied VLM planners — chain-of-thought depth, model size, and memory context — are qualitatively distinct and non-interchangeable: CoT depth helps on tasks with implicit spatial/semantic constraints, model size governs skill breadth, and memory helps on history-dependent tasks but can hurt elsewhere. Building on this diagnostic, the paper introduces a lightweight multimodal router that allocates per-task compute by matching each task's inferred cognitive demands to the cheapest capable VLM configuration. Physical Franka arm validation (DROID setup) shows DIRECT matches frontier model success rates at up to 65% lower average latency — a practical blueprint for deploying efficient agentic systems under real-world constraints.

---

### DrivingAgent: Design and Scheduling Agents for Autonomous Driving Systems
**arXiv:** [2606.12236](https://arxiv.org/abs/2606.12236)
**Authors:** Zhongyu Xia, Wenhao Chen, Yongtao Wang, **Ming-Hsuan Yang**
**Score:** 75

DrivingAgent addresses two bottlenecks that arise when incorporating foundation models into autonomous driving: the labor-intensive manual design/integration process and the lack of intelligent scheduling strategies for multi-model pipelines. The paper proposes an agent-based framework that automates both the design of new model integrations and the runtime scheduling of foundation models, adapting to diverse driving scenarios and long-tail cases. Notable: co-authored by close collaborator Ming-Hsuan Yang.

---

## 2026-06-12

### InterleaveThinker: Reinforcing Agentic Interleaved Generation
**arXiv:** [2606.13679](https://arxiv.org/abs/2606.13679)
**Authors:** Dian Zheng, Harry Lee, Manyuan Zhang, Kaituo Feng, Zoey Guo, Ray Zhang, Hongsheng Li
**Score:** 92

InterleaveThinker introduces the first multi-agent pipeline that endows any existing image generator with interleaved text-image generation capabilities by deploying a planner agent (organizes multi-step plans) and a critic agent (detects deviations and refines instructions) in a closed loop. RL training with GRPO on single-step critic corrections effectively guides trajectories spanning 25+ generator calls without full-trajectory optimization, achieving GPT-5-comparable performance on interleaved generation benchmarks. The paradigm — plan, generate, critique, refine — generalizes across generator architectures and delivers surprising gains on visual reasoning benchmarks beyond interleaved generation.

---

### SpatialClaw: Rethinking Action Interface for Agentic Spatial Reasoning
**arXiv:** [2606.13673](https://arxiv.org/abs/2606.13673)
**Authors:** Seokju Cho, Ryo Hachiuma, Abhishek Badki, Hang Su, Byung-Kwan Lee, Chan Hee Song, Sifei Liu, Subhashree Radhakrishnan, Seungryong Kim, Yu-Chiang Frank Wang, Min-Hung Chen
**Score:** 83

SpatialClaw demonstrates that the choice of action interface is a primary driver of agentic spatial reasoning performance: code-as-action with a stateful Python kernel outperforms both single-pass code (no mid-course correction) and structured tool-calls (limited compositionality) by +11.2 points across 20 benchmarks. The framework is training-free and generalizes to 6 VLM backbones, suggesting the interface design principle — persistent kernel, per-step execution, observation of all prior outputs — is model-agnostic. This is a concrete design lesson for building agentic systems that need to reason iteratively over structured tool outputs.

---

### ComAct: Reframing Professional Software Manipulation via COM-as-Action Paradigm
**arXiv:** [2606.13239](https://arxiv.org/abs/2606.13239)
**Authors:** Jiaxin Ai, Tao Hu, Xuemeng Yang, Shu Zou, Hairong Zhang
**Score:** 77

ComAct identifies the Component Object Model (COM) as a unified executable abstraction for professional software (CAD, Office, etc.), proposing COM-as-Action: reframing software interaction as deterministic program synthesis rather than sequential visual GUI control. Frontier models achieve near-zero success under GUI-based interaction on the new ComCADBench benchmark, while COM-based execution yields substantial immediate gains; ComActor (a self-correcting agent via progressive 3-stage training) further closes the gap to geometric accuracy. This paradigm shift from visual fragility to deterministic API synthesis is directly relevant to agentic AI for professional tool use.

---

### IterCAD: An Iterative Multimodal Agent for Visually-Grounded CAD Generation and Editing
**arXiv:** [2606.13368](https://arxiv.org/abs/2606.13368)
**Authors:** Tao Hu, Jiaxin Ai, Licheng Wen, Xueheng Li, Shu Zou
**Score:** 73

IterCAD formulates CAD generation and editing as a closed-loop multi-turn interaction between a multimodal agent and an executable CAD sandbox, covering drawing-to-code, text-to-code, and interactive editing tasks. Progressive SFT followed by geometry-aware RL with viable-prefix masking trains the agent to produce executable, geometrically precise code across multiple interaction turns. The IterCAD-Bench benchmark introduces the CD-TR curve (Chamfer Distance Tolerance-Recall) as a survivor-bias-free metric unifying code validity and geometric precision — a useful evaluation framework for agentic code generation in structured domains.

---

### Perceive, Interact, Reason: Building Tool-Augmented Visual Agents for Spatial Reasoning
**arXiv:** [2606.12830](https://arxiv.org/abs/2606.12830)
**Authors:** Changye Li, Meng Lu, Yi Wu, Ligeng Zhu
**Score:** 73

PERIA is a tool-augmented visual agent for spatial reasoning that trains multi-tool behavior via OR-GIGPO (Observation-Relaxed Group-in-Group Policy Optimization), combining supervised tool-use trajectory synthesis with composite rewards. PERIA-8B improves over its Qwen3-8B backbone by 10.0% on in-distribution and 4.4% on out-of-distribution spatial benchmarks, with performance comparable to much larger models (Qwen3-VL-235B, GPT-5) — demonstrating that targeted RL training for tool use can make small models competitive with frontier models on structured spatial tasks.

---

## 2026-06-15

### MUSE: Agentic 3D Scene Authoring via Memory-Grounded Incremental Requirement Satisfaction
**arXiv:** [2606.14168](https://arxiv.org/abs/2606.14168)
**Authors:** Ruijie Xu, Xinnan Zhu, Jiayu Ying, Daoguo Dong, Yuzhou Ji, Xin Tan
**Score:** 84

MUSE is a multi-agent framework for controllable 3D scene authoring in which an Architect compiles natural language into structured requirement programs, a Sculptor executes local scene operations, and an Inspector verifies each step while updating three persistent memory stores (Working, Scene, Skill). The system formulates scene construction and editing as incremental requirement satisfaction — when a sub-goal fails, Skill Memory guides targeted local retry rather than full-scene regeneration, achieving 80.7 all-goal success (up from 37.9) and 99.9% preservation rate on editing benchmarks.

---

### Orchestra-o1: Omnimodal Agent Orchestration
**arXiv:** [2606.13707](https://arxiv.org/abs/2606.13707)
**Authors:** Fan Zhang, Vireo Zhang, Shengju Qian, Haoxuan Li, Hao Wu, Jinyang Wu, Donghao Zhou, Zhihong Zhu, Zheng Lian, Xin Wang, Pheng-Ann Heng
**Score:** 82

Orchestra-o1 is a multi-agent orchestration framework that enables agent swarms to handle tasks spanning text, image, audio, and video modalities through modality-aware task decomposition and parallel sub-agent specialization. A custom RL training method (DA-GRPO) trains the orchestrator to make high-quality decomposition decisions rather than optimizing only final output, achieving +10.3% over the best prior approach on OmniGAIA and SOTA among all open-source omnimodal agents at 8B scale.

---

### Naive Visual Memory is Not Enough: A Failure-Mode Study of GUI Agents
**arXiv:** [2606.14106](https://arxiv.org/abs/2606.14106)
**Authors:** Seoyoung Choi, Minseok Ko, Hyunseok Lee, Kunwoong Kim, Woomin Song, Chanseok Jeon, Jinwoo Shin
**Score:** 74

This paper introduces a taxonomy of four GUI agent failure modes (cognitive failure, visual state misunderstanding, hidden operation blindness, grounding error) and shows that prepending full-image visual memory to GUI agents has a divergent effect: it reduces state-level failures but worsens action-level ones, particularly hidden operation blindness and grounding errors. The proposed Action-Grounded Visual Memory (AGMem) stores local image crops around successful/recovery actions rather than full screenshots, improving task success by 33.3% over full-image memory on OSWorld.

---

### μ₀: A Scalable 3D Interaction-Trace World Model
**arXiv:** [2606.13769](https://arxiv.org/abs/2606.13769)
**Authors:** Seungjae Lee, Yoonkyo Jung, Jusuk Lee, Jonghun Shin, Amir Hossein Shahidzadeh, Yao-Chih Lee, H. Jin Kim, Jia-Bin Huang, Furong Huang
**Score:** 72

μ₀ is an embodiment-agnostic world model that forecasts 3D trajectories (B-spline traces) for salient interaction keypoints (objects, tools, hands, contact regions) rather than predicting dense pixels or embodiment-specific actions, enabling scalable pretraining from diverse video sources via automated TraceExtract supervision. The frozen μ₀ world model can be paired with lightweight action experts for downstream robot manipulation, achieving performance competitive with VLA models pretrained with action supervision despite requiring no action labels during pretraining.

---

## 2026-06-16

### Qwen-RobotWorld Technical Report: Unifying Embodied World Modeling through Language-Conditioned Video Generation
**arXiv:** [2606.17030](https://arxiv.org/abs/2606.17030)
**Authors:** Jie Zhang, Xiaoyue Chen, Anzhe Chen, Chenxu Lv, Deqing Li, Gengze Zhou, Hang Yin, Haoqi Yuan, Haoyang Li, Jiahao Li et al. (Qwen Team)
**Score:** 85

Qwen-RobotWorld is a language-conditioned video world model for embodied intelligence that treats natural language as a universal action interface, enabling a single 60-layer double-stream MMDiT to predict physically grounded future visual trajectories across robotic manipulation, autonomous driving, indoor navigation, and human-to-robot transfer. The key architectural insight is coupling a frozen Qwen2.5-VL backbone with video-VAE latents through layer-wise joint attention, while training on the 8.6M-video EWK corpus (200M+ frames, 20+ embodiments, 500+ action categories) via a general+expert progressive curriculum. Achieves 1st place on EWMBench and DreamGen Bench; most directly relevant as a blueprint for scalable synthetic data generation for robot policy training and cross-embodiment world knowledge transfer.

---

### DreamX-World 1.0: A General-Purpose Interactive World Model
**arXiv:** [2606.16993](https://arxiv.org/abs/2606.16993)
**Authors:** DreamX Team, Yancheng Bai, Rui Chen, Xiangxiang Chu, Rujing Dang, Hao Dou, Bingjie Gao, Qiwen Gu, Siyu Hong, Jiachen Lei et al.
**Score:** 85

DreamX-World 1.0 is a streaming interactive world model (up to 16 FPS on 8× RTX 5090) built from Wan2.2 with five progressive training stages: camera control (E-PRoPE), long-horizon scene persistence (camera-geometry memory + residual recycling), composable event control (structured event instruction tuning), autoregressive distillation (causal forcing + DMD), and RL alignment for post-distillation quality recovery. The five-stage progressive pipeline — where each capability is an independent stage and RL is the final quality-recovery layer — is a reusable recipe for converting any large video diffusion backbone into a deployable interactive world model. Relevant to agentic AI as a real-time simulation substrate for embodied agents requiring persistent spatial memory.

---

### Kairos: A Native World Model Stack for Physical AI
**arXiv:** [2606.16533](https://arxiv.org/abs/2606.16533)
**Authors:** Kairos Team, Fei Wang, Shan You, Qiming Zhang, Tao Huang, Zuoyi Fu, Zhisheng Zheng, Yunlong Xi, Feng Lv, Xiaoming Wu et al.
**Score:** 84

Kairos provides both a theoretical foundation and a complete practical system for world models as deployable physical-AI infrastructure. The core theoretical contribution is a formal proof that local continuation heuristics are provably insufficient for long-horizon state maintenance (irreducible excess risk), motivating the Hybrid Linear Temporal Attention (HLTA) architecture — gated linear attention for persistent global memory + dilated/standard sliding-window for local dynamics — which bounds error accumulation across extended horizons. Training follows a three-stage cross-embodiment curriculum (physical pretraining → human-centric embodied pretraining → joint world-action training), with deployment-aware inference optimizations for both server-grade and consumer hardware. Code and models available at https://github.com/kairos-agi/kairos-sensenova.

---

### Context-Aware RL for Agentic and Multimodal LLMs
**arXiv:** [2606.17053](https://arxiv.org/abs/2606.17053)
**Authors:** Peiyang Xu, Bangzheng Li, Sijia Liu, Karthik R. Narasimhan, Pramod Viswanath et al.
**Score:** 75

ContextRL trains agentic and multimodal LLMs to identify and attend to the single decisive piece of evidence in long or complex contexts — a tool trace line, a subtle image detail, a specific passage — that determines the correct answer. Applied to both text-only agentic settings (tool traces) and multimodal settings, ContextRL is a targeted remedy for the failure mode where frontier LLMs give wrong answers despite the answer being present in context because they fail to locate the critical evidence. Directly relevant to long-horizon agentic loops where the agent must act on evidence buried in large observation histories.

---

## 2026-06-17

### OmniDrive (DRIVE-CHOREO): LLM-Choreographed Multi-Agent World Model for Multi-View Driving Video Generation
**arXiv:** [2606.17536](https://arxiv.org/abs/2606.17536)
**Authors:** Zijie Meng, Yufei Liu, Chengqian Ma, Zhiyu Li, Jiyuan Liu, Wenhua Nie, Bingcai Wei, Shuqin Chen, Weichen Xu, Jiquan Yuan, Miao Zhang
**Score:** 76

DRIVE-CHOREO introduces a three-agent LLM pipeline (Director parsing user intent into structured WorldScript, Cartographer grounding it into spatially-anchored layout tokens, Auditor feeding cross-view critiques back as auxiliary supervision) that jointly authors a position-aware token sequence for controllable multi-view driving video generation. All control signals — free-form language, HD-maps, trajectories, camera poses — are unified into a single symbolic interlingua aligned at the latent-token level, co-compressed with multi-view video via a view-time permutation enforcing inter-camera geometry within a 3-D VAE. Sets new state-of-the-art multi-view consistency and BEV mAP (21.6) on nuScenes; the three-agent Director/Cartographer/Auditor decomposition is a reusable pattern for LLM-orchestrated generative pipelines.

---

### ProCUA-SFT Technical Report: Computer-Use Agent Supervised Fine-Tuning
**arXiv:** [2606.17321](https://arxiv.org/abs/2606.17321)
**Authors:** Jaehun Jung, Ximing Lu, Brandon Cui, Muhammad Khalifa, Shaokun Zhang, Hao Zhang, Jin Xu, Amala Sanjay Deshmukh, Karan Sapra, Andrew Tao, Yejin Choi, Jan Kautz, Mingjie Liu, Yi Dong
**Score:** 73

ProCUA-SFT is a 3.1M step-level SFT dataset for computer-use agents produced by a fully-automated pipeline: a single VLM (Kimi-K2.5) serves as goal generator, precondition judge, and trajectory executor across 2,484 application combinations on live desktops seeded with real-world content, distilling 93K synthetic trajectories into step-prefix samples that exactly reproduce inference-time context layouts. Fine-tuning UI-TARS 7B for one epoch yields 45.0% on OSWorld — an 18.7 percentage-point improvement over the base model and >35% above AgentNet-trained counterparts, demonstrating that automated SFT data generation at this scale is sufficient to substantially improve computer-use performance. The finding that human-collected AgentNet data (22.5K trajectories) causes negative transfer while synthetic data at 4× scale causes strong positive transfer is a key empirical data point for automated agent training pipelines.

---

### GASE: Gaussian Splatting-Based Automated System for Embodied Simulation Environment Construction
**arXiv:** [2606.17520](https://arxiv.org/abs/2606.17520)
**Authors:** Jiawei Zhang, Yiming Yan, Chao Liang, Nuo Xu, Seson Sun, Qichen Zhang, Yuhao Xu, Yantai Yang, Yingqiao Wang, Qin Jin, Zhipeng Zhang
**Score:** 70

GASE is a highly automated pipeline for constructing high-fidelity simulation environments from multi-view panoramic video, using a camera-pose-based 2D strategy for robust foreground object extraction, high-quality scene inpainting, and independent 3DGS reconstruction of objects and background before import into physics simulators. Outperforms existing 3DGS-based methods in segmentation accuracy by over 10% while achieving state-of-the-art inpainting quality; real-robot deployment on manipulation and navigation tasks shows <10% performance gap vs. policies trained on real-world data. Directly addresses the automated sim-to-real pipeline bottleneck, enabling scalable robot training data generation without skilled operators or expensive hardware.

---

### AnnotateAnything: Automatic Annotation of 3D Assets for Robot Manipulation
**arXiv:** [2606.17446](https://arxiv.org/abs/2606.17446)
**Authors:** Haoran Lu, Mutian Shen, Shuyang Yu, Yu Xiao, Songling Liu, Jianshu Zhang, Shang Wu, Yue Chen, Guo Ye, Jiayi Wang, Zhaoran Wang, Han Liu
**Score:** 70

AnnotateAnything converts passive 3D assets into manipulation-ready assets via two complementary pipelines: a visual-language annotation pipeline using VLM reasoning to infer semantics, interaction constraints, and 3D-grounded cues; and a massively parallel physics annotation pipeline that generates diverse executable action labels (grasp poses, dexterous contacts, articulation waypoints, insertion directions, hanging affordances, navigation targets) through candidate generation, geometry optimization, and trajectory synthesis. The framework supports downstream affordance detection, robotic VQA, and visual instruction fine-tuning — demonstrating that automated annotation at scale can replace manual labeling across diverse object categories and robot embodiments. The asynchronous parallel simulation data-collection system enables orders-of-magnitude faster dataset construction than existing annotation pipelines.

---

---

## 2026-06-18

### CHIEF: Creator-Driven Recurrent Video Generation with Agentic Feedback Loops
**arXiv:** [2606.18591](https://arxiv.org/abs/2606.18591)
**Authors:** Denis Savytski, Aiden Lei, Heding Liu, Warren Yang, Sihan Liang, Alexander Liu, Zhe Zhao
**Score:** 82

CHIEF is a multi-agent, human-in-the-loop video generation framework where persona-conditioned LLM agents — instantiated from real viewer comment histories (YouTube, Rotten Tomatoes) — simulate diverse audience perspectives and produce structured, urgency-ranked critique that drives iterative prompt refinement across a Video Generator, Feedback Agents, and Feedback Translator pipeline. The key agentic insight is replacing aggregated reward-model feedback with individuated persona simulation, capturing the subjective diversity of real audience sentiment that uniform reward signals miss. Demonstrated with non-expert students producing a 10-minute film rated 4.1/5 by a live audience (vs. 2.4/5 for the unrefined baseline), establishing persona-conditioned multi-agent feedback as a practical substitute for human viewer panels in creative content iteration.

---

### SCPE: Self-Correcting Process Editing — Taming I2V Models for Image HOI Editing
**arXiv:** [2606.19073](https://arxiv.org/abs/2606.19073)
**Authors:** Jiayi Gao, Qingchao Chen, Yuxin Peng, Yang Liu
**Score:** 88

SCPE is an agentic self-correcting framework for Human-Object Interaction image editing that uses I2V models' temporal generation as a "failure replay" mechanism: a Video Analyst diagnoses failure modes (physics violations, incorrect trajectory, wrong entity selection) from generated video, a Critic aggregates these into a dynamic Playbook mapping failure patterns to validated prompting strategies, and the loop iteratively refines instructions until the generated video correctly depicts the target HOI. The framework also introduces HOI-Edit, the first hierarchical benchmark for HOI editing across three cognitive levels (foundational dynamic edits, context spatial understanding, causal and physical reasoning), with HOI-Eval providing grounded pair-wise region-sensitive metrics. Achieves SOTA among open-source models and competitive with commercial SOTA (Google Nano Banana) on interaction metrics; the Playbook-driven iterative refinement pattern is directly transferable to any agentic generative editing pipeline.

---

## 2026-06-19

### Agentic AutoResearch for Space Autonomy: An Auditable, LLM-Driven Research Agent for Aerospace Control Problems
**arXiv:** [2606.20394](https://arxiv.org/abs/2606.20394)
**Authors:** Amit Jain, Richard Linares
**Score:** 83

AutoResearch is an LLM-driven agentic framework in which the model autonomously reads a natural-language problem description and an append-only run history, proposes a single edit to a training script, executes it, and logs the outcome — closing the full hypothesis→experiment→analysis loop for aerospace control problems without any human intervention. Its distinguishing contribution over AI Scientist / FunSearch is a credibility layer embedded inside the loop: per-problem seed noise is measured first, the best configuration is reseeded and reverified, and leave-one-out pruning isolates which individual edits carry each result — making autonomous gains auditable rather than just fast. Demonstrated on CW relative rendezvous and safety-constrained collision-avoidance docking, the framework produces audited policies clearing measured seed noise by many standard deviations, while undirected search yields no feasible policy at all on the harder task; the "family contract" abstraction (description + editable script + single metric + run log) is domain-agnostic and directly reusable.

---

### Automating SKILL.md Generation for Computer-Using Agents via Interaction Trajectory Mining
**arXiv:** [2606.20363](https://arxiv.org/abs/2606.20363)
**Authors:** Yuexing Hao, Xiaomin Li
**Score:** 71

This work studies whether skill libraries for computer-using agents can be automatically mined from interaction trajectory data in a way that actually improves downstream policies, using a three-stage pipeline: GUI trajectory segmentation, clustering of segments into candidate skills, and skill-aware policy training from the resulting annotations. Five of eight mined clusters achieve ≥0.95 purity against ground-truth task labels, validating that automated skill extraction produces readable, coherent skills rather than noise. The framework is a step toward self-improving computer-using agents that build their own explicit skill libraries from logged experience rather than relying on hand-authored documentation.

---

## 2026-06-22

### S-Agent: Spatial Tool-Use Elicits Reasoning for Spatial Intelligence
**arXiv:** [2606.20515](https://arxiv.org/abs/2606.20515)
**Authors:** Yalun Dai, Hao Li, Shulin Tian, Runmao Yao, Yuhao Dong, Fangzhou Hong, Zhaoxi Chen, Fangfu Liu, Baoliang Tian, Dingwen Zhang, Tao Wang, Kim-Hui Yap, Ziwei Liu
**Score:** 91

S-Agent casts the VLM as a semantic planner that iteratively requests spatial evidence from a three-level tool hierarchy (2D perception → 3D geometric lifting → spatial knowledge aggregation), while dual memory — Scene Memory for persistent entity-centric 3D state and Agent Memory for the reasoning trajectory — enables evidence integration across frames and reasoning steps without redundant re-processing. In a training-free setting it improves GPT-5.4 on MMSI-Bench by 4.5%; fine-tuning Qwen3-VL-8B on 300K auto-generated S-Agent trajectories (S-300K) yields S-Agent-8B, a compact model that matches GPT-5.4 and Gemini 3 Pro across multiple spatial benchmarks. The separation of semantic planning from spatial evidence acquisition is a directly exportable architecture for any embodied or spatial reasoning agent, and the trajectory-distillation recipe demonstrates that agentic scaffolds, not model scale alone, can close the gap to frontier models.

---

### Current World Models Lack a Persistent State Core
**arXiv:** [2606.20545](https://arxiv.org/abs/2606.20545)
**Authors:** Jinpeng Lu, Dexu Zhu, Haoyuan Shi, Linghan Cai, Guo Tang, Yinda Chen, Jie Cao, Duyu Tang
**Score:** 76

This position paper exposes a fundamental blind spot in current video world models: they learn to render convincing frames but lack an internal state that evolves decoupled from observation — objects must persist and events must run to their conclusions even when no camera is watching, just as the moon holds its orbit unseen. The paper proposes a new benchmark dimension measuring whether world models maintain hidden object-state beyond what is directly visible, arguing that frame fidelity, motion realism, and camera controllability are necessary but not sufficient for genuine world modeling. The persistent-state requirement is directly relevant to designing agentic world models for long-horizon planning where agents must reason about parts of the world currently outside their observation window.

---

### HumanScale: Egocentric Human Video Can Outperform Real-Robot Data for Embodied Pretraining
**arXiv:** [2606.20521](https://arxiv.org/abs/2606.20521)
**Authors:** Juncheng Ma, Jianxin Bi, Yufan Deng, Xuanran Zhai, Kewei Zhang, Ye Huang, Bo Liang, Shukai Gong, et al.
**Score:** 72

HumanScale demonstrates that egocentric human video — scalable, high-diversity, and low-cost — can outperform teleoperated robot trajectories as pretraining data for embodied foundation models when the embodiment gap is properly addressed. The key finding is that behavioral and environmental diversity in pretraining data matters more than embodiment alignment for downstream policy generalization, reversing the conventional assumption that robot-collected trajectories are irreplaceable. This has direct implications for scaling agentic robotic systems: human video can serve as the primary pretraining source, dramatically reducing the data collection bottleneck that has constrained embodied AI.

---

### EventVLA: Event-Driven Visual Evidence Memory for Long-Horizon Vision-Language-Action Policies
**arXiv:** [2606.20092](https://arxiv.org/abs/2606.20092)
**Authors:** Ganlin Yang, Zhangzheng Tu, Yuqiang Yang, Sitong Mao, Junyi Dong, Tianxing Chen, Jiaqi Peng, Jing Xiong, et al.
**Score:** 71

EventVLA introduces sparse visual evidence memory for VLA policies: rather than buffering all frames or relying on unselective context windows, the system records task-relevant cues (object appearance, occlusion events, key state changes) exactly when they occur as discrete events, enabling long-horizon manipulation policies to retrieve critical information on demand without accumulating visual redundancy. End-to-end training avoids the high latency of decoupled dual-system memory while achieving better task success than dense frame buffers on occlusion-heavy long-horizon tasks. The event-driven selective memory pattern — write on event, read on demand — is applicable to any long-horizon agentic system that must track intermittently observable state.

---

## 2026-06-23

### VideoAgent: All-in-One Framework for Video Understanding and Editing
**arXiv:** [2606.23327](https://arxiv.org/abs/2606.23327)
**Authors:** Hengji Zhou, Lingxuan Huang, Jian Wang, Bing Zhou, Si Wu, Lianghao Xia, Chao Huang
**Score:** 88

VideoAgent is a multi-agent orchestration framework that unifies video understanding and editing through a Shot Planning Agent (coherent narrative decomposition + cross-modal retrieval) and a library of 30+ specialized editing agents assembled via textual-gradient graph optimization. It achieves 87–95% orchestration success across diverse video genres (news, music video, commentary) while reducing API costs by 60%, producing content rated only 4% below human-created videos on human evaluation. The textual-gradient graph optimization technique — which propagates feedback through non-linear agent workflow graphs to adapt pipeline structure without manual specification — is directly applicable to any complex multi-agent research pipeline.

---

### World Action Models: A Survey
**arXiv:** [2606.20781](https://arxiv.org/abs/2606.20781)
**Authors:** Qiuhong Shen, Shihua Zhang, Yue Liao, Qi Li, Zhenxiong Tan, Shizun Wang, Shuicheng Yan, Xinchao Wang
**Score:** 82

This survey taxonomizes World Action Models (WAMs) — embodied predictive-action systems that couple future prediction with control — using a dual framework: a three-way design-philosophy split (Render-and-Decode / Latent-Only / Video-Generation-Free) and a four-axis anatomy (predictive substrate, backbone, action coupling, deployment regime). The key emergent principle is "dream less, act more": the strongest WAMs retain only the minimal predicted future that control requires, trading representational richness for compute and latency efficiency. Seven open challenges are identified including data sourcing for each training stage, memory scalability, and physical plausibility evaluation — providing a direct research roadmap for next-generation agentic world models.

---

### RS-Gen: A Multi-Stage Agentic Framework for Reasoning and Search-Augmented Image Generation
**arXiv:** [2606.23221](https://arxiv.org/abs/2606.23221)
**Authors:** Feifei Bian, Zhimin Zheng, Wei Deng, Daiguo Zhou et al.
**Score:** 79

RS-Gen addresses the failure of standard T2I models on ambiguous intentions, logical reasoning, and OOD knowledge by introducing a multi-stage agentic pipeline that interleaves deep reasoning and real-time search retrieval before and during image generation. The agentic architecture enables the model to autonomously clarify intent, retrieve external information, and iteratively refine generation — moving image synthesis from a single-step mapping to a multi-turn reasoning process. This is an early demonstration of agentic orchestration closing the quality gap in image generation for underspecified or knowledge-intensive prompts.

---

### AIR: Adaptive Interleaved Reasoning with Code in MLLMs
**arXiv:** [2606.23678](https://arxiv.org/abs/2606.23678)
**Authors:** Cong Han, Xiaohan Lan, Haibo Qiu, Yujie Zhong
**Score:** 75

Following the o3 paradigm, AIR enables multimodal large language models to adaptively interleave natural-language reasoning steps with code execution, deciding dynamically when to invoke code rather than committing to a fixed reasoning mode. The adaptive switching — conditioned on problem type and current reasoning state — outperforms both pure-language CoT and always-code baselines on multimodal reasoning tasks. This is a practical architecture for building agentic reasoning loops in MLLMs that need both symbolic precision (code) and semantic flexibility (language).

---

### HoloAgent-0: A Unified Embodied Agent Framework with 3D Spatial Memory
**arXiv:** [2606.23565](https://arxiv.org/abs/2606.23565)
**Authors:** Xiaolin Zhou, Liu Liu, Tingyang Xiao, Wei Feng et al.
**Score:** 75

HoloAgent-0 extends the standard LLM agent loop (reason → tool call → inspect → revise) to physical robots by adding a persistent 3D spatial memory that accumulates scene observations across manipulation steps, enabling spatial reasoning and multi-step object interaction beyond what short context windows allow. The unified framework bridges the gap between digital LLM agents and physical embodied systems without requiring task-specific robot code. As 3D spatial state is a fundamental requirement for any agent operating in the physical world, the spatial memory architecture is a broadly reusable component for embodied agentic systems.

---

### ENVS: Environment-Native Verified Search for Long-Horizon GUI Agents
**arXiv:** [2606.22948](https://arxiv.org/abs/2606.22948)
**Authors:** Yincheng Zhou, Athena Zhuoming Zhong, Shijie Zhang, Kevin Zhang et al.
**Score:** 72

ENVS frames long-horizon GUI agent tasks as trajectory discovery in live desktop environments, using environment-native execution feedback (not simulated rollouts) to verify intermediate actions and guide search through the exponentially large action space. The key insight is that real execution feedback is both cheaper and more reliable than model-based verification for GUI tasks, where visual state changes are the ground truth. The verified search approach — discovering successful trajectories by executing and checking rather than hallucinating outcomes — is directly applicable to any agentic system that controls real software through observation-action loops.

---

## 2026-06-24

### Sol Video Inference Engine: Agent-Native Full-Stack Acceleration Framework for Efficient Video Generation
**arXiv:** [2606.23743](https://arxiv.org/abs/2606.23743)
**Authors:** Yitong Li, Junsong Chen, Haopeng Li, Haozhe Liu, Jincheng Yu, Ligeng Zhu, Ping Luo, Song Han, Enze Xie
**Score:** 83

Sol Video Inference Engine is a multi-agent system that automatically discovers instance-optimal acceleration stacks for video diffusion models: parallel skill agents each optimize one technique (caching, sparse attention, token pruning, quantization, kernel fusion), and an agent integrator composes them via global search, with a human validator in the loop. The framework replaces the multi-team manual engineering traditionally required to deploy video models on new hardware, achieving >2× speedup with near-lossless quality across three diverse models (64B, 22B, 2B). This is a compelling demonstration of agentic AI applied to AI infrastructure — the configuration space for video diffusion acceleration is too large for humans to explore manually, but well-suited to autonomous agent-driven search.

---

### VisCritic: Visual State Comparison as Process Reward for GUI Agents
**arXiv:** [2606.24525](https://arxiv.org/abs/2606.24525)
**Authors:** Jiachen Qian
**Score:** 78

VisCritic introduces a visual process reward model for GUI agents that verifies action success by directly comparing pre-action and post-action screenshots in feature space using a Siamese vision transformer, rather than relying on textual reasoning alone about GUI state changes. The Action-Aware Critic Head jointly evaluates action success, task progress, and error type, and weak supervision from existing trajectories enables training without additional human labels. The plug-and-play design improves diverse GUI agents across five benchmarks, addressing a core bottleneck for long-horizon task automation.

---

### Agentic Collaborative Cognition for Zero-Shot 3D Understanding
**arXiv:** [2606.24649](https://arxiv.org/abs/2606.24649)
**Authors:** Wenxin Wang, Bo Zhang, Feng Chen, Zixuan Wang, Wen Li, Changsheng Li, Yinjie Lei
**Score:** 76

A two-agent system for zero-shot 3D scene understanding: a Planning Agent selects query-relevant viewpoints and supplements missing perspectives based on a cognitive map, while a Perception Agent builds a structured holistic map with consistent object identifiers across viewpoints and provides feedback to filter candidates and guide further exploration. The closed-loop iterative collaboration outperforms single-agent and retrieval-only baselines by 11.1% Acc@0.5 on ScanRefer and 14.6 BLEU-1 on 3D dialog, demonstrating that structured multi-agent collaboration with explicit feedback channels substantially improves agentic 3D perception.

---

### Autonomous Video Generation with Counterfactual Controllability for Self-Evolving World Models
**arXiv:** [2606.24152](https://arxiv.org/abs/2606.24152)
**Authors:** Xin Wang, Wenxuan Liu, Tongtong Feng, Wenwu Zhu
**Score:** 75

Position paper arguing that video generation models learn a partial, implicit world model — but not a grounded or controllable one — because scaling visual prediction alone does not yield agents that can ask "what would happen under action X." The authors define counterfactual controllability as the decisive criterion for self-evolving world models: generating futures that survive embodiment constraints and feed resulting action knowledge back into future imagination. The framing clarifies the gap between current video generation and truly agentic world modeling, and suggests that counterfactual data and intervention-based training are the missing ingredients.

---
