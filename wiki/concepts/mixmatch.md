# MixMatch

**Type**: concept  
**Tags**: #concept

## Overview

MixMatch (Berthelot et al., NeurIPS 2019) is a holistic semi-supervised framework unifying **consistency regularization**, **entropy minimization**, and **MixUp**. For each unlabeled sample it averages predictions over $K$ augmentations, aligns the marginal class distribution, sharpens with temperature $T$, then applies MixUp across labeled and unlabeled batches.

## Appearances

- [[Learning with not Enough Data Part 1: Semi-Supervised Learning]] — Label guessing pipeline, loss definitions, ablations; also referenced in Part 3 as noise filter for generated data.

## Algorithm sketch

1. For each $\mathbf{u}$: generate $K$ augmentations $\bar{\mathbf{u}}^{(k)}$, average predictions $\hat{y} = \frac{1}{K}\sum_k p_\theta(y|\bar{\mathbf{u}}^{(k)})$
2. Sharpen $\hat{y}$ with temperature $T$ to reduce class overlap
3. $\bar{\mathcal{X}}, \bar{\mathcal{U}} = \text{MixMatch}(\mathcal{X}, \mathcal{U}, T, K, \alpha)$ via MixUp
4. Minimize:
   - $\mathcal{L}_s^\text{MM} = \frac{1}{|\bar{\mathcal{X}}|}\sum D[y, p_\theta(y|\bar{\mathbf{x}}^l)]$
   - $\mathcal{L}_u^\text{MM} = \frac{1}{L|\bar{\mathcal{U}}|}\sum \|\hat{y} - p_\theta(y|\bar{\mathbf{u}})\|_2^2$

## ReMixMatch extensions (2020)

- **Distribution alignment**: normalize $p_\theta(y|\mathbf{u})$ by $p(y)/\tilde{p}(\hat{y})$ so unlabeled marginal matches labeled marginal
- **Augmentation anchoring**: weak-augment anchor + $K$ strong CTAugment views within network tolerance
- Additional rotation self-supervised loss

## Ablation insights

- MixUp on **unlabeled** data is critical
- Temperature sharpening on pseudo distributions is necessary
- Averaging $K$ augmentations for guessing is required

## Related

- [[FixMatch]]
- [[ReMixMatch]]
- [[DivideMix]]
- [[Consistency Regularization]]
- [[Semi-Supervised Learning]]
