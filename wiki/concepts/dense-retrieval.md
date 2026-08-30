# Dense Retrieval

**Type**: concept  
**Tags**: #concept

## Overview

Dense retrieval uses learned embeddings to represent queries and candidate passages, then retrieves nearest neighbors in vector space, often with approximate nearest-neighbor indexes and reranking. It is a core technique in [[Embedding and Retrieval]] and retrieval-augmented generation.

## Appearances

- [[Papers Explained: Is Grep All You Need]] - compared against grep on LongMemEval-style agent memory tasks; inline vector retrieval usually trails grep, but file-based programmatic vector retrieval beats programmatic grep in several harness-model pairs.

## Notes

Dense retrieval can find paraphrases and semantically related evidence that [[Lexical Search]] misses. The trade-off, highlighted by [[Papers Explained: Is Grep All You Need]], is that semantically similar but irrelevant passages can distract the model, especially when the harness or model is weak at query refinement and reranker-aware reading.

## Related

- [[Lexical Search]]
- [[Agentic Search]]
- [[Embedding and Retrieval]]
- [[k-Nearest Neighbors]]
- [[Cosine Similarity]]
