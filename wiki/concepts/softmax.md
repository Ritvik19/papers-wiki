# Softmax

**Type**: concept  
**Tags**: #concept

## Overview

The softmax function maps a vector of logits to a probability distribution (non-negative entries summing to one) via exp-normalization. It is the standard output layer for multi-class classification.

## Appearances

- [[Deep Learning]] — Section 6.3 (hidden units and output layers) and information-theoretic treatment in Chapter 3 link softmax to cross-entropy and log-likelihood.
- [[Learning Word Embedding]] — Full softmax p(w_O|w_I) over vocabulary is O(V) per Word2Vec sample; motivates [[Hierarchical Softmax]], [[Noise-Contrastive Estimation]], and [[Negative Sampling]].
- Word2Vec skip-gram/CBOW output layers (vocabulary-sized multinomial).

## Notes

Temperature scaling divides logits before softmax to sharpen or flatten distributions (used in distillation and calibration). Numerical overflow is avoided by subtracting max(logits).

In skip-gram, softmax normalizes over all context words: p(w_O|w_I) = exp(v'_{w_O}^T v_{w_I}) / Σ_i exp(v'_{w_i}^T v_{w_I}). At V ≈ 10⁵–10⁶, exact normalization dominates training cost.

### Word2Vec output layer

Scores z_i = v'_{w_i}^T v_{w_I} are **logits** (unnormalized); softmax converts to probabilities. Cross-entropy loss L = −log p(w_O|w_I) = −z_{IO} + log Σ_i exp(z_i). See [[Learning Word Embedding]] for gradient decomposition and why [[Negative Sampling]] approximates the partition sum.

**Numerical stability**: subtract max(z) before exp (standard log-sum-exp trick; see [[Log-Sum-Exp Trick]]).

### Approximations at scale

| Method | Replaces full softmax denominator |
|--------|-----------------------------------|
| [[Hierarchical Softmax]] | Tree path product of sigmoids |
| [[Noise-Contrastive Estimation]] | Noise-contrastive logistic |
| [[Negative Sampling]] | Sigmoid on true + N negatives |

## Related

- [[Cross-Entropy Loss]]
- [[Maximum Likelihood Estimation]]
- [[Negative Sampling]]
- [[Hierarchical Softmax]]
- [[Word2Vec]]
- [[Learning Word Embedding]]
- [[Deep Learning]]
