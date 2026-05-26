# Category Report: Image Generation

> Tracking papers on image generation, text-to-image, image editing, diffusion models, autoregressive image models, and controllable generation.

---

## 2026-05-26

### ERNIE-Image Technical Report
**arXiv:** [2605.25347](https://arxiv.org/abs/2605.25347)  
**Authors:** Jiaxiang Liu, Zhida Feng, Pengyu Zou, Zhenyu Qian, Tianrui Zhu, Jun Xia et al. (Baidu)

An open-source 8B single-stream DiT text-to-image model aiming to close the gap to leading closed-source systems via better data mining and supervision. Pre-training uses a bottom-up pipeline (fine-grained categorization, rich captions, aesthetic assessment, hierarchical sampling); post-training adds top-down data construction, diversified prompts, and a stabilized DPO strategy. A notable open T2I release.

---

### Everything at Every Scale: Scale-Invariant Diffusion with Continuous Super-Resolution
**arXiv:** [2605.26032](https://arxiv.org/abs/2605.26032)  
**Authors:** Zixin Jessie Chen, Zhuo Chen, Archer Wang, Jeff Gore, **William T. Freeman**, Congyue Deng, **Marin Soljačić**

SKILD unifies generation and continuous super-resolution in a single unconditional framework by exploiting scale invariance: the forward process attenuates content from fine to coarse scales while injecting spectrum-matched noise, making scale an explicit coordinate of the diffusion dynamics. The same reverse process does both tasks by varying only the starting timestep — no task-specific heads. An elegant reframing of generation and SR as scale-wise information recovery.

---

### Reinforcing Few-step Generators via Reward-Tilted Distribution Matching
**arXiv:** [2605.26108](https://arxiv.org/abs/2605.26108)  
**Authors:** Yushi Huang, Xiangxin Zhou, Ruoyu Wang, Chi Zhang, Jun Zhang, **Tianyu Pang**

RTDMD unifies distribution matching distillation with reward-guided RL for few-step flow generators, showing the reward-tilted-teacher KL objective decomposes into a distribution-matching term and a reward-maximization term. An Ambient-Consistent DMD stage stabilizes the fake-score model under limited updates, then reward optimization is jointly applied. Aligns efficient few-step image generators with human preferences without sacrificing fidelity.

---

### Diff-Instruct with Diffused Reward: Towards Principled One-step Generator RL
**arXiv:** [2605.24001](https://arxiv.org/abs/2605.24001)  
**Authors:** Junyi Wu, Weijian Luo, Haoyang Zheng, Runzhe Zhang, Guang Lin

DIDR is a data-free trajectory-level RL alignment framework for one-step T2I generators, derived from Integral KL minimization. Instead of terminal image-space reward optimization (which exploits stochastic degrees of freedom and harms fidelity), it propagates the RLHF-optimal reward-tilted clean-image distribution across all noise levels along the diffusion trajectory. Better balances reward gains and image quality.

---

### Adversarial Error Correction for Visual Autoregressive Generation
**arXiv:** [2605.24843](https://arxiv.org/abs/2605.24843)  
**Authors:** Ligong Bi, Tao Huang, Jianyuan Guo, **Chang Xu**

AID-VAR is a plug-and-play framework that combats cascading error propagation in next-scale visual autoregressive models, where coarse-scale mispredictions amplify across the hierarchy. A discriminator diagnoses fidelity gaps at each scale transition and a lightweight guidance injector — a non-invasive adapter on a frozen VAR backbone — proactively corrects the feature manifold. Improves VAR synthesis fidelity without retraining the backbone.

---

### CollectionLoRA: Collecting 50 Effects in 1 LoRA via Multi-Teacher On-Policy Distillation
**arXiv:** [2605.25378](https://arxiv.org/abs/2605.25378)  
**Authors:** Fangtai Wu, Hailong Guo, Shijie Huang, Jiayi Song, Yubo Huang, Mushui Liu, Zhao Wang, Yunlong Yu, Jiaming Liu, Ruihua Huang

Distills up to 50 different customized image-editing effect LoRAs, plus few-step generation, into a single LoRA via multi-teacher on-policy distillation. This removes the deployment overhead of storing/loading many LoRAs and resolves the parameter interference (concept bleeding, style degradation) caused by cascading effect LoRAs with acceleration modules. A practical recipe for scalable customized editing.

---

## 2026-05-25

### ⭐ PiD: Fast and High-Resolution Latent Decoding with Pixel Diffusion
**arXiv:** [2605.23902](https://arxiv.org/abs/2605.23902)  
**Authors:** Yifan Lu, Qi Wu, Jay Zhangjie Wu, Zian Wang, Huan Ling, **Sanja Fidler** et al.

Reformulates the latent-to-pixel decoder as conditional pixel diffusion, unifying decoding and upsampling into a single generative module that synthesizes 4×–8× upscaled images. A sigma-aware adapter injects noise-corrupted latents (enabling early termination of latent diffusion) and DMD2 distillation cuts inference to 4 steps. Works for VAE and semantic (SigLIP/DINOv2) RAE latents; ~6× faster than cascaded SR.

---

### Composing People Together: Iterative Pose-Image Generation for Multi-Person Interaction Scenes
**arXiv:** [2605.23178](https://arxiv.org/abs/2605.23178)  
**Authors:** Wenxuan Peng, **Bharath Hariharan**, Hadar Averbuch-Elor

Introduces a dual pose-image representation that brings person-centric structural priors into pretrained diffusion transformers, jointly predicting a 2D pose visualization and its RGB image so structure and appearance co-evolve. A cross-modal alignment scheme binds text/pose/image and an iterative construction scheme decomposes complex multi-human scenes, improving prompt alignment and scene diversity.

---

### VINS-120K: Ultra High-Resolution Image Editing with A Large-Scale Dataset
**arXiv:** [2605.23518](https://arxiv.org/abs/2605.23518)  
**Authors:** Zhizhou Chen, Shanyan Guan, Zhanxin Gao, En Ci, Yanhao Ge, Wei Li, et al.

The first large-scale dataset for instruction-based ultra-high-resolution image editing: 120K curated (instruction, input, edited) triplets, each image ≥4096×4096, plus a VINS-4KEval benchmark. A high-frequency-aware post-adaptation strategy extends pretrained non-HR models to the UHR regime, improving fine-grained detail and texture realism.

---

## 2026-05-22

### ⭐ Lens: Rethinking Training Efficiency for Foundational Text-to-Image Models
**arXiv:** [2605.21573](https://arxiv.org/abs/2605.21573)  
**Authors:** Dong Chen, Fangyun Wei, Ziyu Wan, Dongdong Chen, et al.

A 3.8B-parameter T2I model competitive with or surpassing 6B+ models (e.g., Z-Image) using only ~19.3% of their training compute. Two key strategies: (1) maximize data information density per batch, (2) compact model design. Practical and impressive efficiency result — worth studying for training strategy insights.

---

### UniVL: Unified Vision-Language Embedding for Spatially Grounded Contextual Image Generation
**arXiv:** [2605.21611](https://arxiv.org/abs/2605.21611)  
**Authors:** Jiayun Wang, Yu Wang, Weijie Gan, Zhenting Wang, Wei Wei

Controllable image generation where text is **rendered onto a spatial mask** as part of the visual input — binding semantics to locations via a single unified encoder, removing the need for a separate text encoder at inference. Novel conditioning paradigm for spatially grounded generation.

---

### DecQ: Detail-Condensing Queries for Enhanced Reconstruction and Generation in Representation Autoencoders
**arXiv:** [2605.22777](https://arxiv.org/abs/2605.22777)  
**Authors:** Tianhang Wang, Yitong Chen, Wei Song, Zuxuan Wu, Min Li, Jiaqi Wang

Addresses a core limitation of representation autoencoders (RAEs) used in latent diffusion: freezing the VFM encoder constrains spatial reconstruction capacity. Introduces detail-condensing queries to recover fine-grained generation and editing without full VFM fine-tuning.

---

### SEGA: Spectral-Energy Guided Attention for Resolution Extrapolation in Diffusion Transformers
**arXiv:** [2605.22668](https://arxiv.org/abs/2605.22668)  
**Authors:** Javad Rajabi, Kimia Shaban, Koorosh Roohi, David B. Lindell, Babak Taati

Training-free method for DiTs to generate at resolutions beyond their training range. Uses spectral-energy analysis to guide RoPE extrapolation and attention scaling. Useful if you need higher-resolution outputs from an existing model.

---

### Rethinking Token Reduction for Diffusion Models via Output-Similarity-Awareness
**arXiv:** [2605.22011](https://arxiv.org/abs/2605.22011)  
**Authors:** Hangyeol Lee, Hyojeong Lee, Joo-Young Kim

Points out that existing token reduction methods for DiTs use input-token similarity (a ViT paradigm) but this misaligns with the generative objective. Proposes output-similarity-aware reduction. Companion to ORBIS [2605.22015] for video.

---
