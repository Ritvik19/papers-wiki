# NuExtract

**Type**: tool  
**Tags**: #entity

## Overview

**NuExtract** is [[NuMind]]'s open model family for **[[Structured Extraction]]** — mapping documents (text or images) plus a JSON **template/schema** to structured output. Later generations add **OCR/Markdown content extraction**, **vision**, **typed fields**, **in-context examples**, and **toggleable reasoning**. Hugging Face collections span 1.0 through 3.0; larger **PRO** models are API-only on [nuextract.ai](https://nuextract.ai/).

## Appearances

| Generation | Summary page | Highlights |
|------------|--------------|------------|
| NER backbone | [[A Foundation Model for Entity Recognition]] | BERT-size token encoder for NER (pre-NuExtract branding) |
| 1.0 | [[NuExtract: A Foundation Model for Structured Extraction]] | Phi-3 / Qwen decoders 0.5B–7B; text-only; empty JSON templates |
| 1.5 | [[NuExtract 1.5 — Multilingual, Infinite context, still small, and better than GPT-4o!]] | Phi-3.5; multilingual C4; continuation infinite context |
| 2.0 | [[NuExtract 2.0: Outclassing Frontier LLMs in Information Extraction]] | Qwen VL 2B–8B + PRO; vision, typed templates, ICL |
| 3.0 | [[NuExtract3: The Reasoning Open-Source OCR & Structured Extraction LLM]] | Qwen3.5-4B VLM; unified JSON + Markdown; SFT+RL reasoning |

## Notes

- Downloads: 1.x–2.x lines reported **several million** HF downloads by Jul 2025; NuExtract line **2M+**, NuMarkdown-Thinking **1.5M+** before v3 unification.
- Template evolution: `""` string leaves (1.0) → typed fields + `null` (2.0) → 20 ISO/RFC types + freeform instructions (3.0).

## Related

- [[NuMind]] — parent org.
- [[Structured Extraction]] — task definition.
- [[Papers Explained 287 - NuExtract]] — Medium explainer covering 1.0 through 3.0 lineage.
