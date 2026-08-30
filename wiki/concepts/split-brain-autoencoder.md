# Split-Brain Autoencoder

**Type**: concept  
**Tags**: #concept

## Overview

The Split-Brain Autoencoder, introduced by Zhang et al. (2017), is a self-supervised representation learning architecture that modifies traditional generative autoencoders to learn high-fidelity semantic visual features. Instead of training a single network to reconstruct an entire input image (which often leads to the model learning trivial pixel copy shortcuts or identity mappings), the Split-Brain Autoencoder divides the network into two disjoint, parallel sub-networks. The input data is split into two disjoint channel blocks (for example, luminance $L$ and color channels $ab$). Each sub-network is tasked with predicting one set of channels from the other, converting a standard generative task into two complementary cross-channel prediction problems.

```
                    Split-Brain Autoencoder Architecture
                    
                         Input Image X (Lab Color Space)
                                /            \
                     Luminance X_1          Chrominance X_2
                     [H x W x 1]              [H x W x 2]
                          |                        |
                    +-----------+            +-----------+
                    | Sub-Net 1 |            | Sub-Net 2 | (Disjoint Encoders)
                    |  F_1(X_1) |            |  F_2(X_2) |
                    +-----------+            +-----------+
                          |                        |
                   Predicts Chrominance      Predicts Luminance
                      \hat{X}_2                \hat{X}_1
                     [H x W x Q]              [H x W x 1]
                          |                        |
                     Classifier Loss           Regression/Clas Loss
                     (Discretized ab)          (Luminance L)
```

---

## Technical Formulation & Channel Splitting

Let $X \in \mathbb{R}^{H \times W \times C}$ be an input image. The channels are divided into two disjoint subsets:
- $X_1 \in \mathbb{R}^{H \times W \times C_1}$
- $X_2 \in \mathbb{R}^{H \times W \times C_2}$
where $C_1 \cap C_2 = \emptyset$ and $C_1 \cup C_2 = C$.

In the canonical image colorization setup using **Lab Color Space**:
- $X_1$ is the Luminance channel ($L$, $C_1 = 1$).
- $X_2$ represents the Chrominance channels ($ab$, $C_2 = 2$).

The architecture trains two independent sub-networks $F_1$ and $F_2$:
- $F_1$ predicts representation maps for $X_2$ given $X_1$:
  $$ \hat{X}_2 = F_1(X_1) $$
- $F_2$ predicts representation maps for $X_1$ given $X_2$:
  $$ \hat{X}_1 = F_2(X_2) $$

During inference or downstream transfer, the representations (feature maps) from both sub-networks are concatenated to form a single, robust visual feature map that captures both structural/geometric contours ($F_1$) and color/semantic associations ($F_2$).

---

## Multinomial Classification vs. $L_2$ Regression

A key technical breakthrough in the Split-Brain paper is the choice of loss objective. Standard autoencoders use Mean Squared Error ($L_2$ loss) to predict color values:
$$ \mathcal{L}_{L_2} = \|X_2 - \hat{X}_2\|_2^2 $$

*The Problem:* The color distribution of objects in the real world is inherently **multimodal**. For instance, an apple can be red or green. An $L_2$ loss forces the network to predict the mean value, yielding a dull grayish-brown blend, which does not represent any real color and discourages the model from committing to sharp, semantic object representations.

*The Classification Solution:* The authors formulate color prediction as a **multinomial classification** task:
1. The $ab$ chrominance space is quantized into $Q = 313$ discrete, non-overlapping color bins.
2. The ground-truth color $X_2(p)$ for each pixel $p$ is mapped to a soft-assigned probability label vector $Y_2(p, \cdot) \in [0, 1]^Q$ over the 313 bins using a soft-encoding scheme based on spatial proximity.
3. The network output $\hat{X}_2(p)$ is a 313-dimensional vector of log-probabilities.

The classification loss $\mathcal{L}_1$ for the colorization network is computed using spatial multi-class cross-entropy:
$$ \mathcal{L}_1(X_1, X_2) = - \sum_{p \in \text{pixels}} \sum_{q=1}^Q Y_2(p, q) \log \left( \frac{\exp(F_1(X_1)_{p, q})}{\sum_{j=1}^Q \exp(F_1(X_1)_{p, j})} \right) $$

For predicting luminance $X_1$ from chrominance $X_2$, since the luminance distribution is continuous and less highly multimodal, either $L_2$ regression or a discretized classification model can be used:
$$ \mathcal{L}_2(X_2, X_1) = - \sum_{p \in \text{pixels}} \sum_{l=1}^{L_{\text{bins}}} Y_1(p, l) \log P(\hat{X}_{1, p} = l \mid X_2) $$

### Total Combined Loss
The entire Split-Brain network is optimized by minimizing the joint cross-entropy loss:
$$ \mathcal{L}_{\text{total}} = \mathcal{L}_1(X_1, X_2) + \mathcal{L}_2(X_2, X_1) $$

This cross-channel task forces the encoders to extract highly correlated and semantically grounded features—like identifying a circular shape ($L$) and mapping it to the red/green classification bins ($ab$), indicating the presence of an apple—to successfully solve the prediction loop.

---

## Appearances

- [[Self-Supervised Representation Learning]] — Noted as a cross-channel generative pretext task that predicts color channels from luminance and vice versa to enforce feature correlation.

## Related

- [[Representation Learning]]
- [[Self-Supervised Representation Learning]]
- [[Autoencoders]]
