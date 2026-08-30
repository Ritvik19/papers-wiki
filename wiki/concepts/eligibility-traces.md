# Eligibility Traces

**Type**: concept  
**Tags**: #concept

## Overview

Eligibility traces provide a **backward-view** mechanism for credit assignment in temporal-difference learning. Each state (or state–action pair) maintains a trace e(s) that decays over time and is incremented when visited; TD errors update all states in proportion to their current trace. TD(λ) unifies TD(0) and Monte Carlo: λ=0 is one-step TD; λ→1 approaches full MC returns.

Sutton & Barto treat traces separately from n-step forward-view methods (Chapter 12), with replacing vs accumulating traces, Sarsa(λ), Watkins’s Q(λ), and tree backup.

## Appearances

- [[Reinforcement Learning: An Introduction]] — Chapter 12; 19-state random walk, Mountain Car with Sarsa(λ).

## Notes

Traces are less common in large-scale deep RL than in tabular and linear-function settings, but the λ-return idea informs advantage estimation horizons in modern policy optimization.

## Related

- [[Temporal-Difference Learning]]
- [[n-Step Methods]]
- [[Monte Carlo Methods]]
- [[Reinforcement Learning: An Introduction]]
