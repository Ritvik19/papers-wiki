Source URL: https://research.perplexity.ai/articles/pplx-embed-state-of-the-art-embedding-models-for-web-scale-retrieval
Title: pplx-embed: State-of-the-Art Embedding Models for Web-Scale Retrieval

---
title: "pplx-embed: State-of-the-Art Embedding Models for Web-Scale Retrieval"
description: Today we are releasing pplx-embed-v1 and pplx-embed-context-v1, two state-of-the-art text embedding models built for real-world, web-scale retrieval.
published: "Jun 1, 2026, 5:44 PM UTC"
---

Feb 26, 2026

# pplx-embed: State-of-the-Art Embedding Models for Web-Scale Retrieval

Today we are releasing **pplx-embed-v1** and **pplx-embed-context-v1**, two state-of-the-art text embedding models built for real-world, web-scale retrieval. **pplx-embed-v1** is optimized for standard dense text retrieval, while **pplx-embed-context-v1** embeds passages with respect to surrounding document-level context.

Both families are available at 0.6B and 4B parameter scales. The 0.6B models target lightweight, low-latency embedding generation; the 4B models maximize retrieval quality. The family leads public benchmarks including MTEB(Multilingual, v2), BERGEN, ToolRet, and ConTEB, and delivers best-in-class results on internal web-scale benchmarks PPLXQuery2Query and PPLXQuery2Doc.

The models produce INT8 and binary embeddings, reducing storage by 4× and 32× respectively compared to FP32.

Technical report: https://arxiv.org/abs/2602.11151
