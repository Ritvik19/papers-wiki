# Gemma 4 MTP Transformers Guide

**Source**: `raw/gemma-4-mtp-transformers-guide/full-article.md` (157 KB)  
**URL**: https://ai.google.dev/gemma/docs/mtp/mtp  
**Ingested**: 2026-07-12  
**Tags**: #summary

## Summary

Google's hands-on guide for running **Gemma 4 Multi-Token Prediction (MTP)** with **Hugging Face Transformers**. Each Gemma 4 IT target checkpoint (E2B, E4B, 12B, 31B, 26B-A4B) has a matching `-assistant` drafter: a lightweight 4-layer MTP head that proposes candidate tokens while the target verifies them in parallel.

Usage is minimal: load both models with `AutoModelForCausalLM`, then pass `assistant_model=assistant_model` to `target_model.generate()`. The drafter proposes **N** tokens autoregressively; the target accepts high-probability drafts and rejects from the first mismatch onward, always emitting one additional token per verification pass. Draft length is tunable via `num_assistant_tokens` and `num_assistant_tokens_schedule` (`"heuristic"` adapts length up on full acceptance, down on any rejection; `"constant"` keeps a fixed draft count).

## Key Claims

- Target + assistant pairing: `google/gemma-4-{size}-it` + `google/gemma-4-{size}-it-assistant`.
- MTP enabled by a single `assistant_model=` argument to `generate()`.
- Verification loop: drafter proposes N tokens → target verifies in one forward pass → accept prefix → target always adds one more token.
- More draft tokens: higher speedup potential when acceptance is high, but more wasted compute on rejection.
- Fewer draft tokens: higher acceptance rate but less speedup from the drafter.
- `num_assistant_tokens_schedule="heuristic"`: auto-increase draft length by 2 on full accept, decrease by 1 on any reject.

## Figures

No images found in source.

## Entities

- [[Gemma 4]] — target model family.
- [[Gemma 4 MTP Overview]] — architectural overview companion doc.
- [[Gemma4 Assistant Docs]] — `Gemma4AssistantForCausalLM` class reference.
- [[Hugging Face]] — Transformers library and model hosting.
- [[Multi-Token Prediction]] — MTP concept.
- [[Speculative Decoding]] — underlying inference technique.

## Questions & Gaps

- Colab notebook output in source may be stale; model IDs should be verified against current Hub releases.
- Does not document vLLM/SGLang server flags (mentioned in launch blog, not this page).
- Assistant model naming ("drafter" vs "assistant") used interchangeably in Google docs.

## Related

- [[Gemma 4 MTP Overview]] — architecture and MoE batching notes.
- [[Gemma4 Assistant Docs]] — forward-pass details (shared KV, cross-attention, centroid LM head).
- [[Gemma 4 Multi-Token Prediction]] — release announcement and ecosystem backends.
- [[Gemma 4 Technical Report]] — training-side drafter spec.
- [[Hugging Face]] — model hosting and Transformers integration.
- [[Inference Engineering]] — speculative decoding production guidance.
