# Structured Extraction

**Type**: concept  
**Tags**: #concept

## Overview

**Structured extraction** is the information-extraction task of filling a **hierarchical template (schema)** — usually JSON — with values read from unstructured text or document images: entities, quantities, dates, relations, and nested lists. It generalizes NER and relation extraction to arbitrary tree depth and field names. NuMind's [[NuExtract]] family is a primary open implementation; [[NuMind]] describes it as "the holy grail of information extraction."

## Appearances

- [[NuExtract: A Foundation Model for Structured Extraction]] — defines task; empty-JSON template format; C4 + Llama 3 synthetic training.
- [[NuExtract 1.5 — Multilingual, Infinite context, still small, and better than GPT-4o!]] — multilingual templates; continuation for long docs.
- [[NuExtract 2.0: Outclassing Frontier LLMs in Information Extraction]] — typed templates (`verbatim-string`, enums, dates); vision inputs.
- [[NuExtract3: The Reasoning Open-Source OCR & Structured Extraction LLM]] — 20 field types; model instructions; unified with OCR pipeline.
- [[Papers Explained 287 - NuExtract]] — Medium pedagogical coverage.

## Notes

- **Precision over recall** is often preferred in production (empty/`null` better than wrong DB rows) — explicit in NuExtract 2.0 PRO design.
- Evaluation commonly uses **tree leaf matching** (NuMind EXTRA metric ≈ leaf accuracy).

## Related

- [[NuExtract]] — specialized model family.
- [[Document AI]] — invoices, claims, contracts, RAG preprocessing.
- [[Task-Specific Foundation Models]] — how NuExtract models are built.
