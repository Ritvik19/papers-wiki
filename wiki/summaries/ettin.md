# Ettin Suite: SoTA Paired Encoders and Decoders

**Source**: `raw/ettin/full-article.md` (365 KB), `raw/ettin/full-article.md`
**Ingested**: 2026-07-10
**Tags**: #summary

## Summary

Ettin is a suite from JHU CLSP that trains encoder-only and decoder-only models in pairs, at six matched sizes (17M, 32M, 68M, 150M, 400M, 1B), on identical data (2T open tokens), identical architecture, and identical training recipe. The only difference between an encoder and its decoder twin is the attention pattern (bidirectional vs causal) and the training objective (masked language modeling vs causal language modeling). This is the first controlled apples-to-apples comparison between the two architecture families: every prior encoder-vs-decoder comparison confounded the question by using different data, shapes, or recipes.

The recipe builds directly on ModernBERT (three-phase pre-training/context-extension/decay schedule, unpadded attention, RoPE, GeGLU), but unlike ModernBERT, every data source used for Ettin is public and reproducible. Applying the recipe to encoders beats ModernBERT at every size; applying the identical recipe to decoders produces models that beat Llama 3.2 1B and SmolLM2 at comparable sizes. Both outcomes come from the same 2T-token mixture and training loop, isolating the architecture choice as the variable of interest.

With that controlled setup, the authors also test what happens when you flip an architecture's objective: continuing to pretrain an encoder with a causal objective (or a decoder with MLM, the LLM2Vec-style recipe) for 50B additional tokens. The cross-objective models are consistently weaker than their native counterparts, and the decoder-from-encoder conversion is particularly poor at larger sizes. The paper's headline finding is that architecture, not just objective, drives which tasks a model is good at: encoders keep a lasting edge on classification/retrieval and decoders keep a lasting edge on generation, even when every other factor is held constant.

## Key Claims

- Ettin encoders outperform ModernBERT at every one of the six matched sizes (17M-1B) while training on fully open data; ModernBERT's data pipeline was not public.
- Ettin decoders outperform or match Llama 3.2 1B and SmolLM2 at comparable sizes, with the largest gains on knowledge-intensive tasks like SciQ.
- Controlled comparison at fixed data/recipe: a 150M encoder (89.2 MNLI) beats a 400M decoder (88.2 MNLI) on classification; decoders keep a widening lead on generation as scale increases. A 400M encoder beats a 1B decoder on classification, and a 400M decoder beats a 1B encoder on generation, i.e. size alone doesn't erase the architecture gap.
- Cross-objective training (LLM2Vec-style encoder-from-decoder, and the reverse decoder-from-encoder) underperforms native training in both directions; the gap is worse for decoder-from-encoder at larger scale.
- On WinoGender bias probes, encoders prefer gender-neutral pronouns more often than decoders (60%+ vs 30%+ neutral); both show male bias, decoders more so.
- 250+ intermediate training checkpoints are released publicly for studying training dynamics.

## Figures

No figures were extracted for this ingest; the source article's images (attention-pattern diagrams, size/data charts, and benchmark comparison plots) are referenced inline in the summary text above but not downloaded, per this batch's no-figure-download policy.

## Entities

- [[Hugging Face]] — hosts the blog post, model weights, and the collection page.
- Johns Hopkins University Center for Language and Speech Processing (JHU CLSP) — the authoring lab (Orion Weller, Kathryn Ricci, Marc Marone, Antoine Chaffin, Dawn Lawrie, Ben Van Durme); no dedicated entity page created, tracked via [[Papers Explained 277 - ModernBERT]] lineage instead.
- [[Papers Explained 277 - ModernBERT]] — the architecture and training recipe Ettin directly builds on and beats.
- [[Papers Explained 187a - Llama 3]] — one of the decoder baselines Ettin decoders beat.
- [[Papers Explained 176 - Smol LM]] — SmolLM2 is the other decoder baseline Ettin decoders beat.

## Questions & Gaps

- The blog does not report absolute compute cost (GPU-hours) for the full six-size suite, only that all sizes share the same 2T-token recipe.
- It is unclear whether the cross-objective conversion gap is inherent to the objective mismatch or an artifact of only training for 50B additional tokens; the authors note the decoder-to-encoder conversion used MLM rather than LLM2Vec's proposed MNTP, which may explain part of the gap.
- No comparison is given against very recent encoder baselines beyond ModernBERT (e.g. no EuroBERT or mmBERT comparison in this post).

## Related

- [[Introducing the Ettin Reranker Family]] — Sentence Transformers CrossEncoder rerankers built on top of the Ettin encoders.
- [[Papers Explained 471 - mmBERT]] — sibling JHU CLSP project ("mmBERT: ModernBERT goes Multilingual") extending the same ModernBERT-style recipe to multilingual pretraining.
- [[Papers Explained 277 - ModernBERT]] — architectural and training-recipe ancestor.
- [[Papers Explained 176 - Smol LM]] — SmolLM2 decoder baseline.
- [[Papers Explained 187a - Llama 3]] — Llama 3.2 decoder baseline.
- [[Embedding and Retrieval]] — topic page for encoder/retrieval model coverage.
- [[Hugging Face]]
