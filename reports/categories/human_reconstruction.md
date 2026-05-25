# Category Report: Human Video & Reconstruction (incl. Face)

> Tracking papers on human video generation, body/face reconstruction, avatars, talking heads, portrait video, and face generation.

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
