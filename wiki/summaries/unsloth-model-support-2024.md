# Unsloth Model Support 2024

**Ingested**: 2026-07-22  
**Tags**: #summary #topic

## Summary

2024 was Unsloth's model-launch year: from **Mistral 7B** speed benchmarks through **Gemma**, **Llama 3/3.1/3.3**, **Phi-3**, **Gemma 2**, **Mistral NeMo**, and **Llama 3.2 Vision**. Each launch paired day-zero QLoRA support with custom kernels and often GGUF export. The [[Hugging Face]] collaboration (unsloth-trl) brought Unsloth into the official TRL docs; TinyLlama GGUF work established the project's quantization/export story.

## Key Claims

| Model | Speed / VRAM highlights | Context |
|-------|-------------------------|---------|
| Mistral 7B | Up to **30×** faster vs HF; 4-bit QLoRA | mistral-benchmark |
| Gemma 2B/7B | Day-zero support; fixed upstream bugs | gemma |
| Llama 3 8B/70B | 2× faster; 60% less memory | llama3 |
| Phi-3 mini/medium | 2× faster training | phi3 |
| Gemma 2 9B/27B | 1.9× faster; 50% less VRAM | gemma2 |
| Mistral NeMo 12B | 128K context; 2× faster | mistral-nemo |
| Llama 3.1 8B/70B/405B | 405B on 2×24GB via 4-bit | llama3-1 |
| Llama 3.2 Vision 11B/90B | Multimodal QLoRA | vision |
| Llama 3.3 70B | Long-context + Cut Cross Entropy | llama3-3 |
| TinyLlama | GGUF Q4_K_M export path | tinyllama-gguf |

- **unsloth-trl**: official HF blog documenting TRL + Unsloth integration for SFT/DPO.
- Continued pretraining patterns introduced in contpretraining (cross-ref [[Continued Pretraining]]).

## Figures

| Figure | Caption |
|--------|---------|
| — | Per-model benchmark cards skipped; numbers in table above |

## Entities

- [[Mistral AI]] — Mistral 7B, NeMo.
- [[Meta]] — Llama 3 family, Llama 3.2 Vision, Llama 3.3.
- [[Google Research]] — Gemma, Gemma 2.
- [[Microsoft]] — Phi-3.
- [[Hugging Face]] — TRL integration.
- [[Unsloth]] — implementation layer.

## Questions & Gaps

- 405B multi-GPU recipes depend on specific cluster topology; consumer reproducibility unclear.
- Vision fine-tuning memory for 90B variant needs independent profiling.

## Related

- [[Unsloth Origins and Mission]]
- [[Unsloth Model Bug Fixes]]
- [[Unsloth Long Context Training]]
- [[Cut Cross Entropy]]
- [[Llama 3.3]]

## Sources

- `raw/mistral-benchmark/full-article.md`
- `raw/unsloth-trl/full-article.md`
- `raw/tinyllama-gguf/full-article.md`
- `raw/gemma/full-article.md`
- `raw/llama3/full-article.md`
- `raw/phi3/full-article.md`
- `raw/gemma2/full-article.md`
- `raw/mistral-nemo/full-article.md`
- `raw/llama3-1/full-article.md`
- `raw/vision/full-article.md`
- `raw/llama3-3/full-article.md`
