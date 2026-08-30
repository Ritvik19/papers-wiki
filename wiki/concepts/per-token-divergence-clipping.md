# Per-Token Pointwise Divergence Clipping

**Type**: concept  
**Tags**: #concept

## Overview
A regularization technique for on-policy knowledge distillation that bounds token-level distribution divergence $\delta_n(v)$ within $[-\gamma, \gamma]$, preventing gradient spikes caused by heavy-tailed stylistic and formatting tokens and focusing learning on pivotal reasoning steps.

## Appearances
- [[Papers Explained 592: Self-Distilled Reasoner]] — introduced by Chen et al. (2026).

## Notes
- Stabilizes full-vocabulary logit distillation in math and code reasoning tasks.

## Related
- [[On-Policy Self-Distillation]]
- [[Generalized Knowledge Distillation]]
