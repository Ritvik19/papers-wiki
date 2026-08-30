# Contrastive Predictive Coding

**Type**: concept  
**Tags**: #concept

## Overview

Contrastive Predictive Coding (CPC), proposed by van den Oord et al. (2018), is a highly influential self-supervised representation learning framework designed to extract compact, semantically rich features from high-dimensional sequence data (such as audio, text, video, or 2D image grids). CPC operates by predicting future segments of a sequence in a *latent space* rather than in the raw pixel or waveform space. Instead of relying on generative decoders that compute high-cost reconstruction losses (which waste capacity encoding irrelevant high-frequency noise), CPC optimizes a density ratio metric using a contrastive objective called **InfoNCE**. 

```
                          Contrastive Predictive Coding (CPC) Flow
                          
   Sequence Inputs x_t          Latent Space z_t             Context Vector c_t
   +----------------+           +--------------+
   |   x_{t+2}      | ========> |   z_{t+2}    | (Positive Target)
   +----------------+           +--------------+
   |   x_{t+1}      | ========> |   z_{t+1}    |
   +----------------+           +--------------+             +------------+
   |   x_t          | ========> |   z_t        | =======+==> | GRU/Convs  | ===> c_t
   +----------------+           +--------------+        |    |  g_ar(z)   |
   |   x_{t-1}      | ========> |   z_{t-1}    | =======+    +------------+
   +----------------+           +--------------+                   ||
                                                                   || Predicts (W_k * c_t)
                                                                   \/
                                                         +--------------------+
   Negative Targets z_j                                  |   Contrastive      |
   (From other clips/times) ===========================> |   InfoNCE Loss     | <=== Maximize similarity
                                                         +--------------------+      with z_{t+k}
```

---

## Core Architecture Components

1. **Encoder ($g_{\text{enc}}$)**: A non-linear neural network (typically a 1D or 2D CNN) that maps the raw high-dimensional observation sequence $x_t$ to a compact latent representation sequence:
   $$ z_t = g_{\text{enc}}(x_t) $$
2. **Autoregressive Context Model ($g_{\text{ar}}$)**: An autoregressive network (typically a GRU or a masked CNN) that aggregates all latent representations up to the current timestep $t$ to produce a context vector:
   $$ c_t = g_{\text{ar}}(z_{\leq t}) $$

---

## The InfoNCE Objective & Mutual Information Bound

Instead of reconstructing the future observation $x_{t+k}$ directly, CPC models a **density ratio** that measures how much more likely the positive future latent $z_{t+k}$ is given the context $c_t$, relative to its unconditioned distribution:
$$ f_k(x_{t+k}, c_t) = \exp(z_{t+k}^\top W_k c_t) \propto \frac{p(x_{t+k} \mid c_t)}{p(x_{t+k})} $$
where $W_k$ is a learnable linear transformation specific to the prediction step size $k$.

For a batch containing one true positive sample $x_{t+k}$ drawn from $p(x_{t+k} \mid c_t)$ and $N-1$ negative samples $x_j$ drawn from the proposal distribution $p(x_{t+k})$, the **InfoNCE Loss** is defined as:
$$ \mathcal{L}_{\text{InfoNCE}}^{(k)} = - \mathbb{E}_{\mathcal{X}} \left[ \log \frac{f_k(x_{t+k}, c_t)}{\sum_{j=1}^N f_k(x_j, c_t)} \right] $$

### Mathematical Proof of the Mutual Information Lower Bound
Minimizing the InfoNCE loss maximizes the mutual information $I(x_{t+k}; c_t)$ between the context and the future representation. 

Let the optimal value of the density ratio function be $f_k(x, c) = c \cdot \frac{p(x \mid c)}{p(x)}$. Inserting this optimal predictor into the loss expectation:
$$ \mathcal{L}_{\text{InfoNCE}}^{(k)} = - \mathbb{E} \left[ \log \frac{\frac{p(x_{t+k} \mid c_t)}{p(x_{t+k})}}{\frac{p(x_{t+k} \mid c_t)}{p(x_{t+k})} + \sum_{j \neq t+k}^N \frac{p(x_j \mid c_t)}{p(x_j)}} \right] $$

