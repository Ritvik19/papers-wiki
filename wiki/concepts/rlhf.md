# RLHF

**Type**: concept  
**Tags**: #concept

## Overview

Reinforcement Learning from Human Feedback (RLHF) is a post-training method that aligns language models to human preferences by training a reward model on comparison data and optimizing the policy with RL (or related preference-optimization methods). It targets hard-to-specify objectives—tone, helpfulness, harmlessness, format—that are awkward to capture with demonstration-only [[Supervised Fine-Tuning]].

The canonical pipeline has three stages: instruction tuning, reward-model training on preference pairs, and policy optimization (PPO, [[GRPO]], rejection sampling, or [[Direct Preference Optimization]]-style alternatives).

## Appearances

- [[Reinforcement Learning from Human Feedback]] — comprehensive textbook treatment: history, algorithms, data, over-optimization, evaluation, RLVR, and product character training.
- [[Papers Explained 48 - InstructGPT]] — early canonical RLHF recipe for instruction-following chat models.
- [[Papers Explained 60 - Llama 2]] — iterative RLHF with rejection sampling and parallel reward-model refresh.
- [[Papers Explained 149 - RLHF Workflow]] — online iterative RLHF implementation focus.

## Notes

Modern post-training treats RLHF as one layer inside a larger stack that also includes [[Reinforcement Learning with Verifiable Rewards]] for math, code, and other checker-verified domains. Reward models are proxy objectives; [[KL Regularization]] and rejection sampling are common mitigations for over-optimization.

## Related

- [[Reinforcement Learning]]
- [[Reinforcement Learning with Verifiable Rewards]]
- [[Supervised Fine-Tuning]]
- [[KL Regularization]]
- [[Reward Hacking]]
- [[GRPO]]
- [[Direct Preference Optimization]]
- [[Reinforcement Learning Topic]]
