# Category Report: Image Generation

> Tracking papers on image generation, text-to-image, image editing, diffusion models, autoregressive image models, and controllable generation.

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
