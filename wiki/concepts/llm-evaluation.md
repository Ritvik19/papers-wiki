# LLM Evaluation

**Type**: concept  
**Tags**: #concept

## Overview

The practice of measuring language-model capability, quality, and fitness for deployment. [[Understanding the 4 Main Approaches to LLM Evaluation (From Scratch)]] identifies four dominant public methods—multiple-choice benchmarks, verifiers, preference leaderboards, and [[LLM-as-a-Judge]]—grouped into benchmark-based and judgment-based evaluation. Internal metrics (loss, perplexity, reward) are typically used during training rather than reported externally.

## Appearances

- [[Understanding the 4 Main Approaches to LLM Evaluation (From Scratch)]] — practitioner taxonomy with from-scratch code for MMLU letter matching, Elo leaderboards, and Ollama-based judging.

## Notes

- No single evaluation method is sufficient; Raschka recommends combining multiple signal types and domain-specific proprietary test sets.
- Multiple choice ([[MMLU]]) measures knowledge recall; verifiers handle free-form answers in math/code; leaderboards ([[LM Arena]]) capture human preference; judges scale rubric grading.
- Complements corpus coverage in [[Evaluation and Benchmarks]] including RewardBench, Prometheus, IFBench, and harness-specific evals.

## Related

- [[Evaluation and Benchmarks]]
- [[MMLU]]
- [[LM Arena]]
- [[LLM-as-a-Judge]]
- [[Sebastian Raschka]]
