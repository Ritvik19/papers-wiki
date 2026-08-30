# Distributed Representations

**Type**: concept  
**Tags**: #concept

## Overview

Distributed representations encode concepts as patterns of activity across many units (as opposed to one-hot localist codes), enabling similarity, compositionality, and generalization to unseen combinations of features.

## Appearances

- [[Deep Learning]] — Section 15.4 argues for distributed representations as a core advantage of deep learning over classical feature engineering.
- [[Learning Word Embedding]] — Word2Vec skip-gram/CBOW learn distributed word vectors (dense N-dim) replacing one-hot V-dim encodings; Mikolov et al. "distributed representations of words and phrases" (2013).

## Notes

Word embeddings, hidden layer activations, and latent codes in autoencoders are distributed. The book connects this to exponential efficiency gains from depth (15.5).

Static word2vec/GloVe vectors assign one embedding per word **type**; contextual models (BERT+) produce token-dependent distributed states. Analogy structure (king − man + woman) emerges when dimensions jointly encode multiple features of meaning.

### Word2Vec as distributed codes

In [[Skip-Gram]], each word's embedding is a point in ℝ^N where **many dimensions participate** in representing gender, animacy, syntax, topic, etc.—unlike one-hot where exactly one dimension fires. [[Word2Vec]] matrix W stores these codes; training adjusts all dimensions co-adaptively from co-occurrence signal.

**Efficiency argument** (Goodfellow et al., Ch. 15.5): some concepts need exponentially more parameters in shallow localist codes than in distributed codes with depth—motivation for embeddings + neural depth in modern NLP.

## Related

- [[Word Embedding]]
- [[Word2Vec]]
- [[Learning Word Embedding]]
- [[Representation Learning]]
- [[Embedding and Retrieval]]
- [[Deep Learning]]
