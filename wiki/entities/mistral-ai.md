# Mistral AI

**Type**: org  
**Tags**: #entity

## Overview

French AI company (founded 2023; co-founders include Arthur Mensch, Timothée Lacroix, Guillaume Lample) building open-weight and commercial **Mistral**, **Mixtral**, **Ministral**, **Codestral**, **Devstral**, **Pixtral**, **Magistral**, **Voxtral**, and **Mistral OCR** model families. Known for efficient dense and sparse architectures (GQA, sliding-window attention, MoE), Apache 2.0 general-purpose releases, and enterprise API offerings on **la Plateforme** and cloud partners (Azure, GCP Vertex, AWS Bedrock, IBM watsonx).

## Appearances

### Foundation & general-purpose LLMs (official blog summaries)

- [[Mistral 7B]] — 7.3B Apache 2.0 model with GQA and sliding-window attention; outperforms Llama 2 13B.
- [[Au Large (Mistral Large)]] — Feb 2024 flagship; 32K context, multilingual, function calling, Azure partnership.
- [[Large Enough (Mistral Large 2)]] — Mistral Large 2 (123B); 128K context, code/reasoning, MRL license.
- [[Mistral NeMo]] — 12B NVIDIA collaboration; 128K context, Tekken tokenizer, FP8 inference.
- [[Mistral Small 3]] — 24B Apache 2.0 latency-optimized model; rivals 70B-class models at 3× speed.
- [[Mistral Small 3.1]] — multimodal + 128K context upgrade to Small 3.
- [[Mistral Saba]] — 24B regional model for Arabic and South Asian languages.
- [[Medium is the new large.]] — Mistral Medium 3 enterprise model; SOTA at ~8× lower cost than Claude Sonnet 3.7.
- [[Introducing Mistral 3]] — Dec 2025 family: Ministral 3 (3B/8B/14B) + Mistral Large 3 (675B MoE, 41B active).
- [[Introducing Mistral Small 4]] — unified instruct/reasoning/multimodal MoE (119B total, 6B active).

### Mixture of Experts

- [[Mixtral of experts]] — Mixtral 8x7B SMoE; 46.7B total, 12.9B active; Apache 2.0.
- [[Cheaper, Better, Faster, Stronger]] — Mixtral 8x22B; 141B total, 39B active; 64K context.

### Edge / on-device

- [[Un Ministral, des Ministraux]] — Ministral 3B and 8B edge models; 128K context.

### Code models

- [[Codestral]] — first 22B code model; 80+ languages, 32K context, FIM.
- [[Codestral Mamba]] — 7.3B Mamba-based code model; Apache 2.0; linear-time inference.
- [[Codestral 25.01]] — faster Codestral with 256K context; SOTA FIM in weight class.
- [[Codestral Embed]] — code-specialized embedding model for RAG and semantic search.
- [[Announcing Codestral 25.08 and the Complete Mistral Coding Stack for Enterprise]] — enterprise coding stack: Codestral, Codestral Embed, Devstral, Mistral Code IDE.
- [[Devstral]] — agentic coding LLM; 46.8% SWE-Bench Verified; Apache 2.0.
- [[Upgrading agentic coding capabilities with the new Devstral models]] — Devstral Small 1.1 (53.6%) and Devstral Medium (61.6%) on SWE-Bench.
- [[Introducing: Devstral 2 and Mistral Vibe CLI.]] — Devstral 2 (123B, 72.2% SWE-Bench) + Vibe CLI agent.
- [[Leanstral: Open-Source foundation for trustworthy vibe-coding]] — Lean 4 proof assistant agent; sparse 120B-A6B.

### Reasoning & STEM

- [[Magistral]] — first Mistral reasoning model; Magistral Small (24B open) + Magistral Medium.
- [[MathΣtral]] — 7B STEM-specialized model from Mistral 7B; 56.6% MATH.

### Vision

- [[Announcing Pixtral 12B]] — 12B multimodal on Mistral NeMo; 400M vision encoder; Apache 2.0 (deprecated).
- [[Pixtral Large]] — 124B multimodal on Mistral Large 2; frontier VLM (deprecated).

### Document AI

- [[Mistral OCR]] — OCR API for documents, tables, equations; multilingual; RAG-ready output.
- [[Introducing Mistral OCR 3]] — upgraded OCR with handwriting, forms, HTML tables; Document AI Playground.

### Audio

- [[Voxtral]] — 24B and 3B speech understanding; transcription + Q&A + function calling.
- [[Voxtral transcribes at the speed of sound.]] — Voxtral Transcribe 2 + Realtime; diarization, timestamps.
- [[Speaking of Voxtral]] — Voxtral TTS; 9 languages; low-latency streaming synthesis.

### Papers Explained (Medium wiki coverage)

- [[Papers Explained - Mistral 7B]] — Mistral 7B architecture and benchmarks.
- [[Papers Explained 95 - Mixtral 8x7B]] — Mixtral 8x7B MoE technical survey.
- [[Papers Explained 219 - Pixtral]] — Pixtral 12B multimodal architecture.
- [[Papers Explained 388 - Magistral]] — Magistral reasoning model training (GRPO).
- [[Papers Explained 434 - Voxtral]] — Voxtral speech understanding.
- [[Papers Explained 526 - Ministral 3]] — Ministral 3 edge model family.
- [[Unsloth Model Support 2024]] — Mistral 7B benchmark (30× claim) and Mistral NeMo 128K QLoRA.

## Notes

- Product blog: https://mistral.ai/news  
- Mistral renews Apache 2.0 commitment for general-purpose open models (Jan 2025); commercial/MRL licenses for Large 2 and some specialist models.  
- Pixtral 12B and Pixtral Large are deprecated in favor of newer vision models (per Mistral blog notices).

## Related

- [[Large Language Models]] — Mistral, Mixtral, Ministral generative models.
- [[Mixture of Experts]] — Mixtral and Mistral Large 3 sparse MoE architectures.
- [[Code Models]] — Codestral and Devstral coding/agentic lines.
- [[Reasoning Models]] — Magistral and Mathstral.
- [[Vision Language Models]] — Pixtral multimodal models.
- [[Document AI]] — Mistral OCR document understanding.
- [[Audio Models]] — Voxtral STT and TTS.
- [[Multilingual Models]] — NeMo, Saba, and multilingual Mixtral/Mistral Large coverage.
- [[Model Compression and Efficiency]] — GQA, SWA, edge Ministral models.
- [[Embedding and Retrieval]] — Codestral Embed for code RAG.
- [[Agentic AI]] — Devstral, Vibe CLI, and function-calling APIs.
