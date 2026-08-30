# Curse of Dimensionality

**Type**: concept  
**Tags**: #concept

## Overview

The curse of dimensionality refers to phenomena that arise when analyzing data in high-dimensional spaces: distances concentrate (all points become roughly equidistant), volume explodes exponentially, and intuitions from low-dimensional geometry break down. It is a fundamental challenge in machine learning, information retrieval, and statistics.

## Appearances

- [[Cosine Similarity in High-Dimensional Embedding Spaces]] — the core mechanism behind why cosine similarity degrades in very high-dimensional embedding models; specifically causes orthogonality of random vectors and concentration of pairwise distances.

## Notes

- **Concentration of measure**: in high dimensions, the ratio of the maximum to minimum pairwise distance between random points tends to 1, making nearest-neighbor search unreliable.
- **Orthogonality**: random unit vectors in high dimensions are nearly perpendicular with high probability. This means cosine similarity scores cluster around 0 for unrelated items.
- **Sparse data**: the volume of a high-dimensional hypersphere is concentrated near its surface; data points become sparse relative to the space's volume.
- Contrastive training partially counteracts the curse by explicitly shaping the angular structure of the embedding space.

## Related

- [[Cosine Similarity]]
- [[Contrastive Learning]]
- [[Embedding and Retrieval]]
- [[DIEM]]
