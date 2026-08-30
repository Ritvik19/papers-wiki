# Gemma 4 MTP Overview

**Source**: `raw/gemma-4-mtp-overview/full-article.html` (136 KB)  
**URL**: https://ai.google.dev/gemma/docs/mtp/overview  
**Ingested**: 2026-07-12  
**Tags**: #summary

## Summary

Google's official overview of **Multi-Token Prediction (MTP)** in [[Gemma 4]]: MTP is the architecture that enables efficient [[Speculative Decoding]] at inference. A small draft model proposes multiple future tokens; the heavy target model verifies them in one parallel forward pass. Rejected drafts still yield the correct token at that position, so no compute is wasted.

Gemma 4's drafter is tightly coupled to the target: it **shares the input embedding table** and builds on **last-layer activations** (concatenated with token embeddings, then down-projected). Output quality is **identical** to standard autoregressive generation. Three named enhancements improve draft quality and speed: shared embeddings, target-activation reuse, and an **efficient clustered embedder** (E2B/E4B only) that avoids full-vocabulary logit computation.

The doc also explains why **26B-A4B MoE** drafters may not speed up at batch size 1: different drafted tokens can route to different experts, forcing extra weight loads; higher batch sizes increase expert overlap and restore gains.

## Key Claims

- MTP in Gemma 4 = speculative decoding with a coupled draft model, not an independent small LLM.
- Draft model shares target input embeddings and last-layer activations; guarantees exact same output quality as autoregressive decoding.
- Dense targets verify multiple drafts with minimal overhead (same weights per token).
- MoE 26B-A4B: expert routing per drafted token can offset gains at batch size 1; batching improves expert reuse.
- E2B/E4B efficient embedder: cluster vocabulary, predict top clusters first, restrict final logits to tokens in selected clusters.

## Figures

No images found in source.

## Entities

- [[Gemma 4]] — model family MTP accelerates.
- [[Gemma 4 Multi-Token Prediction]] — launch blog for MTP drafter release.
- [[Multi-Token Prediction]] — concept hub for coupled draft-head training.
- [[Speculative Decoding]] — verify-and-accept inference paradigm.
- [[Mixture of Experts]] — MoE-specific batching caveat for 26B-A4B drafters.
- [[Google DeepMind]] — Gemma inference documentation.

## Questions & Gaps

- Does not specify drafter layer counts, dimensions, or parameter counts (see [[Gemma 4 Technical Report]]).
- No code examples (see [[Gemma 4 MTP Transformers Guide]]).
- Clustered embedder details are qualitative; full cluster count and top-k not in this page.

## Related

- [[Gemma 4 MTP Transformers Guide]] — Hugging Face usage and draft-length scheduling.
- [[Gemma 4 Technical Report]] — canonical Section 2.6 drafter architecture spec.
- [[Gemma 4 Multi-Token Prediction]] — May 2026 launch announcement and benchmarks.
- [[Gemma4 Assistant Docs]] — `Gemma4AssistantForCausalLM` API reference.
- [[A Visual Guide to Gemma 4]] — illustrated MTP section with activation and KV-cache flow.
- [[Gemma 4 MTP Explained in 5 Minutes]] — third-party contrast with EAGLE and DeepSeek V3.
- [[Multi-Token Prediction]] — concept overview.
- [[Speculative Decoding]] — general inference acceleration paradigm.
