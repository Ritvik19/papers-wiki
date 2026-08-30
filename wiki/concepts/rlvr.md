# Reinforcement Learning with Verifiable Rewards

**Type**: concept  
**Tags**: #concept

## Overview

Reinforcement Learning with Verifiable Rewards (RLVR) is a post-training stage that optimizes language models with rule-based or programmatic reward checkers—unit tests, math answer verification, instruction-constraint evaluators—rather than learned preference reward models. It is the third layer in Nathan Lambert's post-training taxonomy (after instruction tuning and preference fine-tuning / [[RLHF]]) and underpins modern reasoning-model training alongside [[GRPO]].

## Appearances

- [[Reinforcement Learning from Human Feedback]] — dedicated chapter on RLVR, reasoning models, and inference-time scaling; contrasts verifier rewards with preference-based RLHF.
- [[Papers Explained 283 - Tulu V3]] — open recipe introducing RLVR after SFT and DPO on GSM8K, MATH, and IFEval.
- [[Papers Explained: IFBench]] — IF-RLVR with deterministic instruction checkers as rewards.
- [[Controlling Reasoning Effort in LLMs]] — effort-conditioned RLVR with per-token length penalties; format reward $R_\text{total}=R_\text{accuracy}+R_\text{format}$ for think tokens.
- [[Unsloth Reinforcement Learning]] — GRPO/RLVR recipes for DeepSeek R1, GPT-OSS, and custom verifiable reward environments.
- [[Papers Explained: On-policy Distillation with Verifiable Reward]] — [[OPDVR]] uses binary verifiable reward correctness to ReLU-gate on-policy distillation log-probability ratios, and [[GRPD]] combines verifiable group advantages with token distillation.

## Notes

RLVR complements rather than replaces [[RLHF]]: preferences capture style and subjective quality; verifiers capture domains with checkable correctness. Combining both in one post-training stack is now common for frontier open models. Furthermore, verifiable reward outcomes can be combined with dense on-policy token distillation via [[OPDVR]] to accelerate convergence and surpass teacher capability.

## Related

- [[RLHF]]
- [[GRPO]]
- [[OPDVR]]
- [[GRPD]]
- [[On-Policy Distillation]]
- [[Verifier-Bounded Learning]]
- [[Verifiable Instruction Following]]
- [[Reasoning Models]]
- [[Controlling Reasoning Effort in LLMs]]
- [[Reasoning Effort]]
- [[Think Tokens]]
- [[Reinforcement Learning Topic]]
