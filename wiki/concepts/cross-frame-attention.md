# cross-frame-attention

**Type**: concept  
**Tags**: #concept

## Overview

The core challenge in adapting 2D image diffusion models to generate videos is maintaining **temporal consistency**. Without explicit temporal anchoring, independent denoising of frames leads to severe flickering, background drift, and structural deformation. **Cross-frame attention** is an architectural family of mechanisms that replaces or augments standard spatial self-attention within pre-trained neural networks. By mapping and querying key-value pairs across different frames in a sequence, these attention patterns enforce global identity, retain background stability, and preserve object consistency across time.

---

## Appearances

- [[Diffusion Models for Video Generation]] — Master synthesis where zero-shot and one-shot cross-frame attention mechanisms are analyzed.

---

## Technical Implementations & Mathematical Variants

There are three primary variants of cross-frame attention, each offering a different trade-off between temporal consistency, computational complexity, and one-shot or zero-shot capability.

### 1. First-Frame Anchoring (Text2Video-Zero)
To avoid any fine-tuning or training, **Text2Video-Zero** (Khachatryan et al., 2023) replaces the spatial self-attention layer of a pre-trained Stable Diffusion model. Each frame $k$ in the generated sequence is forced to attend *only* to the first frame ($k=1$). This anchors the appearance, color palette, and identity of foreground objects to the initial frame.

$$\text{Cross-Frame-Attn}(\mathbf{Q}^k, \mathbf{K}, \mathbf{V}) = \text{Softmax}\Big( \frac{\mathbf{Q}^k (\mathbf{K}^1)^\top}{\sqrt{d}} \Big) \mathbf{V}^1$$

Where:
- $\mathbf{Q}^k = \mathbf{W}^Q \mathbf{z}_k$ represents the query projection of the latent features of the current frame $k$.
- $\mathbf{K}^1 = \mathbf{W}^K \mathbf{z}_1$ and $\mathbf{V}^1 = \mathbf{W}^V \mathbf{z}_1$ are the key and value projections derived exclusively from the **first frame** ($k=1$).
- $d$ is the projection channel dimension.

By keeping $\mathbf{K}$ and $\mathbf{V}$ anchored to the first frame, spatial positions across the video sequence retrieve features directly from the source frame, preventing visual drift over long durations.

### 2. Spatiotemporal Cross-Frame Attention (Tune-A-Video)
**Tune-A-Video** (Wu et al., 2023) generalizes first-frame anchoring to a spatiotemporal attention block (ST-Attention). In one-shot video editing, querying only the first frame can lead to rigid motion. To allow smooth local dynamics while maintaining structural anchoring, Tune-A-Video configures each frame $v_i$ to query a concatenated set of keys and values from the **first frame** ($v_1$) and the **immediately preceding frame** ($v_{i-1}$):

$$\mathbf{Q} = \mathbf{W}^Q \mathbf{z}_{v_i}, \quad \mathbf{K} = \mathbf{W}^K \Big[\mathbf{z}_{v_1}, \mathbf{z}_{v_{i-1}}\Big], \quad \mathbf{V} = \mathbf{W}^V \Big[\mathbf{z}_{v_1}, \mathbf{z}_{v_{i-1}}\Big]$$

$$\text{ST-Attention}(\mathbf{Q}, \mathbf{K}, \mathbf{V}) = \text{Softmax}\Big(\frac{\mathbf{Q} \mathbf{K}^\top}{\sqrt{d}}\Big) \cdot \mathbf{V}$$

Where:
- $\mathbf{z}_{v_i}$ is the feature map of frame $i$.
- $\Big[\mathbf{z}_{v_1}, \mathbf{z}_{v_{i-1}}\Big]$ denotes spatial axis concatenation. If each frame has $H \times W$ spatial tokens, the concatenated sequence has length $2 \times H \times W$.
- During one-shot fine-tuning, only the **query projection matrix** $\mathbf{W}^Q$ is updated in the ST-Attention blocks. This preserves the prior text-to-image knowledge embedded in $\mathbf{W}^K$ and $\mathbf{W}^V$.

### 3. Full Cross-Frame Interaction (ControlVideo)
For conditional video generation, **ControlVideo** (Zhang et al., 2023) scales cross-frame attention to a fully global spatiotemporal attention map. Instead of selecting sparse frame references, *all* latent frames across the entire sequence of length $m$ are projected into unified matrices. Let $\mathbf{Z} \in \mathbb{R}^{m \times HW \times C}$ be the spatiotemporal latent sequence:

$$\mathbf{Q} = \mathbf{Z} \mathbf{W}^Q, \quad \mathbf{K} = \mathbf{Z} \mathbf{W}^K, \quad \mathbf{V} = \mathbf{Z} \mathbf{W}^V$$

$$\text{Full-Cross-Frame}(\mathbf{Q}, \mathbf{K}, \mathbf{V}) = \text{Softmax}\Big(\frac{\mathbf{Q} \mathbf{K}^\top}{\sqrt{d}}\Big) \mathbf{V}$$

