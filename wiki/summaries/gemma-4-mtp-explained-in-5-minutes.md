# Gemma 4 MTP Explained in 5 Minutes

**Source**: `raw/gemma-4-mtp-explained-in-5-minutes/full-article.md` (231 KB)  
**URL**: https://tianhaozhou.medium.com/gemma-4-mtp-explained-in-5-minutes-0b12ad381240  
**Ingested**: 2026-07-12  
**Tags**: #summary

## Summary

Jackson MZ's short explainer contrasts **Gemma 4 MTP** with popular speculative-decoding baselines (**DeepSeek V3**, **EAGLE-3**). Gemma 4 uses **shared weights** for autoregressive multi-token drafting (not one token per MTP module) and **cross-attends the main model's KV cache** rather than attending to raw hidden states.

Implementation highlights: the drafter pulls the target's latest-layer KV cache, combines it with draft token embeddings, and runs autoregressive draft steps **without maintaining its own KV cache**—each draft step depends only on the previous draft token's projected activation, not a growing self-attention history. Per-layer customizations include pre/post projection between target and draft dimensions and a **bidirectional attention mask** over the target KV (implementation convenience, not seq2seq). A **hierarchical LM head** clusters the vocabulary and computes logits only for top-K clusters.

## Key Claims

- Gemma 4 MTP = speculative decoding with a lightweight drafter verifying against the heavy target.
- vs DeepSeek V3 / EAGLE-3: shared-weight autoregressive drafting; attends target KV cache, not hidden states.
- Drafter has **no independent KV cache**; draft trajectory tracked via projected activations only.
- Bidirectional mask lets draft queries attend to full target KV in one shot.
- Hierarchical LM head: second-level vocab clusters reduce logit compute for small drafters.
- KV-cache sharing eliminates drafter prefill—major efficiency win at inference.

## Figures

No images extracted (Medium member-gated figures not downloadable from HTML export).

## Entities

- [[Gemma 4]] — model family discussed.
- [[Gemma 4 Multi-Token Prediction]] — Google's official MTP release.
- [[EAGLE (Speculative Decoding)]] — contrast baseline (EAGLE-3).
- [[DeepSeek]] — contrast baseline (DeepSeek V3 MTP).
- [[Multi-Token Prediction]] — concept.
- [[Speculative Decoding]] — technique.

## Questions & Gaps

- Diagrams reference external blog (heji-study-blog.web.app); not ingested here.
- Author is independent (ex-Google/DeepMind); not a primary Google source—cross-check against [[Gemma 4 Technical Report]].
- Member-only Medium figures unavailable in raw HTML.

## Related

- [[Gemma 4 MTP Overview]] — official architecture summary.
- [[Gemma 4 Technical Report]] — canonical drafter spec (Section 2.6).
- [[A Visual Guide to Gemma 4]] — illustrated MTP walkthrough from Google DeepMind.
- [[Gemma4 Assistant Docs]] — Transformers implementation details.
- [[EAGLE (Speculative Decoding)]] — related draft-from-hidden-states approach.
- [[Multi-Token Prediction]] — concept hub.
- [[Speculative Decoding]] — inference paradigm.
