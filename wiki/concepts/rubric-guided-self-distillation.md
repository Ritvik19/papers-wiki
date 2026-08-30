# Rubric-Guided Self-Distillation

**Type**: concept  
**Tags**: #concept

## Overview

**Rubric-Guided Self-Distillation (RGSD)** trains an unconditioned student policy to match a frozen same-checkpoint teacher that sees the prompt plus rubric criteria. It replaces LLM-judge [[GRPO]] on rubric-graded tasks with dense per-token clipped Jensen–Shannon distillation, eliminating judge calls during training.

## Appearances

- [[Papers Explained 581: Rubric-Guided Self-Distillation]] — RubricHub medical/science eval; parity with GRPO at zero train-time judge cost.

## Notes

Combines [[Self-Distilled Fine-Tuning]] (same-model teacher) with [[On-Policy Distillation]] (student rollouts) and rubric conditioning as privileged teacher context. Reasoning traces are masked to prevent rubric leakage into the student.

## Related

- [[Rubric-Based Reinforcement Learning]]
- [[On-Policy Distillation]]
- [[Self-Distilled Fine-Tuning]]
- [[GRPO]]
