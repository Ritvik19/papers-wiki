# n-Step Methods

**Type**: concept  
**Tags**: #concept

## Overview

n-step methods in RL form a spectrum between one-step [[Temporal-Difference Learning]] and full-episode [[Monte Carlo Methods]]. An n-step return sums n rewards plus the bootstrapped value at step t+n. n-step TD prediction, n-step Sarsa, and n-step off-policy learning (with importance sampling or tree backup) unify many backup diagrams in Sutton & Barto (Chapters 7 and 12).

## Appearances

- [[Reinforcement Learning: An Introduction]] — Chapter 7; random-walk performance curves; connection to eligibility traces (Chapter 12).

## Notes

Choosing n trades bias and variance: small n updates quickly but is biased; large n approaches MC. In deep RL, n-step returns appear in distributed actors (e.g., A3C-style n-step advantages).

## Related

- [[Temporal-Difference Learning]]
- [[Monte Carlo Methods]]
- [[Eligibility Traces]]
- [[Sarsa]]
- [[Reinforcement Learning: An Introduction]]
