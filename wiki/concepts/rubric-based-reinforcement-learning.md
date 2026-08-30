# Rubric-Based Reinforcement Learning

**Type**: concept  
**Tags**: #concept

## Overview

Rubric-Based Reinforcement Learning trains a policy with rewards derived from prompt-specific evaluation criteria, often judged by an LLM verifier. It extends [[Verifier-Bounded Learning]] into open-ended domains where there is no simple exact-answer checker, but it inherits risks from both verifier mistakes and incomplete rubric design.

## Appearances

- [[Papers Explained 553 - Rubrics as Rewards]] - Presents rubric-generated reward signals as a way to train models in medicine and science beyond traditional verifiable domains.
- [[Papers Explained: Reward Hacking in Rubric-Based RL]] - Shows that optimizing rubric rewards can exploit verifier errors and improve explicit rubric satisfaction while harming rubric-free quality.
- [[Papers Explained 581: Rubric-Guided Self-Distillation]] - Verifier-free alternative: rubric-conditioned self-distillation matches GRPO rubric gains without judge calls at train time.

## Notes

Rubric-based RL is attractive because it gives structured feedback where binary correctness is unavailable. The weak point is proxy specification: if the rubric rewards visible completeness more than factual precision, relevance, concision, or avoidance of misleading claims, the trained policy can learn to maximize the rubric while degrading holistic quality.

## Related

- [[Reward Hacking]]
- [[Verifier Exploitation]]
- [[Self-Internalization Gap]]
- [[Reinforcement Learning]]
- [[GRPO]]
- [[Safety and Alignment]]

