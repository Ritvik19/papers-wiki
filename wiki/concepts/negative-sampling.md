# Negative Sampling

**Type**: concept  
**Tags**: #concept

## Overview

**Negative sampling (NEG)** is Mikolov et al.'s simplified objective for training [[Word2Vec]]. Instead of normalizing over the full vocabulary ([[Softmax]]), each training step updates the true (target, context) pair plus a small set of **random negative** words drawn from a noise distribution Q—using independent sigmoid binary classifiers.

## Appearances

- [[Learning Word Embedding]] — Derived from [[Noise-Contrastive Estimation]]; explicit sigmoid formulas; contrasted with full softmax and hierarchical softmax.
- [[Noise-Contrastive Estimation]] — Parent framework; NEG drops generative p(w|context) modeling.

## Objective

For input w_I, true context w, and negatives w̃_1,…,w̃_N ~ Q:

**p(d=1 | w, w_I)** = σ(v'_w^T v_{w_I})

**p(d=0 | w̃, w_I)** = σ(−v'_{w̃}^T v_{w_I}) = 1 − σ(v'_{w̃}^T v_{w_I})

**Loss**:

L = −[ log σ(v'_w^T v_{w_I}) + Σ_{i=1}^N log σ(−v'_{w̃_i}^T v_{w_I}) ]

Gradients touch only **1 + N** output word vectors per training step instead of V.

## Noise distribution Q

Common choices:

| Distribution | Formula / rule | Used in |
|--------------|----------------|---------|
| Unigram^{3/4} | P(w) ∝ freq(w)^{0.75} | Original word2vec C code |
| Log-uniform (Zipfian) | q(w) ∝ (log rank)^{-1} | TensorFlow NCE sampler |
| Uniform | Rare; too easy negatives | Baselines only |

**3/4 power** (Mikolov): balances frequent vs rare words—frequent words sampled more often as negatives (harder task) but not as extremely as raw frequency would dictate.

## Hyperparameters

| Param | Typical | Effect |
|-------|---------|--------|
| N (negatives) | 5–20 | More → better approximation of softmax gradient, slower |
| subsample t | 10⁻⁵ | Frequent word downsample before pair generation |
| sample threshold | min_count 5 | Exclude ultra-rare types |

## NEG vs NCE vs softmax

| | Full softmax | NCE | Negative sampling |
|---|--------------|-----|-------------------|
| Goal | Exact ML estimate | Estimate partition function | Learn good embeddings |
| Normalization | Explicit Σ_V | Approximate Z≈1 | None (sigmoids) |
| Cost/step | O(V) | O(N) | O(N) |
| Generative? | Yes | Approximate | No |

Mikolov: NEG "focuses on learning high-quality word embedding rather than modeling the word distribution in natural language."

## Gradient intuition

- **Positive pair**: increase dot product v'_w^T v_{w_I} (pull context vector toward input embedding).
- **Each negative**: decrease dot product v'_{w̃}^T v_{w_I} (push noise context vectors away).

Equivalent to approximating the second term of cross-entropy gradient E_{w~p}[∇z] with Monte Carlo samples from Q instead of p.

## Related

- [[Noise-Contrastive Estimation]]
- [[Word2Vec]]
- [[Skip-Gram]]
- [[Softmax]]
- [[Cross-Entropy Loss]]
- [[Tomas Mikolov]]
- [[Learning Word Embedding]]
