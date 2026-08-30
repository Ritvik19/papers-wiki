# On-Policy Learning

**Type**: concept  
**Tags**: #concept

## Overview

On-policy learning in RL trains the value function or policy for the **same policy that generates the data**. Updates use targets that depend on actions actually taken under the current policy (including exploration), as in [[Sarsa]] and SARSA-style actor–critic. On-policy methods avoid distribution mismatch between behavior and target but cannot directly learn the optimal policy from arbitrary old data.

## Appearances

- [[Reinforcement Learning: An Introduction]] — Sarsa vs Q-learning (Chapter 6); on-policy policy gradient and actor–critic (Chapter 13).

## Notes

Modern LLM RL (PPO, GRPO) is predominantly on-policy: rollouts come from the current policy, and KL penalties keep updates near the sampling distribution. Contrast with [[Off-Policy Learning]] and [[On-Policy Distillation]] in the LLM wiki.

## Related

- [[Sarsa]]
- [[Off-Policy Learning]]
- [[Policy Gradient]]
- [[On SFT RL and On-Policy Distillation]]
- [[Reinforcement Learning: An Introduction]]
