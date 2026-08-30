# Mixtral of experts

**Source**: `raw/mixtral-of-experts/full-article.md` (217 KB), `raw/mixtral-of-experts/full-article.md` (markdown view)  
**URL**: https://mistral.ai/news/mixtral-of-experts/  
**Ingested**: 2026-06-06  
**Tags**: #summary

## Summary

Mistral AI releases **Mixtral 8x7B**, a sparse mixture-of-experts (SMoE) decoder-only model with **Apache 2.0** open weights. Each layer routes each token to **two of eight expert feedforward blocks**; the model has **46.7B total parameters** but only **12.9B active per token**, yielding inference cost and speed comparable to a 12.9B dense model while matching or beating **Llama 2 70B** and **GPT-3.5** on most benchmarks with **6× faster inference**.

Capabilities include **32k context**, strong **code generation**, and fluency in **English, French, Italian, German, and Spanish**. Mixtral 8x7B Instruct is released alongside the base model, fine-tuned with SFT and **DPO**, scoring **8.30 on MT-Bench**—claimed best open-source instruction model, comparable to GPT-3.5. Bias/hallucination probes on BBQ/BOLD show less bias than Llama 2. Community inference support lands via **vLLM** (Megablocks CUDA kernels) and **Skypilot** deployment; Mixtral 8x7B also powers the **mistral-small** beta endpoint.

Architectural and evaluation details are expanded in [[Papers Explained 95 - Mixtral 8x7B]].

## Key Claims

- Mixtral 8x7B outperforms Llama 2 70B on most benchmarks with 6× faster inference; matches or outperforms GPT-3.5 on standard benchmarks.
- 46.7B total parameters, 12.9B active per token; two experts selected per token per layer from eight expert groups.
- 32k context; multilingual (EN/FR/IT/DE/ES); strong code generation.
- Mixtral 8x7B Instruct scores 8.30 on MT-Bench via SFT + DPO—best open-source instruction model claimed.
- Less bias than Llama 2 on BBQ; more positive sentiment on BOLD with similar variance.
- Apache 2.0 license; vLLM + Megablocks integration for efficient open-source serving.

## Figures

No article-body figures found in the fetched HTML. Benchmark charts referenced in prose ("quality versus inference budget tradeoff") are not embedded as `<img>` tags in the static page.

## Entities

- [[Mixture of Experts]] — sparse MoE architecture with 8 experts, 2 active per token.
- [[Large Language Models]] — open-weight SMoE release in the frontier model landscape.
- [[Multilingual Models]] — native support for five European languages.

## Questions & Gaps

- Benchmark figures and tables are referenced in text but not present as downloadable images in the static HTML export.
- Detailed architecture, routing math, and full benchmark tables are in [[Papers Explained 95 - Mixtral 8x7B]] and the Mistral technical report.

## Related

- [[Papers Explained 95 - Mixtral 8x7B]] — detailed explainer of Mixtral 8x7B architecture, MoE routing, and evaluation.
- [[Mixture of Experts]] — SMoE design patterns and sparse activation.
- [[Large Language Models]] — topic hub for open-weight model releases.
- [[Multilingual Models]] — multilingual pretraining and evaluation.
