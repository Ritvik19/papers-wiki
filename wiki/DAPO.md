# DAPO

**Type**: concept  
**Tags**: #concept

## Overview

Decoupled Clip and Dynamic Sampling Policy Optimization (DAPO) is an improved version of GRPO proposed by ByteDance and Tsinghua in "DAPO: An Open-Source LLM Reinforcement Learning System at Scale" (arXiv 2503.14476). It identifies four key modifications to vanilla GRPO that together achieve AIME 2024 accuracy of 50% with Qwen-2.5-32B, surpassing DeepSeek-R1-Zero (47%) with only half the training steps.

The four DAPO modifications are:
1. **Clip higher**: Decouple the upper and lower clipping bounds. Set ε_low = 0.2 (standard) and ε_high = 0.28 (increased). This prevents entropy collapse by allowing exploration tokens to increase in probability more freely.
2. **Dynamic sampling**: Over-sample prompts and filter out any prompt for which all group completions receive the same reward (zero-gradient batch elements). This maintains effective batch size despite filtering and improves sample efficiency.
3. **Token-level loss**: Aggregate the GRPO loss as a mean over all tokens in the batch, rather than averaging per-sequence then averaging across sequences. Eliminates the length bias where shorter sequences receive disproportionately large gradient updates.
4. **Overlong reward shaping**: Instead of assigning a hard -1 penalty to truncated completions, mask them (zero contribution) or apply a soft length-aware penalty that ramps from 0 to -1 over a "cache interval" of 4K tokens before the maximum 16K token limit.

## Appearances

- [[GRPO++: Tricks for Making RL Actually Work]] — Primary source; DAPO is the first and most extensively covered improvement.

## Notes

- All code (via [verl](https://github.com/volcengine/verl)) and data ([DAPO-Math-17K](https://huggingface.co/datasets/BytedTsinghua-SIA/DAPO-Math-17k)) are openly released.
- Dynamic sampling is also called "zero-gradient filtering" or "active sampling" in OLMo 3.
- The clip-higher idea inspired CISPO's analysis of why pivotal fork tokens get clipped.

## Related

- [[GRPO]] — Base algorithm that DAPO modifies.
- [[Dr. GRPO]] — Parallel work identifying further biases in the GRPO objective.
- [[OLMo 3]] — Adopts several DAPO improvements including dynamic sampling, token-level loss, and clip higher.
