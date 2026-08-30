# k-Nearest Neighbors

**Type**: concept  
**Tags**: #concept

## Overview

k-Nearest Neighbors (kNN) is a non-parametric classification (and regression) algorithm. Given a test item, it finds the k training examples whose distance to the test item is smallest, then assigns the majority label among those k neighbors. No training phase is needed — the training set itself is the model.

kNN's quality is entirely determined by the choice of distance metric. Classical uses employ Euclidean distance over feature vectors; in [[Papers Explained: Text Classification with Gzip]], [[Normalized Compression Distance]] (NCD) replaces learned embeddings as the similarity measure.

## Appearances

- [[Papers Explained: Text Classification with Gzip]] — paired with NCD (using gzip as the compressor) to produce a training-free, non-parametric text classifier that outperforms BERT on OOD datasets.

## Notes

- kNN has O(n) inference time per query (must compare against all training items), which limits scalability to large training sets.
- When combined with NCD, each comparison requires two compression operations (C(x1), C(x2)) plus one joint compression C(x1x2), making inference compute-bound.
- Approximate nearest neighbor (ANN) structures are commonly used to speed up kNN in high-dimensional embedding spaces.

## Related

- [[Normalized Compression Distance]] — the distance metric that replaces learned similarity in the gzip+kNN method.
- [[Kolmogorov Complexity]] — theoretical grounding for NCD, which underlies the gzip+kNN approach.
- [[Embedding and Retrieval]] — traditional kNN retrieval uses learned embeddings; the gzip approach replaces these with compression-based distances.
