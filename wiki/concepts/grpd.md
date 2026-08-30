# GRPD

**Type**: concept  
**Tags**: #concept

## Overview

**Group Relative Policy Distillation (GRPD)** is an extension of [[OPDVR]] to group-based policy optimization (e.g. [[GRPO]]), replacing binary trajectory correctness signs with normalized group-relative advantages $\hat{A}_{i,t}$.

## Formulation

For a group of $G$ sampled responses per prompt $\{o_1, \dots, o_G\}$, standard GRPO computes a scalar trajectory advantage $\hat{A}_{i} = \frac{R(o_i) - \text{mean}(R)}{\text{std}(R)}$. GRPD applies the ReLU-gated distillation mechanism to each sampled token $o_{i,t}$, scaling the resulting signal by the group-relative advantage:

$$R_{\text{GRPD}}(o_{i,t}) = \text{sgn}(\hat{A}_{i,t}) \cdot \text{ReLU}\left(\text{sgn}(\hat{A}_{i,t}) \cdot \log \frac{\pi_T(o_{i,t} \vert q, o_{i,<t})}{\pi_\theta(o_{i,t} \vert q, o_{i,<t})}\right) \cdot |\hat{A}_{i,t}|$$

The complete training objective is optimized directly via policy gradients:

$$\mathcal{L}_{\text{GRPD}}(\theta) = -\mathbb{E}_{q \sim \mathcal{D}, \{o_i\}_{i=1}^G \sim \pi_\theta} \left[ \frac{1}{G} \sum_{i=1}^G \frac{1}{|o_i|} \sum_{t=1}^{|o_i|} R_{\text{GRPD}}(o_{i,t}) \log \pi_\theta(o_{i,t} \vert q, o_{i,<t}) \right]$$

## Appearances

- [[Papers Explained: On-policy Distillation with Verifiable Reward]] — Introduced as the advantage-weighted generalization of OPDVR.

## Notes

- Combines dense token-level teacher guidance with baseline-subtracted group advantages, eliminating the need for a separate critic network.
- Outperforms both pure GRPO and vanilla OPD on competition reasoning benchmarks (e.g. +6.5 on AIME24, +10.9 on AIME25).

## Related

- [[OPDVR]]
- [[GRPO]]
- [[On-Policy Distillation]]
- [[Reinforcement Learning with Verifiable Rewards]]
- [[Reasoning Models]]
- [[Reinforcement Learning Topic]]
