# Latent Diffusion Models

**Type**: concept  
**Tags**: #concept

## Overview

Latent Diffusion Models (LDM) partition generative modeling into a two-stage process: a perceptual compression stage using an autoencoder to compress pixels into low-dimensional latents, and a semantic synthesis stage where a diffusion model operates entirely in this latent space.

## Appearances

- [[What are Diffusion Models?]] — Section on latent space models and backbones.
- [[How Diffusion Models Work: The Math from Scratch]] — AI Summer Stable Diffusion overview: encoder latent diffusion, \(L_{\text{LDM}}\) loss, cascade vs latent scaling strategies.
- [[Papers Explained - GLIDE]] — Referenced as a milestone in scaling text-conditional diffusion models.

## Detailed Architecture

Traditional diffusion models operate directly in the high-dimensional pixel space $\mathcal{X}$, leading to immense training and inference computational costs. **Latent Diffusion Models** (Rombach et al., 2022) decouple this generation pipeline into a two-stage system:

1. **Perceptual Compression (Autoencoder)**: An encoder $\mathcal{E}$ maps an image $x \in \mathcal{X}$ into a low-dimensional latent space $z = \mathcal{E}(x) \in \mathcal{Z}$, which is regularized to prevent high-variance latent configurations. A decoder $\mathcal{D}$ reconstructs the image back to pixels: $\tilde{x} = \mathcal{D}(z)$.
2. **Semantic Generation (Latent Diffusion)**: A U-Net or Transformer denoising backbone is trained to reverse the forward diffusion process inside the low-dimensional latent space $\mathcal{Z}$. The standard training loss is reformulated as:
   $$L_{\text{LDM}} = \mathbb{E}_{\mathcal{E}(x), \epsilon, t} \left[ \|\epsilon - \epsilon_\theta(z_t, t, \tau_\theta(y))\|^2 \right]$$

---

## Autoencoder Regularization: KL vs. VQ

To ensure that the latent space $\mathcal{Z}$ is well-behaved and suitable for diffusion, the autoencoder utilizes one of two regularization frameworks:

### 1. KL-Regularized Autoencoder (KL-AE)
Similar to a Variational Autoencoder (VAE), a mild Kullback-Leibler divergence penalty is applied to direct the latent distribution towards a standard normal distribution $\mathcal{N}(0, \mathbf{I})$:
$$\mathcal{L}_{\text{reg}} = D_{\text{KL}}(q_\phi(z \mid x) \parallel \mathcal{N}(0, \mathbf{I}))$$
This results in continuous, smooth latent activations.

### 2. VQ-Regularized Autoencoder (VQ-AE)
Utilizing a vector quantization layer (similar to VQ-GAN), the continuous encoder activations $z_e = \mathcal{E}(x)$ are mapped to their nearest discrete codebook vectors $e_k \in \mathcal{C} = \{e_1, e_2, \dots, e_K\}$:
$$z_q = \text{quantize}(z_e) = \arg\min_{e_k \in \mathcal{C}} \|z_e - e_k\|_2$$
Although the latent variables represent discrete indices, the diffusion model treats them as continuous vectors by projecting them into the codebook embeddings or directly modeling the continuous quantized features.

---

## Dimensional Reduction and Scale Calculations

Let $f = H / h = W / w$ be the downsampling factor. For a standard $512 \times 512 \times 3$ image (pixels) mapped to a latent space with $f = 8$ and $c = 4$ latent channels:
* **Original Spatial Dimensions**: $H \times W = 512 \times 512 = 262,144$ pixels.
* **Original Feature Count**: $512 \times 512 \times 3 = 786,432$ values.
* **Latent Spatial Dimensions**: $h = H / f = 64$ and $w = W / f = 64$.
* **Latent Feature Volume**: $64 \times 64 \times 4 = 16,384$ values.
* **Dimensional Compression Ratio**:
  $$\text{Ratio} = \frac{786,432}{16,384} = 48\times \quad (97.9\% \text{ reduction in feature volume})$$

