# Introducing Command R7B: Fast and efficient generative AI

**Source**: `raw/command-r7b/full-article.md` (324 KB), `raw/command-r7b/full-article.md` (markdown view)  
**URL**: https://cohere.com/blog/command-r7b  
**Ingested**: 2026-06-06  
**Tags**: #summary

## Summary

[[Cohere]] releases **Command R7B** (`c4ai-command-r7b-12-2024`), the smallest and final model in the Command R enterprise LLM series. The ~7B open-weights model targets developers and businesses optimizing for speed, cost-performance, and low compute: it can run on low-end GPUs, MacBooks, or even CPUs while retaining **128K context**, multilingual support, citation-verified **RAG**, reasoning, tool use, and multi-step agentic behavior.

Cohere positions R7B as class-leading among similarly sized open models on the HuggingFace Open LLM Leaderboard and on enterprise-relevant tasks: math/code/reasoning benchmarks, **ChatRAG-Bench** conversational RAG (PoLL judge ensemble), **BFCL-v3** function calling (including live and irrelevance subsets), and LangChain REACT agents on **Bamboogle** and **StrategyQA**. Human blind head-to-head evaluations favor R7B on customer-facing RAG assistants (customer service, HR, compliance, IT support). API pricing is $0.0375/1M input and $0.15/1M output tokens.

## Key Claims

- Command R7B is the smallest, fastest, and final model in Cohere's R series; open weights on Hugging Face and API on Cohere Platform.
- 128K context with citation-verified RAG, tool use, reasoning, and agentic multi-step behavior in a ~7B footprint.
- Ranks first on average among similarly sized open models on the HuggingFace Open LLM Leaderboard.
- Outperforms size-matched open models on RAG (ChatRAG-Bench), tool use (BFCL-v3), and REACT agents (Bamboogle, StrategyQA).
- Deployable on commodity GPUs, MacBooks, or CPUs for rapid prototyping and high-throughput chat/code workloads.

## Figures

| Figure | Caption | Page |
|--------|---------|------|
| ![fig-1](../assets/command-r7b/fig-1.webp) | Blog hero — Command R7B announcement | — |

![Command R7B announcement](../assets/command-r7b/fig-1.webp)

## Entities

- [[Cohere]] — model author; Command R series lineage.
- [[Large Language Models]] — compact enterprise LLM in the R family.
- [[Model Compression and Efficiency]] — edge/commodity-GPU deployment focus.

## Questions & Gaps

- Exact parameter count and architecture details are not in the blog (Arabic variant cites ~8B including embeddings).
- Benchmark tables are chart-only in the HTML export; scores must be read from figures.
- Blog marks R7B as the "final" R-series model; later Command A family supersedes for flagship workloads.

## Related

- [[Model Compression and Efficiency]] — commodity-GPU, CPU, and edge deployment patterns for compact models.
- [[Large Language Models]] — Command R family and lightweight open-weights releases.
- [[Papers Explained 166 - Command Models]] — deeper wiki coverage of Command R, R+, and R7B in the corpus.
