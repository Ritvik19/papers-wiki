# pseudo-3d-convolution

**Type**: concept  
**Tags**: #concept

## Overview

**Pseudo-3D Convolution (and Attention)** is an architectural adaptation block introduced in Meta's **Make-A-Video** (Singer et al. 2022) to "inflate" pre-trained 2D image diffusion models into 3D spatiotemporal video generators. 

Instead of training a full 3D convolution or attention network from scratch—which is computationally prohibitive and discards pre-trained image weights—a pseudo-3D block factorizes the 3D spatiotemporal operator into a **pre-trained 2D spatial operation** followed by a **newly initialized 1D temporal operation**. By initializing the temporal layers as identity functions, the model starts training behaving exactly like the original 2D image model, fully preserving its text-to-image semantic priors.

## Appearances

- [[Diffusion Models for Video Generation]] — Primary survey page detailing Make-A-Video's model inflation pipeline.

---

## Mathematical Formulation

Let the input hidden feature map tensor be denoted as $\mathbf{h} \in \mathbb{R}^{B \times C \times F \times H \times W}$, where:
- $B$ is the batch size.
- $C$ is the number of channels.
- $F$ is the number of frames (temporal dimension).
- $H, W$ are the spatial height and width.

### 1. Pseudo-3D Convolution ($\text{Conv}_{\text{P3D}}$)
A full 3D spatial-temporal convolution with kernel size $K \times K \times K$ operates simultaneously over space and time. A pseudo-3D convolution factorizes this by sequential application:
1. Apply the pre-trained spatial 2D convolution $\text{Conv}_{\text{2D}}$ (kernel size $1 \times K \times K$) treating the temporal frame dimension as part of the batch dimension:
   $$\mathbf{h}_{\text{spatial}} = \text{Conv}_{\text{2D}}(\mathbf{h}) \quad \text{where} \quad \mathbf{h}_{\text{spatial}} \in \mathbb{R}^{(B \cdot F) \times C \times H \times W}$$
2. Permute the dimensions (swap temporal frame axis with spatial axis) using transpose operator $\circ T$, reshaping the tensor into temporal format $\mathbb{R}^{(B \cdot H \cdot W) \times C \times F}$.
3. Apply a 1D temporal convolution $\text{Conv}_{\text{1D}}$ (kernel size $K \times 1 \times 1$) over the frame axis:
   $$\mathbf{h}_{\text{temporal}} = \text{Conv}_{\text{1D}}(\mathbf{h}_{\text{spatial}} \circ T)$$
4. Reverse the permutation and return the tensor to the original spatiotemporal format:
   $$\text{Conv}_{\text{P3D}}(\mathbf{h}) = \mathbf{h}_{\text{temporal}} \circ T \quad \in \mathbb{R}^{B \times C \times F \times H \times W}$$

Expressing the entire sequence as a single mathematical mapping:
$$\text{Conv}_{\text{P3D}}(\mathbf{h}) = \text{Conv}_{\text{1D}}(\text{Conv}_{\text{2D}}(\mathbf{h}) \circ T) \circ T$$

---

### 2. Pseudo-3D Attention ($\text{Attn}_{\text{P3D}}$)
To perform attention over both spatial and temporal axes efficiently:
1. Apply a spatial 2D self-attention block $\text{Attn}_{\text{2D}}$ across the spatial coordinates, flattening spatial axes ($H \times W \to HW$) and treating the temporal frame dimension as batch:
   $$\mathbf{h}_{\text{att-spatial}} = \text{Attn}_{\text{2D}}(\text{flatten}(\mathbf{h})) \quad \text{where} \quad \mathbf{h} \in \mathbb{R}^{(B \cdot F) \times C \times HW}$$
2. Reshape and permute the spatial attention outputs to cluster temporal coordinates, creating a tensor of shape $\mathbb{R}^{(B \cdot HW) \times C \times F}$.
3. Apply a 1D temporal self-attention block $\text{Attn}_{\text{1D}}$ along the temporal frame dimension $F$:
   $$\mathbf{h}_{\text{att-temporal}} = \text{Attn}_{\text{1D}}(\mathbf{h}_{\text{att-spatial}} \circ T)$$