### Self-Attention Computational Savings
Since self-attention computational complexity scales quadratically $\mathcal{O}(N^2)$ with the sequence length $N$ (the number of spatial patches):
* **Pixel Space Sequence Length**: $N_{\text{pixel}} = 512 \times 512 = 262,144$.
* **Latent Space Sequence Length**: $N_{\text{latent}} = 64 \times 64 = 4,096$.
* **Computational Reduction**:
  $$\text{Savings} = \left(\frac{262,144}{4,096}\right)^2 = 64^2 = 4,096\times$$
  Operating the diffusion process inside $\mathcal{Z}$ reduces self-attention sequence operations by a factor of $4,096\times$, allowing for massive batch sizes and fast training.

---

## Architecture Flow Diagram

```
Pixel Space (X)                      Latent Space (Z)
+---------------+                    +---------------+
|               | ---- Encoder E --->|   z = E(x)    |
|   Image (x)   |                    | (Low-dim Grid)|
| (512x512x3)   |<--- Decoder D -----|   (64x64x4)   |
+---------------+                    +---------------+
                                             |
                                     [Forward Diffusion]
                                             v
                                     +---------------+
                                     |   Noisy z_t   |
                                     +---------------+
                                             |
                                             v
                             +-------------------------------+
                             |    U-Net Denoising Backbone   |
                             |  +-------------------------+  |
                             |  |      Self-Attention     |  |
                             |  +-------------------------+  |
                             |               |               |
                             |               v               |
                             |  +-------------------------+  |
                             |  |     Cross-Attention     |<------- Key (K), Value (V)
                             |  +-------------------------+  |               ^
                             +-------------------------------+               |
                                             |                               |
                                    Predicts Latent Noise                    |
                                             |                        +---------------+
                                             +----------> Loss        |   Encoder     |
                                                                      | tau_theta(y)  |
                                                                      +---------------+
                                                                             ^
                                                                             |
                                                                       Condition (y)
                                                                     (e.g., text, map)
```

---

## Conditional Guidance via Cross-Attention

To support text, semantic maps, or layout conditions $y$, LDMs map the conditioning variable into an intermediate representation $\tau_\theta(y) \in \mathbb{R}^{M \times d_T}$. The diffusion backbone integrates this conditioning via **Cross-Attention**:

$$\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d}}\right)V$$

where:
* $Q = W_Q \cdot \varphi_i(z_t)$ is the query vector projected from intermediate U-Net activations $\varphi_i(z_t)$.
* $K = W_K \cdot \tau_\theta(y)$ and $V = W_V \cdot \tau_\theta(y)$ are the keys and values projected from condition embeddings.
* $d$ is the projection dimension per attention head.

---

## Video Latent Diffusion Models (Video LDM)

To extend Latent Diffusion Models to temporal sequences, **Video LDM** (Blattmann et al., 2023) leverages a pre-trained, frozen 2D image LDM. By keeping spatial layers frozen, the model retains its vast structural and semantic priors. To model motion, the spatial backbone is inflated by interleaving **temporal convolution** and **temporal attention layers** after each spatial block. Only these newly inserted temporal parameters are trained on video sequences.

### Autoencoder Temporal Fine-Tuning and 3D Patch Discriminator
While freezing the encoder $\mathcal{E}$ keeps the latent space projection consistent, decoding video latents frame-by-frame using a frozen 2D spatial decoder $\mathcal{D}$ leads to severe high-frequency temporal flickering. To enforce temporal consistency without changing the latent representations, the autoencoder **decoder is fine-tuned** on video data.

This fine-tuning is guided by a **video-aware, patch-wise 3D temporal discriminator**. It evaluates temporal coherence across sequential patches in pixel space, pushing the reconstructed frames to be smooth and flicker-free while the encoder remains entirely frozen to preserve latent-space compatibility.

---

## Stable Video Diffusion (SVD)

**Stable Video Diffusion (SVD)** represents a robust video generation framework based on Video LDMs. It establishes a standardized **three-stage training schedule** alongside a highly automated data curation pipeline:

### 1. The Three-Stage Training Pipeline
1. **Text-to-Image Pretraining**: Establishes strong spatial composition, geometry, and semantic alignment priors using static images.
2. **Systematic Video Pretraining**: The backbone is inflated with temporal layers and trained on a large-scale, general-purpose video dataset (e.g., millions of clips) to learn general motion dynamics.
3. **High-Quality Video Fine-Tuning**: The model is fine-tuned on a smaller, extremely high-quality video subset (high resolution, high aesthetic appeal, clean motion) to produce production-grade outputs.

