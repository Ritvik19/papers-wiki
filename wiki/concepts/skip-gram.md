# Skip-Gram

**Type**: concept  
**Tags**: #concept

## Overview

**Skip-gram** is the [[Word2Vec]] architecture that predicts **context words** from a **target** (center) word. Each (target, context) pair within a sliding window is a separate training example. Skip-gram generally performs better on **large corpora** and **rare words** because each occurrence of a rare target generates multiple context predictions.

## Appearances

- [[Learning Word Embedding]] — Fig. 1 architecture; full Ned Stark window table; all loss derivations use skip-gram as the running example.

## Forward pass (step by step)

Given input target word index I and vocabulary size V, embedding dimension N:

1. **One-hot input** x ∈ {0,1}^V with x_I = 1.
2. **Lookup**: h = x^T W = W[I, :] = v_{w_I} ∈ ℝ^N (embedding vector).
3. **Output scores**: z_j = v'_{w_j}^T v_{w_I} for all j (matrix form: z = W′ h).
4. **Probabilities**: p(w_j | w_I) = exp(z_j) / Σ_k exp(z_k) ([[Softmax]]).

Output word w_O is one context word; training maximizes log p(w_O | w_I) or approximations thereof.

## Training sample explosion

Window size 5 on a sentence of length T generates roughly O(T × window) pairs—many more updates per token than [[Continuous Bag-of-Words]], which uses one averaged context vector per position.

Example (from source): target **"swing"** in *"… sentence should swing the sword"* → four training pairs:
- (swing, sentence), (swing, should), (swing, the), (swing, sword).

## Loss variants

All variants share parameters (W, W′) but differ in how they normalize or sample the output layer:

| Variant | Update touches |
|---------|----------------|
| Full softmax | All V output dimensions |
| [[Hierarchical Softmax]] | O(log V) nodes on path to w_O |
| [[Negative Sampling]] | w_O + N random negatives |
| [[Noise-Contrastive Estimation]] | w_O + N noise samples via logistic loss |

## Practical tips (Mikolov)

- Use **soft sliding window**: randomize effective window size per step; down-weight distance-d context by sampling probability 1/d.
- **Subsample** words with P_drop = 1 − √(t/f(w)) before generating pairs.
- Run **phrase detection** so multi-token entities are single vocabulary items.

## Skip-gram vs CBOW

| | Skip-gram | CBOW |
|---|-----------|------|
| Predicts | each context word from target | target from mean of contexts |
| Samples per position | multiple | one |
| Rare words | more gradient signal | less |
| Large data | preferred | competitive |
| Small data | can be noisy | averaging helps |

## Related

- [[Word2Vec]]
- [[Continuous Bag-of-Words]]
- [[Negative Sampling]]
- [[Hierarchical Softmax]]
- [[Softmax]]
- [[Cross-Entropy Loss]]
- [[Learning Word Embedding]]