4. Reverse the permutation and unflatten the spatial dimension to yield the spatiotemporal output:
   $$\text{Attn}_{\text{P3D}}(\mathbf{h}) = \text{flatten}^{-1}(\mathbf{h}_{\text{att-temporal}} \circ T) \quad \in \mathbb{R}^{B \times C \times F \times H \times W}$$

Expressing the complete mapping:
$$\text{Attn}_{\text{P3D}}(\mathbf{h}) = \text{flatten}^{-1}\left( \text{Attn}_{\text{1D}}(\text{Attn}_{\text{2D}}(\text{flatten}(\mathbf{h})) \circ T) \circ T \right)$$

---

## Identity Initialization and Training Dynamics

The newly inserted 1D temporal convolution and 1D temporal attention layers are initialized as **identity operations**:
- For $\text{Conv}_{\text{1D}}$, the temporal kernel weights are set to $1.0$ at the center coordinate and $0.0$ elsewhere, with biases set to $0$.
- For $\text{Attn}_{\text{1D}}$, the projection output weights (or biases) are initialized to zero, making the block output a shortcut skip-connection.

This configuration guarantees that at timestep $0$ of training, the model behaves exactly like the pre-trained 2D image generator:
$$\text{Conv}_{\text{P3D}}(\mathbf{h}) \approx \text{Conv}_{\text{2D}}(\mathbf{h}), \quad \text{Attn}_{\text{P3D}}(\mathbf{h}) \approx \text{Attn}_{\text{2D}}(\mathbf{h})$$

During training, the 2D spatial weights inherited from the image model are kept **frozen**, and **only the newly added 1D temporal layers** are fine-tuned on target video datasets. This prevents catastrophic forgetting, allowing the model to generate coherent motion dynamics while fully retaining its capacity to generate high-fidelity, complex scenes from text prompts.

---

## Worked Example: A Pseudo-3D Convolution Tensor Trace

Let's trace a spatiotemporal hidden state through the pseudo-3D convolution pipeline.
- Input tensor dimensions: $B=2, C=64, F=4, H=8, W=8$.
- Input shape: $[2, 64, 4, 8, 8]$

1. **Spatial Dims Grouping**:
   Reshape the tensor to treat frames as part of the batch for spatial 2D convolution:
   * Batch size for 2D convolution: $B_{\text{spatial}} = B \cdot F = 2 \cdot 4 = 8$
   * Spatial tensor shape: $[8, 64, 8, 8]$

2. **Spatial 2D Convolution**:
   Apply spatial 2D convolution (e.g. padding preserved, channel size kept at $C=64$):
   * Output spatial tensor shape: $[8, 64, 8, 8]$

3. **Temporal Dims Grouping ($\circ T$)**:
   Reshape back to spatiotemporal format $[2, 64, 4, 8, 8]$, then transpose (permute) dimensions to prepare for 1D temporal convolution:
   * Target coordinates to collapse: Batch size and spatial coordinates ($B \cdot H \cdot W = 2 \cdot 8 \cdot 8 = 128$)
   * Permute to put temporal axis at the end: $[B \cdot H \cdot W, C, F] = [128, 64, 4]$

4. **Temporal 1D Convolution**:
   Apply a 1D convolution with kernel size $3 \times 1 \times 1$ along the temporal frame axis (dimension of size $4$):
   * Output temporal tensor shape: $[128, 64, 4]$

5. **Inverse Permutation and Reshape ($\circ T$)**:
   Permute the axes back to $[B, C, F, H, W]$ format:
   * Output shape: $[2, 64, 4, 8, 8]$

The tensor has successfully passed through factorized spatial and temporal feature extractions while retaining its original dimensions.

---

## Related

- [[space-time-u-net]] — Architectural concept page using factorized spatiotemporal convolutions.
- [[What are Diffusion Models?]] — Foundational architectures and 2D U-Net backbones.
