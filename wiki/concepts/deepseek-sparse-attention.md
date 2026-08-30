# DeepSeek Sparse Attention

**Tags**: #concept

DeepSeek Sparse Attention (DSA) is a learned sparse attention pattern introduced in the DeepSeek V3.2 line and adopted in GLM-5. Like [[Sliding Window Attention]], each token attends to only a subset of prior positions—but the subset is **selected dynamically** rather than defined by a fixed local window.

## Overview

DSA uses a two-stage mechanism:

1. **Lightning indexer** — scores prior tokens for each new query using compressed representations (from [[Multi-Head Latent Attention]] in DeepSeek V3.2), producing relevance scores over the prefix.
2. **Token selector** — keeps a smaller high-scoring subset (e.g., top-\(k\) positions) that defines the sparse attention mask.

Relative to SWA: both limit attention span; SWA hard-codes locality, DSA learns which past tokens merit revisit. DeepSeek V3.2 pairs DSA with MLA—MLA compresses cache storage; DSA reduces how much of the prior context must be attended over.

DSA is newer and more complex to implement than [[Grouped-Query Attention]], so adoption remains narrower (DeepSeek V3.2, GLM-5 at time of Raschka's March 2026 article).

## Appearances

- [[A Visual Guide to Attention Variants in Modern LLMs]] — DSA vs SWA comparison, indexer/selector diagrams, DeepSeek V3.2 reference architecture.
- [[Beyond Standard LLMs]] — sparse/subquadratic attention mentioned in linear-hybrid landscape.

## Notes

- Not to be confused with unstructured academic sparse attention patterns (Longformer, Sparse Transformer)—DSA is a production DeepSeek design with learned indexing.
- Serving stacks for DSA + MLA hybrids are still maturing versus classic GQA kernels.

## Related

- [[Sliding Window Attention]]
- [[Multi-Head Latent Attention]]
- [[Linear Attention Hybrids]]
- [[Long Context]]
- [[Model Compression and Efficiency]]
