# Cosine Similarity in High-Dimensional Embedding Spaces

**Source**: Google AI Mode answer  
**Query**: "in embedding models if we keep on adding more dimensions does the cosine similarity become irrelevant because points keep on going further and further"  
**Source URL**: https://share.google/aimode/1zsaZrPGb4CNgfKaG  
**Saved**: 2026-05-12

---

Yes, as the number of dimensions in embedding models increases, the effectiveness of cosine similarity can diminish, a phenomenon driven by the "curse of dimensionality". While adding dimensions allows models to capture more nuanced semantic relationships, it simultaneously pushes vectors to become nearly orthogonal (perpendicular) to each other, causing cosine similarity scores to cluster around a narrow band, often near zero or a high constant value, reducing their discriminative power. [1, 2, 3, 4, 5]

## Why High Dimensions Impact Cosine Similarity

- **Orthogonality and Sparsity:** In very high-dimensional spaces, most vectors tend to be nearly perpendicular, resulting in cosine similarity values close to zero.
- **Concentration of Measure:** Distances between points tend to concentrate, meaning all points appear roughly equidistant from each other. This makes it difficult to differentiate between "nearby" neighbors and "far" points.
- **Constant High Similarity:** Surprisingly, some modern high-dimensional models (like text-embedding-ada-002) can result in relatively high cosine similarities (e.g., >0.68) for all pairs, even when the texts are dissimilar, making the metric less useful for ranking. [2, 4, 5, 6, 7, 8]

## Why Cosine Similarity Often Remains Relevant

Despite these issues, cosine similarity is still the default for high-dimensional text embeddings for several reasons:

- **Direction Over Magnitude:** Unlike Euclidean distance, which grows with the number of dimensions, cosine similarity focuses only on the angle between vectors.
- **Learned Clustering:** In practice, embedding models are trained (using contrastive loss) to ensure that semantically similar items, while sparse, still form clusters with smaller angles, keeping their cosine similarity higher than random pairs.
- **Normalization:** Modern embedding APIs often normalize vectors (unit length), reducing the effect of vector magnitude differences. [3, 4, 9, 10, 11]

## Summary Table: Dimensionality Impact

| Factor [2, 3, 4] | Low Dimensions | High Dimensions |
|---|---|---|
| Cosine Similarity | Distinguishable | Tends to concentrate around a mean value |
| Vector Angles | Diverse | Mostly orthogonal (~90° or 0 similarity) |
| Data Structure | Dense | Sparse (points far apart) |

## When to Look Beyond Cosine Similarity

If you find that your model's, say, 1536-dimensional embeddings are giving you too many similar results, you might consider alternatives like using [Dimension Insensitive Euclidean Metric (DIEM)](https://arxiv.org/html/2407.08623v4) or, if you have trained the model with a specific distance metric in mind (e.g., Siamese networks), using that metric for retrieval. [3, 12, 13]

## References

1. https://stats.stackexchange.com/questions/341535/curse-of-dimensionality-does-cosine-similarity-work-better-and-if-so-why
2. https://milvus.io/ai-quick-reference/what-is-the-curse-of-dimensionality-and-how-does-it-affect-vector-search
3. https://www.linkedin.com/posts/anirshar_embedding-similarity-traps-cosine-isnt-activity-7403455176805957632-VQYC
4. https://x.com/rohanpaul_ai/status/1754190135359615327
5. https://community.openai.com/t/why-cosine-similarity-between-embedding-vectors-is-always-above-68/661144
6. https://www.linkedin.com/posts/anirshar_embedding-similarity-traps-cosine-isnt-activity-7403455176805957632-VQYC
7. https://www.youtube.com/watch?v=L9eNxU-9jBQ
8. https://community.openai.com/t/why-cosine-similarity-between-embedding-vectors-is-always-above-68/661144
9. https://www.ibm.com/think/topics/cosine-similarity
10. https://www.dataquest.io/blog/measuring-similarity-and-distance-between-embeddings/
11. https://arxiv.org/pdf/2504.16318
12. https://arxiv.org/html/2407.08623v4
13. https://www.emergentmind.com/topics/cosine-similarity-reflects-distance-hypothesis
