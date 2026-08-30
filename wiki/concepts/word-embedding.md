# Word Embedding

**Type**: concept  
**Tags**: #concept

## Overview

A **word embedding** is a dense vector **e_w ∈ ℝ^N** (N ≪ |V|) representing a word or phrase such that **semantic similarity** corresponds to geometric closeness (cosine distance, Euclidean distance) and **relational regularities** can appear as vector offsets (e_king − e_man + e_woman ≈ e_queen).

Embeddings solve the **curse of dimensionality** of one-hot encoding: one-hot vectors are orthogonal for all distinct words—no notion of similarity—while embeddings pack meaning into N ≈ 50–300 continuous dimensions.

## Appearances

- [[Learning Word Embedding]] — Foundational tutorial: one-hot limitations, count vs context methods, Word2Vec, GloVe, training tricks (Lilian Weng, 2017).
- [[How Transformers Work in Deep Learning and NLP: An Intuitive Introduction]] — token embeddings as transformer input; combined with [[Positional Encoding]] before self-attention.
- [[Distributed Representations]] — Why distributed (many active dimensions per concept) beats localist one-hot codes.
- [[Embedding and Retrieval]] — Modern sentence/multimodal encoders; dense retrieval stacks.

## Properties of good embeddings

| Property | Mechanism | Example |
|----------|-----------|---------|
| Similarity | Nearby vectors for synonymous/near-synonym words | cat ↔ kitten |
| Analogy | Consistent offset vectors | king − man + woman ≈ queen |
| Clustering | Domain or topic groups | medical terms cluster |
| Compositionality (limited) | Phrase tokens ("New_York") | Phrase detection pre-training |

All rely on **distributional** learning from co-occurrence—either explicit counts ([[GloVe]]) or predictive context ([[Word2Vec]]).

## Historical evolution

```
One-hot (localist)
  → LSA / PPMI + SVD (count-based dense)
  → Word2Vec skip-gram/CBOW + negative sampling (2013)
  → GloVe global log-regression (2014)
  → fastText subword buckets (2016)
  → ELMo contextual (2018)
  → BERT / transformer encoders (2018+)
  → Sentence-BERT, E5, Gemini Embedding (sentence & multimodal)
```

**Static** embeddings (Word2Vec, GloVe): one vector per word **type**—"bank" (river) and "bank" (finance) share a vector.

**Contextual** embeddings: vector depends on surrounding sentence—required for polysemy in modern NLP.

## Training checklist (static embeddings)

1. **Corpus scale** — billions of tokens preferred for general English.
2. **Tokenization** — consistent lowercasing/punctuation; detect **phrases** before training.
3. **Subsample** frequent words (Word2Vec) or weight counts (GloVe).
4. **Architecture** — skip-gram for large data; CBOW for small.
5. **Loss** — negative sampling (5–20 negatives) in practice.
6. **Dimension** — 100–300; tune on intrinsic + downstream task.
7. **Evaluation** — WordSim, SimLex, analogy sets; task-specific NER/classification.

## Evaluation modes

| Type | Benchmarks | What it measures |
|------|------------|------------------|
| Intrinsic similarity | WordSim353, SimLex999, MEN | Correlation with human similarity judgments |
| Intrinsic analogy | Google, MSR | Vector offset arithmetic |
| Extrinsic | NER, sentiment, parsing with frozen embeddings | Utility as features ([[Papers Explained - GloVe 2024]]) |

## Limitations

- No subword morphology in vanilla Word2Vec (use fastText for OOV).
- No sentence-level meaning (use sentence encoders for retrieval).
- Static sense conflation.
- Gender/racial bias from corpus statistics (mitigation requires separate debiasing research).

## Related

- [[Word2Vec]]
- [[GloVe]]
- [[Skip-Gram]]
- [[Continuous Bag-of-Words]]
- [[Distributed Representations]]
- [[Cosine Similarity]]
- [[Embedding and Retrieval]]
- [[Learning Word Embedding]]
