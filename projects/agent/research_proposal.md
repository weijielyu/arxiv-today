# Research Proposal: Agentic Acceleration of Video/Image Generation Models

**Author:** Weijie Lyu | **Internship end:** 2026-08-14 | **Last updated:** 2026-05-26

---

## 1. Motivation

Acceleration methods (quantization, pruning, efficient attention, operator fusion) are among the most practically impactful techniques in computer vision, yet unlike other methods they do not transfer across hardware. A new attention mechanism or loss function works wherever the model runs; the same acceleration technique may deliver large speedups on an H100 but little benefit on an A100, an M-series chip, or a mobile NPU, because performance depends on memory bandwidth, compute density, kernel support, and compiler behavior that vary fundamentally between devices.

This creates a structural problem: every published acceleration method is a point solution, tuned and validated for one hardware configuration. Reproducing state-of-the-art acceleration on a new device requires re-profiling, re-tuning, and often re-implementing from scratch. The field produces methods, not methodology.

The right response is to build **a way to find the solution**: an adaptive agent that takes a model and a target device and automatically discovers the best acceleration configuration for that context. Agents are a natural fit because the optimization space (quantization schemes, pruning patterns, kernel choices, compilation flags) is too large for manual search; the feedback signal (latency and generation quality) is automatically measurable; iterative refinement is natural; and the objective is well-defined (improve the speed-quality Pareto frontier for a given device).

No existing work applies an agent loop to accelerating image or video generation models. All current methods (TaylorSeer [9], ClusCa [10], LAPTOP-Diff [14], Taming DiT for Mobile [12], etc.) are hand-designed and fixed.

---

## 2. Problem Statement

**Given:** A video or image generation model (e.g., a DiT-based text-to-video model) and a target hardware configuration.

**Find:** An acceleration configuration that maximizes generation quality subject to a latency/memory budget, or maximizes speed subject to a quality floor, for that specific device.

**How:** An agentic loop that autonomously proposes, implements, evaluates, and iterates over acceleration strategies, guided by a research agent reasoning over experiment history and relevant literature.

---

## 3. Pipeline

The system has four components operating in **a closed loop**. Human involvement is limited to defining the initial model and device target.

```
┌─────────────────────────────────────────────────────────────────┐
│                        Research Agent                           │
│  (analyzes history, proposes next strategy, issues instructions)│
└────────────────────────┬────────────────────────────────────────┘
                         │ instructions
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│                      Code-Writing Agent                         │
│  (implements the proposed acceleration change on the model)     │
└────────────────────────┬────────────────────────────────────────┘
                         │ modified model code
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│                      Experiment Runner                          │
│  (executes the model: generates N images/clips, measures time)  │
└────────────────────────┬────────────────────────────────────────┘
                         │ outputs + timing
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│                     Evaluation Agent                            │
│  (measures speed: latency/throughput/memory;                    │
│   measures quality: FID/FVD or VLM perceptual feedback)         │
└────────────────────────┬────────────────────────────────────────┘
                         │ metrics
                         └──────────────────────► Research Agent
                                                   (next cycle)
```

### 3.1 Code-Writing Agent

Receives a natural-language instruction and implements the change in the model codebase. Must handle multi-file repositories and self-debug: if the modified code fails to run, the agent diagnoses and fixes the error before handing off to the runner [6].

### 3.2 Experiment Runner

Runs a fixed evaluation protocol on the target device: generate N prompts (identical across all experiments), record wall-clock latency, peak memory, and throughput, and save outputs for quality evaluation. A fixed protocol ensures experiments are directly comparable [1].

### 3.3 Evaluation Agent

Two components:
- **Speed evaluator:** parses profiling logs into latency, throughput, and memory footprint.
- **Quality evaluator:** computes FID/FVD against a reference set, or uses a VLM for perceptual feedback.

A change is accepted only if Pareto-dominant (does not worsen either dimension). The analysis agent is kept separate from the hypothesis agent so it stays grounded in measured results [3].

### 3.4 Research Agent

- **Experiment log:** record each cycle's strategy, before/after metrics, acceptance decision, and reasoning [1].
- **Analysis:** understand why a change worked or failed (e.g., INT8 helped because the bottleneck was memory bandwidth on this device, not compute).
- **Proposal:** select the next experiment from the action space (quantization, attention kernel replacement, caching, pruning, distillation, compilation flags). Techniques for generating and selecting proposals:
  - *Tournament-based ranking* [2]: generate 3-5 candidate strategies, debate their expected impact against experiment history, implement only the winner.
  - *Two-speed literature access* [3]: before proposing a technique, check whether it has been applied to this model class or device target. Crow does a quick broad scan; Falcon does a full deep read of the most relevant papers.
  - *Progressive tree search* [5]: maintain a tree of experiment branches rather than a single chain; prune underperforming branches to avoid local optima.
  - *RAG over experiment history* [7]: retrieve past successful strategies before generating new proposals, rather than relying solely on LLM prior.

