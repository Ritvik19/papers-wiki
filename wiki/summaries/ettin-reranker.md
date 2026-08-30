# Introducing the Ettin Reranker Family

**Source**: `raw/ettin-reranker/full-article.html` (490 KB), `raw/ettin-reranker/full-article.md`
**Ingested**: 2026-07-10
**Tags**: #summary

## Summary

Tom Aarsen releases six Sentence Transformers `CrossEncoder` rerankers, one per Ettin encoder size (17M to 1B parameters), trained with a single distillation recipe: pointwise MSE regression onto the raw logits of the 1.54B-parameter teacher `mxbai-rerank-large-v2`, over roughly 143M `(query, document, teacher_score)` triples drawn from LightOn's pre-training and fine-tuning embedding datasets. Only the learning rate and batch size change across the six sizes; everything else in the ~150-line training script is identical.

Architecturally, each reranker wraps its Ettin encoder backbone in a "headless" `Transformer` module (loading plain `AutoModel` rather than `AutoModelForSequenceClassification`) followed by CLS pooling, a Dense+GELU layer, LayerNorm, and a final scoring Dense layer. Loading through `AutoModel` rather than the sequence-classification wrapper is what lets the model propagate unpadded sequences through every layer when Flash Attention 2 is enabled, rather than only unpadding inside the attention op. That distinction is the source of most of the release's headline speed numbers: at 150M parameters, the Ettin reranker hits 3237 pairs/second on an H100 versus 1418-1404 for two architecturally identical ModernBERT-based peers (`gte-reranker-modernbert-base`, `granite-embedding-reranker-english-r2`) that load via `AutoModelForSequenceClassification` and therefore stay padded outside the attention kernel.

On quality, the six rerankers are state-of-the-art at their size class on MTEB(eng, v2) Retrieval and NanoBEIR: the 17M beats the 33M `ms-marco-MiniLM-L12-v2` by a wide margin at half the parameters, the 150M is the strongest sub-600M reranker tested, and the 1B comes within 0.0001 NDCG@10 of its 1.54B teacher while running at 2.4x the teacher's throughput. The post frames the whole release as a demonstration piece for the `train-sentence-transformers` Agent Skill shipped in Sentence Transformers v5.5.0, which an AI coding agent can install and use to bootstrap a similar training script.

| Reranker | Params | MTEB(eng, v2) NDCG@10 | H100 pairs/sec |
|---|---|---|---|
| mxbai-rerank-large-v2 (teacher) | 1.54B | 0.6115 | 387 |
| ettin-reranker-1b-v1 | 1.00B | 0.6114 | 928 |
| ettin-reranker-400m-v1 | 401M | 0.6091 | 1738 |
| ettin-reranker-150m-v1 | 151M | 0.5994 | 3237 |
| gte-reranker-modernbert-base | 150M | 0.5843 | 1418 |
| granite-embedding-reranker-english-r2 | 150M | 0.5656 | 1404 |
| ettin-reranker-68m-v1 | 68.6M | 0.5915 | 4913 |
| ms-marco-MiniLM-L12-v2 | 33.4M | 0.5066 | 3311 |
| ettin-reranker-17m-v1 | 17.6M | 0.5576 | 7517 |

Full source table has 23 rerankers total (including Qwen3-Reranker, jina-reranker-m0, BGE, and mxbai-v1 variants); rows above are the six Ettin sizes plus the teacher and the closest same-size peers cited in the post's text.

## Key Claims

- Distillation recipe: MSE loss on raw (unrescaled) logits from teacher `mxbai-rerank-large-v2`, trained on ~143M triples from `lightonai/embeddings-pre-training` (32 non-curated splits) plus a rescored subset of `lightonai/embeddings-fine-tuning` (7 splits, subsampled to 64 candidates/query via top-32 + 32 stratified sampling).
- MTEB(eng, v2) Retrieval NDCG@10 (mean over 6 embedder pairings): ettin-reranker-1b-v1 0.6114 (vs 0.6115 for the 1.54B teacher); ettin-reranker-400m-v1 0.6091; ettin-reranker-150m-v1 0.5994 (best under-600M reranker tested, beating Qwen3-Reranker-0.6B's 0.5940); ettin-reranker-17m-v1 0.5576 (beats 33.4M ms-marco-MiniLM-L12-v2's 0.5066 by +0.051 at half the params).
- Speed (H100, bf16, pairs/second): 17m = 7517, 32m = 6602, 68m = 4913, 150m = 3237, 400m = 1738, 1b = 928. The 1B model is 2.4x faster than its 1.54B teacher (928 vs 387 pairs/sec) at matching quality.
- Architecture ablation: going from `fp32+SDPA` to `bf16+FA2` with unpadded inputs is a 1.71x-8.26x speedup depending on model size; most of the speedup at large sizes comes from bf16 itself, and the unpadding step adds another 1.78x-2.45x on top of padded FA2.
- CLS pooling outperformed mean pooling in ablations, attributed to ModernBERT's alternating global/local attention pattern concentrating enough signal in the sparse global layers.
- All six models and the ~143M-row training dataset (`cross-encoder/ettin-reranker-v1-data`) are released under Apache 2.0.

## Figures

No figures were extracted for this ingest; the source article's MTEB bar charts (per-embedder-pairing NDCG@10) are referenced inline in the summary above but not downloaded, per this batch's no-figure-download policy. A condensed quality/speed table is preserved as markdown above.

## Entities

- [[Hugging Face]] — publishes the blog and hosts the Sentence Transformers library used throughout.
- [[Introducing the Ettin Reranker Family|Ettin Suite: SoTA Paired Encoders and Decoders]] (see [[Ettin Suite: SoTA Paired Encoders and Decoders]]) — the paired encoder/decoder suite whose encoders are the reranker backbones.
- IBM Granite (`granite-embedding-reranker-english-r2`) — one of the 150M-parameter speed/quality comparison peers; see [[IBM]] and [[Granite Embedding Multilingual R2]].
- Mixedbread AI (`mxbai-rerank-large-v2`) — the 1.54B teacher model distilled from; no dedicated entity page created.

## Questions & Gaps

- The post does not report results on RTEB's private-dataset split, so it's unclear whether the distillation recipe generalizes as well to held-out domains as it does to public MTEB benchmarks; see [[Introducing RTEB: A New Standard for Retrieval Evaluation]] for why that distinction matters.
- No ablation is given for training with a stronger or different teacher, though the author notes the recipe should transfer cleanly if a better teacher becomes available.

## Related

- [[Ettin Suite: SoTA Paired Encoders and Decoders]] — the encoder backbones these rerankers are built on.
- [[Introducing RTEB: A New Standard for Retrieval Evaluation]] — the open/private retrieval benchmark methodology relevant to evaluating reranker generalization.
- [[Granite Embedding Multilingual R2]] — IBM's competing 150M ModernBERT-based reranker peer cited in the speed/quality comparison.
- [[Papers Explained 277 - ModernBERT]] — architectural ancestor of the Ettin encoder backbones.
- [[Embedding and Retrieval]] — topic page for retrieval/reranking coverage.
- [[Hugging Face]]
