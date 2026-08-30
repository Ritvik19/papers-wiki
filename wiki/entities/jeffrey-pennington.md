# Jeffrey Pennington

**Type**: person  
**Tags**: #entity

## Overview

Jeffrey Pennington is a researcher; first author of **GloVe: Global Vectors for Word Representation** (with Richard Socher and Christopher Manning, EMNLP 2014). GloVe combines global word–word co-occurrence statistics with a log-bilinear vector model.

## Appearances

- [[Learning Word Embedding]] — GloVe ice/steam ratio motivation, log objective, bias terms b_i / b̃_j, weighting function f(c).
- [[Papers Explained - GloVe 2024]] — Lineage of refreshed 2024 English GloVe models evaluated on analogy, similarity, and NER.

## GloVe contributions (2014 paper)

| Idea | Detail |
|------|--------|
| Ratio of co-occurrence probabilities | Encodes meaning beyond raw p_co |
| Log-linear model | log X_{ij} ≈ w_i^T w̃_j + b_i + b̃_j |
| Weighted least squares | Sparse matrix; f(c) caps huge counts |
| Public embeddings | 50d–300d vectors widely used as baselines |

Stanford NLP group released pretrained vectors (Wikipedia 2014 + Gigaword 5); [[Papers Explained - GloVe 2024]] documents modern corpus updates (Dolma subset, larger vocab).

## Related

- [[GloVe]]
- [[Count-Based Vector Space Model]]
- [[Papers Explained - GloVe 2024]]
- [[Word Embedding]]
- [[Learning Word Embedding]]
