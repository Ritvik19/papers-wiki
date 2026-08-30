# Meta Pseudo Labels

**Type**: concept  
**Tags**: #concept

## Overview

Meta Pseudo Labels (Pham et al., CVPR 2021) trains teacher and student **in parallel**: the student learns from teacher pseudo labels on unlabeled data; the teacher is updated to minimize the student's loss on **labeled** data (meta-learning the label generator). Approximates bi-level optimization with one-step student gradient (MAML-style).

## Appearances

- [[Learning with not Enough Data Part 1: Semi-Supervised Learning]] — Objective derivation, alternating update procedure, results vs FixMatch/Noisy Student.
- [[Best Deep CNN Architectures and Their Principles: from AlexNet to EfficientNet]] — teacher feedback loop correcting pseudo-label confirmation bias; 90.2% Top-1 with EfficientNet-L2 (2021).

## Bi-level objective

$$\min_{\theta_T} \mathcal{L}_s(\theta^\text{PL}_S(\theta_T)) = \min_{\theta_T} \mathbb{E}_{(\mathbf{x}^l,y)\in\mathcal{X}} \text{CE}[y, f_{\theta_S}(\mathbf{x}^l)]$$

$$\text{where } \theta^\text{PL}_S(\theta_T) \approx \theta_S - \eta_S \nabla_{\theta_S} \mathcal{L}_u(\theta_T, \theta_S)$$

$\mathcal{L}_u$ = CE between teacher and student on unlabeled pseudo labels. Teacher also gets UDA consistency loss.

## Update loop

1. **Student**: SGD on unlabeled batch with teacher pseudo labels → $\theta'_S$
2. **Teacher**: SGD on labeled batch using $\theta'_S$ as implicit student state

Soft pseudo labels required for differentiability; hard labels need REINFORCE.

## Related

- [[Noisy Student]]
- [[Unsupervised Data Augmentation]]
- [[Semi-Supervised Learning]]
