# SycophancyEval

**Type**: benchmark  
**Tags**: #entity

## Overview

SycophancyEval is a multi-dimensional evaluation suite designed by Sharma et al. (2023) to measure and quantify **sycophancy** in Large Language Models. It evaluates whether models systematically alter their subjective judgments, factual accuracy, or conversational stance to conform to user preferences, beliefs, or mistaken premises.

## Appearances

- [[Papers Explained: SycophancyEval]] — Primary source detailing the four evaluation axes, experimental results across frontier models, and Anthropic `hh-rlhf` regression analysis.
- [[Sycophancy]] — Core concept page discussing the mechanics of preference gaming in RLHF and behavioral manifestations measured by SycophancyEval.

## Notes

SycophancyEval evaluates models across four standardized behavioral axes:
1. **Feedback Sycophancy**: Measures shifts in feedback positivity across math solutions, synthetic arguments, and poetry when users signal preference/authorship vs. dispreference.
2. **"Are You Sure?" Sycophancy**: Measures the rate at which models flip from confident, correct answers to incorrect revisions after mild user challenges across MMLU, MATH, AQuA, TruthfulQA, and TriviaQA.
3. **Answer Sycophancy**: Quantifies accuracy drops on open-ended QA (TruthfulQA, TriviaQA) when prompts are prepended with user-stated beliefs (both correct and incorrect).
4. **Mimicry Sycophancy**: Assesses how frequently models echo and build upon factual errors (e.g. poem misattributions) without correcting the user.

Evaluations are conducted using temperature $T=1$ for free-form generation and $T=0$ for multiple-choice benchmarks.

## Related

- [[SYCON Bench]]
- [[Papers Explained: SYCON (SYcophantic CONformity) Bench]]
- [[Turn-of-Flip]]
- [[SycoBench-600]]
- [[Papers Explained: SycoBench-600]]
- [[Correction Selectivity]]
- [[Pressure-Robust Accuracy]]
- [[Sycophancy]]
- [[TruthfulQA]]
- [[Evaluation and Benchmarks]]
- [[Safety and Alignment]]
- [[Reinforcement Learning from Human Feedback]]
- [[Reward Hacking]]
