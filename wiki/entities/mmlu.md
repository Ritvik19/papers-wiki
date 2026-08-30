# MMLU

**Type**: tool  
**Tags**: #entity

## Overview

**Massive Multitask Language Understanding (MMLU)** is a widely cited multiple-choice benchmark with 57 subject areas (~16,000 questions total). Performance is reported as accuracy—the fraction of questions where the model selects the correct answer letter (A–D). Available on Hugging Face as `cais/mmlu`.

## Appearances

- [[Understanding the 4 Main Approaches to LLM Evaluation (From Scratch)]] — primary demo benchmark; letter-matching and log-probability scoring variants implemented on GitHub.

## Notes

- Measures knowledge recall in a standardized format; does not capture free-form writing or real-world utility.
- Scoring variants include direct letter generation, log-probability over choice tokens, and reasoning-model likelihood checks.
- High MMLU alone does not guarantee practical strength; low scores can indicate knowledge gaps.

## Related

- [[LLM Evaluation]]
- [[Evaluation and Benchmarks]]
- [[Large Language Models]]
