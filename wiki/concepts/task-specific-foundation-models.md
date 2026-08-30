# Task-Specific Foundation Models

**Type**: concept  
**Tags**: #concept

## Overview

A **task-specific foundation model** is specialized for one generic NLP/vision task (sentiment, NER, structured extraction) while remaining **domain-agnostic** — users fine-tune or prompt for their schema. They are typically **small**, **privately deployable**, and can **outperform much larger general LLMs** on that task at lower cost. [[NuMind]]'s standard recipe: diverse corpus → **LLM synthetic labels** (imperfect OK) → **fine-tune compact base model**.

## Appearances

- [[A Foundation Model for Entity Recognition]] — RoBERTa-size NER encoder from LLM-labeled C4 concepts.
- [[NuExtract: A Foundation Model for Structured Extraction]] — explicit recipe definition; Phi-3 / Qwen decoders on Llama 3 labels.
- [[NuExtract 1.5 — Multilingual, Infinite context, still small, and better than GPT-4o!]] — 500× smaller than GPT-4o at similar English extraction quality.
- [[NuExtract 2.0: Outclassing Frontier LLMs in Information Extraction]] — VLM specialists beating GPT-4.1 on extraction benchmark.

## Notes

- Contrasts with frontier **generalist** LLMs where in-context learning **saturates** on extraction ([[Papers Explained 286 - NuNER]]).
- Related wiki pattern: [[Model Compression and Efficiency]] for deployment benefits.

## Related

- [[NuMind]] — primary practitioner in this wiki corpus.
- [[Synthetic Data]] — LLM annotation pipelines.
- [[Structured Extraction]] — flagship NuExtract task.
