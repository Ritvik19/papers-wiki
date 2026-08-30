# Gemma 3n fully available in the open-source ecosystem!

**Source**: `raw/gemma3n/full-article.html` (272 KB), `raw/gemma3n/full-article.md`
**Ingested**: 2026-07-10
**Tags**: #summary

## Summary

Gemma 3n is Google's natively multimodal, on-device Gemma variant, announced as a preview at Google I/O and released in full on Hugging Face with day-0 support across `transformers`, `timm`, MLX, llama.cpp (text only), Transformers.js, Ollama, and Google AI Edge. Unlike Gemma 3, it accepts image, text, audio, and video inputs directly, and it is built specifically to run on consumer hardware rather than a datacenter GPU.

Two sizes ship, each in base and instruct form: `gemma-3n-E2B` and `gemma-3n-E4B`. The `E` stands for "Effective": the models have 5B and 8B real parameters respectively, but memory-efficiency techniques let them run in as little as 2GB and 3GB of GPU RAM, the footprint of a 2B and 4B model. That gap between real and effective parameter count comes from two architecture choices. MatFormer is a nested transformer design, similar in spirit to Matryoshka embeddings, where E2B is trained as a literal sub-model of E4B; the two are trained together, and users can mix and match layers from either to hit a specific hardware budget. Per-Layer Embeddings (PLE) offload embedding tables to CPU memory, which is why E2B's 5B real parameters cost about as much GPU memory as a 2B model.

The multimodal side runs through a new MobileNet-v5-300 vision encoder (300M parameters, added to `timm`) that hits 60 FPS on a Google Pixel while using a third of the parameters of ViT-Giant, and an audio encoder based on the Universal Speech Model that processes audio in 160ms chunks for speech-to-text and translation. A shared KV cache across modalities gives 2x faster prefill on long audio/video inputs compared to Gemma 3 4B. The release also ships ONNX weights for `gemma-3n-E2B-it` for Transformers.js, and free Colab notebooks (including an audio-specific one) for fine-tuning.

## Key Claims

- E4B is the first sub-10B model to score 1300+ on LMArena.
- E2B runs in as little as 2GB of GPU RAM; E4B in 3GB, despite having 5B/8B real parameters, via MatFormer nesting plus Per-Layer Embedding CPU offload.
- MobileNet-v5-300 (300M params) hits 60 FPS on a Google Pixel and outperforms ViT-Giant while using 3x fewer parameters; supports 256x256, 512x512, and 768x768 resolutions.
- KV Cache Sharing across the audio/video pipeline gives 2x faster prefill versus Gemma 3 4B.
- Multilingual support: 140 languages for text, 35 languages for multimodal interaction.
- llama.cpp support is text-only at launch; full multimodal (vision/audio) support ships through MLX, transformers, and Google AI Edge instead.

## Figures

No figures were extracted for this ingest; the source article's MatFormer/PLE architecture diagrams and benchmark charts are referenced inline in the summary above but not downloaded, per this batch's no-figure-download policy.

## Entities

- [[DeepMind]] — Google's AI research org; Gemma model family.
- [[Hugging Face]] — hosts the blog, model weights, and `transformers`/`timm` integrations.

## Questions & Gaps

- The post does not give exact MMLU numbers for E4B/E2B or the Mix-n-Match intermediate configurations, only that they are "competitive."
- No direct benchmark comparison is given against Gemma 3's text-only line at a matched effective parameter count.
- The relationship between Gemma 3n's MatFormer/PLE efficiency techniques and later Gemma releases is not discussed in this post.

## Related

- [[Papers Explained 329 - Gemma 3]] — the prior Gemma generation this model builds efficiency techniques on top of.
- [[nanoVLM: The simplest repository to train your VLM in pure PyTorch]] — cites Gemma 3n as a contemporaneous small-VLM release from the same period.
- [[Vision Language Models]] — topic page for multimodal model coverage.
- [[DeepMind]]
- [[Hugging Face]]
