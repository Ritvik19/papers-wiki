# Diffusion Transformer

**Type**: concept  
**Tags**: #concept

## Overview

Diffusion Transformer (DiT) is a generative model architecture that replaces the traditional convolutional U-Net backbone with a patchified Vision Transformer (ViT) operating over latent spaces, demonstrating strong scaling behavior and improved generative sample efficiency.

## Appearances

- [[What are Diffusion Models?]] — Section on modern backbones and scalable diffusion architectures.

## Detailed Architecture

In traditional [[Latent Diffusion Models]] (LDM), the denoising backbone is a convolutional U-Net. **Diffusion Transformer** (DiT) (Peebles & Xie, 2023) replaces this backbone entirely with a Vision Transformer (ViT) operating over latent sequences:

1. **Patchification**: The input latent $z \in \mathbb{R}^{C \times H \times W}$ is divided into a sequence of non-overlapping patches $z_p \in \mathbb{R}^{p^2 C}$ with patch size $p$ (typically $p=2$ or $p=4$). The patches are flattened and linearly projected to sequence embeddings.
2. **Denoising Transformers**: The sequence is augmented with standard learnable positional embeddings and passed through a series of DiT blocks.
3. **Linear Decoder**: Output tokens from the last DiT block are un-flattened and linearly projected back to the target latent shape.

---

## Block Conditioning Variants

Peebles & Xie compared four distinct strategies for injecting the timestep $t$ and conditional labels $y$ into the transformer block:

1. **In-Context Conditioning**:
   The timestep and label embeddings are prepended as two additional tokens to the sequence, similar to a CLS token. While computationally cheap, this increases sequence length.
2. **Cross-Attention Conditioning**:
   Condition embeddings are absorbed via an extra cross-attention block inserted inside each transformer block, identical to standard LDMs. This adds massive parameter overhead ($\approx 15\%$).
3. **Adaptive Layer Normalization (adaLN)**:
   Timestep and class label embeddings are summed to a conditioning vector $c = \text{MLP}(t) + \text{MLP}(y)$, which is then mapped by a linear layer to predict scale $\gamma$ and shift $\beta$ parameters to modulate normalization:
   $$\text{adaLN}(h, y, t) = \gamma(y, t) \odot \left(\frac{h - \mu}{\sigma}\right) + \beta(y, t)$$
4. **adaLN-Zero (Best Performing)**:
   Extends standard adaLN by predicting an additional block-level scale parameter $\alpha$ initialized to zero. This acts as a residual gate, initializing the entire model to act as an identity function at step zero, greatly stabilizing early training.

---

## The adaLN-Zero Block Equations

For a sequence vector $x$ entering a DiT block, we predict six dimension-wise scaling, shifting, and gating parameters from the conditioning vector $c$:

$$\left(\gamma_1, \beta_1, \alpha_1, \gamma_2, \beta_2, \alpha_2\right) = \text{Linear}(c)$$

where the Linear layer is block-specific and initialized to output zero. The block updates are formulated as:

### 1. Multi-Head Self-Attention (MSA) Path
$$\tilde{x} = x + \alpha_1 \cdot \text{MSA}\left(\text{adaLN}(x, \gamma_1, \beta_1)\right)$$

### 2. Point-wise Feedforward Network (FFN) Path
$$x_{\text{out}} = \tilde{x} + \alpha_2 \cdot \text{FFN}\left(\text{adaLN}(\tilde{x}, \gamma_2, \beta_2)\right)$$

where:
$$\text{adaLN}(h, \gamma, \beta) = (1 + \gamma) \odot \left(\frac{h - \mu}{\sigma}\right) + \beta$$

Since $\alpha_1, \alpha_2$ are initialized to zero, at the start of training $x_{\text{out}} = x$, allowing the model to act as a stable identity mapping initially, which accelerates training convergence.

---

## adaLN-Zero Block Diagram

```
                        x (Input sequence)
                        |
            +-----------+-----------+
            |                       |
            |                 [adaLN-1] <--- Modulation parameters (gamma1, beta1)
            |                       |
            |                 [ MSA  ]
            |                       |
            |                 [* alpha1] <-- Scale gate alpha1 (init to 0)
            |                       |
            +------------> [ + ] <-- Add residual
                            |
                            v (Intermediate state x_tilde)
            +---------------+-------+
            |                       |
            |                 [adaLN-2] <--- Modulation parameters (gamma2, beta2)
            |                       |
            |                 [ FFN  ]
            |                       |
            |                 [* alpha2] <-- Scale gate alpha2 (init to 0)
            |                       |
            +------------> [ + ] <-- Add residual
                            |
                            v
                       x_out (Output sequence)
```

---

## Spacetime Patch Tokenization (Sora)

