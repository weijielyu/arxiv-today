# Category Report: Human Video & Reconstruction (incl. Face)

> Tracking papers on human video generation, body/face reconstruction, avatars, talking heads, portrait video, and face generation.

---

## 2026-05-26

### Loki: Representation over Architecture for Diffusion-Based Portrait Animation
**arXiv:** [2605.24176](https://arxiv.org/abs/2605.24176)  
**Authors:** Pouyan Navard, **Sernam Lim**

Argues that stacking trained expression/pose/identity modules in SOTA diffusion portrait animators only compensates for an upstream choice: learning expression and pose from RGB, where identity, pose, and expression are inseparable. Loki instead encodes driver expression and head pose with a face model whose parameter axes are identity-orthogonal by construction, rasterizes them into a spatial map consumed natively by the diffusion backbone, and routes identity separately. Cuts trainable parameters and residual entanglement.

---

### Multi-view Consistent 3D Gaussian Head Avatars 'without' Multi-view Generation
**arXiv:** [2605.25220](https://arxiv.org/abs/2605.25220)  
**Authors:** Aviral Chharia, **Fernando De la Torre**

Learns conditional and unconditional 3D Gaussian head models from randomly sampled 2D images alone — no multi-view data, 3D supervision, or intermediate view synthesis. MVCHead is a single-shot state-space model that enforces multi-view consistency directly in the 3D representation, with a Hierarchical State Space block (and a bi-directional Mamba scan) that refines Gaussians coarse-to-fine while capturing long-range dependencies. Removes the usual multi-view data dependency for head avatars.

---

### COSY: Compositional 3DGS Synthesis for Disentangled Human Head Editing
**arXiv:** [2605.24114](https://arxiv.org/abs/2605.24114)  
**Authors:** Florian Barthel, **Shalini De Mello**, **Koki Nagano**, Wieland Morgenstern, Anna Hilsmann, Peter Eisert

Tackles entangled latent spaces in 3DGS head GANs, where editing one attribute (hair color, glasses) unintentionally changes identity or appearance. COSY's generator synthesizes components — hair, skin, glasses, torso — completely independently, so the latent for one region can change while others stay fixed, achieving disentanglement by construction rather than post-hoc direction estimation. Enables clean semantic editing of photorealistic real-time 3D heads.

---

### Towards Anatomically Plausible Human Image Generation via Synthetic Localized Preferences
**arXiv:** [2605.25759](https://arxiv.org/abs/2605.25759)  
**Authors:** Bao Li, **Yuliang Xiu**, Zhen Liu

Addresses persistent anatomical errors in T2I human generation, where high-quality human-photo datasets are limited and standard DPO treats all pixels equally despite anatomical artifacts being localized. The ASAP framework constructs controlled preference pairs via a localized degradation mechanism on high-fidelity humans, giving DPO a sharp localized signal. Improves anatomical plausibility without part-specific modules.

---

### SplitAvatar: One-shot Head Avatar with Autoregressive Gaussian Splitting
**arXiv:** [2605.25751](https://arxiv.org/abs/2605.25751)  
**Authors:** Hongzhe Liao, Chuhua Xian, Hongmin Cai, Haiyang Liu, Fa-Ting Hong

Reconstructs an animatable head avatar from a single image while fixing the Gaussian-count magnitude mismatch between image-based and 3DMM-based approaches that causes expression detail loss. A graph-splitting network progressively generates Gaussians coarse-to-fine with an autoregressive architecture, and a mesh-topology-extension method keeps the GNN connectivity aligned with the growing Gaussian count. Yields finer-grained expressions from one-shot input.

---

### Test-Time Self-Adaptive Conditioning for Stable Audio-Driven Talking-Head Generation
**arXiv:** [2605.25488](https://arxiv.org/abs/2605.25488)  
**Authors:** Zhicheng Zhang, Lei Wang, Yu Zhang, Yongsheng Gao

Addresses identity drift and temporal inconsistency caused by conditioning the whole video on a single static reference image. TT-SAC is a parameter-free inference framework that composes the generator with its encoder in a feedback loop, letting pretrained talking-head models adapt their conditioning representations during inference without retraining, gradient updates, or extra supervision. A lightweight, broadly applicable stabilization for existing systems.

---

### Data-driven Head Motion Generation through Natural Gaze-Head Coordination
**arXiv:** [2605.25810](https://arxiv.org/abs/2605.25810)  
**Authors:** Xiaohan Liu, Yilin Wen, Yusuke Sugano

The first data-driven approach to model temporal gaze-head coordination from large-scale in-the-wild facial videos, with an automatic pipeline that extracts natural gaze/head motions via off-the-shelf gaze estimators. A conditional VAE captures the probabilistic gaze-head correlation, and the framework is applied to gaze-controlled facial video generation with realistic head motion correlated to input gaze — an aspect not previously emphasized.

---

## 2026-05-25

### TrioMan: Generator-Refiner-Examiner Tri-Module Data Augmentation for 3D Human Avatars
**arXiv:** [2605.23555](https://arxiv.org/abs/2605.23555)  
**Authors:** Gangjian Zhang, Jian Shu, Sicheng Yu, Wenhao Shen, Yu Feng, Hao Wang

Addresses data scarcity in reconstructing photorealistic, animatable 3D human avatars from monocular video via a tri-module augmentation pipeline: a Generator perturbs pose/camera for unseen samples, a Refiner improves them with one-step diffusion guided by texture/geometry cues, and an Examiner selects subject-consistent samples via dual-branch attention similarity. Outperforms SOTA on X-Humans and NeuMan.

---

## 2026-05-22

### ⭐ BodyReLux: Temporally Consistent Full-Body Video Relighting
**arXiv:** [2605.21766](https://arxiv.org/abs/2605.21766)

Subject-specific video diffusion framework for relighting full-body human performances in a **temporally consistent** way. Trained on pixel-aligned video relighting pairs across diverse lighting and performance conditions. Relevant to human video generation and post-production editing.

---

### AtomicMotion: Learning Human Motion From Different Human Parts
**arXiv:** [2605.22631](https://arxiv.org/abs/2605.22631)  
**Authors:** Runzhen Liu, Chuhua Xian, Fa-Ting Hong

Reconstructs full-body pose from sparse **head + hand trajectories** (AR/VR setting). Key insight: decomposes motion into "atomic intents" from different body parts, capturing fine-grained signal variations and structural body topology. Avoids the error accumulation of treating the body as a monolithic entity.

---

### PIU: Proximity-guided Identity Unlearning in ID-Conditioned Diffusion Models
**arXiv:** [2605.22311](https://arxiv.org/abs/2605.22311)  
**Authors:** Jose Edgar Hernandez Cancino Estrada et al.

Studies **identity unlearning** in face diffusion models that are conditioned on identity embeddings (not text). Addresses the "right to be forgotten" problem in ID-conditioned generation. More of a privacy/safety paper than a generation quality paper, but touches the face generation ecosystem.

---
