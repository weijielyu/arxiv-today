# Category Report: 3D Reconstruction & Generation

> Tracking papers on 3D reconstruction, novel view synthesis, NeRF, Gaussian Splatting, 3D generation, and scene understanding.

---

## 2026-05-25

### ⭐ GenRecon: Bridging Generative Priors for Multi-View 3D Scene Reconstruction
**arXiv:** [2605.23888](https://arxiv.org/abs/2605.23888)  
**Authors:** Katharina Schmid, Nicolas von Lützow, Jozef Hladký, **Angela Dai**, **Matthias Nießner**

Casts high-fidelity multi-view RGB scene reconstruction as conditional 3D generation over spatially-localized overlapping chunks that tile the scene, scaling an object-level generative prior (Trellis.2) to scene scale. A view-order-independent projection-based conditioning mechanism lifts posed multi-view features into a coherent 3D representation, yielding editable PBR mesh reconstructions that beat SOTA reconstruction by 16%.

---

### HorizonStream: Long-Horizon Attention for Streaming 3D Reconstruction
**arXiv:** [2605.23889](https://arxiv.org/abs/2605.23889)  
**Authors:** Chong Cheng, Peilin Tao, Nanjie Yao, Guanzhi Ding, Xianda Chen, Yuansen Du, et al.

Formalizes geometric propagation as an "evidence influence kernel" and factorizes it: Geometric Linear Attention learns channel-wise decay for bounded multi-timescale long-range propagation, while Geometric Local Attention with spatiotemporal RoPE handles short-range matching and suppresses attention sinks. Trained on 48-frame clips, it generalizes to 10,000+ frame sequences with constant memory and linear time.

---

### RiGS: Rigid-aware 4D Gaussian Splatting from a Single Monocular Video
**arXiv:** [2605.23672](https://arxiv.org/abs/2605.23672)  
**Authors:** Chenyu Wu, Wanhua Li, Zhu-Tian Chen, **Hanspeter Pfister**

Models dynamic monocular scenes across temporal scales using three Gaussian primitive types — static, rigid (long-term low-frequency motion), and transient (short-term high-frequency dynamics). An object-wise dynamic mask guides static/dynamic decomposition and rigid Gaussians can transition to transient ones under scene-flow supervision, achieving SOTA novel-view synthesis on dynamic benchmarks.

---

### LangFlash: Feed-forward 3D Language Gaussian Splatting from Sparse Unposed Images
**arXiv:** [2605.23287](https://arxiv.org/abs/2605.23287)  
**Authors:** Yilong Liu, Wanhua Li, Chen Zhu-Tian, **Hanspeter Pfister**

A feed-forward framework that predicts geometry and language-aligned semantic features as Gaussian primitives in a single pass from sparse unposed multi-view images — no per-scene optimization or poses. A sparse semantic encoding scheme (global dictionary + per-primitive weights) reduces representation cost, with RealEstate10k enriched for dense semantic supervision.

---

### Good Token Hunting: A Hitchhiker's Guide to Token Selection for Visual Geometry Transformers
**arXiv:** [2605.23892](https://arxiv.org/abs/2605.23892)  
**Authors:** Shuhong Zheng, Michael Oechsle, Erik Sandström, Marie-Julie Rakotosaona, **Federico Tombari**, Igor Gilitschenski

Tackles the quadratic cost of global attention in feed-forward multi-view 3D transformers by restricting each query's key/value set. A two-stage scheme — diversity-based inter-frame selection for scene coverage, then entropy-guided layer-aware intra-frame sparsification — accelerates inference by over 85% on 500-image scenes while maintaining or improving accuracy.

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