Here, $\mathbf{Q}, \mathbf{K}, \mathbf{V} \in \mathbb{R}^{mHW \times d}$. The attention matrix is of size $mHW \times mHW$, allowing every spatial coordinate in every frame to attend to every spatial coordinate in every other frame. This achieves maximum temporal coherency at the cost of quadratic computational scaling $\mathcal{O}(m^2 H^2 W^2)$ in sequence length.

---

## Background Masking Integration

To further enhance background stability, zero-shot pipelines combine cross-frame attention with explicit spatial masking. If a background/foreground mask $\mathbf{M}_k \in [0, 1]^{H \times W}$ is available for the $k$-th frame, we can merge the actual latent code $\mathbf{x}^k_t$ (which has been updated via cross-frame attention) with the warped camera-motion latent code $\tilde{\mathbf{x}}^k_t$:

$$\bar{\mathbf{x}}^k_t = \mathbf{M}^k \odot \mathbf{x}^k_t + (1 − \mathbf{M}^k) \odot \Big(\alpha\tilde{\mathbf{x}}^k_t +(1−\alpha)\mathbf{x}^k_t\Big)$$

Where:
- $\odot$ represents element-wise multiplication.
- $\tilde{\mathbf{x}}^k_t$ is the warped latent code representing global camera movement.
- $\alpha \approx 0.6$ is a blending weight, smoothing the background across frames while allowing the foreground to update dynamically.

---

## Mathematical Trace of Tune-A-Video ST-Attention

Let's trace a simplified toy example of Tune-A-Video's ST-Attention step.
Consider a video sequence of $m=3$ frames. Let's compute the updated spatial token for frame $v_2$ ($i=2$).
Assume each frame has only 1 spatial token (feature vector) of dimension $d=4$.

- Frame 1 Latent: $\mathbf{z}_{v_1} = [1.0, 0.0, 1.0, 0.0]^\top$
- Frame 1 Latent (previous frame): $\mathbf{z}_{v_{i-1}} = \mathbf{z}_{v_1} = [1.0, 0.0, 1.0, 0.0]^\top$
- Frame 2 Latent: $\mathbf{z}_{v_2} = [0.0, 1.0, 0.0, 1.0]^\top$

Assume projection matrices are identities for simplicity: $\mathbf{W}^Q = \mathbf{W}^K = \mathbf{W}^V = \mathbf{I}_{4 \times 4}$.

1. **Construct Q, K, and V**:
   - Query: $\mathbf{Q} = \mathbf{z}_{v_2} = [0.0, 1.0, 0.0, 1.0]^\top$
   - Concatenated keys/values source: $\Big[\mathbf{z}_{v_1}, \mathbf{z}_{v_1}\Big]$
   - Keys: $\mathbf{K} = \begin{bmatrix} 1.0 & 1.0 \\ 0.0 & 0.0 \\ 1.0 & 1.0 \\ 0.0 & 0.0 \end{bmatrix}^\top \in \mathbb{R}^{2 \times 4}$
   - Values: $\mathbf{V} = \begin{bmatrix} 1.0 & 1.0 \\ 0.0 & 0.0 \\ 1.0 & 1.0 \\ 0.0 & 0.0 \end{bmatrix}^\top \in \mathbb{R}^{2 \times 4}$

2. **Compute raw attention scores**:
   $$\mathbf{A}_{\text{raw}} = \mathbf{Q} \mathbf{K}^\top = \begin{bmatrix} 0.0 & 1.0 & 0.0 & 1.0 \end{bmatrix} \begin{bmatrix} 1.0 & 1.0 \\ 0.0 & 0.0 \\ 1.0 & 1.0 \\ 0.0 & 0.0 \end{bmatrix} = \begin{bmatrix} 0.0 & 0.0 \end{bmatrix}$$
   - Scaling factor: $\sqrt{d} = \sqrt{4} = 2$.
   $$\mathbf{A}_{\text{scaled}} = \frac{\mathbf{A}_{\text{raw}}}{2} = \begin{bmatrix} 0.0 & 0.0 \end{bmatrix}$$

3. **Compute Softmax probabilities**:
   $$\text{softmax}(\mathbf{A}_{\text{scaled}}) = \begin{bmatrix} 0.5 & 0.5 \end{bmatrix}$$

4. **Multiply by Values matrix**:
   $$\mathbf{O} = \begin{bmatrix} 0.5 & 0.5 \end{bmatrix} \cdot \begin{bmatrix} 1.0 & 0.0 & 1.0 & 0.0 \\ 1.0 & 0.0 & 1.0 & 0.0 \end{bmatrix} = \begin{bmatrix} 1.0 & 0.0 & 1.0 & 0.0 \end{bmatrix}$$

Thus, the updated representation for frame 2, via cross-frame attention, is completely aligned with the visual structure of frame 1 ($\mathbf{O} = [1.0, 0.0, 1.0, 0.0]$), anchoring the generated sequence's identity.

---

## Related

- [[Denoising Diffusion Implicit Models]] — Core deterministic sampling rules adapted by Text2Video-Zero.
- [[Latent Diffusion Models]] — Stable Diffusion backbone used by Tune-A-Video and ControlVideo.
- [[pseudo-3d-convolution]] — Alternative method for temporal modeling by factorizing convolutions rather than reprogramming attention.
