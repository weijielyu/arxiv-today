# Category Report: Video Generation

> Tracking papers on video generation, video diffusion, motion control, camera control, autoregressive video, and text/image-to-video synthesis.

---

## 2026-05-25

### ⭐ Geo-Align: Video Generation Alignment via Metric Geometry Reward
**arXiv:** [2605.23903](https://arxiv.org/abs/2605.23903)  
**Authors:** Zizun Li, Haoyu Guo, Runzhe Teng, **Chunhua Shen**, Tong He

The first RL framework for camera-controlled video re-rendering, removing the dependence on scarce synchronized multi-view real data. A metric 3D estimator extracts camera trajectories from generated videos and a scale-aware perceptual reward explicitly penalizes rotation/translation error, with a pipeline that needs no paired data. Outperforms supervised baselines in both camera controllability and fidelity.

---

### ⭐ One-Forcing: Towards Stable One-Step Autoregressive Video Generation
**arXiv:** [2605.23458](https://arxiv.org/abs/2605.23458)  
**Authors:** Jiaqi Feng, Justin Cui, Yuanhao Ban, **Cho-Jui Hsieh**

Augments the DMD objective with an auxiliary GAN loss to reach a stable one-step autoregressive regime, fixing Self-Forcing's blur and consistency distillation's weak dynamics. Hits VBench 83.76 (SOTA among one-step causal methods) and enables stable one-step framewise generation at one-third the training cost of chunkwise models.

---

### ⭐ CoMoGen: Controllable Motion Dynamics and Interactions with Mask-Guided Video Generation
**arXiv:** [2605.22996](https://arxiv.org/abs/2605.22996)  
**Authors:** Adil Meric, Lin Geng Foo, Mert Kiray, Benjamin Busam, Rishabh Dabral, **Christian Theobalt**

Generates interactive dynamics from a single binary mask sequence + input image via a lightweight MaskAdapter injected into an MMDiT through a cosine-weighted schedule. Introduces a way to identify "Motion Layers" in MMDiT attention space and LoRA-tunes only those, with no architecture change. SOTA motion fidelity and perceptual realism.

---

### LaMo: Self-Supervised Latent Motion Priors for Physical Realism in Video Generation
**arXiv:** [2605.23878](https://arxiv.org/abs/2605.23878)  
**Authors:** Bo Jiang, Depu Meng, Yihan Hu, Yichen Xie, Tianshuo Xu, Wei Zhan

Extracts motion supervision from the unlabeled videos already used to train diffusion models, via a latent motion prior over frame-to-frame latent changes. Exposed as a Motion Drift Loss (training) and Motion Prior Guidance (sampling), both plug-and-play. Improves CogVideoX physical fidelity on VideoPhy/VideoPhy2 without external simulators or curated physics data.

---

### EM-Vid: Training-Free Entity-Centric Memory for Efficient and Consistent Multi-Shot Video Generation
**arXiv:** [2605.23610](https://arxiv.org/abs/2605.23610)  
**Authors:** Jente Vandersanden, Matheus Gadelha, Chun-Hao P. Huang, Hyeonho Jeong, Yulia Gryaditskaya

Replaces full-frame memory with an entity-indexed bank of latent patches, using sparse token conditioning to restrict self-attention to entity-relevant tokens. A budgeted update and noise-injection mechanism keep memory compact and prevent transient-context leakage, improving cross-shot subject consistency, prompt adherence, and efficiency.

---

### Smart-Insertion-V: Photorealistic Video Insertion via a Closed-Loop Feedback Dual-Stream Framework
**arXiv:** [2605.23891](https://arxiv.org/abs/2605.23891)  
**Authors:** Xiao Cao, Yansong Qu, Xiangzhen Chang, Wen Xiao, Jiakui Hu, et al. (**Xuelong Li**)

Mask-free video object insertion that handles severe style gaps by jointly running insertion and style transfer in a dual-stream framework with a closed-loop feedback mechanism. A Dual-World-View RoPE disentangles conditioning signals via spatio-temporal offsets and a VLM-based Decoupled Guidance Module handles spatial grounding; an open-source dataset is promised.

---

## 2026-05-22

### ⭐ MotiMotion: Motion-Controlled Video Generation with Visual Reasoning
**arXiv:** [2605.22818](https://arxiv.org/abs/2605.22818)  
**Authors:** Lee Hsin-Ying, Hanwen Jiang, Yiqun Mei, Jing Shi, **Ming-Hsuan Yang**, **Zhixin Shu**

Reformulates motion control as a reasoning-then-generation problem. A VLM first infers causally complete, commonsense-consistent motion (including secondary effects missed by sparse user trajectories), then guides the video diffusion model. Addresses a fundamental weakness of trajectory-following I2V models. Notable: co-authored by Weijie's close collaborators.

---

### ⭐ Bernini: Latent Semantic Planning for Video Diffusion
**arXiv:** [2605.22344](https://arxiv.org/abs/2605.22344)  
**Authors:** Bernini Team (Chenchen Liu, Junyi Chen, Lei Li, Lu Chi, Mingzhen Sun, et al.)

Proposes a clean division of labor: MLLM handles **semantic planning** over heterogeneous multimodal inputs (text, images, video clips), while the diffusion model renders from high-level semantic + low-level visual features. Large team signals a potentially high-impact system-level paper. Watch for project page / code release.

---

### ORBIS: Output-Guided Token Reduction for Video Diffusion Acceleration
**arXiv:** [2605.22015](https://arxiv.org/abs/2605.22015)  
**Authors:** Hangyeol Lee, Joo-Young Kim

Token reduction method for video DiTs that uses output similarity (not just input similarity) to guide reduction, improving matching quality and throughput. Companion paper to "Rethinking Token Reduction" [2605.22011] for image DiTs.

---

### EasyVFX: Frequency-Driven Decoupling for Resource-Efficient VFX Generation
**arXiv:** [2605.22051](https://arxiv.org/abs/2605.22051)  
**Authors:** Sixiang Chen et al.

Decouples spatial textures and temporal dynamics in frequency domain to reduce the cost of realistic VFX synthesis. Interesting approach for resource-constrained video generation.

---
