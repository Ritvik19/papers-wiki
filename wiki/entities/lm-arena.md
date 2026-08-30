# LM Arena

**Type**: tool  
**Tags**: #entity

## Overview

**LM Arena** (formerly **Chatbot Arena**) is a human preference leaderboard where users compare side-by-side responses from two models on the same prompt and vote for the preferred answer. Aggregated votes produce model rankings. As of 2025, LM Arena uses a **Bradley–Terry** statistical model (replacing raw Elo) for joint rating estimation with confidence intervals, though "Elo" remains common parlance.

## Appearances

- [[Understanding the 4 Main Approaches to LLM Evaluation (From Scratch)]] — judgment-based evaluation example; includes from-scratch Elo implementation and Bradley–Terry comparison.

## Notes

- Captures style, helpfulness, and safety implicitly but not factual correctness.
- Vulnerable to demographic bias, prompt selection, voting bias, and gaming; expensive and slow for iterative model development.
- Preference votes can be outsourced to LLM judges, blurring the line with [[LLM-as-a-Judge]].

## Related

- [[LLM Evaluation]]
- [[Evaluation and Benchmarks]]
- [[LLM-as-a-Judge]]
