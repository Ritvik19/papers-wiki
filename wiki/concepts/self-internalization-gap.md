# Self-Internalization Gap

**Type**: concept  
**Tags**: #concept

## Overview

Self-Internalization Gap is a verifier-free diagnostic for rubric-based RL. It compares a policy's log-probability for rubric-conditioned samples under two contexts: prompt-only and rubric-conditioned. As the gap moves closer to zero, the policy is interpreted as having internalized more of the rubric behavior.

## Appearances

- [[Papers Explained: Reward Hacking in Rubric-Based RL]] - Proposed as a cheaper complement to exploitation-rate measurement, which requires repeated frontier-judge panel calls.

## Notes

The diagnostic can act as a stopping heuristic: continue training while prompt-only behavior becomes closer to rubric-conditioned behavior, and be cautious once the gap stops improving. It does not by itself prove that the rubric captures the full target behavior.

## Related

- [[Rubric-Based Reinforcement Learning]]
- [[Verifier Exploitation]]
- [[Reward Hacking]]
- [[Reinforcement Learning]]
- [[Evaluation and Benchmarks]]

