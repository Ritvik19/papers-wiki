# Introducing Mistral 3

**Source**: `raw/mistral-3/full-article.html` (225 KB), `raw/mistral-3/full-article.md` (markdown view)  
**URL**: https://mistral.ai/news/mistral-3/  
**Ingested**: 2026-06-06  
**Tags**: #summary

## Summary

Mistral AI launches **Mistral 3**, a multi-tier open model family under **Apache 2.0**. The release spans **Ministral 3** dense models (**3B, 8B, 14B**, each in base/instruct/reasoning variants with **image understanding**) and **Mistral Large 3**, a sparse MoE with **675B total / 41B active parameters**—Mistral's first MoE since Mixtral. Large 3 was trained from scratch on **3000 NVIDIA H200 GPUs** and debuts at **#2 among OSS non-reasoning models** on LMArena (#6 overall among OSS).

Large 3 targets parity with top instruction-tuned open models on general prompts, plus **image understanding** and **best-in-class multilingual** (non-English/Chinese) conversation. An **NVFP4 checkpoint** (via llm-compressor) enables efficient serving on **Blackwell NVL72** or a single **8×A100/H100** node with vLLM. NVIDIA collaboration covers TensorRT-LLM, SGLang, speculative decoding, and edge deployment (DGX Spark, RTX, Jetson).

Ministral 3 offers edge/local deployment with multimodal and **40+ native languages**; instruct variants match or exceed comparably sized models while producing **~10× fewer tokens** in real use. Reasoning variants reach **85% on AIME '25** (14B). Availability spans Mistral AI Studio, Amazon Bedrock, Azure Foundry, Hugging Face, Modal, IBM WatsonX, OpenRouter, Fireworks, Unsloth AI, Together AI; NVIDIA NIM and AWS SageMaker coming soon.

Ministral 3 architecture and training (Cascade Distillation) are detailed in [[Papers Explained 526 - Ministral 3]].

## Key Claims

- Mistral 3 family: Ministral 3 (3B/8B/14B dense, base/instruct/reasoning, multimodal) + Mistral Large 3 (675B total, 41B active MoE); all Apache 2.0.
- Mistral Large 3: #2 OSS non-reasoning on LMArena; trained on 3000 H200 GPUs; base + instruct released; reasoning version coming.
- NVFP4 Large 3 checkpoint runs on Blackwell NVL72 or 8×A100/H100 via vLLM; NVIDIA TensorRT-LLM/SGLang support across family.
- Ministral 3: best cost-to-performance among OSS; instruct models often 10× fewer output tokens; 14B reasoning hits 85% AIME '25.
- Multimodal (text + image) and 40+ native languages across the family.
- Wide platform availability day-of-release across cloud and open inference stacks.

## Figures

No article-body figures found in the fetched HTML. LMArena ranking and benchmark visuals referenced in prose are not embedded as `<img>` tags in the static page.

## Entities

- [[Large Language Models]] — multi-tier open model family from edge to frontier MoE.
- [[Mixture of Experts]] — Mistral Large 3 sparse MoE (675B total, 41B active).
- [[Model Compression and Efficiency]] — Ministral 3 edge-optimized dense models and token efficiency.
- [[Vision Language Models]] — native image understanding in Ministral 3 and Large 3.
- [[Multilingual Models]] — 40+ native languages.

## Questions & Gaps

- Large 3 architecture details (expert count, routing) not fully specified in the blog; reasoning variant not yet released.
- Benchmark charts and LMArena screenshots absent from static HTML.
- Ministral 3 training recipe and ablations are in [[Papers Explained 526 - Ministral 3]], not the announcement post.

## Related

- [[Papers Explained 526 - Ministral 3]] — detailed explainer of Ministral 3 architecture, Cascade Distillation, and benchmarks.
- [[Mixture of Experts]] — Mistral Large 3 as return to MoE after Mixtral series.
- [[Model Compression and Efficiency]] — edge deployment and token-efficiency claims.
- [[Vision Language Models]] — multimodal capabilities across Ministral 3 and Large 3.
- [[Mixtral of experts]] — prior Mistral MoE release (Mixtral 8x7B).
