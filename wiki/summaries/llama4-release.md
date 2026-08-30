# Welcome Llama 4 Maverick & Scout on Hugging Face

**Source**: `raw/llama4-release/full-article.md` (204 KB), `raw/llama4-release/full-article.md`
**Ingested**: 2026-07-10
**Tags**: #summary

## Summary

Hugging Face's launch post for Meta's Llama 4 family: Llama 4 Maverick (~400B total, 128 experts) and Llama 4 Scout (~109B total, 16 experts), both Mixture-of-Experts models with 17B active parameters and both natively multimodal via early fusion of text and image inputs. Both were trained on up to 40 trillion tokens across 200 languages, with dedicated fine-tuning support for 12 languages. The models shipped with day-one integration into `transformers` (v4.51.0+, tensor-parallel and automatic device mapping) and Text Generation Inference, plus Xet storage backend achieving ~25% deduplication on base checkpoints and ~40% on community derivatives.

The post's main technical contribution is documenting the architecture choices behind Llama 4's unusually long context windows: 1M tokens for Maverick, 10M for Scout on the instruct variants (both pretrained at 256K). Meta calls the combination `iRoPE`: NoPE (No RoPE) layers appear every 4 layers and use a full causal mask with no positional encoding, interleaved with 3 RoPE layers that use chunked attention (8192-token chunks) to bound memory, a more compute-efficient relative of sliding window attention. Attention temperature tuning (a scaled softmax) is applied in the NoPE layers to counteract softmax score decay at long sequence lengths and is called out as a likely key factor behind Scout's 10M context. Scout additionally applies QK normalization (parameter-free RMSNorm on Q/K states after RoPE) in its RoPE layers. Maverick alternates MoE and dense layers (experts active in half the layers) and was co-distilled from a larger internal model, "Llama Behemoth," via a loss that dynamically weights student/teacher logits. Both models use MetaP, a MuP-inspired hyperparameter-tuning methodology across training budget and model size.

- Instruct-model benchmarks: Maverick reaches 80.5% MMLU-Pro and 69.8% GPQA Diamond (0-shot); Scout reaches 74.3% and 57.2% respectively, both ahead of Llama 3.1 405B (73.4% / 49.0%) despite Scout's much smaller active/total parameter count.
- LiveCodeBench (10/2024-02/2025, 0-shot, pass@1): Maverick 43.4 vs. Llama 3.1 405B's 27.7; Scout 32.8.
- Multimodal (0-shot): Maverick 73.4% MMMU / 90.0% ChartQA / 94.4% DocVQA; Scout 69.4% MMMU / 88.8% ChartQA. Llama 3.1 405B has no multimodal support for comparison.
- Long-context MTOB (full book, English->Kalamang chrF): Maverick 50.8, Scout 39.7, on a low-resource machine-translation task used as a long-context stress test (128K context in Llama 3.1 vs. up to 10M in Scout).
- Deployment: Scout fits on a single server-grade GPU via on-the-fly 4-bit/8-bit quantization; Maverick ships in BF16 and FP8.
- Released under the custom Llama 4 Community License Agreement, gated behind license acceptance on the Hub.

Pretrained-model benchmarks (0-5 shot, vs. Llama 3.1):

| Category | Benchmark | Llama 3.1 70B | Llama 3.1 405B | Llama 4 Scout | Llama 4 Maverick |
|---|---|---|---|---|---|
| Reasoning & Knowledge | MMLU (5-shot) | 79.3 | 85.2 | 79.6 | 85.5 |
| Reasoning & Knowledge | MMLU-Pro (5-shot) | 53.8 | 61.6 | 58.2 | 62.9 |
| Reasoning & Knowledge | MATH (4-shot) | 41.6 | 53.5 | 50.3 | 61.2 |
| Code | MBPP (3-shot, pass@1) | 66.4 | 74.4 | 67.8 | 77.6 |
| Image | ChartQA (0-shot) | no multimodal support | no multimodal support | 83.4 | 85.3 |

Instruct-model benchmarks (0-shot, vs. Llama 3.1/3.3):

| Category | Benchmark | Llama 3.1/3.3 70B | Llama 3.1 405B | Llama 4 Scout | Llama 4 Maverick |
|---|---|---|---|---|---|
| Reasoning & Knowledge | MMLU-Pro | 68.9 | 73.4 | 74.3 | 80.5 |
| Reasoning & Knowledge | GPQA Diamond | 50.5 | 49.0 | 57.2 | 69.8 |
| Coding | LiveCodeBench (10/2024-02/2025, pass@1) | 33.3 | 27.7 | 32.8 | 43.4 |
| Image Reasoning | MMMU | no multimodal support | no multimodal support | 69.4 | 73.4 |
| Image Reasoning | MathVista | no multimodal support | no multimodal support | 70.7 | 73.7 |
| Image Understanding | DocVQA (test, ANLS) | no multimodal support | no multimodal support | 94.4 | 94.4 |
| Long context | MTOB full book, eng->Kalamang (chrF) | 128K context window | - | 39.7 | 50.8 |

## Figures

No figures were extracted for this ingest; the ASCII chunked-attention diagram is preserved inline in the source markdown, and the pre-trained/instruct benchmark tables are kept as markdown above, per this batch's no-figure-download policy.

## Entities

- [[Meta]] — developer of Llama 4.
- [[Hugging Face]] — hosts the blog, model weights, and `transformers`/TGI integration.

## Questions & Gaps

- The post repeatedly notes "until an official technical report is published, this is what we know so far": several architecture claims (NoPE cadence, co-distillation loss, MetaP details) are Hugging Face's inference from the released code/config rather than a confirmed Meta specification.
- No mention of Llama 4 Behemoth's own parameter count or release status beyond its role as Maverick's distillation teacher.
- Community comments on the original post flag `transformers` compatibility errors (unrecognized image processor) shortly after release, suggesting the initial integration had rough edges.

## Related

- [[Papers Explained 187a - Llama 3]] and [[Papers Explained 187b - Llama 3.1]] — direct predecessors; Llama 4 benchmark tables use Llama 3.1 70B/405B as the baseline throughout.
- [[Positional Encoding]] — NoPE and iRoPE are direct extensions of positional-encoding design space.
- [[Mixture of Experts]] — Maverick/Scout's MoE routing and alternating dense/MoE layer pattern.
- [[Meta]]
- [[Large Language Models]]
- [[Vision Language Models]]
- [[Long Context]]
