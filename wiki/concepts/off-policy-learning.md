# Off-Policy Learning

**Type**: concept  
**Tags**: #concept

## Overview

Off-policy learning in RL means learning about one policy (the **target** policy, often greedy or optimal) while following a different **behavior** policy (often exploratory, e.g. ε-greedy). [[Q-learning]] is the canonical off-policy TD control algorithm. Off-policy methods can reuse data from any behavior policy but require [[Importance Sampling]] corrections or special algorithms to remain stable.

Sutton & Barto contrast off-policy with **on-policy** methods like [[Sarsa]], which learn the value of the policy actually being followed (Chapter 6–7, 11).

## Appearances

- [[Reinforcement Learning: An Introduction]] — Chapters 5–7, 11; Baird’s counterexample and deadly triad with function approximation.

## Notes

LLM RL is often on-policy (PPO, GRPO) for stability, but off-policy ideas appear in replay buffers (DQN), importance-weighted corrections ([[Truncated Importance Sampling]]), and DPO-style preference learning from static data.

## Related

- [[Q-learning]]
- [[Sarsa]]
- [[Importance Sampling]]
- [[Deadly Triad]]
- [[Reinforcement Learning: An Introduction]]
