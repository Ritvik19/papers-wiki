# NVIDIA

**Type**: org  
**Tags**: #entity

## Overview

NVIDIA develops GPUs, inference stacks, and the **Nemotron** open model family. **Nemotron 3 Ultra** (550B/55B active Hybrid Mamba-Attention MoE) extends Nemotron 3 Super with 20T-token pre-training, 1M context, unified RLVR, and multi-teacher on-policy distillation.

## Appearances

- [[Papers Explained 580: Nemotron 3 Ultra]] — flagship Nemotron v3 agentic reasoning model.
- [[Papers Explained - Nemotron 3 Super]] — architectural predecessor at smaller scale.
- [[Papers Explained 518 - Nemotron Cascade]] — related Nemotron training lineage.
- [[Build a Domain-Specific Embedding Model in Under a Day]] — `nemotron embed` CLI recipe for fine-tuning Llama-Nemotron-Embed-1B-v2 on synthetic domain data.
- [[Welcome the NVIDIA Llama Nemotron Nano VLM to Hugging Face Hub]] — 8B document-intelligence VLM built on Llama-3.1-8B-Instruct and the C-RADIOv2-VLM-H vision backbone.
- [[StarCoder2 and The Stack v2]] — trained the flagship StarCoder2-15B model using NeMo on NVIDIA-accelerated infrastructure, as part of the BigCode collaboration.
- [[Apriel-H1: The Surprising Key to Distilling Efficient Reasoning Models]] — Nemotron-Nano-9B-v2 cited as a from-scratch-trained comparison point on the throughput/quality efficiency frontier (4.6x throughput at similar quality, at far higher training cost than ServiceNow's distillation approach).
- [[Efficient MultiModal Data Pipeline]] — nanoVLM's balanced knapsack packing strategy for multimodal batches is adapted from NVIDIA's Eagle 2 data-strategy paper.
- [[Nemotron 3.5 Content Safety: Customizable Multimodal Safety for Global Enterprise AI]] — 4B multimodal/multilingual safety classifier on a Gemma 3 base, with custom-policy enforcement and auditable THINK-mode reasoning traces.
- [[NVIDIA Cosmos Reason 2 Brings Advanced Reasoning to Physical AI]] — 2B/8B open reasoning VLM for robotics and physical AI, topping the Physical AI Bench and Physical Reasoning leaderboards.
- [[Introducing NVIDIA Nemotron 3 Nano Omni: Long-Context Multimodal Intelligence for Documents, Audio and Video Agents]] — hybrid Mamba-Transformer-MoE omni model adding document, audio, video, and agentic-computer-use understanding on top of the Nemotron 3 Nano backbone.
- [[The Open Evaluation Standard: Benchmarking NVIDIA Nemotron 3 Nano with NeMo Evaluator]] — publishes the full evaluation recipe/config behind Nemotron 3 Nano's model-card benchmark numbers via the open-source NeMo Evaluator library.
- [[Nemotron-Personas-India: Synthesized Data for Sovereign AI]] — 21M-persona synthetic dataset for Indic languages/demographics, built with NeMo Data Designer.
- [[NVIDIA Releases 6 Million Multi-Lingual Reasoning Dataset]] — Nemotron Post-Training Dataset v2, translating English reasoning data into five languages; co-announces Nemotron Nano 2 9B.
- [[Data for Agents]] — Nemotron team essay arguing agentic AI needs open (synthetic) data; introduces the Nemotron Post-Training v3 Prompt Atlas.
- [[Inkling]] — pretrained on NVIDIA GB300 NVL72; ships an [[NVFP4]] Blackwell inference checkpoint alongside BF16.
- [[Unsloth Training Efficiency and Kernels]] — NVIDIA collaboration post on packed-metadata caching, double-buffered checkpointing, and MoE bincount routing.
- [[What Even Is a Kernel?]] — discusses NVIDIA CUDA thread grids, warps, and HBM/GDDR memory traffic.
- [[Two Speeds of a GPU]] — benchmarks NVIDIA H100 SXM5 and RTX 4090 under the Roofline Model.

## Notes

LatentMoE and NVFP4 recipes shared across Nemotron 3 Super and Ultra technical reports.

## Related

- [[Mixture of Experts]]
- [[NVFP4]]
- [[GPU Inference Hardware]]
- [[GPU Kernel]]
- [[Roofline Model]]
- [[Arithmetic Intensity]]
- [[Agentic AI]]