---

## 4. Key Open Questions

### 4.1 Action space definition

What acceleration techniques should the agent have access to, and in what order?

**Current answer:** Start with techniques that have known implementations: attention kernel replacement (FlashAttention variants), feature caching (TaylorSeer-style, ClusCa-style), and post-training quantization. Expand to pruning and distillation after the basic loop is validated.

**Open:** The right starting point depends on the target model's profiling characteristics (attention-bottlenecked vs. memory-bandwidth-bottlenecked), which requires profiling the specific target first.

### 4.2 Combined metric design

How to combine speed and quality into a single signal, given they are in tension?

**Current answer:** Track separately; accept only Pareto-dominant changes. Use quality / latency as a tiebreaker for Pareto-incomparable strategies.

**Open:** The right speed-quality weighting depends on the deployment scenario (real-time streaming vs. batch vs. mobile), which cannot be fixed until the use case is chosen.

### 4.3 Code agent failure rate

How robust does the code-writing agent need to be before the loop is useful?

**Current answer:** The agent must self-debug failed experiments before handing off. Silent wrong outputs are more dangerous than crashes and require a validation step after each code change.

**Open:** Acceptable failure rate depends on cycle time. Current AI scientist systems fail at implementation 42% of the time [8]; whether that is tolerable is determined by how long each cycle takes.

### 4.4 Evaluation cost

FID/FVD is expensive. How often should full quality evaluation run?

**Current answer:** Use VLM perceptual feedback as a fast proxy during the main loop. Run full FID/FVD at checkpoints (e.g., every 5 accepted changes, or when a new best speed is achieved).

**Open:** The right checkpoint frequency depends on how stable VLM proxy scores are for the specific model and task, requiring empirical calibration in early runs.

### 4.5 Stopping criterion

When does the loop terminate?

**Current answer:** Stop when no Pareto improvement is found in N consecutive cycles. N = 5 is a reasonable starting value.

**Open:** The right N depends on evaluation noise and action space size. Noisier evaluation requires larger N to avoid stopping on a false plateau.

---

## 5. Timeline

| # | Period | Milestone |
|---|--------|-----------|
| 1 | May 26 - May 31 | Complete literature review; narrow to 2-3 candidate target models |
| 2 | June 1 - June 13 | Lock target model and device; build pipeline MVP (one complete cycle end-to-end) |
| 3 | June 14 - July 13 | Experiment phase: run the agentic loop, collect results, iterate on the research agent |
| 4 | July 14 - August 14 | Paper writing |
| 5 | August 14, 2026 | Internship ends |

---

## 6. References

