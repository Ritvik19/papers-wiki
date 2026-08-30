# RL's Razor

**Type**: concept  
**Tags**: #concept

## Overview

RL's Razor is a theoretical property of on-policy reinforcement learning showing that, even without an explicit KL divergence penalty during training, on-policy policy gradient updates implicitly bias optimization toward solutions that minimize the KL divergence from the initialization policy ($D_{KL}(\pi^* || \pi_0)$).

## Implications

Because on-policy rollouts explore locally around the current model's functional region rather than fitting a distant extrinsic supervisor distribution:
- **Minimal Parameter Updates**: Update vectors $\Delta W$ maintain tiny $L_2$ norms ($\approx 3 \times 10^{-2}$).
- **Parameter Sparsity**: Only a small fraction (~20%) of model parameters undergo noticeable magnitude shifts ($> 10^{-5}$).
- **High-Dimensional Orthogonality**: In high-dimensional parameter spaces, sparse independent vectors are mutually orthogonal with high probability, preventing interference across different tasks.

## Appearances

- [[Papers Explained: SFT Conflicts, RL Coexists]] — Used to explain why RL updates remain sparse, minimal, and mutually orthogonal across diverse reasoning domains.

## Related

- [[KL Regularization]]
- [[Gradient Interference]]
- [[Task Coexistence]]
- [[On-Policy Learning]]
- [[Supervised Fine-Tuning]]
- [[Reinforcement Learning]]