OpenAI's **Sora** scales the Diffusion Transformer (DiT) architecture to serve as a unified spatiotemporal video generator. While prior methods factorize video generations using separate 2D spatial and 1D temporal networks, Sora treats the video sequence as a unified 3D spatiotemporal volume. The key technique enabling this is **Spacetime Patch Tokenization**:

```
Spacetime Volume Partitioning:
[  Frame 1  ] [  Frame 2  ] [  Frame 3  ] [  Frame 4  ]
+-----------+ +-----------+ +-----------+ +-----------+
| (px, py)  | |           | |           | |           |
|  [Patch]  | |  [Patch]  | |           | |           |
+-----------+ +-----------+ +-----------+ +-----------+
    |               |
    +-------+-------+
            v
    [ 3D Spacetime Block ] ---> Flattened 1D Visual Token
```

1. **3D Latent Compression**: A video $x \in \mathbb{R}^{T \times H \times W \times C}$ is encoded into a lower-dimensional latent variable $z \in \mathbb{R}^{t \times h \times w \times c}$ using a spatiotemporal autoencoder. This autoencoder compresses both spatial resolution and temporal frame rate.
2. **Non-Overlapping Spacetime Blocks**: The compressed 3D latent volume is sliced into small, non-overlapping spacetime blocks of shape $p_t \times p_h \times p_w$. For example, a block might span $p_t = 2$ temporal frames and $p_h \times p_w = 4 \times 4$ spatial latent grid cells.
3. **Flat Sequence Projection**: Each 3D block is flattened into a vector of size $p_t \cdot p_h \cdot p_w \cdot c$ and linearly projected into a vector of dimension $d$, representing a single visual token. The total sequence length passed to the DiT is:
   $$N = \left(\frac{t}{p_t}\right) \cdot \left(\frac{h}{p_h}\right) \cdot \left(\frac{w}{p_w}\right)$$
4. **Handling Arbitrary Dimensions**: Since the Transformer operates on a flat 1D sequence of tokens, the network can process inputs of **any resolution, aspect ratio, or duration**. Rather than cropping videos to fixed sizes, SVD/Sora simply packs whatever number of spacetime patches are generated by the video dimensions, adapting dynamically by providing corresponding 3D positional embeddings to the visual sequence.

---

## Model Classes and Sizes

| Model Class | Depth | Hidden Dimension $d$ | Attention Heads | Parameters (M) | GFLOPs ($p=2$) | GFLOPs ($p=4$) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **DiT-S** | 12 | 384 | 6 | 33M | 9.9 | 2.5 |
| **DiT-B** | 12 | 768 | 12 | 130M | 39.1 | 9.8 |
| **DiT-L** | 24 | 1024 | 16 | 458M | 137.9 | 34.5 |
| **DiT-XL**| 28 | 1152 | 16 | 675M | 203.2 | 50.8 |

---

## Worked Example: adaLN-Zero Denoising Block Update

Let's compute the output of an adaLN-Zero self-attention path for a single feature value $h = 2.0$ inside an input sequence $x$.
* Let the current layer stats be mean $\mu = 0.5$ and standard deviation $\sigma = 1.5$.
* Let the linear projection from conditioning vector $c$ predict modulation parameters:
  $$\gamma_1 = 0.3 \quad \text{and} \quad \beta_1 = -0.2$$
* Let the block scale parameter be $\alpha_1 = 0.5$.
* Assume the Multi-Head Attention layer outputs a coordinate activation of $\text{MSA}_{\text{out}} = 1.2$.

1. **Calculate the Normalized Activation**:
   $$\hat{h} = \frac{h - \mu}{\sigma} = \frac{2.0 - 0.5}{1.5} = 1.0$$

2. **Compute modulated adaLN output**:
   $$\text{adaLN}(h, \gamma_1, \beta_1) = (1 + \gamma_1) \cdot \hat{h} + \beta_1$$
   $$\text{adaLN} = (1 + 0.3) \cdot 1.0 + (-0.2) = 1.3 - 0.2 = 1.1$$

3. **Apply the Gated MSA Update**:
   Assuming the input sequence value is $x = h = 2.0$:
   $$\tilde{x} = x + \alpha_1 \cdot \text{MSA}_{\text{out}}$$
   $$\tilde{x} = 2.0 + 0.5 \cdot 1.2 = 2.0 + 0.6 = 2.6$$

This worked update demonstrates how the predicted conditioning factors linearly modulate normalization scaling, and how $\alpha_1$ gates the update residual back into the primary latent sequence.

## Related

- [[Latent Diffusion Models]]
- [[Denoising Diffusion Probabilistic Models]]
- [[What are Diffusion Models?]]
- [[space-time-u-net]]
- [[pseudo-3d-convolution]]

#concept
#topic
