# Build a Domain-Specific Embedding Model in Under a Day

**Source**: `raw/domain-specific-embedding-finetune/full-article.md` (221 KB), `raw/domain-specific-embedding-finetune/full-article.md`
**Ingested**: 2026-07-10
**Tags**: #summary

## Summary

NVIDIA publishes an end-to-end recipe, packaged as a `nemotron embed` CLI, for turning a directory of unlabeled domain documents into a fine-tuned, deployed embedding model on a single GPU in under a day, with no manual labeling required. The pipeline chains together several NVIDIA open-source projects: NeMo Data Designer for synthetic query-passage generation, a custom hard-negative-mining step, NeMo Automodel for contrastive fine-tuning, BEIR for evaluation, and NeMo Export-Deploy plus NVIDIA NIM for ONNX/TensorRT export and production serving. The worked example fine-tunes NVIDIA's own `Llama-Nemotron-Embed-1B-v2` model.

The core insight is that most teams have no labeled (query, relevant document) pairs, and labeling one by hand is slow and inconsistent. The pipeline instead uses an LLM (`nvidia/nemotron-3-nano-30b-a3b`) to read document chunks and synthesize QA pairs directly, tagging each with a query type (contextual vs multi-hop), reasoning type, complexity level (2-5), and a quality sub-score; only pairs above a quality threshold are kept. Multi-hop questions, which require connecting information across 2-3 passages, are deliberately generated alongside simple factual questions, then "unrolled" into one training example per (query, positive-document) pair so the contrastive loss sees each positive independently.

Hard negatives are mined by embedding the full corpus with the base model, computing query-passage similarity, masking out labeled positives, applying a 95%-of-minimum-positive-score exclusion margin (to avoid selecting unlabeled documents that are actually correct), and keeping the top-5 remaining near-misses per query. Fine-tuning then uses a biencoder with contrastive loss at an aggressive temperature of 0.02, chosen because the hard negatives are already confusing enough that the model needs strong gradients to separate them. On NVIDIA's own public-documentation synthetic benchmark, the recipe produces a ~10% relative improvement in NDCG@10 and Recall@10; Atlassian's independent application of the same recipe to a JIRA dataset raised Recall@60 from 0.751 to 0.951 (a 26.7% relative gain) on a single A100.

## Key Claims

- Full pipeline (SDG → hard-negative mining → fine-tune → eval → export → deploy) runs in six CLI commands and completes in under a day on one GPU; a small corpus (~500 documents) completes in 2-3 hours end-to-end.
- Hard-negative mining uses a 95%-of-minimum-positive-score margin filter to exclude candidate negatives that are likely unlabeled true positives, then keeps the top-5 scoring survivors per query as hard negatives (default).
- Multi-hop questions (1-3 hops) are generated alongside single-hop factual questions and unrolled into independent (query, positive) training pairs, teaching the model that multiple passages can all be relevant to one complex query.
- Contrastive fine-tuning uses temperature 0.02 (aggressive/sharp), 1e-5 learning rate, global batch size 128, and 5 passages per query (1 positive + 4 hard negatives) as defaults; the docs note 3 epochs is tuned for the small example dataset and most real-world data needs only 1-2 epochs to avoid overfitting.
- On the released `nvidia/Retrieval-Synthetic-NVDocs-v1` benchmark: NDCG@10 improved from 0.55506 to 0.61559 (+10.9%), Recall@10 from 0.62979 to 0.69296 (+10.0%), comparing base vs fine-tuned `Llama-Nemotron-Embed-1B-v2`.
- Atlassian case study: fine-tuning the same base model on a Jira dataset on one A100 80GB raised Recall@60 from 0.751 to 0.951, a 26.7% relative improvement, described in a companion Atlassian blog post on their Rovo search product.
- Deployment exports to ONNX (opset 17) and optionally TensorRT (with FP8 quantization option), served behind an OpenAI-compatible `/v1/embeddings` endpoint via NVIDIA NIM; a verification step re-runs the BEIR evaluation against the deployed endpoint to catch accuracy regressions from quantization/export (tolerance: 0.03 at @1, 0.01 at @5+).

## Figures

No figures were extracted for this ingest; the source article's SDG pipeline diagram and contrastive-learning diagram are referenced inline in the summary above but not downloaded, per this batch's no-figure-download policy. The before/after benchmark numbers are preserved as text/markdown above.

## Entities

- [[NVIDIA]] — publishing organization; Nemotron model and NeMo tooling family.
- [[Hugging Face]] — hosts the blog post and the referenced `nvidia/llama-nemotron-embed-1b-v2` model and `nvidia/Retrieval-Synthetic-NVDocs-v1` dataset.

## Questions & Gaps

- The post does not report absolute BEIR scores for the base `Llama-Nemotron-Embed-1B-v2` model against other embedding models of similar size, only relative before/after gains from this specific fine-tuning recipe.
- No comparison is given between this synthetic-QA-generation approach and other domain-adaptation strategies (e.g. continued pretraining, distillation from a larger teacher) for the same task.
- The Atlassian case study is summarized secondhand from a companion Atlassian blog post that was not separately ingested.

## Related

- [[Embedding and Retrieval]] — topic page for retrieval/fine-tuning coverage.
- [[Papers Explained 392 - Hard Negative Mining for Domain-Specific Retrieval]] — related prior work on hard-negative mining for enterprise/domain-specific retrieval.
- [[NVIDIA]]
- [[Hugging Face]]
