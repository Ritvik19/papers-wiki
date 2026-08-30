# Cross-Entropy Loss

**Type**: concept  
**Tags**: #concept

## Overview

Cross-entropy loss measures dissimilarity between a predicted probability distribution and a target (often one-hot) distribution. For classification it is the standard training objective, equivalent to negative log-likelihood under a softmax parameterization.

## Appearances

- [[Deep Learning]] — Derived from maximum likelihood (Chapter 5) and used throughout supervised deep learning (Chapters 6–12).
- [[Learning Word Embedding]] — Skip-gram loss L = −log p(w_O|w_I) with one-hot y; gradient −∇z_{IO} + E_{w_i~Q}[∇z_{Ii}] motivates noise-based approximation of the partition sum.

## Notes

Numerical stability uses log-softmax rather than log(softmax) directly. Multi-class, multi-label, and sequence losses (per-token cross-entropy) are extensions used in modern LLMs.

For Word2Vec, expanding L = −z_{IO} + log Σ exp(z_{Ii}) shows the true context word receives positive reinforcement while other vocabulary entries contribute negative gradient mass—estimated via sampled negatives in production training.

### Skip-gram gradient (from [[Learning Word Embedding]])

Let z_{IO} = v'_{w_O}^T v_{w_I}. Then:

∇_θ L = −∇_θ z_{IO} + Σ_{i=1}^V p(w_i|w_I) ∇_θ z_{Ii}

The second term is an expectation over the **full vocabulary** under the model distribution—expensive. [[Negative Sampling]] and [[Noise-Contrastive Estimation]] replace this sum with samples from noise distribution Q.

**Connection to information theory**: Minimizing cross-entropy H(y, p) equals maximizing log-likelihood of the correct class under a softmax parameterization ([[Maximum Likelihood Estimation]]).

## Related

- [[Softmax]]
- [[Maximum Likelihood Estimation]]
- [[Negative Sampling]]
- [[Noise-Contrastive Estimation]]
- [[Skip-Gram]]
- [[Word2Vec]]
- [[Learning Word Embedding]]
- [[Feedforward Neural Networks]]
- [[Deep Learning]]
