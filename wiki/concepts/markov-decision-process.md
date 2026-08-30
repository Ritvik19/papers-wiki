# Markov Decision Process

**Type**: concept  
**Tags**: #concept

## Overview

A Markov decision process (MDP) is the standard mathematical framework for reinforcement learning: an agent observes states, selects actions, receives rewards, and transitions to new states. The Markov property requires that future dynamics depend only on the current state and action, not on full history. MDPs define policies π(a|s), value functions v_π(s) and q_π(s,a), Bellman equations, and optimal policies π*.

## Appearances

- [[Reinforcement Learning: An Introduction]] — Chapter 3 formalizes the agent–environment interface, episodic vs continuing tasks, and optimality conditions.

## Notes

Sutton & Barto treat finite MDPs first (tabular), then extend to function approximation where the state is a feature vector rather than a table index. Modern LLM RL often hides the MDP behind token-level MDPs or contextual bandits, but the same return, discount, and policy-value structure applies.

## Related

- [[Reinforcement Learning: An Introduction]]
- [[Reinforcement Learning]]
- [[Dynamic Programming]]
- [[Multi-Armed Bandits]]
- [[Temporal-Difference Learning]]
- [[Monte Carlo Methods]]
- [[Q-learning]]
- [[Policy Gradient]]
