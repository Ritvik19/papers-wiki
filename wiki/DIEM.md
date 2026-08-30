# DIEM

**Type**: concept  
**Tags**: #concept

## Overview

DIEM (Dimension Insensitive Euclidean Metric) is a proposed distance metric for high-dimensional vector spaces, designed to remain discriminative where standard Euclidean distance or cosine similarity suffer from concentration of measure. Reference: [arxiv.org/html/2407.08623v4](https://arxiv.org/html/2407.08623v4).

## Appearances

- [[Cosine Similarity in High-Dimensional Embedding Spaces]] — cited as an alternative to cosine similarity when high-dimensional embeddings (e.g., 1536-dimensional) give insufficiently discriminative similarity scores.

## Notes

- Standard Euclidean distance suffers from the curse of dimensionality: all pairwise distances tend to converge to the same value, making nearest-neighbor retrieval unreliable.
- DIEM is designed to normalise or correct for this concentration effect, preserving meaningful distance relationships at high dimensionality.
- Not yet in mainstream use — most production systems still default to cosine similarity or dot product.

## Related

- [[Cosine Similarity]]
- [[Curse of Dimensionality]]
- [[Embedding and Retrieval]]
