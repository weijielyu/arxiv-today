# Category Report: Image Generation

> Tracking papers on image generation, text-to-image, image editing, diffusion models, autoregressive image models, and controllable generation.

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