Since the $N-1$ negative samples $x_j$ are drawn from the unconditioned proposal distribution $p(x)$, the expectation of the sum of density ratios over the negatives can be approximated using the law of large numbers:
$$ \sum_{j \neq t+k}^N \frac{p(x_j \mid c_t)}{p(x_j)} \approx (N-1) \mathbb{E}_{x \sim p(x)} \left[ \frac{p(x \mid c_t)}{p(x)} \right] = (N-1) \int p(x) \frac{p(x \mid c_t)}{p(x)} dx = N - 1 $$

Substituting this back into the InfoNCE loss:
$$ \mathcal{L}_{\text{InfoNCE}}^{(k)} \approx - \mathbb{E} \left[ \log \frac{\frac{p(x_{t+k} \mid c_t)}{p(x_{t+k})}}{\frac{p(x_{t+k} \mid c_t)}{p(x_{t+k})} + N - 1} \right] $$
$$ \mathcal{L}_{\text{InfoNCE}}^{(k)} \approx \mathbb{E} \left[ \log \left( 1 + (N-1) \frac{p(x_{t+k})}{p(x_{t+k} \mid c_t)} \right) \right] $$

For large $N$, the term $(N-1) \frac{p(x_{t+k})}{p(x_{t+k} \mid c_t)}$ is much larger than 1, allowing the approximation:
$$ \mathcal{L}_{\text{InfoNCE}}^{(k)} \approx \mathbb{E} \left[ \log \left( (N-1) \frac{p(x_{t+k})}{p(x_{t+k} \mid c_t)} \right) \right] $$
$$ \mathcal{L}_{\text{InfoNCE}}^{(k)} \approx \log(N-1) - \mathbb{E} \left[ \log \frac{p(x_{t+k} \mid c_t)}{p(x_{t+k})} \right] $$
Since $\mathbb{E}_{x, c} \left[ \log \frac{p(x \mid c)}{p(x)} \right]$ is exactly the definition of Mutual Information $I(x_{t+k}; c_t)$:
$$ \mathcal{L}_{\text{InfoNCE}}^{(k)} \approx \log(N) - I(x_{t+k}; c_t) $$

Thus, we obtain the fundamental lower bound on mutual information:
$$ I(x_{t+k}; c_t) \geq \log(N) - \mathcal{L}_{\text{InfoNCE}}^{(k)} $$

*Interpretation:* Minimizing the InfoNCE loss raises the lower bound on mutual information. Furthermore, the capacity of the mutual information bound increases logarithmically with the number of negative samples $N$.

---

## Modality Configurations

### 1D Speech/Audio Setup
- **Input**: Raw audio sampled at $16\text{ kHz}$.
- **Encoder ($g_{\text{enc}}$)**: A 5-layer 1D convolutional network with downsampling striding (total downsampling factor of 160, matching a $10\text{ ms}$ frame step).
- **Context Model ($g_{\text{ar}}$)**: A Gated Recurrent Unit (GRU) with a latent state size of 256 or 512.
- **Pretext Task**: Predict the representations of the next $K=12$ frames ($120\text{ ms}$ into the future).

### 2D Computer Vision Setup (CPC-2D)
- **Input**: High-resolution image (e.g. $256 \times 256$ pixels).
- **Grid Division**: The image is split into a $7 \times 7$ grid of $64 \times 64$ patches with a $32$-pixel overlap.
- **Encoder ($g_{\text{enc}}$)**: A ResNet backbone that maps each patch individually to a single latent vector $z_{i,j}$.
- **Context Model ($g_{\text{ar}}$)**: A 2D Masked Convolutional Neural Network. It runs top-down over the grid to generate context vectors $c_{i,j}$.
- **Pretext Task**: Predict patches in the rows *below* the context boundary $i$ using $c_{i,j}$ (e.g. predicting $z_{i+k, j}$).

---

## Appearances

- [[Self-Supervised Representation Learning]] — Detailed as a unified contrastive framework mapping temporal (audio, video) and spatial (image grids) sequences into metric spaces.
- [[Contrastive Representation Learning]] — Highlighted as a seminal work that mathematically linked contrastive representation learning to the maximization of a lower bound on mutual information.

## Related

- [[Representation Learning]]
- [[Self-Supervised Representation Learning]]
- [[Contrastive Representation Learning]]
- [[Contrastive Learning]]
- [[InfoNCE Loss]]
