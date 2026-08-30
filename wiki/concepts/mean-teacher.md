# Mean Teacher

**Type**: concept  
**Tags**: #concept

## Overview

Mean Teacher (Tarvainen & Valpola, NeurIPS 2017) maintains an exponential moving average (EMA) of student **weights** as a separate teacher network. The student is trained to match teacher predictions on augmented unlabeled inputs, providing smoother consistency targets than per-epoch prediction ensembling (temporal ensembling) on large datasets.

## Appearances

- [[Learning with not Enough Data Part 1: Semi-Supervised Learning]] — Compared to Π-model on SVHN; ablation on $\beta$, augmentation, and loss choice.

## Update rule

$$\theta' \leftarrow \beta \theta' + (1-\beta)\theta$$

Student weights $\theta$ update every step; teacher $\theta'$ is a slow EMA. Consistency loss minimizes $D[p_{\theta'}(y|\mathbf{x}), p_\theta(y|\bar{\mathbf{x}})]$ (MSE preferred over KL in ablations).

## Design choices

| Factor | Recommendation |
|--------|----------------|
| Augmentation / dropout | Required on **student** only |
| EMA $\beta$ | $0.99$ during ramp-up, $0.999$ later |
| Consistency metric | MSE > KL in reported experiments |
| vs Temporal ensembling | Faster target refresh; better on large data |

## Related

- [[Consistency Regularization]]
- [[MoCo]]
- [[BYOL]]
- [[Semi-Supervised Learning]]
