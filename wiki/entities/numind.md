# NuMind

**Type**: org  
**Tags**: #entity

## Overview

**NuMind** (also branded **NuExtract**) is a French AI company building **task-specific foundation models** for information extraction — entity recognition, structured JSON extraction, and document OCR. They open-source many models under **MIT** or **Apache 2.0** and operate the [nuextract.ai](https://nuextract.ai/) extraction platform with API access to larger **PRO** checkpoints.

## Appearances

- [[A Foundation Model for Entity Recognition]] — Nov 2023 BERT-size NER foundation model; MIT English + multilingual weights.
- [[NuExtract: A Foundation Model for Structured Extraction]] — Jun 2024 NuExtract 1.0 text-to-JSON family (0.5B–7B).
- [[NuExtract 1.5 — Multilingual, Infinite context, still small, and better than GPT-4o!]] — Oct 2024 multilingual + continuation long-context extraction.
- [[NuExtract 2.0: Outclassing Frontier LLMs in Information Extraction]] — Jul 2025 VLM extraction + PRO API platform.
- [[NuExtract3: The Reasoning Open-Source OCR & Structured Extraction LLM]] — May 2026 unified JSON + Markdown 4B VLM with RL reasoning.
- [[Papers Explained 286 - NuNER]] / [[Papers Explained 287 - NuExtract]] — independent Medium summaries.

## Notes

- Shared recipe across products: **diverse corpus (C4, Fine-PDF) + LLM synthetic labels + compact specialized fine-tune** (often SFT, increasingly RL for reasoning).
- Etienne Bernard (Co-Founder & CEO) authors most launch posts.

## Related

- [[NuExtract]] — flagship model family entity.
- [[Structured Extraction]] — core task.
- [[Document AI]] — primary application domain.
