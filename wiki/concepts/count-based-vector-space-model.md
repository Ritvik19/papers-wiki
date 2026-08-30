# Count-Based Vector Space Model

**Type**: concept  
**Tags**: #concept

## Overview

**Count-based vector space models** learn word representations from **global co-occurrence statistics**—how often words appear together in a corpus—then apply matrix factorization or regression to obtain dense low-dimensional vectors. They embody the **distributional hypothesis**: words in similar contexts have similar meanings.

## Appearances

- [[Learning Word Embedding]] — Contrasted with context-based [[Word2Vec]]; examples: PCA, topic models, neural probabilistic LMs; [[GloVe]] as modern count+vector hybrid.
- [[Deep Learning]] — Historical neural language models (Bengio et al.) as early count-inspired distributed learning.

## Pipeline

```
Corpus → co-occurrence / term-document matrix → transform counts → factorize → word vectors
```

| Stage | Common transforms |
|-------|-------------------|
| Raw counts | Term-document, word–context window matrix |
| Smoothing | Add-k, discard infrequent |
| Weighting | PMI, PPMI, log, entropy |
| Reduction | SVD (LSA), NMF, weighted regression ([[GloVe]]) |

**Raw counts alone are weak**—high-frequency function words dominate; PMI/log emphasizes associations beyond chance.

## Representative methods

| Method | Matrix | Technique | Output |
|--------|--------|-----------|--------|
| **LSA** | Term-document | SVD on TF-IDF | Latent semantic dimensions |
| **LDA** | Bag-of-words per doc | Topic generative model | Word–topic distributions |
| **Hyperspace Analogue to Language (HAL)** | Word–context grid | Summed co-occurrence vectors | Explicit word vectors |
| **GloVe** | Word–word X_{ij} | Weighted log regression | w_i, w̃_j, biases |
| **Neural LM (2003)** | Streaming contexts | Predict next word with learned features | Embeddings as NN weights |

## Count-based vs context-based (Word2Vec)

| Dimension | Count-based | Context-based (skip-gram/CBOW) |
|-----------|-------------|-------------------------------|
| Data pass | Often two-pass (build matrix, then fit) | Streaming one-pass friendly |
| Signal | Global sufficient statistics | Local predictive constraints |
| Objective | Reconstruction / regression on X | Classification / noise contrast |
| Sparsity | Exploit matrix sparsity explicitly | Implicit via sampling |

Baroni et al. (ACL 2014, *Don't count, predict!*): systematic comparison—neither family universally wins on similarity, analogy, or downstream tasks.

## Connection to GloVe

[[GloVe]] is explicitly a **count-based** method that borrows the **dot-product scoring** of predictive models:

log X_{ij} ≈ w_i^T w̃_j + b_i + b̃_j

Thus the wiki taxonomy treats GloVe as the bridge concept between classical factorization and Word2Vec.

## Related

- [[GloVe]]
- [[Word Embedding]]
- [[Word2Vec]]
- [[Distributed Representations]]
- [[Principal Component Analysis]]
- [[Learning Word Embedding]]
