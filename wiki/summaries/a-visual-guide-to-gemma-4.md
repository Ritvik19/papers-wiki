# A Visual Guide to Gemma 4

**Source**: `raw/a-visual-guide-to-gemma-4/full-article.html` (783 KB)  
**URL**: https://newsletter.maartengrootendorst.com/p/a-visual-guide-to-gemma-4  
**Ingested**: 2026-07-12  
**Tags**: #summary

## Summary

Maarten Grootendorst's illustrated Substack guide to the **Gemma 4** family (E2B, E4B, 31B dense, 26B A4B MoE), published at Gemma 4 launch (Apr 2026). Covers shared architecture innovations vs Gemma 3—**5:1 local-to-global attention** (4:1 on E2B) with the **last layer always global**, **K=V** on global layers, **p-RoPE** (p=0.25), **grouped-query attention** (8 queries per KV head on global layers), vision encoder with **variable aspect ratio** (2D RoPE) and **soft-token budgets** (70–1120), **MoE** routing (128 experts, 8 active + 3× shared expert), E2B/E4B **per-layer embeddings** (PLE) stored in flash, and a **305M audio conformer** encoder.

A dedicated **MTP section** explains speculative decoding: the E2B drafter (~76M params, 4 layers, dim 256) reuses **target activations** (concat + down-project), **cross-attends the target KV cache** (local slice + global KV), shares the embedding table, and uses a **clustered LM head** on E2B/E4B. Updated May 2026 with the MTP drafter section.

## Key Claims

- Four launch sizes: E2B (2B effective), E4B (4B effective), 31B dense, 26B A4B MoE (4B active).
- Global attention efficiency: K=V, p-RoPE, 8:1 GQA on global layers, doubled key dimension.
- Vision: adaptive resize preserving aspect ratio; 3×3 patch pooling to soft-token budget; 150M ViT (edge) / 550M (large).
- MoE: 128 routed experts, 8 active per token, plus always-on shared expert (3× size).
- PLE: per-layer 256-dim lookup tables in flash; gating + projection between decoder blocks.
- MTP drafter: target last-layer activations + token embeddings → down-project; KV cache sharing eliminates drafter prefill; clustered vocab for fast LM head on edge drafters.

## Figures

No images extracted (article contains ~300 Substack CDN figures; not bulk-downloaded).

## Entities

- [[Maarten Grootendorst]] — author; Google DeepMind, Gemma 4 core contributor.
- [[Gemma 4]] — model family explained.
- [[Google DeepMind]] — research org.
- [[Mixture of Experts]] — 26B A4B architecture.
- [[Multi-Token Prediction]] — MTP drafter section.
- [[Papers Explained 193 - BERTopic]] — author's prior work (BERTopic creator).

## Questions & Gaps

- Figures not mirrored locally; read online or see [[Gemma 4 Technical Report]] Figure 1 for MTP diagram.
- 12B encoder-free variant covered in a follow-up post (Gemma 4 12B visual guide), not this article.
- Independent explainer; cross-check numeric claims against [[Gemma 4 Technical Report]].

## Related

- [[Gemma 4]] — launch blog.
- [[Gemma 4 Technical Report]] — formal architecture and benchmark tables.
- [[Gemma 4 Multi-Token Prediction]] — MTP drafter release.
- [[Gemma 4 MTP Overview]] — Google MTP docs.
- [[Gemma 4 12B]] — follow-on mid-size variant.
- [[Maarten Grootendorst]] — author entity.
- [[Mixture of Experts]] — MoE details.
- [[Multi-Token Prediction]] — MTP concept.
