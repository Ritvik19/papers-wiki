# FixMatch

**Type**: concept  
**Tags**: #concept

## Overview

FixMatch (Sohn et al., CVPR 2020) simplifies semi-supervised learning to two steps on unlabeled data: (1) produce a pseudo label using a **weakly** augmented view, keeping only predictions above confidence threshold $\tau$; (2) train the model to predict that pseudo label on a **strongly** augmented view. Combined with standard supervised loss on labeled data, it achieved state-of-the-art results on CIFAR-10/100 and SVHN among methods using only the provided unlabeled training set.

## Appearances

- [[Learning with not Enough Data Part 1: Semi-Supervised Learning]] — Full algorithm, ablations, and comparison to MixMatch/UDA/ReMixMatch.

## Loss formulation

$$\mathcal{L}_s = \frac{1}{B}\sum_{b=1}^B \text{CE}(y_b, p_\theta(y|\mathcal{A}_\text{weak}(\mathbf{x}_b)))$$

$$\mathcal{L}_u = \frac{1}{\mu B}\sum_{b=1}^{\mu B} \mathbb{1}[\max(\hat{y}_b) \geq \tau]\;\text{CE}(\hat{y}_b, p_\theta(y|\mathcal{A}_\text{strong}(\mathbf{u}_b)))$$

where $\hat{y}_b = \arg\max_y p_\theta(y|\mathcal{A}_\text{weak}(\mathbf{u}_b))$ and $\mu$ controls labeled:unlabeled batch ratio.

## Augmentation asymmetry

| Role | Augmentation | Purpose |
|------|--------------|---------|
| Label guessing | $\mathcal{A}_\text{weak}$: flip-and-shift | Stable pseudo labels |
| Training target | $\mathcal{A}_\text{strong}$: RandAugment, Cutout, CTAugment | Hard consistency |

## Worked example: confidence thresholding

Suppose 3-class CIFAR-style problem, $\tau = 0.95$, one unlabeled image $\mathbf{u}$.

**Weak-augment pass** (flip + shift only):

| Class | $p_\theta(y|\mathcal{A}_\text{weak}(\mathbf{u}))$ |
|-------|-----------------------------------------------------|
| cat | 0.02 |
| dog | **0.96** |
| truck | 0.02 |

$\max = 0.96 \geq \tau$ → pseudo label $\hat{y} = \text{dog}$; sample **included** in $\mathcal{L}_u$.

**Counterexample** (flat distribution after weak aug):

| Class | Probability |
|-------|-------------|
| cat | 0.40 |
| dog | 0.35 |
| truck | 0.25 |

$\max = 0.40 < \tau$ → $\mathbb{1}[\cdot] = 0$; sample **skipped** (no gradient from this $\mathbf{u}$).

**Strong-augment pass** (only if included): RandAugment + Cutout view must still predict dog via CE — forces invariance to heavy distortion. If strong aug collapses prediction to uniform, CE loss is high and pushes representation toward aug-invariant dog features.

Typical hyperparameters from source: $\tau \in [0.9, 0.95]$; $\mu = 7$ (7× more unlabeled than labeled per batch).

## Critical ablations (from source)

- **Sharpening** with temperature $T$ has negligible effect when $\tau$ is used.
- **Cutout + CTAugment** in strong branch are necessary for best results.
- Replacing weak with strong for guessing → early divergence; no weak → overfits guessed labels.
- Strong-only pseudo prediction → unstable performance.

## Related

- [[MixMatch]]
- [[Consistency Regularization]]
- [[Unsupervised Data Augmentation]]
- [[Semi-Supervised Learning]]
- [[DivideMix]]
