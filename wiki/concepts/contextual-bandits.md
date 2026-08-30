# Contextual Bandits

**Type**: concept  
**Tags**: #concept

## Overview

Contextual bandits (associative search in Sutton & Barto) extend [[Multi-Armed Bandits]] with **context**: before each action, the agent observes features describing the situation and must choose an arm whose reward depends on that context. There is still no state transition—each round is independent—but actions have different values in different contexts. This is a bridge between bandits and full [[Markov Decision Process]] control.

## Appearances

- [[Reinforcement Learning: An Introduction]] — Section 2.8 (associative search).

## Notes

Recommendation systems and ad placement are often contextual bandits. LLM reranking and tool selection can be framed similarly when each prompt is a context.

## Related

- [[Multi-Armed Bandits]]
- [[Exploration-Exploitation Tradeoff]]
- [[Reinforcement Learning: An Introduction]]
