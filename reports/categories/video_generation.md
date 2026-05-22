# Category Report: Video Generation

> Tracking papers on video generation, video diffusion, motion control, camera control, autoregressive video, and text/image-to-video synthesis.

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
