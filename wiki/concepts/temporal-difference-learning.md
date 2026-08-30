# Temporal-Difference Learning

**Type**: concept  
**Tags**: #concept

## Overview

Temporal-difference (TD) learning is a family of reinforcement learning methods that bootstrap: they update value estimates using other learned estimates rather than waiting for complete episode outcomes. The TD(0) prediction rule adjusts V(S_t) toward R_{t+1} + γ V(S_{t+1}). TD methods combine advantages of Monte Carlo (learning from experience) and dynamic programming (online bootstrapping). Key control algorithms include Sarsa, Q-learning, and Expected Sarsa.

## Appearances

- [[Reinforcement Learning: An Introduction]] — Chapter 6 introduces TD prediction and control; Chapter 12 covers eligibility traces as the backward-view generalization.

## Notes

TD learning's connection to dopamine reward prediction errors (Chapter 15) is one of the book's bridges to neuroscience. In LLM post-training, token-level advantage estimation in policy gradient methods (PPO, GRPO) inherits the bootstrapping spirit of TD, though the state space and reward structure differ.

## Related

- [[Reinforcement Learning: An Introduction]]
- [[Monte Carlo Methods]]
- [[Sarsa]]
- [[Q-learning]]
- [[n-Step Methods]]
- [[Eligibility Traces]]
- [[Dynamic Programming]]
- [[Markov Decision Process]]
- [[Policy Gradient]]
- [[Reinforcement Learning from Human Feedback]]
