# RubricHub

**Type**: concept  
**Tags**: #entity

## Overview

**RubricHub** is a benchmark and training corpus for rubric-graded open-ended generation in medical and science domains. Each instance pairs a free-form prompt with a weighted rubric of criteria; responses are scored by LLM judges at evaluation time.

## Appearances

- [[Papers Explained 581: Rubric-Guided Self-Distillation]] — 12,519 medical and 19,806 science train prompts; 300-prompt validation subsets.

## Notes

Also used as the training domain for judge-based GRPO baselines in RGSD. OOD eval uses HealthBench (medical) and ResearchQA (science).

## Related

- [[Rubric-Based Reinforcement Learning]]
- [[Papers Explained 553 - Rubrics as Rewards]]
- [[Evaluation and Benchmarks]]
