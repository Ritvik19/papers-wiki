# Virtual Adversarial Training

**Type**: concept  
**Tags**: #concept

## Overview

Virtual Adversarial Training (VAT; Miyato et al., 2018) applies adversarial perturbations to inputs that maximally change model predictions while staying within an $\epsilon$-ball — without requiring labels. In semi-supervised learning, the reference distribution is the model's own prediction on the clean input (fixed weight copy $\hat{\theta}$), making VAT applicable to unlabeled data.

## Appearances

- [[Learning with not Enough Data Part 1: Semi-Supervised Learning]] — SSL extension of supervised adversarial training; smoothness regularization on prediction manifolds.
- [[Consistency Regularization]] — Listed in method lineage table.

## Loss

$$\mathcal{L}_u^\text{VAT}(\mathbf{x},\theta) = D[p_{\hat{\theta}}(y|\mathbf{x}), p_\theta(y|\mathbf{x}+r_\text{vadv})]$$

## Related

- [[Consistency Regularization]]
- [[Adversarial Training]]
- [[Unsupervised Data Augmentation]]
