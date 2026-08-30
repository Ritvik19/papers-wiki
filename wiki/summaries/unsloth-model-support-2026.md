# Unsloth Model Support 2026

**Ingested**: 2026-07-22  
**Tags**: #summary #topic

## Summary

Early 2026 Unsloth coverage tracks frontier open models: **Qwen3.5**, **Qwen3.6**, **Gemma 4** (run + train + QAT), **DiffusionGemma**, **DeepSeek V4**, and **GLM-5.2**. Docs emphasize local inference (GGUF, vLLM, Ollama), QLoRA/SFT recipes, multimodal paths, and cross-links to existing wiki pages for the same models from non-Unsloth sources.

## Key Claims

| Model | Unsloth focus | Wiki cross-link |
|-------|---------------|-----------------|
| Qwen3.5 | Day-zero QLoRA; thinking/non-thinking modes | — |
| Qwen3.6 | Updated arch; long context; MoE variants | — |
| Gemma 4 | Run locally; train guide; QAT path | [[Gemma 4]], [[Gemma 4 QAT]] |
| DiffusionGemma | Image diffusion + text; fine-tune notebooks | [[Diffusion Gemma]] |
| DeepSeek V4 | MoE; FP8; RL-ready | [[DeepSeek V4]] |
| GLM-5.2 | Zhipu flagship; efficient kernels | [[GLM-5.2 Blog]] |

- **Gemma 4 train** doc covers multi-stage SFT, vision/audio towers, and memory tips (gemma-4-train).
- Unsloth-specific pages **do not overwrite** [[Gemma 4]], [[DeepSeek V4]], or [[GLM-5.2 Blog]]—they add training/deployment lens.
- QAT for Gemma 4 documented separately under [[Unsloth Quantization-Aware Training]].

## Figures

| Figure | Caption |
|--------|---------|
| — | Model cards; VRAM tables in source docs |

## Entities

- [[Qwen]] — Qwen3.5, Qwen3.6.
- [[Google Research]] — Gemma 4, DiffusionGemma.
- [[DeepSeek]] — DeepSeek V4.
- [[Zhipu AI]] — GLM-5.2.
- [[Unsloth]] — training stack.

## Questions & Gaps

- Qwen3.6 vs 3.5 migration guide for existing fine-tunes.
- DiffusionGemma RL / preference tuning not yet documented by Unsloth.

## Related

- [[Unsloth Model Support 2025]]
- [[Unsloth Quantization-Aware Training]]
- [[Gemma 4]]
- [[DeepSeek V4]]
- [[Diffusion Gemma]]
- [[GLM-5.2 Blog]]

## Sources

- `raw/qwen3.5/full-article.md`
- `raw/qwen3.6/full-article.md`
- `raw/gemma-4/full-article.md`
- `raw/gemma-4-train/full-article.md`
- `raw/diffusiongemma/full-article.html`
- `raw/deepseek-v4/full-article.md`
- `raw/glm-5.2/full-article.md`
