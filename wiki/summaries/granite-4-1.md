# Granite 4.1 LLMs: How They're Built

**Source**: `raw/granite-4-1/full-article.md` (194 KB), `raw/granite-4-1/full-article.md`
**Ingested**: 2026-07-10
**Tags**: #summary

## Summary

IBM's technical walkthrough of Granite 4.1, a family of dense, decoder-only LLMs at 3B, 8B, and 30B parameters, trained from scratch on roughly 15 trillion tokens and released under Apache 2.0. The architecture is a standard dense transformer (Grouped Query Attention, RoPE, SwiGLU, RMSNorm, shared input/output embeddings), differing across the three sizes only in embedding size, layer count, and MLP width. Pretraining runs a five-phase pipeline: Phase 1 (10T tokens, general web/code/math mix), Phase 2 (2T tokens, sharply increased math/code proportion), Phase 3 and 4 (2T + 0.5T tokens of "high-quality data annealing" that blends in chain-of-thought and instruction data with decaying learning rates), and Phase 5, a staged long-context extension (4K -> 32K -> 128K -> 512K) using progressively more book/code-repository data, with model merging after each stage to preserve short-context performance.

Supervised fine-tuning uses roughly 4.1M curated samples filtered through an LLM-as-Judge pipeline that scores only the assistant's response (treating system prompts, retrieved documents, and tool outputs as context) across six weighted dimensions: instruction following, correctness, completeness, conciseness, naturalness, and calibration. Hard-reject rules for hallucination, false premise, or incorrect computation override the score. A separate rule-based pipeline handles structural filtering (truncation, schema validation, leakage detection, global deduplication). Reinforcement learning then runs as a four-stage sequential pipeline using on-policy GRPO with DAPO loss: multi-domain RL (joint training across 9 domains including math, Text2SQL, and temporal reasoning, to minimize catastrophic forgetting), RLHF (generic-chat reward-model tuning, +18.9 points average AlpacaEval improvement), identity/knowledge-calibration RL (~40 steps), and a dedicated Math RL stage that recovers the math-benchmark regression the RLHF stage otherwise causes.

The headline result: the dense 8B instruct model matches or exceeds the previous-generation Granite 4.0-H-Small, a 32B-parameter Mixture-of-Experts model with 9B active parameters, across IFEval, AlpacaEval, MMLU-Pro, BBH, GSM8K, DeepMind-Math, EvalPlus, ArenaHard, BFCL v3, and MBPP(+), despite using a simpler, smaller dense architecture. FP8-quantized variants are also released, cutting disk footprint and GPU memory roughly in half via weight/activation-only quantization on transformer linear layers.

## Key Claims

- Instruct benchmarks (3B / 8B / 30B): MMLU-Pro 49.83 / 55.99 / 64.09; IFEval avg 82.30 / 87.06 / 89.65; AlpacaEval 2.0 38.57 / 50.08 / 56.16; GSM8K 86.88 / 92.49 / 94.16; BFCL v3 60.80 / 68.27 / 73.68.
- RULER long-context benchmark on base models at 128K: 3B 58.0, 8B 73.0, 30B 76.7 (context extended via Phase 5 LCE to 512K).

| RULER (base models) | 32K | 64K | 128K |
|---|---|---|---|
| granite-4.1-3b-base | 75.0 | 66.6 | 58.0 |
| granite-4.1-8b-base | 83.6 | 79.1 | 73.0 |
| granite-4.1-30b-base | 85.2 | 84.6 | 76.7 |

| Instruct benchmark | 3B | 8B | 30B |
|---|---|---|---|
| MMLU (5-shot) | 67.02 | 73.84 | 80.16 |
| MMLU-Pro (5-shot, CoT) | 49.83 | 55.99 | 64.09 |
| BBH (3-shot, CoT) | 75.83 | 80.51 | 83.74 |
| GPQA (0-shot, CoT) | 31.70 | 41.96 | 45.76 |
| AlpacaEval 2.0 | 38.57 | 50.08 | 56.16 |
| IFEval avg | 82.30 | 87.06 | 89.65 |
| ArenaHard | 37.80 | 68.98 | 71.02 |
| GSM8K (8-shot) | 86.88 | 92.49 | 94.16 |
| DeepMind Math (0-shot, CoT) | 64.64 | 80.07 | 81.93 |
| HumanEval+ (pass@1) | 74.39 | 80.49 | 85.98 |
| BFCL v3 | 60.80 | 68.27 | 73.68 |
| SALAD-Bench (safety) | 93.95 | 95.80 | 96.41 |

Full source table covers 30 benchmarks across general, alignment, math, code, tool-calling, multilingual, and safety categories; rows above are the ones most representative of each category.
- Granite 4.1-8B (dense) matches or beats Granite 4.0-H-Small (32B-A9B MoE) across nearly every benchmark cited, despite far fewer active parameters.
- RLHF stage caused an average math-benchmark regression that the dedicated Math RL stage reversed and then exceeded: +3.8 points average on GSM8K, +23.48 points average on DeepMind-Math over the SFT checkpoint.
- SFT training used 16 nodes x 4 GB200 GPUs, 3 epochs, 5e-6 learning rate, 16,384-token sequences, ~4.1M total samples.
- Trained on an NVIDIA GB200 NVL72 cluster (CoreWeave), with 72-GPU NVLink intra-rack domains and non-blocking fat-tree NDR 400 Gb/s InfiniBand inter-rack.
- Supports 12 languages: English, German, Spanish, French, Japanese, Portuguese, Arabic, Czech, Italian, Korean, Dutch, Chinese.

## Figures

No figures were extracted for this ingest; the five-phase pretraining pipeline diagram, SFT data-quality-pipeline diagram, RL pipeline diagram, and 8B-vs-32B-MoE comparison chart are described inline above but not downloaded, per this batch's no-figure-download policy. All benchmark tables are preserved as markdown above.

## Entities

- [[IBM]] — releasing organization; Granite model family.
- [[Hugging Face]] — hosts the blog and model weights.

## Questions & Gaps

- The post cites "PRISM: Demystifying Retention and Interaction in Mid-Training" (arXiv 2603.17074) as a resource but doesn't explain how PRISM's findings specifically shaped the Phase 3/4 annealing design.
- DAPO loss and on-policy GRPO are cited from Yu et al. 2025 and Shao et al. 2024 respectively, but the post doesn't detail why dynamic sampling (part of standard DAPO) was disabled for compute reasons, beyond a brief mention.
- No comparison is given against Granite 4.0's dense (non-hybrid) siblings, only against the hybrid-SSM Granite 4.0-H-Small MoE.

## Related

- [[Granite 4.0 Nano: Just How Small Can You Go?]] — sibling release in the same Granite 4.0/4.1 family, targeting sub-1B/edge deployment instead of the 3B-30B dense range covered here.
- [[Granite Embedding Multilingual R2]] — uses Granite 4.1 Instruct as one of its multi-teacher distillation sources for embedding training.
- [[GRPO]] — the RL algorithm (with DAPO loss) underlying Granite 4.1's multi-stage RL pipeline.
- [[IBM]]
- [[Large Language Models]]
- [[Long Context]]
- [[Reinforcement Learning Topic]]
