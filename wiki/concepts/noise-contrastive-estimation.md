# Noise-Contrastive Estimation

**Type**: concept  
**Tags**: #concept

## Overview

**Noise-contrastive estimation (NCE)** (Gutmann & Hyvärinen, AISTATS 2010) trains models on unnormalized densities by learning to **discriminate observed data from a known noise distribution**. It avoids computing the [[Partition Function]] by reducing learning to binary classification—directly applicable to large-vocabulary language models and [[Word2Vec]] output layers.

## Appearances

- [[Deep Learning]] — Section 18.6: partition-function workaround for undirected models.
- [[Learning Word Embedding]] — Full derivation for skip-gram: joint p(d, word | w_I), posteriors p(d=1|·), simplified loss with Z≈1, log-uniform noise.

## Word2Vec formulation

Given input w_I, true output w, and N noise samples w̃_i ~ Q:

**Classifier loss**:

L = −[ log p(d=1|w,w_I) + Σ_{i=1}^N log p(d=0|w̃_i,w_I) ]

**Generative story** (mixture of true + noise):

| Event | Probability |
|-------|-------------|
| Pick true word w | 1/(N+1) · p(w|w_I) |
| Pick noise w̃ | N/(N+1) · q(w̃) |

**Posteriors**:

p(d=1|w,w_I) = p(w|w_I) / (p(w|w_I) + N·q(w̃))

p(d=0|w̃,w_I) = N·q(w̃) / (p(w|w_I) + N·q(w̃))

## Partition function trick

p(w|w_I) = exp(v'_w^T v_{w_I}) / Z(w_I) still contains Z(w_I) = Σ_V exp(·).

**Mnih & Teh (2012)**: assume Z(w) ≈ 1 after softmax normalization pressure → drop explicit partition term in loss, yielding logistic form with exp(v'_w^T v_{w_I}) in numerator and denominator.

## Noise distribution Q

Design goals:
1. **Similar** to data distribution (informative negatives).
2. **Easy to sample** (e.g. unigram table, log-uniform alias method).

**Log-uniform / Zipfian** (TensorFlow):

q(w̃) = (log(r_{w̃}+1) − log r_{w̃}) / log V

where r is frequency rank (1 = most frequent). Matches heavy-tailed word frequencies.

## NCE vs [[Negative Sampling]]

| | NCE | Negative sampling |
|---|-----|-------------------|
| Target | Approximate softmax likelihood | Embedding quality |
| Uses p(w|w_I) explicitly | Replaced by σ(dot) |
| Theoretical link | Consistent estimator under assumptions | Heuristic simplification |
| Practice in word2vec | Less common | **Default** |

[[Negative Sampling]] is the production Word2Vec specialization of NCE ideas.

## Broader uses

- Unnormalized graphical models ([[Deep Learning]] Ch. 18).
- Contrastive representation learning (modern encoders use similar noise-contrastive / InfoNCE flavors).
- Any exponential-family model where Z is intractable.

## Related

- [[Negative Sampling]]
- [[Partition Function]]
- [[Word2Vec]]
- [[Softmax]]
- [[Representation Learning]]
- [[Deep Learning]]
- [[Learning Word Embedding]]
