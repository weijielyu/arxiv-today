# Category Report: 3D Reconstruction & Generation

> Tracking papers on 3D reconstruction, novel view synthesis, NeRF, Gaussian Splatting, 3D generation, and scene understanding.

---

## 2026-05-22

### ⭐ No Pose, No Problem in 4D: Feed-Forward Dynamic Gaussians from Unposed Multi-View Videos
**arXiv:** [2605.22190](https://arxiv.org/abs/2605.22190)

First feed-forward model to jointly handle **dynamic content + multi-view input + unknown camera poses** in a single pass. Prior work always required at least one of these to be given (poses known, or only monocular, or static scene). A significant step toward unconstrained real-world 4D reconstruction.

---

### ⭐ PhysX-Omni: Unified Simulation-Ready Physical 3D Generation for Rigid, Deformable, and Articulated Objects
**arXiv:** [2605.21572](https://arxiv.org/abs/2605.21572)  
**Authors:** Ziang Cao, Yinghao Liu, Haitian Li, Fangzhou Hong, Zhaoxi Chen, Liang Pan, **Ziwei Liu**

From Ziwei Liu's lab. Unified 3D generation pipeline that produces simulation-ready assets with physical properties across rigid, deformable, and articulated objects — prior methods were single-category. Practically valuable for robotics simulation and digital content pipelines.

---

### ForeSplat: Optimization-Aware Foresight for Feed-Forward 3D Gaussian Splatting
**arXiv:** [2605.22020](https://arxiv.org/abs/2605.22020)  
**Authors:** Yuke Li, Weihang Liu, Cheng Zhang, Yuefeng Zhang et al.

Feed-forward 3DGS is trained to minimize zero-step rendering error, but deployed with post-hoc per-scene optimization — a train/test gap. ForeSplat trains the network to predict initializations that are **good for subsequent optimization** (optimization-aware foresight). Clean insight, principled fix.

---

### TWINGS: Thin Plate Splines Warp-aligned Initialization for Sparse-View Gaussian Splatting
**arXiv:** [2605.22069](https://arxiv.org/abs/2605.22069)  
**Authors:** Hyeseong Kim, Geonhui Son, Deukhee Lee, Dosik Hwang

Sparse-view 3DGS with TPS-based warp alignment to initialize Gaussians more coherently from limited viewpoints. Addresses point sparsity — the core problem in sparse-view 3DGS.

---

### Diffusion-guided Generalizable Enhancer for Urban Scene Reconstruction
**arXiv:** [2605.22420](https://arxiv.org/abs/2605.22420)  
**Authors:** Henry Che, Jingkang Wang, Yun Chen, Ze Yang, Sivabalan Manivasagam, **Raquel Urtasun**

Uses diffusion models to enhance neural rendering quality under large viewpoint shifts for urban scenes — a core limitation of NeRF/3DGS methods trained on driving trajectories. From Waabi (Urtasun's group). Interesting use of diffusion for reconstruction enhancement.

---
