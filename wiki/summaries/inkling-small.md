# Inkling-Small

**Source**: `raw/inkling-small/full-article.html`, `raw/inkling-small/full-article.md` (secondary); `raw/thinkingmachines-inkling/full-article.html` (Small deployment sections)  
**URLs**: https://thinkingmachines.ai/news/inkling-small/ · https://huggingface.co/blog/thinkingmachines-inkling  
**Ingested**: 2026-07-31  
**Tags**: #summary

## Summary

Inkling-Small is [[Thinking Machines Lab]]'s efficient open-weights model in the Inkling family, released July 30, 2026. It is a sparse [[Mixture of Experts]] with **276B total / 12B active** parameters — roughly one-quarter the size of [[Inkling]] (975B / 41B active) — trained on NVIDIA GB300 NVL72 systems. It shares Inkling's encoder-free multimodal architecture, [[Controllable Thinking Effort]], and 1M-token context window, but targets workloads where cost and latency matter more than maximum knowledge coverage.

Inkling-Small began training after Inkling, letting Thinking Machines improve the pretraining data mix and ML recipe. Post-training used **[[On-Policy Distillation]]** from Inkling as teacher on an earlier preview checkpoint, followed by two weeks of scaled agentic coding RL. The result surpasses Inkling on several reasoning and agentic coding benchmarks while Inkling retains advantages on knowledge and factuality (especially SimpleQA Verified).

Full weights are on Hugging Face; the model is available for fine-tuning on [[Tinker]] and for text/image/audio chat on Tinker Playground. Output pricing is **$1.20 / 1M tokens** vs Inkling's **$4.05 / 1M tokens**.

## Key Claims

- 276B total / 12B active MoE; same multimodal encoder-free stack as Inkling (dMel audio, 40×40 hMLP image patches).
- Training improvements: better pretrain recipe; on-policy distillation from Inkling teacher; +2 weeks agentic coding RL after preview checkpoint.
- Beats Inkling on reasoning/agentic: HLE text-only **31.6%** vs 29.7%; SWE-Bench Verified **80.2%** vs 77.6%; IFBench **82.2%** vs 79.8%.
- Inkling retains factuality edge: SimpleQA Verified **43.9%** vs Inkling-Small **20.6%**.
- Strong multimodal audio: Audio MC **54.9%**, VoiceBench **90.1%**, MMAU **77.0%** — competitive with Inkling at lower cost.
- Token-efficiency: among the most efficient open-weights models on GDPval-AA v2, τ³-Banking, AA-Briefcase, and CritPt Pareto frontiers.
- Safety inherited from Inkling: StrongREJECT **98.4%**, FORTRESS adversarial **71.6%**, FORTRESS benign **96.9%**.
- Deployment (HF blog): Inkling-Small BF16 ~600 GB VRAM (8× H200); NVFP4 ~180 GB (1× B300 W4A4 or 2× H200 W4A16); Inference Endpoints one-click deploy up to ~160 TPS.

## Training

Inkling-Small's training pipeline reflects lessons from the larger model:

1. **Pretraining** — improved data mix and recipe relative to Inkling's initial run.
2. **On-policy distillation** — Inkling-Small (preview) checkpoint post-trained with Inkling as same-family teacher ([[On-Policy Distillation]]).
3. **Agentic coding RL** — two additional weeks scaling coding/agent RL from the distilled checkpoint.

This same-family distillation is effective because teacher and student share tokenizer, vocabulary, and training recipe, making per-token log-probability signals directly comparable.

## vs Inkling

| Dimension | Inkling-Small | Inkling |
|-----------|---------------|---------|
| Params (active / total) | 12B / 276B | 41B / 975B |
| HLE (text only) | 31.6% | 29.7% |
| SWE-Bench Verified | 80.2% | 77.6% |
| Terminal-Bench 2.1 | 64.7% | 63.8% |
| IFBench | 82.2% | 79.8% |
| SimpleQA Verified | 20.6% | 43.9% |
| VoiceBench | 90.1% | 91.4% |
| Output price / 1M tokens | $1.20 | $4.05 |

