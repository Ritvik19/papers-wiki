# Dr. GRPO

**Type**: concept  
**Tags**: #concept

## Overview

Dr. GRPO ("GRPO Done Right") is a de-biased variant of GRPO proposed in "Understanding r1-zero-like training: A critical perspective" (arXiv 2503.20783, Liu et al., 2025). It targets two specific biases in the vanilla GRPO objective not fully addressed by DAPO:

1. **Response-level length bias**: GRPO normalizes each sequence's summed loss by the number of tokens in that sequence. This makes shorter sequences receive larger gradient updates for positive advantages and makes longer incorrect responses receive smaller negative updates — effectively biasing the policy toward using more tokens for wrong answers. Dr. GRPO normalizes by a fixed constant (MAX_TOKENS) instead.

2. **Question-level difficulty bias**: The standard deviation term in GRPO's advantage denominator causes advantage magnitudes to explode when a prompt is either very easy (all completions correct → near-zero std) or very hard (all completions wrong → near-zero std). Dr. GRPO removes the std term entirely, computing advantage as a simple mean-subtraction.

When trained on the MATH dataset using Qwen-2.5-Math-7B, Dr. GRPO achieves 43.3% on AIME 2024 — state-of-the-art for that model scale at time of publication — completing training in ~27 hours on 8 A100 GPUs.

## Appearances

- [[GRPO++: Tricks for Making RL Actually Work]] — Section 2; both modifications and their motivation are detailed here.

## Notes

- The paper also reveals that Qwen-2.5 base models behave like SFT-trained models (they were pretrained on concatenated Q-A data), which inflates apparent RL-Zero gains.
- The "Aha moment" (self-reflection) was found to be partially pre-existing in DeepSeek-V3-Base and is not purely emergent from RL.
- Code: [https://github.com/sail-sg/understand-r1-zero](https://github.com/sail-sg/understand-r1-zero).

## Related

- [[GRPO]] — Base algorithm.
- [[DAPO]] — Parallel work; token-level loss in DAPO partially addresses the same length bias.
- [[Reasoning Models]] — Context for why RL-Zero training is studied.
