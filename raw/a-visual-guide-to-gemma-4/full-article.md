# A Visual Guide to Gemma 4

**Source URL**: https://newsletter.maartengrootendorst.com/p/a-visual-guide-to-gemma-4  
**Author**: Maarten Grootendorst (Google DeepMind)

Visual explainer for the Gemma 4 family (E2B, E4B, 31B dense, 26B A4B MoE): shared architecture (interleaved local/global attention, K=V on global layers, p-RoPE, vision encoder with variable aspect ratio and soft-token budget), MoE routing (128 experts, 8 active + shared expert), E2B/E4B per-layer embeddings (PLE) and audio encoder, and Multi-Token Prediction (MTP) drafters.

## MTP section (key points)

- Drafter for E2B: ~76M params, 4 layers, embedding dim 256 vs target 1536.
- Target activations concatenated with token embeddings, down-projected to drafter dim; round 1 uses target activations, later rounds use drafter's prior-step activations (up-projected).
- KV cache sharing: drafter cross-attends target's last local KV slice and global KV (last target layer is always global).
- Efficient embedder (E2B/E4B): vocabulary clustered; LM head predicts cluster logits first, then token logits within top clusters.

See full article HTML in `raw/a-visual-guide-to-gemma-4/full-article.html`.
