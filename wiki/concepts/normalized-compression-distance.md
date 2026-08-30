# Normalized Compression Distance

**Type**: concept  
**Tags**: #concept

## Overview

Normalized Compression Distance (NCD) is a computable approximation of [[Kolmogorov Complexity]]-based information distance. It measures how similar two objects are by comparing how much a lossless compressor can exploit shared structure when compressing them jointly versus individually. NCD values range from 0 (identical) to ~1 (no shared information).

The formula is:

> NCD(x, y) = [C(xy) − min{C(x), C(y)}] / max{C(x), C(y)}

where C(x) is the compressed length of x and C(xy) is the compressed length of their concatenation. If x and y share a lot of structure, C(xy) ≈ max{C(x), C(y)}, driving NCD toward 0. If they share nothing, C(xy) ≈ C(x) + C(y), driving NCD toward 1.

## Appearances

- [[Papers Explained: Text Classification with Gzip]] — used as the similarity measure in a training-free gzip+kNN text classifier; outperforms BERT on OOD datasets.
- [[gzip Predicts Data-dependent Scaling Laws]] — the paper uses gzip compressibility (the raw C(x)/|x| ratio, related to NCD) as a dataset-level complexity metric to predict scaling law parameters.

## Notes

- NCD is parameter-free and data-type-agnostic: the same formula applies to text, DNA, images, or any byte sequence.
- The choice of compressor affects quality: gzip, bz2, and zstd each provide different approximation fidelity to true Kolmogorov complexity.
- The main practical bottleneck is inference time: computing NCD for a test item against all training items is O(n) compression operations.
- NCD was originally applied in bioinformatics (genome comparison) and anomaly detection before being adapted for text classification.

## Related

- [[Kolmogorov Complexity]] — the theoretical foundation NCD approximates.
- [[k-Nearest Neighbors]] — the classifier paired with NCD in the gzip text classification method.
- [[Embedding and Retrieval]] — NCD provides a non-learned, compression-based alternative to embedding similarity.
