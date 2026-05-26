# Category Report: 3D Reconstruction & Generation

> Tracking papers on 3D reconstruction, novel view synthesis, NeRF, Gaussian Splatting, 3D generation, and scene understanding.

---

## 2026-05-26

### ⭐ Helix4D: Complex 4D Mesh Generation
**arXiv:** [2605.26109](https://arxiv.org/abs/2605.26109)  
**Authors:** Jiraphon Yenphraphai, Jianqi Chen, Jian Wang, Gordon Qian, **Sergey Tulyakov**, Rameen Abdal, Raymond A. Yeh, **Peter Wonka**, Chaoyang Wang

Adapts the Trellis2 image-to-3D prior into video-conditioned 4D mesh generation, handling complex topology changes, transparent materials, thin structures, and inner surfaces that current video-to-4D methods fail on. Sliding-window cross-frame attention anchored on a Trellis2-generated first frame shares cross-frame information while preserving pretrained quality on rare cases, and a temporal injection scheme adds time without breaking the 3D positional encoding. Strong dynamic-3D generation from Snap Research.

---

### ⭐ TriSplat: Simulation-Ready Feed-Forward 3D Scene Reconstruction
**arXiv:** [2605.26115](https://arxiv.org/abs/2605.26115)  
**Authors:** Weijie Wang, Zimu Li, Jinchuan Shi, Zeyu Zhang, Botao Ye, **Marc Pollefeys**, Donny Y. Chen, **Bohan Zhuang**

Replaces Gaussian primitives with oriented triangle primitives so a single feed-forward pass directly exports simulation-ready meshes, removing the expensive post-hoc surface-extraction step that breaks the feed-forward promise. From input images the network jointly predicts local 3D point maps, triangle attributes, camera poses, and optional intrinsics in a pose-free setting. A clean, practical advance for downstream simulation, physics, and embodied interaction.

---

### ⭐ Full-4D: Generating Full-Scope 4D Scenes from a Single-View Video
**arXiv:** [2605.25500](https://arxiv.org/abs/2605.25500)  
**Authors:** Tingxi Chen, Ke Hao, Yabo Chen, Zhengxue Cheng, Rong Xie, Li Song, Haibin Huang, Chi Zhang, **Xuelong Li**

Casts the ill-posed single-view-to-4D problem as multi-view video synthesis followed by optimization-based 4D reconstruction from the generated views, escaping the small-viewpoint-perturbation limits of prior monocular methods. Introduces Real-MV-4D, a large-scale dataset of synchronized multi-view videos capturing full-scope dynamic scenes. A compelling video→4D pipeline bridging video generation and 3D.

---

### Pantheon360: Taming Digital Twin Generation via 3D-Aware 360° Video Diffusion
**arXiv:** [2605.25449](https://arxiv.org/abs/2605.25449)  
**Authors:** Ting-Hsuan Chen, Ying-Huan Chen, Tao Tu, Jie-Ying Lee, Cho-Ying Wu, Fangzhou Lin, Hengyuan Zhang, David Paz, Xinyu Huang, Yuliang Guo, Yu-Lun Liu, **Yue Wang**, Liu Ren

A controllable 360° video generation framework for digital-twin creation that exploits panoramic coverage to simplify camera-trajectory design and maintain global coherence — avoiding the cross-view inconsistency that narrow-FoV perspective generators suffer on long trajectories. An explicit 3D Cache reconstructed from the input serves as a geometric scaffold for any user-defined camera path. Produces high-fidelity videos with precise camera control from sparse 360° inputs.

---

### ArtSplat: Feed-Forward Articulated 3D Gaussian Splatting from Sparse Multi-State Uncalibrated Views
**arXiv:** [2605.24304](https://arxiv.org/abs/2605.24304)  
**Authors:** Inseo Lee, Yoonji Kim, Eugene Sohn, Jiwoong Lee, Jungmin You, Joonseok Lee, Jin-Hwa Kim

The first feed-forward framework for articulated 3D Gaussian Splatting, reconstructing both geometry and joint parameters from sparse multi-view images across multiple articulation states in a single forward pass — no dense views, strong priors, or per-object optimization. A per-pixel joint-map representation integrates joint-parameter estimation into the feed-forward pipeline. Removes the heavy supervision typical of NeRF/3DGS articulated reconstruction.

---

### Fishbone: From One 3D Asset to a Million Controllable Edits
**arXiv:** [2605.24805](https://arxiv.org/abs/2605.24805)  
**Authors:** Yumeng He, Xiaoying Wang, Peihao Li, Yanjia Huang, Joe Masterjohn, **Jiajun Wu**, **Leonidas Guibas**, Yin Yang, Ying Jiang, Chenfanfu Jiang

A unified rib-spine representation for general shapes — a central spine governs global shape while cross-sectional ribs control local variation — supporting controllable parametric mesh deformation, reduced-space dynamics, and animation. Given an input mesh it computes a geodesic scalar field via an adaptive heat method and extracts the control structure automatically. Generates large families of controllable variations from a single asset for graphics, embodied AI, and robotics.

---

### CodecSplat: Ultra-Compact Latent Coding for Feed-Forward 3D Gaussian Splatting
**arXiv:** [2605.25563](https://arxiv.org/abs/2605.25563)  
**Authors:** Pengpeng Yu, Runqing Jiang, Qi Zhang, Dingquan Li, Jing Wang, Yulan Guo

Provides the compact scene representation that feed-forward 3DGS pipelines lack, by entropy-coding an intermediate 2D Gaussian-generation feature into a scene bitstream rather than compressing the final irregular 3D primitives. At decode, the latent feature is reconstructed and used to predict depth and Gaussian parameters mapped to 3D Gaussians. Couples compression with the feature-to-Gaussian process for better efficiency.

---

### SRUG: Shadow-Guided Relightable Urban Scene with Generation Model
**arXiv:** [2605.24700](https://arxiv.org/abs/2605.24700)  
**Authors:** Yonghao Zhao, Zexin Yin, Jian Yang, Beibei Wang, Jin Xie

Creates relightable urban scenes from sparse images/videos where unobserved regions still cast shadows onto visible areas. SRUG uses shadows to guide a 3D completion model that recovers geometry of invisible regions, easing the material-decomposition ambiguity under sparse views and complex illumination. Targets a genuinely ill-posed relighting setting in unbounded outdoor scenes.

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
