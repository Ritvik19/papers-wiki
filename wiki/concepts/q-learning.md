# Q-learning

**Type**: concept  
**Tags**: #concept

## Overview

Q-learning is an off-policy temporal-difference control algorithm that learns the optimal action-value function q* directly. The update rule bootstraps from the maximum over next-state actions: Q(S_t, A_t) ← Q(S_t, A_t) + α[R_{t+1} + γ max_a Q(S_{t+1}, a) − Q(S_t, A_t)]. It is one of the most widely taught RL algorithms and underpins many deep RL systems (e.g., DQN) when combined with function approximation.

## Appearances

- [[Reinforcement Learning: An Introduction]] — Section 6.5; compared with Sarsa, Expected Sarsa, and Double Q-learning for maximization bias.

## Notes

Off-policy learning lets Q-learning learn about the greedy policy while following an exploratory behavior policy (e.g., ε-greedy). With function approximation and off-policy data, instability can arise (the deadly triad, Chapter 11). Double Q-learning mitigates maximization bias from using max over estimated Q values.

## Related

- [[Temporal-Difference Learning]]
- [[Sarsa]]
- [[Expected Sarsa]]
- [[Off-Policy Learning]]
- [[Markov Decision Process]]
- [[Reinforcement Learning: An Introduction]]
- [[Reinforcement Learning]]
- [[Policy Gradient]]
