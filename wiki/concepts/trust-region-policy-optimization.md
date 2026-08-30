# Trust Region Policy Optimization

**Type**: concept  
**Tags**: #concept

## Overview

Trust Region Policy Optimization (TRPO) maximizes a policy improvement surrogate subject to a **KL divergence** constraint E[KL(π_old, π_new)] ≤ δ, keeping each update inside a local trust region where approximations remain valid. The constrained problem is solved numerically with conjugate gradient on a linearized objective and quadratically approximated KL constraint.

## Appearances

- [[Trust Region and Proximal Policy Optimization (TRPO and PPO)]] — AI Summer intuitive walkthrough of trust regions, KL constraint, and conjugate-gradient solve.
- [[Proximal Policy Optimization]] — simpler clip/penalty formulation that largely superseded TRPO in practice.

## Notes

TRPO motivated PPO by showing constrained policy updates improve stability over vanilla policy gradients with fixed learning rates.

## Related

- [[Proximal Policy Optimization]]
- [[KL Divergence]]
- [[Actor-Critic Methods]]
- [[Policy Gradient]]
