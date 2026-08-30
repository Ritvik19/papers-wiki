# Consistency Regularization

**Type**: concept  
**Tags**: #concept

## Overview

Consistency regularization (consistency training) penalizes changes in model predictions under **valid perturbations** of inputs or network stochasticity (dropout, augmentation, adversarial noise). It is the dominant form of unsupervised loss $\mathcal{L}_u$ in vision semi-supervised learning and shares motivation with self-supervised methods ([[SimCLR]], [[BYOL]], [[SimCSE]]) where augmented views should map to similar outputs.

## Appearances

- [[Learning with not Enough Data Part 1: Semi-Supervised Learning]] — Π-model, temporal ensembling, Mean Teacher, VAT, ICT, UDA, FixMatch.
- [[Contrastive Representation Learning]] — Augmented-view invariance in contrastive and non-contrastive SSL.

## Method lineage

| Method | Perturbation | Target |
|--------|-------------|--------|
| Π-model | Dropout / stochastic layers | Second pass same network |
| Temporal ensembling | Single pass | EMA of past predictions $\tilde{\mathbf{z}}_i$ |
| Mean Teacher | Augmentation | EMA weight-averaged teacher |
| VAT | Virtual adversarial $r$ | Fixed-copy prediction |
| ICT / MixUp | Interpolated unlabeled pairs | Interpolated teacher preds |
| UDA / FixMatch | RandAugment / strong aug | Weak-augment or sharpened pseudo label |

## VAT (semi-supervised extension)

$$\mathcal{L}_u^\text{VAT}(\mathbf{x},\theta) = D[p_{\hat{\theta}}(y|\mathbf{x}), p_\theta(y|\mathbf{x}+r_\text{vadv})]$$
$$r_\text{vadv} = \arg\max_{\|r\|\leq\epsilon} D[p_{\hat{\theta}}(y|\mathbf{x}), p_\theta(y|\mathbf{x}+r)]$$

$\hat{\theta}$ is a fixed weight copy (no gradients). Encourages smooth prediction manifolds.

## Assumptions

Grounded in SSL hypotheses H1–H4 ([[Semi-Supervised Learning]]): smoothness, clustering, low-density separation, and manifold structure in [[Representation Learning]].

## Related

- [[Mean Teacher]]
- [[FixMatch]]
- [[Unsupervised Data Augmentation]]
- [[Virtual Adversarial Training]]
- [[Contrastive Representation Learning]]
