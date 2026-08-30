# Generalized Knowledge Distillation

**Type**: concept  
**Tags**: #concept

## Overview
A foundational knowledge distillation framework introduced by Agarwal et al. (2023) that unifies on-policy and off-policy distillation across generalized divergence metrics (Forward KL, Reverse KL, and JSD), addressing exposure bias by training students on their own generated rollouts with teacher feedback.

## Appearances
- [[Papers Explained 591: Generalized Knowledge Distillation]] — foundational paper.
- [[On-Policy Distillation]] — theoretical foundation.

## Notes
- Introduces on-policy mixture parameter $\lambda$ and compares mode-covering (Forward KL) with mode-seeking (Reverse KL) behavior.

## Related
- [[On-Policy Distillation]]
- [[Model Distillation]]
- [[Distillation Regimes Compared]]
