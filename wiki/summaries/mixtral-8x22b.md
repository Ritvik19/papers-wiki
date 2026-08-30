# Cheaper, Better, Faster, Stronger

**Source**: `raw/mixtral-8x22b/full-article.md` (216 KB), `raw/mixtral-8x22b/full-article.md` (markdown view)  
**URL**: https://mistral.ai/news/mixtral-8x22b/  
**Ingested**: 2026-06-06  
**Tags**: #summary

## Summary

Mistral AI releases **Mixtral 8x22B**, a sparse mixture-of-experts model with **141B total parameters** and **39B active per token**, continuing the Mixtral open-model family under **Apache 2.0**. The blog positions it as faster than any dense 70B model while outperforming other open-weight models on standard benchmarks. Key capabilities include **64K context**, native **function calling** (with constrained output on la Plateforme), strong **math and coding**, and fluency in **English, French, Italian, German, and Spanish**.

Performance claims span reasoning/knowledge (MMLU, HellaSwag, WinoGrande, ARC, TriviaQA, NaturalQS), multilingual benchmarks vs. Llama 2 70B, and coding/math (HumanEval, MBPP, GSM8K, MATH). The instructed variant reports **90.8% GSM8K maj@8** and **44.6% MATH maj@4**. Mixtral 8x22B sits on the same efficient performance-vs-inference-budget curve as Mistral 7B and Mixtral 8x7B.

## Key Claims

- 141B total parameters, 39B active per token; Apache 2.0 release with no usage restrictions.
- Faster than dense 70B models; more capable than other open-weight models per Mistral's benchmarks.
- 64K context window; native function calling; strong math, coding, and five-language fluency.
- Instruct variant: 90.8% GSM8K maj@8, 44.6% MATH maj@4.
- Outperforms Llama 2 70B on multilingual HellaSwag, ARC, and MMLU in FR/DE/ES/IT.
- Available on la Plateforme for exploration and fine-tuning.

## Figures

No article-body figures found in the fetched HTML. Four benchmark charts (MMLU vs. inference budget, reasoning/knowledge, multilingual, math/coding) are referenced as "Figure 1–4" in prose only.

## Entities

- [[Mixture of Experts]] — sparse MoE scaling from 8x7B to 8x22B.
- [[Large Language Models]] — open-weight frontier model release.
- [[Multilingual Models]] — native multilingual reasoning and knowledge.

## Questions & Gaps

- Benchmark chart images not embedded in static HTML; numeric tables not fully reproduced in the blog body.
- No cross-linked wiki explainer page for Mixtral 8x22B architecture specifics (distinct from [[Papers Explained 95 - Mixtral 8x7B]]).

## Related

- [[Papers Explained 95 - Mixtral 8x7B]] — prior Mixtral SMoE release and architectural foundation.
- [[Mixture of Experts]] — sparse activation and expert routing.
- [[Large Language Models]] — open model releases and benchmark comparisons.
- [[Multilingual Models]] — multilingual evaluation across European languages.
