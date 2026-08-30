# GSPO

**Type**: concept  
**Tags**: #concept

## Overview

Group Sequence Policy Optimization (GSPO) is a GRPO variant proposed in arXiv 2507.18071 (Zheng et al., 2025) and used to train Qwen 3 models (including Qwen3-235B-A22B). Its key innovation is computing the importance ratio at the **sequence level** rather than the **token level**.

In standard GRPO, each token in a completion has its own importance ratio (ratio of new to old policy probability for that token). These token-level ratios can vary wildly within a sequence, introducing high-variance gradient estimates and training instability — especially for MoE models where expert-selection volatility compounds this variance. GSPO instead computes one importance ratio per completion (the ratio of full-sequence log-probabilities), normalizes by sequence length T to avoid length sensitivity, and clips this single ratio. All tokens in the completion then share the same stable importance weight.

This aligns the optimization level (sequence) with the reward assignment level (also sequence-level outcome rewards), reducing gradient variance and providing more stable training for large MoE models. GSPO was shown to naturally resolve the MoE routing-replay issue that required a special workaround when training Qwen 3 with vanilla GRPO.

## Appearances

- [[GRPO++: Tricks for Making RL Actually Work]] — Covered in the "More Tweaks" section alongside GMPO and CISPO.
- [[Unsloth Reinforcement Learning]] — VLM-RL guide documents GSPO for vision-language GRPO training.

## Notes

- GSPO is used in production for Qwen 3, the most performant open-weight model family at time of writing.
- Offers better sample efficiency and overall performance vs. GRPO in ablations.
- Also naturally stabilizes MoE routing without routing-replay caching.

## Related

- [[GRPO]] — Base algorithm.
- [[GMPO]] — Alternative fix for the high-variance token-level importance ratio problem (geometric mean instead of sequence-level ratio).
- [[Mixture of Experts]] — GSPO particularly benefits MoE training stability.
