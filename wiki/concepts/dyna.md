# Dyna

**Type**: concept  
**Tags**: #concept

## Overview

Dyna is an architecture that integrates **planning** and **learning** in RL (Sutton, 1990). The agent learns a model from real experience, then uses that model to generate simulated experience for additional value updates—planning in the background while acting in the world. Dyna-Q alternates real Q-learning updates with simulated updates from a learned transition model.

Sutton & Barto extend the idea to prioritized sweeping, expected vs sample updates, RTDP, and heuristic search (Chapter 8).

## Appearances

- [[Reinforcement Learning: An Introduction]] — Chapter 8; maze blocking and shortcut tasks.

## Notes

AlphaGo’s MCTS is a sophisticated form of planning with a learned model; Dyna is the tabular pedagogical bridge between [[Dynamic Programming]] (known model) and model-free TD.

## Related

- [[Dynamic Programming]]
- [[Temporal-Difference Learning]]
- [[Reinforcement Learning: An Introduction]]