Inkling-Small's effort-sweep curves sit above Inkling's on Terminal-Bench 2.1, HLE, and IFBench across all thinking budgets, indicating better performance-per-compute rather than only peak-effort wins.

## Capabilities

**Reasoning and agentic tasks.** Matches or exceeds Inkling on HLE at every thinking budget; >80% SWE-Bench Verified; strong token-efficiency on agentic reasoning benchmarks.

**Multimodality.** Same natively multimodal stack as Inkling; improved Python-assisted visual reasoning (crop/zoom/programmatic inspection). Nearly matches Inkling on most multimodal evals at lower cost.

**Epistemics.** Matches Inkling on ForecastBench and Prophet Arena calibration; same censorship-resistance and instruction-following training.

**Safety.** Same post-training safety recipe and pre-deployment red-teaming as Inkling.

## Benchmarks (effort=0.99)

| Category | Benchmark | Inkling-Small |
|----------|-----------|---------------|
| Model info | AA Index v4.1 | 40.0% |
| Agentic coding | SWE-Bench Verified | 80.2% |
| Agentic coding | SWE-Bench Pro (public) | 55.9% |
| Agentic coding | Terminal-Bench 2.1 | 64.7% |
| Agentic general | GDPval-AA v2 | 1269 |
| Agentic general | MCP Atlas (public) | 79.6% |
| Reasoning | HLE (text only) | 31.6% |
| Reasoning | HLE (with tools) | 47.8% |
| Reasoning | GPQA Diamond | 89.5% |
| Reasoning | AIME 2026 | 95.5% |
| Reasoning | ARC-AGI-2 | 40.1% |
| Factuality | SimpleQA Verified | 20.6% |
| Chat | IFBench | 82.2% |
| Vision | MMMU Pro (Standard 10) | 74.0% |
| Vision | CharXiv RQ (with python) | 81.3% |
| Audio | Audio MC | 54.9% |
| Audio | VoiceBench | 90.1% |
| Safety | FORTRESS (adversarial) | 71.6% |
| Safety | StrongREJECT | 98.4% |

All evals at effort 0.99, temperature 1.0; coding evals with 256K max-token trajectory limit.

## Figures

| Figure | Caption | Source |
|--------|---------|--------|
| ![fig-1](../assets/inkling-small/fig-1.png) | Release announcement cover | inkling-small |

TML announcement charts (spider plot, effort-sweep TFLOPs/cost curves, token-efficiency Pareto plots) are interactive in the HTML source and were not extracted as static images.

## Entities

- [[Thinking Machines Lab]] — trained and released Inkling-Small.
- [[Inkling]] — larger sibling and on-policy distillation teacher.
- [[Tinker]] — fine-tuning platform and Playground for Inkling-Small.
- [[On-Policy Distillation]] — key post-training method from Inkling teacher.

## Questions & Gaps

- SimpleQA gap vs Inkling reflects an intentional efficiency/knowledge tradeoff; whether further RL or distillation can close it without losing efficiency is unknown.
- τ³-Banking (15.5%) still trails Inkling (23.7%) and some peers — agentic finance remains a relative weakness.
- Video OOTB performance, like Inkling, is untested at release.
- HF blog notes MXFP8 and NVFP4 weight variants; independent latency benchmarks across quantization formats are not yet published.

## Related

- [[Inkling]] — larger family member; teacher for on-policy distillation; stronger factuality.
- [[On-Policy Distillation]] — Inkling→Inkling-Small same-family distillation example.
- [[Controllable Thinking Effort]] — shared effort knob across the family.
- [[Tinker]] — fine-tuning and Playground access.
- [[Model Compression and Efficiency]] — MoE sparsity and distillation for smaller deployable models.
- [[Mixture of Experts]] · [[Reasoning Models]] · [[Audio Models]] · [[Code Models]] · [[Evaluation and Benchmarks]]
