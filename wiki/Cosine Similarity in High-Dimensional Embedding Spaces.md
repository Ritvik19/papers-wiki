# Cosine Similarity in High-Dimensional Embedding Spaces

**Source**: `raw/cosine-similarity-high-dimensions/full-article.html` · `raw/cosine-similarity-high-dimensions/full-article.md`  
**Ingested**: 2026-05-12  
**Tags**: #summary

## Summary

As embedding models grow to hundreds or thousands of dimensions, the effectiveness of cosine similarity as a distance metric can degrade due to the **curse of dimensionality**. In very high-dimensional spaces, random vectors tend to be nearly orthogonal to one another — their pairwise angles cluster around 90° — so cosine similarity values collapse toward zero for the vast majority of pairs. This is the orthogonality effect of the curse of dimensionality, and it erodes the discriminative power of the metric when most pairs score near the same value.

A related but counter-intuitive failure mode is **constant high similarity**: some high-dimensional models (notably OpenAI's `text-embedding-ada-002` at 1536 dimensions) produce cosine similarities above 0.68 for nearly all text pairs, even unrelated ones. This is partly an artifact of how models are trained and normalized — vectors are pushed onto a unit hypersphere and cluster in particular directions due to the training distribution — so the effective angular range used by the model is only a narrow slice of the full sphere.

Despite these risks, cosine similarity remains the dominant metric for embedding retrieval because it measures **direction rather than magnitude** (so Euclidean distance's tendency to explode with dimensionality doesn't apply), because contrastive training explicitly teaches models to push semantically similar items closer in angle, and because modern APIs normalize embeddings to unit length, reducing spurious magnitude variation.

When cosine similarity genuinely becomes unreliable, alternatives include **DIEM (Dimension Insensitive Euclidean Metric)**, or using whatever distance metric the model was originally trained with (e.g., dot product for models trained with InfoNCE, or a learned Siamese metric).

## Key Claims

- In high-dimensional spaces, most random vector pairs are nearly orthogonal → cosine similarities concentrate near zero (orthogonality effect).
- **Concentration of measure**: all points appear roughly equidistant, making it hard to distinguish near vs. far neighbors.
- Some production embedding models (e.g., `text-embedding-ada-002`) exhibit a floor effect: cosine similarity is always ≥ 0.68 even for dissimilar texts.
- Cosine similarity's advantage over Euclidean distance is that it is magnitude-invariant and does not grow unboundedly with dimension count.
- Contrastive training (e.g., InfoNCE loss) is the mechanism that keeps cosine similarity useful — similar items are explicitly pulled to smaller angles.
- Unit-normalization by embedding APIs partially mitigates magnitude artifacts but does not fix concentration of measure.
- DIEM is a proposed alternative metric designed to be robust to high dimensionality.

## Entities

- [[Curse of Dimensionality]] — the core mathematical phenomenon driving the failure modes discussed.
- [[Cosine Similarity]] — the metric under scrutiny; remains dominant in embedding retrieval despite these issues.
- [[Contrastive Learning]] — the training paradigm that keeps cosine similarity useful in practice.
- [[Embedding and Retrieval]] — the broader topic area this question belongs to.
- [[DIEM]] — Dimension Insensitive Euclidean Metric; an alternative metric proposed to handle high dimensions.

## Questions & Gaps

- At what dimensionality does the concentration effect become practically problematic? Empirical thresholds are not given.
- Does Matryoshka Representation Learning (MRL) help, since it encourages useful structure at smaller sub-dimensions?
- How does the floor effect in `text-embedding-ada-002` (≥ 0.68) interact with approximate nearest-neighbor search indices (HNSW, IVF)?
- Are there training recipes that specifically combat the constant-high-similarity failure mode, beyond contrastive loss?

## Related

- [[Embedding and Retrieval]] — topic page grouping all embedding model summaries.
- [[Papers Explained 96 - Matryoshka Representation Learning]] — encodes information at multiple granularities; may partially sidestep high-dim concentration.
- [[Papers Explained 110 - Nomic Embed]] — large-context embedding model; operates in high dimensions.
- [[Papers Explained 330 - Gemini Embedding]] — modern production embedding; relevant to the floor-effect observations.