**[1]** [karpathy/autoresearch](https://github.com/karpathy/autoresearch) — GitHub 2024
- LLM agent iteratively edits a single-file training script, runs a fixed 5-minute experiment, keeps the change if it improves the metric, reverts otherwise, and repeats.
- Fixed time budget makes experiments directly comparable; persistent experiment log carries all history forward.

**[2]** [Accelerating Scientific Discovery with Co-Scientist](https://doi.org/10.1038/s41586-026-10644-y) — Nature 2026
- Multi-agent system (Gemini) for hypothesis generation: agents independently generate hypotheses, then engage in pairwise scientific debate, producing win/loss records used to evolve and refine hypotheses through a tournament.
- More compute = more tournament rounds = better hypotheses; validated across 15 expert-curated scientific goals in biomedical domains.

**[3]** [Robin: A Multi-Agent System for Automating Scientific Discovery](https://doi.org/10.1038/s41586-026-10652-y) — Nature 2026
- First system to close the full scientific loop (hypothesis generation through experimental analysis and back) without human involvement in execution.
- Three specialized agents: Crow (fast literature search), Falcon (deep literature search), Finch (data analysis, grounded only in measured results).
- Applied to dry AMD drug discovery: proposed ripasudil from 551 papers, confirmed efficacy in vitro, then autonomously designed and analyzed a follow-up RNA-seq experiment.

**[4]** [The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery](https://arxiv.org/abs/2408.06292) — arXiv 2024
- End-to-end autonomous ML research: idea generation, code writing, experiment execution, paper writing, and automated peer review; ~$15 per paper.
- Limitation: requires human-authored code templates per research domain.

**[5]** [The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree Search](https://arxiv.org/abs/2504.08066) — arXiv 2025
- Eliminates human-authored templates; introduces progressive agentic tree search that explores multiple experiment branches in parallel, pruning underperforming ones.
- One of three submitted papers accepted at an ICLR 2025 workshop — first fully AI-generated peer-review-accepted paper.

**[6]** [Jr. AI Scientist and Its Risk Report](https://arxiv.org/abs/2511.04583) — arXiv 2025
- Given a baseline paper, the system analyzes limitations, formulates improvement hypotheses, iteratively experiments, and writes a paper; handles multi-file codebases using modern coding agents.
- Successfully built on real NeurIPS/ICLR works; includes a comprehensive risk report identifying failure modes.

**[7]** [AutoML-Agent: A Multi-Agent LLM Framework for Full-Pipeline AutoML](https://arxiv.org/abs/2410.02958) — arXiv 2024
- Retrieval-augmented planning: before generating a new plan, the agent retrieves past successful plans via RAG, then generates multiple candidates and selects the best.
- Each plan is decomposed into parallel sub-tasks solved by specialized agents concurrently.

**[8]** [AI Scientists Fail Without Strong Implementation Capability](https://arxiv.org/abs/2506.01372) — arXiv 2025
- Evaluated 28 papers from 5 AI scientist systems; the fundamental bottleneck is not hypothesis quality but execution: the ability to implement rigorous experiments and produce valid papers.
- Systems fail at the implementation step 42% of the time across current systems.

**[9]** [TaylorSeer: From Reusing to Forecasting: Accelerating Diffusion Models](https://arxiv.org/abs/2503.06923) — ICCV 2025
- Uses Taylor expansion to predict future diffusion features from past ones, avoiding redundant computation across timesteps.
- Achieves 4.99x speedup on FLUX with minimal quality loss; training-free and plug-and-play.

**[10]** [ClusCa: Cluster-Driven Feature Caching for Diffusion Transformers](https://arxiv.org/abs/2509.10312) — ACM MM 2025
- Clusters spatial tokens and caches features at the cluster level rather than per-token, reducing both compute and cache overhead.
- Achieves 4.96x speedup on FLUX; complementary to TaylorSeer's temporal caching approach.

**[11]** [FlashAR: Efficient Post-Training Acceleration for Autoregressive Image Generation](https://arxiv.org/abs/2605.09430) — arXiv 2026
- Post-training acceleration for AR image generation models combining parallel decoding and early-exit strategies.
- Achieves 22.9x speedup on LlamaGen without retraining.

**[12]** [Taming Diffusion Transformer for Efficient Mobile Video Generation](https://arxiv.org/abs/2507.13343) — arXiv 2025
- Combines structured pruning and knowledge distillation to compress a DiT-based video model for mobile deployment.
- Achieves 15 FPS on iPhone; demonstrates that hardware-specific design is necessary for mobile targets.

**[13]** [Foveated Diffusion: Efficient Spatially Adaptive Image and Video Generation](https://arxiv.org/abs/2603.23491) — arXiv 2026
- Spatially adaptive computation: higher resolution and more compute in the attended region, lower at the periphery, mimicking human foveal vision.
- Applicable to both image and video generation; reduces total FLOPs without uniform quality loss.

**[14]** [LAPTOP-Diff: Layer Pruning and Normalized Distillation for Diffusion Models](https://arxiv.org/abs/2404.11098) — arXiv 2024
- Prunes entire transformer layers from a diffusion model and recovers quality via normalized distillation.
- Structured pruning reduces inference FLOPs proportionally to layers removed; distillation mitigates quality degradation.

**[15]** [PPCL: Pluggable Pruning with Contiguous Layer Distillation for Diffusion Transformers](https://arxiv.org/abs/2511.16156) — CVPR 2026
- Pluggable layer pruning that removes contiguous blocks of DiT layers and distills from the unpruned model.
- Designed for flexibility: pruning granularity can be adjusted post-hoc without retraining from scratch.

**[16]** [How Far Are AI Scientists from Changing the World?](https://arxiv.org/abs/2507.23276) — arXiv 2025
- Survey of current AI scientist systems: comprehensively analyzes achievements, identifies key bottlenecks, and describes components needed for groundbreaking AI-driven discovery.
- Complements [8] with broader scope; useful entry point for understanding the current state of the field.
