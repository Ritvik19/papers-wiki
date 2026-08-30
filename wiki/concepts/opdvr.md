# OPDVR

**Type**: concept  
**Tags**: #concept

## Overview

**On-policy Distillation with Verifiable Reward (OPDVR)** is a hybrid post-training framework for reasoning large language models that unifies **On-Policy Distillation (OPD)** with **Reinforcement Learning with Verifiable Rewards (RLVR)** through a simple, parameter-free **ReLU gating mechanism**. It provides dense token-level distributional guidance from a teacher policy while strictly guaranteeing that token rewards align with trajectory-level task correctness.

## Mathematical Formulation & Alignment

Sampled-token OPD minimizes sequence loss on student rollouts $o \sim \pi_\theta(\cdot \vert q)$, yielding a policy gradient with an implicit token reward $R_{\text{OPD}}(o_t) = \log \frac{\pi_T(o_t)}{\pi_\theta(o_t)}$. However, unconstrained OPD suffers from sign-correctness misalignment:
- **Correct trajectories** receive *negative* rewards when $\pi_T < \pi_\theta$ (penalizing student confidence).
- **Incorrect trajectories** receive *positive* rewards when $\pi_T > \pi_\theta$ (rewarding erroneous tokens).

OPDVR resolves this by gating the log-probability ratio with binary outcome correctness $R(o) \in \{-1, +1\}$:

$$R_{\text{OPDVR}}(o_t) = \text{sgn}(R(o)) \cdot \text{ReLU}\left(\text{sgn}(R(o)) \cdot \log \frac{\pi_T(o_t \vert q, o_{<t})}{\pi_\theta(o_t \vert q, o_{<t})}\right)$$

1. **On Correct Rollouts ($R = +1$)**: The reward is $\max(0, \log(\pi_T / \pi_\theta)) \ge 0$. Correct tokens receive positive reinforcement when the teacher is more confident than the student, while tokens where the student is already more confident are capped at zero without penalty.
2. **On Incorrect Rollouts ($R = -1$)**: The reward is $-\max(0, \log(\pi_\theta / \pi_T)) \le 0$. Erroneous tokens are penalized in proportion to student overconfidence, while errors shared by the teacher receive zero penalty.

## Appearances

- [[Papers Explained: On-policy Distillation with Verifiable Reward]] — Introduced by Lin et al. (LeapLabTHU, 2026).

## Notes

- Requires no additional loss weighting hyperparameters or heuristic multi-stage switching schedules.
- Enables student models to surpass their teachers on challenging mathematical reasoning tasks (e.g. AIME24, AIME25).

## Related

- [[On-Policy Distillation]]
- [[Reinforcement Learning with Verifiable Rewards]]
- [[GRPD]]
- [[GRPO]]
- [[Reasoning Models]]
- [[Distillation Regimes Compared]]
- [[LeapLabTHU]]
