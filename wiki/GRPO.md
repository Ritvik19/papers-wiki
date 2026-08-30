# GRPO

**Type**: concept  
**Tags**: #concept

## Overview

Group Relative Policy Optimization (GRPO) is an RL optimizer for LLMs introduced in DeepSeekMath [Shao et al., 2024] and popularized by its use in training DeepSeek-R1. It builds on [[Proximal Policy Optimization]] by replacing the learned critic/value model with a simpler group-relative advantage estimate: multiple completions are sampled per prompt, and the advantage for each completion is computed as the z-score of its reward relative to the group mean and standard deviation. This eliminates the need for a separate value model, substantially reducing memory and compute overhead versus PPO.

The GRPO surrogate loss uses the same clipping mechanism as PPO (policy ratio clipped to [1-ε, 1+ε]) and the KL divergence term is typically omitted for reasoning model training. Despite its conceptual simplicity, vanilla GRPO has well-documented failure modes at scale: entropy collapse, reward noise, training instability, and length biases — all of which have spawned a body of follow-up work catalogued in [[GRPO++: Tricks for Making RL Actually Work]].

## Appearances

- [[GRPO++: Tricks for Making RL Actually Work]] — Central subject; article surveys all known improvements to vanilla GRPO.
- [[Reinforcement Learning Topic]] — Listed among core RL algorithms for LLM training.
- [[Reasoning Models]] — Used to train DeepSeek-R1, Qwen reasoning models, OLMo 3 Think, and many open reasoning models.
- [[Papers Explained: OLMo 3]] — OlmoRL builds directly on GRPO, adding zero-gradient filtering, active sampling, token-level loss, no KL loss, asymmetric clipping, and truncated importance sampling.
- [[Papers Explained: IFBench]] - uses GRPO for IF-RLVR, where reward comes from deterministic instruction-constraint verifiers rather than math/code answer checkers.
- [[Papers Explained: Reward Hacking in Rubric-Based RL]] - uses GRPO in medical and science rubric-reward runs to study proxy reward gains, verifier exploitation, and rubric hacking.
- [[Papers Explained 581: Rubric-Guided Self-Distillation]] - GRPO baseline on RubricHub; RGSD matches rubric gains with zero train-time judge queries.
- [[Reinforcement Learning from Human Feedback]] — textbook chapter on GRPO vs PPO/RLOO, implementation, and comparison to GSPO/CISPO.
- [[Advancing Search-Augmented Language Models]] — on-policy GRPO for web search agents with token-level IS and gated composite rewards.
- [[RL Training For Math Reasoning]] — NeMo Aligner + vLLM GRPO implementation, log-prob alignment, and math-reasoning collapse modes.
- [[Unsloth Reinforcement Learning]] — Unsloth GRPO tutorials, memory-efficient RL (Standby), FP8 RL, long-context GRPO, and GPT-OSS reward hacking mitigations.
- [[Papers Explained: SFT Conflicts, RL Coexists]] — Demonstrates that GRPO's standardized advantage zero-sum property algebraically filters out prompt-level mean gradients ($\bar{S}_i(x)$), leaving intra-group residuals that render multi-task gradients variance-limited, mutually orthogonal, and compatible with [[Parallel-RL]].
- [[Papers Explained: On-policy Distillation with Verifiable Reward]] — Introduces [[GRPD]], combining GRPO group-relative advantages with token-level ReLU-gated on-policy distillation.

## Notes

Key failure modes of vanilla GRPO:
1. **Entropy collapse**: symmetric clipping disproportionately suppresses low-probability (exploration) tokens.
2. **Reward noise**: small batch sizes and zero-gradient prompts make the batch gradient noisy.
3. **Length bias**: sequence-level loss normalization underweights long responses during positive advantage, overweights them during negative advantage (biasing toward verbose incorrect answers).
4. **Advantage instability**: dividing by group standard deviation causes explosive advantage magnitudes on easy/hard prompts.

Improved & hybrid variants: [[DAPO]], [[Dr. GRPO]], [[GSPO]], [[GMPO]], [[CISPO]], [[GRPD]].

## Related

- [[GRPD]] — Group Relative Policy Distillation combining GRPO advantages with gated token distillation.
- [[OPDVR]] — On-policy distillation with verifiable rewards.
- [[DAPO]] — GRPO variant with four practical fixes from ByteDance/Tsinghua.
- [[Dr. GRPO]] — De-biased GRPO variant removing std from advantage and using fixed-constant normalization.
- [[GSPO]] — Sequence-level importance ratio variant used in Qwen 3.
- [[Task Coexistence]] — Multi-task capability preservation enabled by GRPO residual orthogonality.
- [[Parallel-RL]] — Merging independent task GRPO updates.
- [[Gradient Interference]] — Variance-limited multi-task interference bound in GRPO.
- [[Proximal Policy Optimization]] — GRPO inherits PPO-style clipped surrogate updates.
- [[Policy Gradient]] — Underlying optimization lens.
- [[KL Regularization]] — Term typically omitted in GRPO for reasoning model training.
- [[Reward Hacking]] — Failure mode that can emerge when GRPO optimizes an incomplete or noisy reward.
