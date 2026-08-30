# Gemma4 Assistant Docs

**Source**: `raw/gemma4-assistant-docs/full-article.html` (333 KB)  
**URL**: https://huggingface.co/docs/transformers/main/en/model_doc/gemma4_assistant  
**Ingested**: 2026-07-12  
**Tags**: #summary

## Summary

Hugging Face Transformers documentation for **`Gemma4AssistantForCausalLM`**, the small text-only model that enables **Multi-Token Prediction (MTP)** speculative decoding with [[Gemma 4]] IT checkpoints (E2B, E4B, 31B, 26B-A4B). Pre-trained `-assistant` weights ship on the Hub for each target size.

Architecturally the assistant shares the `Gemma4TextModel` backbone but differs in four ways: **(1) full KV sharing** with the target (skips assistant prefill, reduces attention compute); **(2) constant `position_ids`** because the assistant cannot update the shared cache; **(3) inputs = concatenation of embeddings + target hidden states**, projected via `nn.Linear` into assistant space (definition of "last seen token" shifts between drafting rounds); **(4) cross-attention** so assistant queries attend to the target's shared KV values for accurate multi-token drafts.

`Gemma4AssistantConfig` exposes `backbone_hidden_size`, centroid parameters for the clustered LM head (`num_centroids=2048`, `centroid_intermediate_top_k=32` defaults), and `use_ordered_embeddings` for embedding-table alignment with the target.

## Key Claims

- `Gemma4AssistantForCausalLM` enables MTP via `model.generate(..., assistant_model=assistant_model)`.
- Assistant reuses target-populated KV cache entirely—no separate prefill phase.
- `position_ids` stay constant; assistant cannot append to shared KV.
- Forward input: concat(embedding, hidden_states) from last seen token, linearly projected to assistant dim.
- Cross-attention: assistant Q attends to target shared KV for context-aware drafting.
- Bidirectional attention masks used over shared KV (with SWA-specific mask flipping documented in API).
- Centroid-based LM head config: 2048 centroids, top-32 active by default (E2B/E4B efficient embedder).
- Supports multimodal targets via `AutoModelForImageTextToText` + assistant in pipeline examples.

## Figures

No images found in source.

## Entities

- [[Gemma 4]] — target model family.
- [[Hugging Face]] — Transformers library and Hub hosting.
- [[Gemma 4 MTP Transformers Guide]] — Google usage tutorial.
- [[Multi-Token Prediction]] — MTP concept.
- [[Speculative Decoding]] — inference technique.
- [[KV Cache]] — shared-cache mechanism.

## Questions & Gaps

- Does not list 12B assistant in overview bullet (Google docs include 12B); verify Hub availability.
- Implementation details of mask flipping for sliding-window attention are in source code, not fully explained in prose.
- `use_ordered_embeddings` reordering semantics need model-card cross-reference.

## Related

- [[Gemma 4 MTP Transformers Guide]] — end-to-end `generate()` tutorial.
- [[Gemma 4 MTP Overview]] — Google architecture overview.
- [[Gemma 4 Technical Report]] — training-side drafter description.
- [[Gemma 4 Multi-Token Prediction]] — release and ecosystem.
- [[Hugging Face]] — library and Hub.
- [[KV Cache]] — cache sharing in Gemma 4.
- [[Multi-Token Prediction]] — concept.
