Source URL: https://research.perplexity.ai/articles/accelerating-sonar-through-speculation
Title: Accelerating Sonar Through Speculation

---
title: Accelerating Sonar Through Speculation
description: Speculative decoding accelerates Sonar LLMs via draft model verification
published: "Jun 1, 2026, 5:44 PM UTC"
---

systems

Jun 10, 2025

# Accelerating Sonar Through Speculation

Speculative decoding accelerates Sonar LLMs via draft model verification.

Speculative decoding speeds up LLM generation by using a quick draft model to produce completion candidates verified by the larger target model. Under this scheme, instead of the expensive target producing a single token per step, multiple tokens can be emitted in one step. This post presents implementation details of speculative decoding schemes applied at Perplexity to reduce inter-token latency on Sonar models.

See canonical HTML at `raw/accelerating-sonar-through-speculation/full-article.md` for full figures and references.
