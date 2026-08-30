# Unsloth Model Support 2025

**Ingested**: 2026-07-22  
**Tags**: #summary #topic

## Summary

2025 expanded Unsloth into reasoning models, Chinese open weights, and deployment-scale architectures: **DeepSeek R1/V3**, **Phi-4**, **QwQ-32B**, **Gemma 3/3n**, **Llama 4**, **Qwen3**, **GPT-OSS**, and **Qwen3-Coder**. Launches emphasized **GRPO/RL fine-tuning**, **dynamic quantization**, **MoE** paths, and **MatFormer** (Gemma 3n) elastic inference. Each release typically shipped within hours of upstream weights.

## Key Claims

| Model / topic | Unsloth contribution |
|---------------|---------------------|
| DeepSeek R1 | Day-zero GRPO; 1.58-bit dynamic quant (see [[Unsloth Dynamic Quantization]]) | deepseek-r1, deepseekr1-dynamic |
| DeepSeek R1-0528 | Updated reasoning weights + RL recipes | deepseek-r1-0528 |
| DeepSeek V3-0324 / V3.1 | MoE QLoRA; FP8 paths | deepseek-v3-0324, deepseek-v3.1 |
| Phi-4 | 14B reasoning; 2× faster SFT | phi4 |
| QwQ-32B | Long-context reasoning QLoRA | qwq-32b |
| Gemma 3 | Multimodal + text; bug fixes | gemma3 |
| Gemma 3n | MatFormer elastic layers; mobile-first | gemma-3n |
| Llama 4 | Scout/Maverick QLoRA; vision variants | llama4 |
| Qwen3 | Dense + MoE; thinking mode | qwen3 |
| Qwen3-Coder | Local run + fine-tune guide | qwen3-coder |
| GPT-OSS | 20B/120B; MXFP4; RL + long context | gpt-oss |
| Dynamic 2.0 | GGUF dynamic quant v2 | dynamic-v2 |

- **GRPO** became the default RL path for reasoning models (cross-ref [[GRPO]], [[Unsloth Reinforcement Learning]]).
- **Llama 4** support cross-links [[Llama 4 Release]] without overwriting that page.

## Figures

| Figure | Caption |
|--------|---------|
| — | MatFormer diagram referenced in [[Unsloth Model Support 2025]] assets (gemma-3n) |

## Entities

- [[DeepSeek]] — R1, V3, MoE reasoning stack.
- [[Qwen]] — Qwen3, QwQ, Qwen3-Coder.
- [[Meta]] — Llama 4.
- [[Google Research]] — Gemma 3, Gemma 3n.
- [[Microsoft]] — Phi-4.
- [[OpenAI]] — GPT-OSS open weights.
- [[Unsloth]] — kernels + notebooks.

## Questions & Gaps

- GPT-OSS reward-hacking mitigations still evolving (see gpt-oss-rl page).
- MatFormer training vs inference size tradeoffs need broader benchmarks.

## Related

- [[Unsloth Model Support 2024]]
- [[Unsloth Model Support 2026]]
- [[Unsloth Reinforcement Learning]]
- [[Unsloth Dynamic Quantization]]
- [[Mixture of Experts]]
- [[Llama 4 Release]]
- [[Gemma 3n]]

## Sources

- `raw/deepseek-r1/full-article.md`
- `raw/phi4/full-article.md`
- `raw/qwq-32b/full-article.md`
- `raw/gemma3/full-article.md`
- `raw/deepseek-v3-0324/full-article.md`
- `raw/llama4/full-article.md`
- `raw/qwen3/full-article.md`
- `raw/deepseek-r1-0528/full-article.md`
- `raw/gemma-3n/full-article.md`
- `raw/deepseek-v3.1/full-article.md`
- `raw/gpt-oss/full-article.md`
- `raw/qwen3-coder/full-article.md`
