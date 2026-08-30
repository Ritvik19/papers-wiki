# Kimina-Prover-RL

**Source**: `raw/kimina-prover-rl/full-article.html` (236 KB), `raw/kimina-prover-rl/full-article.md`
**Ingested**: 2026-07-10
**Tags**: #summary

## Summary

AI-MO releases `kimina-prover-rl`, a slimmed-down, fully open-source training pipeline for formal theorem proving in Lean 4 that reproduces the core methodology behind [[Kimina-Prover: Applying Test-Time RL Search on Large Formal Reasoning Models]] with full compatibility with the open-source Verl RL framework (the complete recipe ships as a fork, in `recipe/kimina-prover-rl`). The approach follows a DeepSeek-R1-inspired two-stage output structure: a natural-language reasoning trace inside `<think>` tags, followed by Lean 4 code, separating planning from execution to improve explainability, error recovery, and generalization. Two released checkpoints, `AI-MO/Kimina-Prover-RL-1.7B` (76.63% Pass@32 on MiniF2F) and `AI-MO/Kimina-Prover-RL-0.6B` (71.30% Pass@32), are both new state-of-the-art for open-source models in their size classes.

Training uses GRPO via Verl: the model generates N outputs per prompt, and each output receives a reward of 1 if its Lean code verifies successfully against `kimina-lean-server` (a new open-source, high-throughput parallel Lean 4 proof-checking server, paired with a lightweight `kimina-client` Python package for interacting with it). Two additional reward components matter for training stability: a format-checking reward and an error-correction turn. The format reward requires exactly one `<think>` block and one Lean code block, rejects repetitive/hallucinated reasoning lines, checks that reasoning contains enough non-comment tactic-level content, thresholds comment density in both reasoning and code to penalize boilerplate, checks semantic alignment between tactics described in the reasoning and the tactics actually used in the Lean code (via IoU/subcode-coverage matching), and penalizes unnecessarily long responses; malformed outputs get zero reward regardless of whether the proof itself is valid. The error-correction mechanism stores failed rollouts (prompt, response, Lean feedback) and creates a new training sample explicitly prompting the model to revise its previous attempt using the compiler's feedback, capped at one fix-turn per failure with a token-length cap on the injected error message.

Training data is `Kimina-Prover-Promptset`, a filtered/augmented subset of `NuminaMath-LEAN` (referred to as NuminaMath-LEAN-RL): easy problems (historical win rate above 0.5) are removed, Gemini generates problem variants for diversity, and hard problems are duplicated to weight them more heavily. Because GRPO training was found to bias toward artificially longer responses (especially for incorrect outputs, per "Understanding R1-Zero-Like Training: A Critical Perspective"), the pipeline uses DrGRPO instead of vanilla GRPO, normalizing token-level losses by a global constant to remove the length bias. Starting from `AI-MO/Kimina-Prover-Distill-1.7B` (itself fine-tuned from Qwen3-1.7B on cold-start data from the 72B Kimina-Prover), training on 8 H100 GPUs for 48 hours (256 samples/step, half error-correction samples, 8 rollouts/sample, 2048 generations/step) raised accuracy from a starting point to 70% best@8 (74% after the error-fix turn) by step 85, with format errors decreasing and average output length increasing over training.

## Key Claims

| Model | Pass@32 | Pass@32 with error fixing |
|---|---|---|
| Kimina-Prover-Distill-1.7B | 72.95% | 75.41% |
| Kimina-Prover-RL-1.7B | 76.23% | 77.87% |

| Model | Pass@32 |
|---|---|
| Kimina-Prover-Distill-0.6B | 68.85% |
| Kimina-Prover-RL-0.6B | 71.30% |
- DrGRPO (global-constant loss normalization) is used instead of vanilla GRPO specifically to counteract GRPO's known bias toward longer responses on incorrect outputs.
- Format-checking reward covers block structure, repetition/hallucination detection, comment-density thresholds, and reasoning-to-code tactic alignment (IoU/subcode matching); malformed outputs get zero reward regardless of proof validity.
- Training setup: 8 H100 GPUs, 48 hours, 256 samples/step (half error-correction), 8 rollouts/sample (2048 generations/step), evaluated every 5 steps via best@8.
- Full training recipe, `kimina-lean-server` (parallel Lean 4 verification), and `kimina-client` (PyPI package) are released open-source.

## Figures

No figures were extracted for this ingest; the accuracy-over-training-steps and format-error-rate charts are described inline but not downloaded, per this batch's no-figure-download policy. Benchmark tables above are preserved as markdown.

## Entities

- [[Numina]] — AI-MO/Project Numina, publisher of this pipeline and the underlying Kimina-Prover models.
- [[Hugging Face]] — hosts the blog post and model releases.

## Questions & Gaps

- The post does not report results scaling beyond 8 GPUs or beyond the 1.7B parameter size; the 72B Kimina-Prover-72B RL results from the original paper are not reproduced here.
- No comparison is given between DrGRPO and vanilla GRPO on this exact setup; the length-bias justification is cited from prior work rather than an ablation in this post.

## Related

- [[Kimina-Prover: Applying Test-Time RL Search on Large Formal Reasoning Models]] — the larger model and TTRL Search framework this pipeline distills a simplified, open-source training recipe from.
- [[GRPO]]
- [[Reasoning Models]]
- [[Reinforcement Learning Topic]]
