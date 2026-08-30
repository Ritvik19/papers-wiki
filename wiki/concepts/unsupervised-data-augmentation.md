# Unsupervised Data Augmentation

**Type**: concept  
**Tags**: #concept

## Overview

Unsupervised Data Augmentation (UDA; Xie et al., NeurIPS 2020) trains models to predict consistently between an unlabeled example and a strongly augmented copy. It emphasizes that **augmentation quality** — not just consistency — drives SSL performance: RandAugment for images, back-translation + TF-IDF word replacement for text.

## Appearances

- [[Learning with not Enough Data Part 1: Semi-Supervised Learning]] — CIFAR-10 with 250 labels; BERT fine-tuning complementarity on text.
- [[Learning with not Enough Data Part 3: Data Generation]] — RandAugment lineage in augmentation policy discussion.

## Loss (with masking and sharpening)

$$\mathcal{L}_u^\text{UDA} = \mathbb{1}[\max_{y'} p_{\hat{\theta}}(y'|\mathbf{x}) > \tau] \cdot D[p^{(\text{sharp})}_{\hat{\theta}}(y|\mathbf{x};T), p_\theta(y|\bar{\mathbf{x}})]$$

$$p^{(\text{sharp})}_{\hat{\theta}}(y|\mathbf{x};T) = \frac{\exp(z^{(y)}/T)}{\sum_{y'} \exp(z^{(y')}/T)}$$

$\hat{\theta}$ fixed (no grad); $\bar{\mathbf{x}}$ augmented; $\tau$ confidence threshold; $T$ sharpening temperature.

## Training techniques

- **Low-confidence masking**: skip examples below $\tau$
- **Sharpening**: low $T$ reduces pseudo-label class overlap
- **In-domain filtration**: classifier filter on large out-of-domain pool to retain in-domain unlabeled data

## Distinction from UDG

**UDA** = consistency SSL with augmentation. **[[Unsupervised Data Generation]]** (UDG) = few-shot LM synthesis of new training examples — different problem despite similar acronym.

## Related

- [[FixMatch]]
- [[Consistency Regularization]]
- [[RandAugment]]
- [[Semi-Supervised Learning]]
