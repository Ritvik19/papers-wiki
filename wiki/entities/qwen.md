# Qwen

**Type**: org  
**Tags**: #entity

## Overview

Qwen (Tongyi Qianwen) is a series of large language models developed by Alibaba Cloud. The family includes dense models, Mixture-of-Experts (MoE) models, and multimodal models across various parameter scales. The Qwen models (specifically the Qwen 2.5 and Qwen 3 generations) are widely recognized as state-of-the-art open-weights models for mathematical reasoning, code generation, and multilingual understanding.

## Appearances

- [[LoRA Without Regret]] — sweep of Qwen3 models (including MoE variants) is used in the rank and LR sweep experiments.
- [[GRPO++: Tricks for Making RL Actually Work]] — Qwen 3 was trained using the GSPO variant of GRPO.
- [[Introducing Composer 2.5]] — Kimi K2.5 and Qwen 3 are compared during base model evaluation for Cursor's coding agent.
- [[The Future of the Global Open-Source AI Ecosystem: From DeepSeek to AI+]] — profiled as the largest derivative-model ecosystem on Hugging Face (113,000+ derivatives, 200,000+ Qwen-tagged repos by mid-2025), fourth most-followed org on the Hub.
- [[State of Open Source on Hugging Face: Spring 2026]] — Alibaba/Qwen's derivative-model count exceeds Google's and Meta's combined; `Qwen2.5-32B-Instruct-AWQ`/`Qwen2.5-14B-Instruct` used as the translation models for NVIDIA's multilingual reasoning dataset.
- [[NVIDIA Releases 6 Million Multi-Lingual Reasoning Dataset]] — `Qwen2.5-32B-Instruct-AWQ` (German) and `Qwen2.5-14B-Instruct` (French/Spanish/Italian/Japanese) used to translate the Nemotron Post-Training Dataset v2.
- [[Papers Explained 587: OpenThoughts Agent]] — Qwen3-8B is used as the base model for 100+ pipeline ablations; Qwen3-32B is fine-tuned to produce OpenThinker-Agent-v1 (44.8% average on 7 agent benchmarks).

## Notes

- Qwen MoE architectures utilize fine-grained routing with shared and active experts to scale parameter count efficiently.
- Qwen models serve as extremely popular base checkpoints for post-training reinforcement learning due to their high knowledge capacity and robust base capabilities.
- [[Unsloth Model Support 2025]] — Qwen3, QwQ-32B, Qwen3-Coder day-zero support.
- [[Unsloth Model Support 2026]] — Qwen3.5 and Qwen3.6 fine-tuning docs.

## Related

- [[LoRA Without Regret]]
- [[GRPO]]
- [[GRPO++: Tricks for Making RL Actually Work]]
- [[Large Language Models]]
- [[Mixture of Experts]]
- [[Reasoning Models]]
