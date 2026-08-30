# Cosine Similarity

**Type**: concept  
**Tags**: #concept

## Overview

Cosine similarity measures the cosine of the angle between two vectors, yielding a value between −1 and 1 (typically 0–1 for non-negative embeddings). It is the dominant distance metric for semantic search over text embeddings because it is magnitude-invariant and scales gracefully compared to Euclidean distance.

## Appearances

- [[Cosine Similarity in High-Dimensional Embedding Spaces]] — central subject; discusses failure modes in high-dimensional embedding spaces including orthogonality collapse and the floor-effect (≥0.68 similarity for all pairs in `text-embedding-ada-002`).

## Notes

- In high-dimensional spaces, random vectors tend to be nearly orthogonal, causing cosine similarities to concentrate near zero for most pairs — eroding discriminative power.
- A counter-intuitive failure mode: some production models produce *high* cosine similarity (≥0.68) for all text pairs regardless of semantic relatedness, due to training distribution effects.
- The metric is robust to vector magnitude, unlike Euclidean distance, which makes it preferable when embeddings have variable norms.
- Modern APIs normalize embeddings to unit length, making cosine similarity equivalent to dot product and removing magnitude as a factor entirely.

## Related

- [[Curse of Dimensionality]]
- [[Contrastive Learning]]
- [[DIEM]]
- [[Embedding and Retrieval]]