### 2. SVD Data Curation and Filtering Metrics
To filter noisy web-scraped video datasets into the high-quality subsets required for pretraining and fine-tuning, SVD implements three key automated filters:
- **Aesthetic Filtering**: Deep aesthetic predictors evaluate visual appeal, filtering out low-contrast, blurred, or poorly composed clips.
- **Optical Flow Motion Filtering**: Videos are filtered by their average optical flow magnitude. SVD discards clips that are completely static (insufficient motion) or have extreme, chaotic movement (camera shakes).
- **OCR Text Filtering**: OCR models detect and remove videos containing dominant text watermarks, subtitles, or channel logos, preventing the network from memorizing web artifacts.

---

## Architectural Comparison: Latent vs. Cascaded Diffusion

| Property | Latent Diffusion Models (LDM) | Cascaded Diffusion Models (e.g., Imagen) |
| :--- | :--- | :--- |
| **Generation Resolution** | Generates entirely in a single low-dimensional latent space ($64 \times 64$). | Generates sequentially across multiple diffusion models ($64^2 \to 256^2 \to 1024^2$). |
| **Inference Efficiency** | **Extremely High** (cheap latent steps + single decoder pass). | Very Low (must run separate heavy diffusion steps at high resolution). |
| **Upscaling Mechanism** | Handled by a deterministic, non-generative pretrained decoder. | Handled by conditional generative super-resolution diffusion models. |
| **Attention Latency** | Low (quadratically cheaper due to short latent sequences). | High (requires massive memory or windowed attention at high-res cascades). |
| **Training Steps** | Two-stage training (autoencoder first, then LDM). | Multi-stage training (each resolution cascade trained separately). |

---

## Worked Example: A Cross-Attention Calculation

Let's compute the cross-attention output for a single latent coordinate query vector $Q$ attending to a text prompt containing two tokens (e.g., "blue sky").
* Let the query vector be $Q = [1.0, 0.0]$.
* Let the key vectors for the two text tokens be $K_1 = [1.0, 1.0]$ and $K_2 = [0.0, 2.0]$.
* Let the value vectors for the two text tokens be $V_1 = [10.0, 20.0]$ and $V_2 = [30.0, 40.0]$.
* Assume scaling dimension $\sqrt{d} = 1.0$ (for simplicity).

1. **Calculate the Alignment Scores (Dot Products)**:
   * For Token 1: $S_1 = Q \cdot K_1 = 1.0 \cdot 1.0 + 0.0 \cdot 1.0 = 1.0$
   * For Token 2: $S_2 = Q \cdot K_2 = 1.0 \cdot 0.0 + 0.0 \cdot 2.0 = 0.0$

2. **Compute Softmax Weights**:
   * Sum of exponentials: $\sum e^{S_i} = e^{1.0} + e^{0.0} \approx 2.7183 + 1.0000 = 3.7183$
   * Weight 1: $W_1 = \frac{e^1}{3.7183} = \frac{2.7183}{3.7183} \approx 0.731$
   * Weight 2: $W_2 = \frac{e^0}{3.7183} = \frac{1.0000}{3.7183} \approx 0.269$

3. **Compute the Weighted Value Output**:
   $$\text{Attention} = W_1 V_1 + W_2 V_2$$
   $$\text{Attention} = 0.731 \cdot [10.0, 20.0] + 0.269 \cdot [30.0, 40.0]$$
   $$\text{Attention} = [7.31, 14.62] + [8.07, 10.76] = [15.38, 25.38]$$

The cross-attention output vector $[15.38, 25.38]$ is injected back into the U-Net spatial block, steering generation towards the features representing Token 1.

## Related

- [[Denoising Diffusion Probabilistic Models]]
- [[Classifier-Free Guidance]]
- [[Diffusion Transformer]]
- [[What are Diffusion Models?]]
- [[space-time-u-net]]
- [[pseudo-3d-convolution]]
- [[cross-frame-attention]]
- [[reconstruction-guidance]]

#concept
#topic
