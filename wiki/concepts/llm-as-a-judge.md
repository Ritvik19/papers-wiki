# LLM-as-a-Judge

**Type**: concept  
**Tags**: #concept

## Overview

An evaluation method where a separate strong LLM scores a candidate model's response against a reference answer using a predefined rubric (typically 1–5). Evaluating answers is often easier than generating them, which partly explains judge effectiveness—but results depend on judge capability, rubric design, and can inherit style biases.

## Appearances

- [[Understanding the 4 Main Approaches to LLM Evaluation (From Scratch)]] — Ollama `gpt-oss:20b` implementation with a five-point rubric; batch MATH-500 evaluation on GitHub.
- [[Papers Explained 170 - Prometheus]] — open-source 13B judge trained on GPT-4-curated rubric feedback data.
- [[Papers Explained 553 - Rubrics as Rewards]] — rubric-based judges as RL reward signals (RaR framework).

## Notes

- Common setups use proprietary API models (e.g., GPT-5); specialized judge models also exist.
- Related to process reward models (PRMs), which score intermediate reasoning steps for RL training rather than pure evaluation.
- Judge ensembles can improve robustness; rubric-free holistic judging may diverge from rubric-based RL gains.

## Related

- [[LLM Evaluation]]
- [[Papers Explained 170 - Prometheus]]
- [[Papers Explained 368 - ThinkPRM]]
- [[Evaluation and Benchmarks]]
