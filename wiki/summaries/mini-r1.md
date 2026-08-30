# Mini-R1: Reproduce Deepseek R1 "Aha Moment", a RL Tutorial

**Source**: `raw/mini-r1/full-article.html` (176 KB), `raw/mini-r1/full-article.md`
**Ingested**: 2026-07-10
**Tags**: #summary

## Summary

A tutorial by Philipp Schmid, cross-posted to the Open-R1 blog, reproducing a small-scale version of DeepSeek-R1's reported "aha moment" (where pure RL teaches a model to reevaluate and extend its own reasoning without supervision) using GRPO and the Countdown Game: given a target number and a set of drawn numbers, combine them with +, -, x, / to reach or approach the target. The setup trains Qwen2.5-3B-Instruct on the `Jiayi-Pan/Countdown-Tasks-3to4` dataset with TRL's `GRPOTrainer`, distributed across 4x H100 80GB GPUs using DeepSpeed for training and vLLM for generation (one GPU reserved for vLLM generation, the rest for training). Two rule-based rewards are used: a format reward checking for `<think>...</think><answer>...</answer>` structure, and an accuracy reward checking that the equation in `<answer>` uses each available number exactly once and evaluates to the target.

Training ran for 450 steps (~6 hours). By step 50 the model had learned the correct output format; by step 100 it solved ~25% of puzzles and began "reasoning" in natural language; by step 200 performance reached ~40% but the model's reasoning style shifted from word-based explanation toward a more programmatic trial-and-error pattern (trying combinations, checking results, adjusting); by step 450 it reached ~50% success while keeping the step-200-era format. The post offers several hypotheses for the shift toward programmatic-style reasoning (base model too small/weak, imperfectly specified reward functions incentivizing a shorter reward-hacking-adjacent strategy, or the narrow single-task training domain naturally converging on the most efficient solving strategy) without settling on one. Starting hyperparameters from the DeepSeekMath paper (LR 1e-6, KL beta 0.04) caused instability after ~150 steps; reducing to LR 5e-7 and beta 0.001 (informed by OpenRLHF) stabilized training.

## Key Claims

- Setup: Qwen2.5-3B-Instruct, TRL `GRPOTrainer`, DeepSpeed + vLLM, 4x H100 80GB, ~45-60s per step, 450 steps (~6 hours total).
- Format reward checks `<think>...</think><answer>...</answer>` structure; accuracy reward checks the equation uses each drawn number exactly once and evaluates to the target.
- Training progression: correct format by ~50 steps; ~25% success and word-based reasoning by 100 steps; ~40% success and a shift to programmatic trial-and-error reasoning by 200 steps; ~50% success by 450 steps, still improving slowly.
- Original DeepSeekMath hyperparameters (LR 1e-6, KL beta 0.04) were unstable after ~150 steps; reducing to LR 5e-7 and beta 0.001 fixed this.
- `num_generations` was fixed at 8 rather than the DeepSeekMath paper's 64, due to compute constraints; the effect of increasing it was not tested.

## Figures

No figures were extracted for this ingest; the GRPO diagram and TensorBoard training curves are described inline but not downloaded, per this batch's no-figure-download policy. Several full reasoning-trace samples from steps up to 450 are preserved as text in the source markdown.

## Entities

- [[Hugging Face]] — cross-posts the tutorial via the open-r1 blog.
- [[DeepSeek]] — the "aha moment" behavior being reproduced originates from DeepSeek-R1's paper.

## Questions & Gaps

- The post explicitly does not determine why the model's reasoning style shifts from word-based to programmatic between steps 100 and 200, offering four competing hypotheses without a resolving experiment.
- No test of higher `num_generations` (16-64) or longer training (thousands of steps, as in the R1 paper) is reported, only proposed as future work.

## Related

- [[Open-R1: A Fully Open Reproduction of DeepSeek-R1]] — the broader reproduction project this tutorial is cross-posted under.
- [[GRPO]]
- [[Reasoning Models]]
- [[Reinforcement Learning Topic]]
