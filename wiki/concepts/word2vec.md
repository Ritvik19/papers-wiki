# Word2Vec

**Type**: concept  
**Tags**: #concept

## Overview

**Word2Vec** is a family of shallow neural models (Mikolov et al., 2013) for learning **static word embeddings** from large unlabeled corpora. Two architectures—[[Skip-Gram]] and [[Continuous Bag-of-Words]]—share the same parameterization (matrices W and W′) but reverse the prediction direction. Training at Google scale relied on [[Negative Sampling]] rather than full-vocabulary [[Softmax]].

## Appearances

- [[Learning Word Embedding]] — Complete tutorial: architectures, all loss variants, Mikolov heuristics, Game of Thrones gensim demo.
- [[Papers Explained - GloVe 2024]] — Later benchmark lineage; original 2014 GloVe compared against Word2Vec-style vectors.

## Architecture

| Component | Shape | Role |
|-----------|-------|------|
| W (input / embedding matrix) | V × N | Row i = embedding of word i when it is the **input** |
| W′ (output / context matrix) | N × V | Column j = context representation of word j when it is the **output** |
| V | scalar | Vocabulary size |
| N | scalar | Embedding dimension (typical 100–300) |

**Independence of W and W′**: W′ is **not** the transpose or inverse of W. The same lexical item has two learned vectors depending on whether it appears as center word or context word.

## Training data generation

1. Tokenize corpus; optionally detect **phrases** (bigram merge) first.
2. Slide window of max size s_max along each sentence.
3. Optionally apply **subsampling** to frequent words.
4. Optionally use **soft window** (random sub-window per step).
5. Emit (target, context) pairs for skip-gram, or (context set, target) for CBOW.

## Loss options

| Loss | When to use |
|------|-------------|
| Full softmax | Tiny vocabularies only |
| [[Hierarchical Softmax]] | O(log V) training; tree design matters |
| [[Noise-Contrastive Estimation]] | Unnormalized models; partition-function trick |
| [[Negative Sampling]] | **Default** for Word2Vec; best speed/quality tradeoff |

## Hyperparameters (typical defaults)

| Parameter | Typical range | Notes |
|-----------|---------------|-------|
| N (size) | 50–300 | Higher dim → more capacity, more data needed |
| window | 5–10 (skip-gram); 5 (CBOW) | Larger → more syntactic + topical context |
| min_count | 5–50 | Filters hapax legomena |
| negative samples | 5–20 | More negatives → sharper discrimination, slower |
| subsample t | 10⁻⁵–10⁻³ | Higher t → more aggressive frequent-word downsample |
| epochs | 5–15+ | Depends on corpus size |
| learning rate | decay schedule | Original code: start ~0.025, reduce |

## Inference and evaluation

- **Similarity**: cosine similarity between rows of W (implementation-dependent whether W or W′ used for queries).
- **Analogy**: king − man + woman ≈ queen (vector arithmetic in embedding space).
- **Intrinsic benchmarks**: word similarity (WordSim353, SimLex999), analogy (Google, MSR).
- **Extrinsic**: feed frozen embeddings to downstream classifiers (NER, sentiment); see [[Papers Explained - GloVe 2024]] for NER with Stanza.

## Ecosystem

| Tool | Notes |
|------|-------|
| Original C word2vec | Reference implementation |
| gensim | `Word2Vec`, `KeyedVectors`, phrase detection |
| fastText | Subword-aware extension (OOV handling) |
| TensorFlow / PyTorch | NCE, negative sampling ops |

## Notes

Word2Vec learns **type-level** embeddings (one vector per word form). Homonyms share one vector; contextual disambiguation requires ELMo, BERT, or later encoders ([[Embedding and Retrieval]]). Despite age, static vectors remain useful for small-data baselines, visualization, and probing what co-occurrence alone encodes.

## Related

- [[Skip-Gram]]
- [[Continuous Bag-of-Words]]
- [[Negative Sampling]]
- [[Hierarchical Softmax]]
- [[Word Embedding]]
- [[Tomas Mikolov]]
- [[GloVe]]
- [[Learning Word Embedding]]
