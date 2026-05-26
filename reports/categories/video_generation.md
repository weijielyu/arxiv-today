# Category Report: Video Generation

> Tracking papers on video generation, video diffusion, motion control, camera control, autoregressive video, and text/image-to-video synthesis.

---

## 2026-05-26

### ⭐ On-Policy Adversarial Flow Distillation for Autoregressive Video Generation
**arXiv:** [2605.26105](https://arxiv.org/abs/2605.26105)  
**Authors:** Yang Luo, Shengju Qian, Xiaohang Tang, Zirui Zhu, Yong Liu, Xin Wang, **Yang You**

Distilling strong black-box teachers into causal autoregressive students is hard because the student learns under its own rollout distribution, making SFT off-policy and score-based distillation inapplicable. AFD rolls out the current student and queries the teacher on shared prompts, trains a prompt-paired Bradley-Terry discriminator to estimate clean-sample teacher-student discrepancy, and converts it into a denoising-time on-policy training signal. Directly targets streaming/long-horizon autoregressive video generation.

---

### ⭐ DeltaCam: Differential Intrinsic Camera Modeling for Video Generation
**arXiv:** [2605.25266](https://arxiv.org/abs/2605.25266)  
**Authors:** Debabrata Mandal, Zhihan Peng, Yujie Wang, Praneeth Chakravarthula

Moves beyond extrinsic pose/motion control to make intrinsic camera behavior — depth-of-field transitions, exposure, lens distortion, color processing — controllable and temporally consistent. Introduces Δ-parameterized neural camera adaptors that operate on relative parameter changes, sidestepping the scarcity of video data with accurate absolute intrinsics. Opens an under-explored control axis for camera-controlled video.

---

### Teaching Video Generators to Remember: Eliciting Dynamic Memory for Out-of-Sight State Evolution
**arXiv:** [2605.25333](https://arxiv.org/abs/2605.25333)  
**Authors:** Tianshuo Xu, Yichen Xie, Depu Meng, Chensheng Peng, Quentin Herau, Bo Jiang, Yihan Hu, Wei Zhan

Argues video world models freeze hidden states when evidence is unobserved even though pretrained DiTs already have KV-cache retrieval. ReMind elicits dynamic memory via memory-oriented data (a taxonomy of 100+ dynamic events), event-aware training with frame graphs and memory-interruption augmentations, and cache adaptation. Enables coherent out-of-sight state evolution during long rollouts.

---

### Reasoning to Align: Implicit Reasoning in Diffusion Transformers for Video Editing
**arXiv:** [2605.24674](https://arxiv.org/abs/2605.24674)  
**Authors:** Yan Li, Lin Liu, Xiaopeng Zhang, **Qi Tian**

RVEDiT addresses two structural flaws in DiT video editors: conditioning signals fed undifferentiated into all blocks, and cross-attention supervised only via pixel reconstruction. It adds Granularity-Routed Token Conditioning (separating global editing intent from fine visual evidence) and more explicit reasoning over the edit. Improves instruction-based editing fidelity and temporal coherence.

---

### Tempered Self-Similarity Alignment for Physically Plausible Video Generation
**arXiv:** [2605.24962](https://arxiv.org/abs/2605.24962)  
**Authors:** Manjin Kim, **Suha Kwak**, **Minsu Cho**

Transfers relational knowledge — spatio-temporal self-similarity (STSS) capturing how objects interact across space and time — from visual foundation models into video generators. The Tempered Self-similarity Alignment loss converts STSS into probabilistic correspondence distributions the generator is trained to match. Reduces appearance drift and implausible motion without external simulators.

---

### PixelWizard: Towards Efficient High-Fidelity Video Generation at Ultra-Large Spatial Resolution
**arXiv:** [2605.25801](https://arxiv.org/abs/2605.25801)  
**Authors:** Wenxue Li, Jingjing Ren, Peng Zhang, Tian Ye, Daiguo Zhou, Jian Luan, Lei Zhu

Decouples global-structure modeling from fine-grained detail synthesis to fix the optimization instability and cost of high-res video gen. A compact spatiotemporal anchor concentrates structural priors and guides high-res detail generation, while Noise-Span Aligned Shortcut Training cuts inference latency. Stabilizes structure without sacrificing high-frequency detail.

---

### Φ-Noise: Training-Free Temporal Video Conditioning via Phase-Based Noise Manipulation
**arXiv:** [2605.24509](https://arxiv.org/abs/2605.24509)  
**Authors:** Ofir Abramovich, Nadav Z. Cohen, Adi Rosenthal, Ariel Shamir

A training-free approach to motion-conditioned video generation that injects low-frequency phase information from a reference video directly into the diffusion noise latents. Transfers motion cues without architecture or pipeline changes, giving control over both appearance and dynamics. Competitive with or better than heavier learned conditioning methods.

---

### Baton: Explicit Semantic Blueprints for Joint Video-Audio Generation
**arXiv:** [2605.25195](https://arxiv.org/abs/2605.25195)  
**Authors:** Shuyuan Tu, **Qi Tian**, Zihan Yang, Yue Wu, Xintong Han, Weijie Kong, Jiangfeng Xiong, Jian-Wei Zhang, Zhao Zhong, Liefeng Bo, **Zuxuan Wu**, **Yu-Gang Jiang**

Introduces explicit semantic planning into joint audio-video generation: semantically rich, modality-aware planned tokens are jointly reasoned and aligned before denoising, complementing coarse text embeddings. This restores fine-grained semantics and gives a shared long-horizon blueprint that coordinates audio and video denoising trajectories. Improves cross-modal synchronization and reasoning-heavy generation.

---

### StreamChar: Long-Horizon Streaming Character Audio-Video Generation with Decoupled Orchestration
**arXiv:** [2605.25659](https://arxiv.org/abs/2605.25659)  
**Authors:** Linrui Tian, Qi Wang, Bang Zhang

Separates long-horizon orchestration from short-window audio-video denoising for real-time streaming character animation. An LLM-based orchestrator produces frame-aligned audio conditions from transcript + history, while a joint audio-video DiT does local bidirectional denoising with reference/motion-frame conditioning, plus two-stage distillation for low latency. Maintains identity and transcript-audio alignment across chunks.

---

### WorldCraft: From Camera Navigation to Object Manipulation in Interactive Video World Models
**arXiv:** [2605.25077](https://arxiv.org/abs/2605.25077)  
**Authors:** Bohai Gu, Taiyi Wu, Yueyang Yuan, Jian Liu, Xiaocheng Lu, Dazhao Du, Jie Zhang, Jinxiang Lai, Shuai Yang, Xiaotong Zhao, Alan Zhao, **Song Guo**

Expands interactive video world models from camera-level navigation to object-level trajectory actions: given a user click and sketched path, the model generates futures where the selected object follows the prescribed trajectory while the camera keeps navigating. A trajectory-centric pipeline with a Normalized World Trajectory representation makes the control object-centric. Moves world models from passive observers toward manipulable environments.

---

### Drift-Resistant Navigation World Model with Anchored Epipolar Guidance
**arXiv:** [2605.24761](https://arxiv.org/abs/2605.24761)  
**Authors:** Po-Chien Luan, Zimin Xia, Wuyang Li, Yang Gao, **Alexandre Alahi**

Mitigates both perceptual drift (noise accumulation from recursive rollout) and geometric drift (predictions deviating from agent motion) in navigation world models. Redesigns prediction as anchor-guided rollout: sparse future anchors serve as stable long-range targets and provide bidirectional-epipolar geometric constraints, with intermediate frames generated within each chunk. Improves long-horizon stability and geometric consistency.

---

### Paris 2.0: A Decentralized Diffusion Model for Video Generation
**arXiv:** [2605.26064](https://arxiv.org/abs/2605.26064)  
**Authors:** Ali Rouzbayani, Bidhan Roy, Marcos Villagra, Zhiying Jiang

The first video generation model pre-trained through decentralized computation, extending the open-weight Decentralized Diffusion Model line from images to temporally coherent video. Against a monolithic model under matched compute, it cuts FVD from 561 to 279 (~2×) and improves CLIP text-video similarity and aesthetics. Demonstrates cluster-free video pretraining is viable.

---

### Nano World Models: A Minimalist Implementation of Future Video Prediction
**arXiv:** [2605.23993](https://arxiv.org/abs/2605.23993)  
**Authors:** Siqiao Huang, Partha Kaushik, Michael Chen, Hengkai Pan, Omar Chehab, Fernando Moreno-Pino, Max Simchowitz

A compact, reproducible codebase for future video prediction centered on diffusion forcing, with a unified interface over generative objectives, model scales, action-conditioning, latent observation spaces, datasets, and long-horizon rollouts. Enables controlled study of world-modeling components usually entangled across implementations. A useful research scaffold rather than a new SOTA model.

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
