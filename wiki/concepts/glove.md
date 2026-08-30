# GloVe

**Type**: concept  
**Tags**: #concept

## Overview

**GloVe** (Global Vectors for Word Representation; Pennington, Socher, Manning, EMNLP 2014) learns word vectors by fitting a **log-bilinear model** to a corpus-wide **word–word co-occurrence matrix**. It combines the global statistical efficiency of count-based methods with the vector space structure of [[Word2Vec]]-style dot products.

## Appearances

- [[Learning Word Embedding]] — Full ice/steam ratio example, bias terms, weighting f(c), objective derivation summary.
- [[Papers Explained - GloVe 2024]] — 2024 retrain: Wikipedia + Gigaword + Dolma; 1.29M+ vocab; NER and analogy benchmarks vs 2014 models.

## Co-occurrence matrix

Build symmetric matrix **X** where X_{ij} counts how often word j appears in context of word i (typically symmetric window, e.g. ±10 tokens). Often X_{ij} = X_{ji}.

**Co-occurrence probability**:

p_co(w_k | w_i) = X_{ik} / Σ_k X_{ik} = C(w_i, w_k) / C(w_i)

Distinct from skip-gram conditional p(w_O | w_I)—GloVe uses **global** counts, not local neural normalization.

## Ratio intuition (ice / steam)

| Target pair | Probe word w̃_k | Ratio p_co(w̃_k\|ice) / p_co(w̃_k\|steam) |
|-------------|------------------|----------------------------------------|
| ice, steam | solid | **High** — solid–ice co-occurrence dominates |
| ice, steam | water | **≈ 1** — related to both domains |
| ice, steam | fashion | **≈ 1** — unrelated to both |

Ratios isolate **relational** structure; raw probabilities conflate word frequency with association.

## Model

Seek vectors w_i, w̃_j and biases b_i, b̃_j such that:

**w_i^T w̃_j + b_i + b̃_j ≈ log X_{ij}**

Derived by modeling F = p_co(w̃_k|w_i) / p_co(w̃_k|w_j) as exp((w_i − w_j)^T w̃_k) and enforcing symmetry between word and context roles.

## Loss function

L = Σ_{i,j=1}^V f(X_{ij}) ( w_i^T w̃_j + b_i + b̃_j − log X_{ij} )²

Only pairs with X_{ij} > 0 contribute (sparsity).

**Weighting** f(c) (paper defaults c_max = 100, α = 0.75):

```
f(c) = (c / c_max)^α   if c < c_max
f(c) = 1               otherwise
```

Properties required: f(0)=0; non-decreasing in c; cap for large c so huge counts do not dominate.

## Training

- Optimize with **AdaGrad** (original paper).
- Precompute sparse X once; iterative stochastic or batch updates on non-zero entries.
- Typical dimensions: 50, 100, 200, 300 (same as Word2Vec benchmarks).
- [[Papers Explained - GloVe 2024]]: symmetric window 10, shuffle co-occurrence matrix with fixed seed, MFT=20 for vocab.

## GloVe vs Word2Vec

| | GloVe | Word2Vec |
|---|-------|----------|
| Signal | Global co-occurrence counts | Local context prediction |
| Objective | Weighted least squares on log counts | Classification (softmax / NEG) |
| Matrix | Explicit sparse X | Implicit via streaming pairs |
| OOV | None (type-level) | None in vanilla form; fastText adds subwords |
| Strength | Efficient use of global stats | Scales to streaming billions of tokens |

Baroni et al. (ACL 2014): neither dominates all intrinsic tasks; choice depends on corpus and evaluation.

## Related

- [[Count-Based Vector Space Model]]
- [[Word2Vec]]
- [[Word Embedding]]
- [[Jeffrey Pennington]]
- [[Papers Explained - GloVe 2024]]
- [[Embedding and Retrieval]]
- [[Learning Word Embedding]]
