# Post-Training

**Type**: concept  
**Tags**: #concept

## Overview

Post-training is the multi-stage process applied after base pretraining to make language models useful for downstream interaction: instruction formatting, preference alignment, verifier-driven RL, tool use, and product-specific character. Nathan Lambert frames it as three optimization layers—instruction / [[Supervised Fine-Tuning]], preference fine-tuning ([[RLHF]] and direct-alignment algorithms), and [[Reinforcement Learning with Verifiable Rewards]].

## Appearances

- [[Reinforcement Learning from Human Feedback]] — primary definitional source in this wiki; walks through InstructGPT, Tülu 3, and DeepSeek R1 as canonical recipes.
- [[Papers Explained 283 - Tulu V3]] — open post-training stack with SFT, DPO, and RLVR.
- [[Papers Explained 60 - Llama 2]] — industrial multi-iteration RLHF post-training.

## Notes

"RLHF" colloquially once meant most of post-training after ChatGPT; the field now splits preference optimization, verifier RL, rejection sampling, synthetic distillation, and evaluation-heavy iteration.

## Related

- [[RLHF]]
- [[Supervised Fine-Tuning]]
- [[Reinforcement Learning with Verifiable Rewards]]
- [[Model Distillation]]
- [[Safety and Alignment]]
- [[Large Language Models]]
