# Multi-Armed Bandits

**Type**: concept  
**Tags**: #concept

## Overview

A multi-armed bandit is a simplified RL problem: the agent repeatedly chooses among k actions (“arms”), each yielding a stochastic reward, with no state transitions. The goal is to maximize cumulative reward by balancing **exploration** (trying arms to estimate their value) and **exploitation** (pulling the arm that currently looks best). Sutton & Barto use bandits (Chapter 2) as the cleanest introduction to the exploration–exploitation tradeoff before full MDP control.

Key algorithms include ε-greedy action selection, optimistic initial values, **upper-confidence-bound (UCB)** action selection, gradient bandit algorithms, and contextual bandits (associative search).

## Appearances

- [[Reinforcement Learning: An Introduction]] — Chapter 2; 10-armed testbed, incremental sample-average updates, nonstationary bandits.

## Notes

Bandits are not MDPs: there is a single state and only action values q*(a) to learn. Many ideas (ε-greedy, UCB, reward baselines) reappear in later chapters for full RL control.

## Related

- [[Exploration-Exploitation Tradeoff]]
- [[Reinforcement Learning: An Introduction]]
- [[Reinforcement Learning]]
- [[Markov Decision Process]]
