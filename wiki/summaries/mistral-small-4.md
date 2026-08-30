# Introducing Mistral Small 4

**Source**: `raw/mistral-small-4/full-article.html` (221 KB), `raw/mistral-small-4/full-article.md` (markdown view)  
**URL**: https://mistral.ai/news/mistral-small-4/  
**Ingested**: 2026-06-06  
**Tags**: #summary

## Summary

Mistral AI releases **Mistral Small 4**, unifying **instruct**, **reasoning** (Magistral), **multimodal** (Pixtral), and **agentic coding** (Devstral) into one **Apache 2.0** hybrid model. Architecture: **MoE with 128 experts, 4 active per token**; **119B total / 6B active parameters** (8B including embeddings/output); **256k context**; native text + image inputs. A new **`reasoning_effort`** parameter toggles fast chat (`"none"`, Mistral Small 3.2-style) vs. deep step-by-step reasoning (`"high"`, Magistral-style verbosity).

Efficiency claims: **40% lower end-to-end completion time** (latency-optimized) and **3× more requests/sec** (throughput-optimized) vs. Mistral Small 3. With reasoning enabled, Small 4 matches or beats **GPT-OSS 120B** on three benchmarks while producing **significantly shorter outputs** (e.g., 0.72 on AA LCR at 1.6K chars vs. Qwen models needing 3.5–4× more text). Minimum deploy: **4× H100**, **2× H200**, or **1× DGX B200**; recommended: doubled GPU counts.

Mistral joins the **NVIDIA Nemotron Coalition** as a founding member. Inference optimized for **vLLM**, **SGLang**, llama.cpp, and Transformers via NVIDIA collaboration. Available on Mistral API/AI Studio, Hugging Face, **build.nvidia.com** (free prototyping), and day-0 **NVIDIA NIM**; NeMo fine-tuning supported.

## Key Claims

- Single model unifies instruct, reasoning, multimodal, and agentic coding; Apache 2.0.
- MoE: 128 experts, 4 active/token; 119B total, 6B active (8B with embeddings); 256k context.
- `reasoning_effort` parameter: `"none"` for fast chat, `"high"` for deep reasoning.
- 40% faster completion vs. Small 3 (latency); 3× throughput (throughput-optimized setup).
- With reasoning: matches/surpasses GPT-OSS 120B on three benchmarks with much shorter outputs.
- Deployable from 4× H100 / 2× H200 / 1× DGX B200 minimum; NVIDIA NIM day-0 availability.

## Figures

No article-body figures found in the fetched HTML. A "Score vs. Output Length" chart is referenced in prose but not embedded as an `<img>` tag in the static page.

## Entities

- [[Mixture of Experts]] — 128-expert MoE with 4 active per token.
- [[Large Language Models]] — unified hybrid small model in the Mistral family.
- [[Reasoning Models]] — configurable reasoning effort (Magistral lineage).
- [[Vision Language Models]] — native text + image inputs (Pixtral lineage).
- [[Agentic AI]] — agentic coding workflows (Devstral lineage).
- [[Model Compression and Efficiency]] — active-parameter efficiency and output-length optimization.

## Questions & Gaps

- Benchmark chart (score vs. output length) not present in static HTML export.
- Full benchmark names for the "three benchmarks" partially abbreviated (AA LCR, LiveCodeBench); complete tables not in blog body.
- No dedicated wiki explainer page for Small 4 architecture ablations or training data mix.

## Related

- [[Introducing Mistral 3]] — prior Mistral generation release (Ministral 3 + Large 3).
- [[Papers Explained 526 - Ministral 3]] — related small-model family architecture and distillation.
- [[Mixture of Experts]] — MoE scaling in the Small tier.
- [[Reasoning Models]] — hybrid reasoning-on-demand design.
- [[Vision Language Models]] — multimodal text+image capabilities.
- [[Agentic AI]] — coding agents and Devstral integration.
