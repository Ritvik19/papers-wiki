# Continuous Bag-of-Words

**Type**: concept  
**Tags**: #concept

## Overview

**Continuous Bag-of-Words (CBOW)** is the [[Word2Vec]] architecture that predicts the **center (target) word** from the **bag of surrounding context words**. Context word vectors are looked up in W and **averaged** to form the hidden state; W′ maps the hidden state to a softmax (or sampled) distribution over the vocabulary.

## Appearances

- [[Learning Word Embedding]] — Fig. 2; predicts "swing" from context {sentence, should, the, sword}; noted as often better for **small datasets** due to averaging smoothing.

## Forward pass

For context word indices {c_1, c_2, …, c_m}:

1. Look up v_{w_{c_k}} = W[c_k, :] for each context word.
2. **Hidden**: h = (1/m) Σ_k v_{w_{c_k}} (element-wise mean).
3. **Output scores**: z = W′ h.
4. **Predict** target word w_t via softmax or [[Negative Sampling]] on z.

**Order invariance**: CBOW treats context as an unordered set—"dog bites man" and "man bites dog" yield the same context bag if window contents are identical (modulo window boundaries). Skip-gram preserves directional (target→context) asymmetry.

## Why averaging helps on small data

Averaging context embeddings **smooths** noise from individual context tokens—analogous to bag-of-words document models. On large corpora, skip-gram's extra per-pair updates usually win; on small corpora, CBOW's denoised hidden state can generalize better.

## Shared machinery with skip-gram

- Same W, W′ parameterization (independent matrices).
- Same loss approximations: full softmax, hierarchical, NCE, negative sampling.
- Same preprocessing: subsampling, soft window, phrase learning.

## CBOW in gensim

```python
from gensim.models import Word2Vec
# sg=0 selects CBOW; sg=1 (default) is skip-gram
model = Word2Vec(sentences, vector_size=100, window=5, sg=0, negative=5)
```

## Related

- [[Word2Vec]]
- [[Skip-Gram]]
- [[Word Embedding]]
- [[Learning Word Embedding]]
