# Papers Explained 574: Jina Embeddings v5 Omni

**Source**: `raw/2026-06-04_Papers-Explained-574--Jina-Embeddings-v5-Omni-1a08a156e52e.md`  
**Paper**: https://arxiv.org/abs/2605.08384  
**Ingested**: 2026-06-13  
**Tags**: #summary

## Summary

**GELATO** (Geometry-preserving Embeddings via Locked Aligned TOwers) extends **Jina Embeddings v5 Text** into **jina-embeddings-v5-omni**, encoding text, image, audio, and video in one semantic space. Frozen scale-matched **Qwen3.5** vision encoders and **Qwen2.5-Omni** audio encoders attach to the same text backbone; only **fc_vision_2**, **fc_audio**, and modality delimiter embeddings train per task (retrieval, text-matching, clustering, classification).

![GELATO architecture](../assets/papers-explained-574-jina-embeddings-v5-omni/fig-2.webp)

The text path is unchanged from v5 Text: token embeddings → frozen transformer → inherited task LoRA → last-token pooling → L2 norm. Vision uses LayerNorm, 2×2 spatial merge (pixel-unshuffle), and two FC layers; audio maps 1280-d encoder output into 1024-d (small) or 768-d (nano) text space. Mixed-modality inputs concatenate text spans and modality segments in document order; videos can prepend an audio track before per-frame visual segments.

Training uses bidirectional in-batch **InfoNCE** with **Matryoshka** prefix losses (τ = 0.02). On open-weight omni models under 5B, **jina-embeddings-v5-omni-small** leads overall four-modality score (**53.93**), best text-only performance, and strong image/audio—though **video** lags baselines. **ViDoRe** document retrieval: small **79.08**, nano **70.05** (beats LanguageBind at its size).

## Key Claims

- Locked aligned towers preserve text embedding geometry while adding vision/audio/video.
- Perceptual-only encoders (SigLIP2, Whisper-large) are avoided in favor of language-aligned multimodal encoders.
- Only projectors + delimiters train; backbone, encoders, and inherited LoRA stay frozen.
- Small model is strongest sub-5B omni embedder on combined MIEB / MMEB-Video / MAEB / MMTEB-style subsets.
- Video retrieval is the main weakness vs larger omni baselines.

## Figures

| Figure | Caption | Page |
|--------|---------|------|
| ![fig-1](../assets/papers-explained-574-jina-embeddings-v5-omni/fig-1.webp) | Title card: Jina Embeddings v5 Omni. | Header |
| ![fig-2](../assets/papers-explained-574-jina-embeddings-v5-omni/fig-2.webp) | Architecture of jina-embeddings-v5-omni. | Architecture |
| ![fig-3](../assets/papers-explained-574-jina-embeddings-v5-omni/fig-3.webp) | Image input sequence construction. | Input sequence |
| ![fig-4](../assets/papers-explained-574-jina-embeddings-v5-omni/fig-4.webp) | Audio input sequence construction. | Input sequence |
| ![fig-5](../assets/papers-explained-574-jina-embeddings-v5-omni/fig-5.webp) | Video frame concatenation. | Input sequence |
| ![fig-6](../assets/papers-explained-574-jina-embeddings-v5-omni/fig-6.webp) | Video with audio track prefix. | Input sequence |
| ![fig-7](../assets/papers-explained-574-jina-embeddings-v5-omni/fig-7.webp) | InfoNCE + Matryoshka training objective. | Training |
| ![fig-8](../assets/papers-explained-574-jina-embeddings-v5-omni/fig-8.webp) | Matryoshka loss sum over prefix dimensions. | Training |
| ![fig-9](../assets/papers-explained-574-jina-embeddings-v5-omni/fig-9.webp) | Open-weight omni model scores on selected subsets. | Evaluation |
| ![fig-10](../assets/papers-explained-574-jina-embeddings-v5-omni/fig-10.webp) | ViDoRe document-retrieval scores. | Evaluation |
| ![fig-11](../assets/papers-explained-574-jina-embeddings-v5-omni/fig-11.webp) | Main benchmark results table. | Evaluation |

## Entities

- [[Jina AI]] — authors of GELATO and the v5 Omni embedding family.
- [[Embedding and Retrieval]] — primary application domain for unified multimodal search.

## Questions & Gaps

- Why video underperforms despite strong document-image retrieval—frame sampling vs temporal modeling?
- Comparison to closed Gemini Embedding 2 on identical benchmark splits not in this explainer.

## Related

- [[Embedding and Retrieval]]
- [[Vision Language Models]]
- [[Multilingual Models]]
- [[Papers Explained 575: Gemini Embedding 2]] — competing native multimodal embedding approach.
