# Kimina-Prover: Applying Test-Time RL Search on Large Formal Reasoning Models

**Source**: `raw/kimina-prover/full-article.html` (224 KB), `raw/kimina-prover/full-article.md`
**Ingested**: 2026-07-10
**Tags**: #summary

## Summary

Numina and Kimi's team release Kimina-Prover-72B, a Lean 4 automated theorem prover built on Qwen2.5-72B and trained with the Kimi k1.5 RL pipeline, plus distilled 8B and 1.7B variants (Kimina-Prover-Distill, on Qwen3). The headline result is a state-of-the-art 92.2% pass rate on miniF2F-test, reached through two main innovations layered on top of the earlier Kimina-Prover Preview model: Test-Time Reinforcement Learning (TTRL) Search, an agentic framework that lets the model recursively discover, generate, and compose intermediate lemmas to build long multi-stage proofs, and an error-fixing capability that reads Lean's compiler error messages and proposes targeted corrections instead of regenerating a proof from scratch.

TTRL Search builds on a "lemma-enabled pattern" learned during RL: a random subset of candidate lemmas is prepended to the problem context, and a preference-based reward shaping strategy (rewarding trajectories that actually use a provided lemma over those that ignore it) raised lemma utilization from near-zero to a stable 30-40%. At test time, TTRL Search treats each problem plus its candidate lemmas as a "search scope," tracks a lemma utilization score, constructs 10 input variants per problem (60% biased toward top-scoring lemmas, 40% mixing in random exploration), prunes lemmas that fail to reach a 0.10 utilization score after 50 attempts, and recursively spins up new sub-searches for any lemma that isn't provable after 128 attempts, letting reasoning depth scale with problem difficulty. A "negation proving" step guards against unsound proofs: any newly generated lemma whose negation is also provable is discarded as logically inconsistent.

Error-fixing was built from an SFT dataset of (incorrect proof, Lean feedback, correct proof) triplets, with Claude 3.7 Sonnet used to synthesize intermediate reasoning chains explaining each fix. Naively folding error correction into the RL loop failed initially (the untrained model's fix success rate was only ~1%, producing sparse, unstable reward), so the team introduced a "batched failure replay" strategy: failed proofs from RL iteration N are collected and mixed with fresh problems into iteration N+1's training batch, giving the model consistent, high-volume exposure to error-correction tasks. Under a fixed sampling budget, 16 initial attempts plus 16 error-fix attempts (35.6% success) beat 32 independent brute-force attempts (28.8%), and scaling to 32+32 reached 44.1%, showing error-fixing is a more efficient use of compute than blind resampling.

Other contributions: a curated RL prompt set (300k problems distilled to a ~90k competition-focused subset, largely from NuminaMath 1.5's olympiad-reference subset, with dynamic difficulty filtering during training); continuous pretraining on a 6B-token Lean corpus (260M tokens of GitHub Lean code plus 5.5B tokens of compiler-validated RL rollout data); "Random Proof Cut" data augmentation (truncating or `sorry`-infilling human proofs so the model learns to extend or fill gaps); and a non-proof problem-solving mode where the model first deduces a numeric answer, then generates a formal proof justifying it, unifying answer-generation and proof-construction tasks.

## Key Claims

- Kimina-Prover-72B reaches 86.4% with one round of error correction, 87.7% at pass@1024, and 92.2% with the full TTRL Search framework (estimated pass upper bound ~42,000).

| Model | pass@1 | pass@32 | pass@1024 |
|---|---|---|---|
| Kimina-Prover-1.7B | 46.7 | 73.4 | - |
| DSP+ | 52.5 | 71.3 | 80.7 |
| DeepSeek-Prover-V2-7B | 58.6 | 75.6 | 79.9 |
| Kimina-Prover-8B | 61.1 | 78.3 | - |
| DeepSeek-Prover-V2-671B | 61.9 | 82.4 | 86.6 |
| Kimina-Prover-72B | 63.9 | 84.0 | 87.7 |
- Scaling behavior shifts from roughly linear (log-scale) gains with sampling budget in earlier versions to diminishing returns beyond pass@1024, arguing further gains need better search strategy (TTRL) rather than more brute-force sampling.
- Reward shaping raised lemma-utilization rate in the lemma-enabled pattern from near-zero to a stable 30-40%.
- Batched failure replay error-fixing: 16+16 attempt-and-fix reaches 35.6% success on a hard 59-problem miniF2F subset, beating 32x1 brute force (28.8%); 32+32 reaches 44.1%.
- Continuous pretraining corpus: 6B tokens total (260M from GitHub, 5.5B compiler-validated RL rollout data, plus state-tactic-state / state-tactic-error structured data).

## Figures

No figures were extracted for this ingest; the miniF2F pass-rate bar chart, TTRL Search architecture diagram, and proof-dependency graph for `imo_1969_p2` are described inline but not downloaded, per this batch's no-figure-download policy. The pass@1/32/1024 comparison table above is preserved as markdown, and full Lean 4 proof listings (including a before/after error-fixing example) are preserved in the source markdown.

## Entities

- [[Numina]] — AI-MO/Project Numina, co-developer of Kimina-Prover with the Kimi team.
- [[Hugging Face]] — hosts the blog post and model releases.

## Questions & Gaps

- The post notes "a large portion of the current sampling is spent on proving unhelpful or redundant lemmas" in TTRL Search, implying significant headroom, but doesn't quantify what fraction of the 42,000-sample budget this represents.
- No ablation isolates the individual contribution of continuous pretraining versus RL versus TTRL Search to the final 92.2% pass rate.

## Related

- [[Kimina-Prover-RL]] — follow-up post releasing a slimmed-down, open-source Verl-compatible training pipeline for the same reasoning-then-generation paradigm.
- [[Reasoning Models]]
- [[Reinforcement Learning Topic]]
