# Introducing NVIDIA Nemotron 3 Nano Omni: Long-Context Multimodal Intelligence for Documents, Audio and Video Agents

**Source**: [HF Blog](https://huggingface.co/blog/nvidia/nemotron-3-nano-omni-multimodal-intelligence) ([raw](/raw/nemotron-3-nano-omni-multimodal-intelligence/full-article.md))
**Published**: April 28, 2026
**Ingested**: 2026-07-10
**Tags**: #summary

## Summary

NVIDIA Nemotron 3 Nano Omni extends the Nemotron multimodal line from a vision-language model into a full text+image+video+audio system, adding document analysis, automatic speech recognition, long audio-video understanding, and agentic computer use on top of general reasoning. It builds on [[Papers Explained 521 - Nemotron Nano V2 VL]] and the [[Papers Explained 506 - Nemotron 3 Nano]] backbone, combining a hybrid Mamba-Transformer Mixture-of-Experts language model with a C-RADIOv4-H vision encoder and a Parakeet-TDT-0.6B-v2 audio encoder. NVIDIA reports best-in-class accuracy on document benchmarks (MMLongBench-Doc, OCRBenchV2), leads on video/audio benchmarks (WorldSense, DailyOmni, VoiceBench), and up to 9.2x higher system throughput than comparable open omni models at a fixed per-user interactivity threshold.

## Architecture

The model uses a unified encoder-projector-decoder design: the Nemotron 3 Nano 30B-A3B language backbone, paired with C-RADIOv4-H for vision and Parakeet-TDT-0.6B-v2 for audio, each connected through a lightweight 2-layer MLP projector, with vision, audio, and text tokens interleaved and processed jointly inside the backbone.

- **Hybrid Mamba-Transformer-MoE backbone**: 23 Mamba selective state-space layers for efficient long-context processing, 23 MoE layers (128 experts, top-6 routing, plus a shared expert), and 6 grouped-query attention layers for global interaction.
- **Dynamic resolution vision**: replaces the v2 model's tiling strategy with native-aspect-ratio processing using 16x16 patches, from a minimum of 1,024 to a maximum of 13,312 patches per image (roughly 512x512 to 1840x1840 for square images).
- **Conv3D temporal compression**: fuses each pair of consecutive video frames into a single "tubelet" before the ViT, halving the vision-token count for a given frame budget (or doubling frame coverage for a given token budget).
- **Efficient Video Sampling (EVS)**: an inference-time step that keeps the first frame in full and, for subsequent frames, retains only tokens where the video content changes, dropping static, redundant tokens; combined with Conv3D for further compression.
- **Native audio input**: Parakeet-TDT-0.6B-v2 processes 16 kHz audio (trained on inputs up to 1,200 seconds/20 minutes; the LLM's context supports 5+ hours), enabling audio, vision, and text tokens to be modeled jointly rather than pre-transcribing audio to text.

## Training

SFT runs on NVIDIA H100 clusters (32 to 128 nodes depending on stage) using Megatron-LM, Transformer Engine, and Megatron Energon, with tensor/expert/sequence/context parallelism, online sequence packing, and selective activation recomputation. Post-SFT RL uses NeMo-RL and NeMo Gym on a Megatron backend, run on a Ray-based distributed setup across B200 and H100 clusters with multimodal deduplication so repeated rollouts don't multiply image/video/audio memory.

- **Text RL**: trained across diverse NeMo-Gym environments evaluating tool calling, code writing, and multi-part planning against verifiable criteria.
- **Omni RL**: trains reasoning jointly across images, video, audio, and text, from single-modality to fully multimodal tasks, using a verifier suite spanning multiple-choice, math, GUI grounding, and ASR formats, including intentionally unanswerable cases so the model learns to abstain rather than hallucinate.
- **Synthetic document data**: ~11.4M synthetic QA pairs (~45B tokens) were generated from real-world PDFs using NeMo Data Designer to strengthen long-context document reasoning, contributing a reported 2.19x accuracy improvement on MMLongBench-Doc.

## Benchmark highlights

| Task | Benchmark | Nemotron 3 Nano Omni | Nemotron Nano V2 VL | Qwen3-Omni 30B-A3B |
|---|---|---|---|---|
| Document understanding | OCRBenchV2-En | **65.8** | 61.2 | - |
| Document understanding | MMLongBench-Doc | **57.5** | 38.0 | 49.5 |
| Document understanding | CharXiv reasoning | **63.6** | 41.3 | 61.1 |
| GUI | ScreenSpot-Pro | 57.8 | 5.5 | **59.7** |
| GUI | OSWorld | **47.4** | 11.0 | 29.0 |
| Video understanding | Video-MME | **72.2** | 63.0 | 70.5 |
| Video + audio | WorldSense | **55.4** | - | 54.0 |
| Video + audio | DailyOmni | **74.1** | - | 73.6 |
| Voice interaction | VoiceBench | **89.4** | - | 88.8 |
| ASR | HF Open ASR (lower is better) | **5.95** | - | 6.55 |

Compared to other open omni models at matched interactivity, NVIDIA reports 7.4x higher system efficiency for multi-document use cases and 9.2x higher for video use cases.

## Key Claims

- Delivers best-in-class accuracy on MMLongBench-Doc and OCRBenchV2 among the compared models, and leads WorldSense/DailyOmni for video+audio and VoiceBench for voice interaction.
- Ranks as the most cost-efficient open video understanding model on MediaPerf, per NVIDIA's framing (specific MediaPerf numbers are not given in the post itself).
- ~11.4M synthetic document QA pairs generated via NeMo Data Designer yield a 2.19x accuracy improvement on MMLongBench-Doc.
- Loses to Qwen3-Omni 30B-A3B specifically on GUI grounding (ScreenSpot-Pro: 57.8 vs. 59.7), the one benchmark in the comparison table where it does not lead.
- Checkpoints ship in BF16, FP8, and NVFP4; NVIDIA open-sources substantial parts of the training code (Megatron-Bridge, NeMo-RL guide, NeMo Data Designer SDG recipes).

## Figures

No figures were extracted for this ingest, per this batch's no-figure-download policy; referenced figures (architecture diagram, efficiency plots, example screenshots) are described inline above but not downloaded.

## Entities

- [[NVIDIA]] — develops Nemotron 3 Nano Omni and the surrounding Nemotron/NeMo tooling (Megatron-LM, NeMo-RL, NeMo Data Designer, Megatron Energon).
- [[Hugging Face]] — hosts the model checkpoints, dataset, and blog post.

## Questions & Gaps

- The MediaPerf "most cost-efficient" claim and some benchmark comparisons (e.g. against other open omni models for the 7.4x/9.2x efficiency figures) are not broken out in a table the post shows directly; they are asserted rather than fully tabulated in-line.
- No ablation is given isolating the individual contribution of Conv3D compression vs. EVS pruning to the reported efficiency gains.

## Related

- [[Papers Explained 521 - Nemotron Nano V2 VL]] — the vision-language predecessor this model extends into full omni-modality.
- [[Papers Explained 506 - Nemotron 3 Nano]] — the text backbone (30B-A3B hybrid Mamba-Transformer-MoE) this model builds on.
- [[Welcome the NVIDIA Llama Nemotron Nano VLM to Hugging Face Hub]] — an earlier, smaller NVIDIA document-intelligence VLM using an earlier C-RADIO vision encoder.
- [[The Open Evaluation Standard: Benchmarking NVIDIA Nemotron 3 Nano with NeMo Evaluator]] — NeMo Evaluator reproducibility methodology, from the same Nemotron 3 Nano family.
- [[Data for Agents]] — same NVIDIA Nemotron team's broader argument for open data underlying models like this one.
