# IBM

**Type**: org
**Tags**: #entity

## Overview

IBM Research builds the **Granite** family of open-weight language and embedding models, released under Apache 2.0 with an emphasis on enterprise governance (curated/filtered training data, no MS-MARCO, licensing review). The Granite Embedding line targets efficient multilingual and English retrieval; the main Granite line covers dense and MoE language models.

## Appearances

- [[Granite Embedding Multilingual R2]] — 97M and 311M ModernBERT-based multilingual embedding models with 32K context.
- [[Granite 4.0 3B Vision: Compact Multimodal Intelligence for Enterprise Documents]] — LoRA-adapter VLM for table, chart, and key-value-pair extraction from enterprise documents.
- [[Granite 4.1 LLMs: How They're Built]] — dense 3B/8B/30B family, five-phase pretraining with long-context extension to 512K, LLM-as-Judge SFT curation, four-stage GRPO+DAPO RL pipeline; 8B dense matches the 32B-A9B MoE predecessor.
- [[Granite 4.0 Nano: Just How Small Can You Go?]] — sub-1B/1B edge models in both hybrid-SSM and traditional transformer variants, targeting on-device and llama.cpp deployment.

## Notes

Granite Embedding R2 models are distilled from Granite 3.3/4.1 Instruct and Mistral v0.2 Instruct decoder teachers, then contrastively fine-tuned and merged, a training recipe pattern IBM reuses across the Granite Embedding family.

## Related

- [[Embedding and Retrieval]]
- [[Mixture of Experts]]
