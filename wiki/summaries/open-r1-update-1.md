# Open R1: Update #1

**Source**: `raw/open-r1-update-1/full-article.md` (316 KB), `raw/open-r1-update-1/full-article.md`
**Ingested**: 2026-07-10
**Tags**: #summary

## Summary

First progress report on [[Open-R1: A Fully Open Reproduction of DeepSeek-R1]], one week into the project. On evaluation, the team reproduced DeepSeek's MATH-500 numbers reasonably closely across the R1-Distill model family using `lighteval`, and published an evaluation leaderboard so the community could track reproduction progress. A key observation: DeepSeek-R1's reasoning traces in the OpenThoughts dataset average roughly 6,000 tokens, with some exceeding 20,000, which makes both evaluation and GRPO training expensive, since long completions need a lot of GPU memory for activations and gradients during the optimization step.

On the training side, GRPO landed in TRL 0.14, integrated with DeepSpeed ZeRO 1/2/3 for scaling and vLLM for fast generation (the main bottleneck in online RL). On synthetic data generation, the team found that naive vLLM batched inference on 2x8 H100 nodes only sustained 8 parallel requests before the KV cache filled up and triggered preemption; switching to 4x8 H100 nodes freed enough VRAM for 32 parallel requests, and switching from batched to streaming request submission (capping active requests at 500, launching new ones as soon as one finished) stabilized GPU utilization substantially.

The post also surveys the broader reaction to DeepSeek-R1: market and AI-lab commentary on the training-cost claim (several independent estimates suggested the ~$5.5M figure was the right order of magnitude), speculation (unconfirmed at the time) about training-data provenance, and a wave of community reproduction efforts including Will Brown's minimal Llama-1B GRPO run, TinyZero's sub-$30 "aha moment" reproduction with a 3B model, and several new open reasoning datasets (Bespoke-Stratos-17k, OpenThoughts-114k, Dolphin-R1, R1-Distill-SFT, Sky-T1_data_17k, Magpie-Reasoning-V2).

## Key Claims

- MATH-500 reproduction (HF lighteval vs. DeepSeek reported): Qwen-1.5B 81.6 vs 83.9, Qwen-7B 91.8 vs 92.8, Qwen-14B 94.2 vs 93.9, Qwen-32B 95.0 vs 94.3, Llama-8B 85.8 vs 89.1, Llama-70B 93.4 vs 94.5.
- DeepSeek-R1 responses in OpenThoughts average ~6,000 tokens, with some exceeding 20,000 tokens (10+ pages), stressing both eval and GRPO training memory budgets.
- GRPO shipped in TRL 0.14 with DeepSpeed ZeRO 1/2/3 and vLLM generation support.
- Switching vLLM inference from 2 to 4 nodes of 8xH100 raised sustainable parallel requests from 8 to 32 by freeing KV-cache headroom; switching from batched to streaming request submission further stabilized GPU utilization.
- Independent back-of-envelope estimates from multiple researchers suggested DeepSeek's reported ~$5.5M training cost for V3/R1 was the right order of magnitude, though unverified pending full reproduction.

## Figures

No figures were extracted for this ingest; the MATH-500 comparison table above is preserved as markdown, and the response-length distribution chart is described inline but not downloaded, per this batch's no-figure-download policy.

## Entities

- [[Hugging Face]] — publishes the update and runs the open-r1 project.
- [[DeepSeek]] — creator of DeepSeek-R1, the model being reproduced.

## Questions & Gaps

- The post does not resolve the media speculation about DeepSeek's training-data provenance, only notes it was circulating.
- No final numbers yet on GRPO training memory reduction techniques; the post flags them as "limitations... ongoing" without specifics.

## Related

- [[Open-R1: A Fully Open Reproduction of DeepSeek-R1]] — project announcement this update reports progress against.
- [[Open R1: Update #2]] — next update, covering the OpenR1-Math-220k dataset.
- [[GRPO]]
- [[Reasoning Models]]
- [[Reinforcement Learning Topic]]
