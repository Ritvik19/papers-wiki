# Granite Embedding Multilingual R2

**Source**: `raw/granite-embedding-multilingual-r2/full-article.html` (243 KB), `raw/granite-embedding-multilingual-r2/full-article.md`
**Ingested**: 2026-07-10
**Tags**: #summary

## Summary

IBM releases two Apache 2.0 multilingual embedding models built on ModernBERT, replacing the XLM-RoBERTa-based Granite Embedding R1 line: `granite-embedding-311m-multilingual-r2` (311M params, 768-d, Matryoshka support) and `granite-embedding-97m-multilingual-r2` (97M params, 384-d). Both cover 200+ languages generally, with enhanced retrieval training for 52 languages plus 9 programming languages, and both extend context from R1's 512 tokens to 32,768 tokens (a 64x increase) via ModernBERT's alternating local/global attention and RoPE.

The two models use different tokenizers deliberately chosen for efficiency rather than reusing XLM-RoBERTa's 250K vocabulary: the 311M model uses the Gemma 3 tokenizer (262K tokens), while the 97M model starts from the GPT-OSS tokenizer and prunes it to a compact 180K-token vocabulary, trading a small amount of cross-lingual transfer capacity for a much smaller embedding table. Both models are trained via multi-teacher knowledge distillation (from Granite 3.3/4.1 Instruct and Mistral v0.2 Instruct decoders adapted for embeddings) followed by contrastive fine-tuning and checkpoint merging; the 311M model adds a fourth stage of Matryoshka Representation Learning so its 768-d output truncates to 512/384/256/128 dimensions with minimal quality loss (97%+ of full performance retained even at 128-d).

The headline number is the 97M model's 60.3 on MTEB Multilingual Retrieval (18 languages), a +9.4-point gap over the next-best sub-100M open model (`multilingual-e5-small` at 50.9), achieved at roughly one-third the size of the 311M model. Both models are explicitly positioned as enterprise drop-in replacements: no task-instruction prefix required, trained without MS-MARCO, IBM governance-reviewed training data, and one-line swaps into LangChain, LlamaIndex, Haystack, and Milvus.

## Key Claims

- MTEB Multilingual Retrieval (18 langs): granite-embedding-97m-multilingual-r2 60.3 (vs 50.9 for multilingual-e5-small, +9.4; vs 48.1 for its own R1 predecessor granite-embedding-107m-multilingual, +12.2); granite-embedding-311m-multilingual-r2 65.2 (#2 among open models under 500M; vs 52.2 for its R1 predecessor, +13.0).
- LongEmbed is the largest R1-to-R2 gain: +31.3 points (97M) and +34.0 points (311M), attributed directly to the 512-to-32K context window jump.
- Code retrieval: +19.7 (97M) and +15.3 (311M) over R1, from new code training data (Python, Go, Java, JavaScript, PHP, Ruby, SQL, C, C++).
- Matryoshka truncation (311M model): 768→256 dims loses only 0.5 points on MTEB Multilingual Retrieval (65.2→64.7) and 0.5 on Code (63.9→63.4); even at 128 dims (6x storage reduction) the model retains 63.7/62.3, over 97% of full-dimension performance.
- Cross-lingual retrieval (Belebele/MLQA): 311M model gains +4.3/+4.1 over its R1 predecessor; the 97M model trades off Belebele performance (52.9 vs R1's 55.1, -2.2) in exchange for its MTEB Multilingual Retrieval and LongEmbed gains, a direct consequence of the pruned 180K vocabulary and reduced 12-layer depth.
- Encoding throughput on H100 (512-token chunks): 97M model >2,500 docs/sec (comparable to multilingual-e5-small); 311M model ~1,800 docs/sec, beating jina-embeddings-v5-text-nano's retrieval quality (65.2 vs 63.3) at 5.5x+ the encoding speed.
- 97M model weights: 195 MB safetensors (less than half of the widely-used `paraphrase-multilingual-MiniLM-L12-v2` at 471 MB), 98 MB quantized ONNX.

| Model | Params | MTEB Multilingual (18) | Code (12) | English Retrieval (10) | LongEmbed (6) |
|---|---|---|---|---|---|
| multilingual-e5-small | 118M | 50.9 | 53.5 | 46.5 | 38.8 |
| granite-embedding-107m-multilingual (R1) | 107M | 48.1 | 40.7 | 47.9 | 34.3 |
| jina-embeddings-v5-text-nano | 212M | 63.3 | 71.2 | 58.8 | 63.6 |
| embeddinggemma-300m | 308M | 62.5 | 68.7 | 54.6 | 55.4 |
| granite-embedding-278m-multilingual (R1) | 278M | 52.2 | 48.5 | 51.5 | 37.7 |
| **granite-embedding-97m-multilingual-r2** | 97M | 60.3 | 60.4 | 50.1 | 65.6 |
| **granite-embedding-311m-multilingual-r2** | 311M | 65.2 (#2) | 63.8 (#3) | 52.6 (#5) | 71.7 (#1) |

Full source table has 15 models including F2LLM-v2-80M, harrier-oss-v1-270m, gte-multilingual-base, snowflake-arctic-embed-m-v2.0, multilingual-e5-large/base, and OpenAI's text-embedding-3-small; rows above are the R1 predecessors plus the closest-sized open competitors.

## Figures

No figures were extracted for this ingest; the source article's architecture diagram, speed-vs-quality scatter plot, and Matryoshka degradation chart are referenced inline in the summary above but not downloaded, per this batch's no-figure-download policy. A condensed model-comparison table is preserved as markdown above.

## Entities

- [[IBM]] — releasing organization; Granite model family.
- [[Hugging Face]] — hosts the blog, model weights, and a live demo Space.
- [[Papers Explained 277 - ModernBERT]] — the encoder architecture both R2 models are built on.

## Questions & Gaps

- The blog reports the 97M model does not support Matryoshka truncation ("384 dimensions is already compact") without detailing why the training recipe excluded it, unlike the 311M model.
- The GneissWeb pretraining corpus and IBM's governance/filtering pipeline are referenced but not detailed in this post; a separate technical report is linked for full methodology.
- No comparison is given against the Ettin or mmBERT encoder families, IBM's closest open-data ModernBERT-style peers in the same size range.

## Related

- [[Introducing the Ettin Reranker Family]] — competing 150M ModernBERT-based reranker (`granite-embedding-reranker-english-r2`) cited in that post's speed comparison.
- [[Papers Explained 465 - EmbeddingGemma]] — competing sub-500M multilingual embedding model cited in the R2 benchmark table (embeddinggemma-300m, 62.5 MTEB Multilingual Retrieval).
- [[Papers Explained 96 - Matryoshka Representation Learning]] — the truncatable-embedding technique used by the 311M model.
- [[Papers Explained 277 - ModernBERT]] — architectural ancestor.
- [[Embedding and Retrieval]] — topic page for retrieval model coverage.
- [[IBM]]
- [[Hugging Face]]
