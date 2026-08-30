# Papers Explained 592: Self-Distilled Reasoner

Papers Explained 592: Self-Distilled Reasoner

Papers Explained 592: Self-Distilled Reasoner

Inspired by the intuition that a sufficiently capable LLM can rationalize external privileged reasoning traces and teach its weaker self…

Papers Explained 592: Self-Distilled Reasoner

Inspired by the intuition that a sufficiently capable LLM can rationalize external privileged reasoning traces and teach its weaker self, On-Policy Self-Distillation (OPSD) is introduced as a learning algorithm where a single LLM acts as both teacher and student with different contexts. The teacher policy conditions on privileged information (e.g., verified reasoning traces) while the student policy sees only the question; training minimizes the per-token divergence between these distributions over the student’s own rollouts.

Learning from Verifiable Reasoning Dataset

Consider a dataset of problem-solution pairs S = {(xi, y*)}, where each x denotes a problem and y* is the corresponding reference solution, which may include chain-of-thought reasoning. There are several ways to exploit the learning signals from this dataset:

Standard supervised fine-tuning (SFT) on S can be viewed as off-policy distillation/imitation learning using expert trajectories, but it suffers from distribution mismatch between training and inference.
Reinforcement learning from verifiable rewards (RLVR) addresses this by optimizing on-policy samples and assigning binary rewards by comparing generated answers against y*. However, RLVR is computationally expensive and the reward signal is sparse, providing same feedback across all tokens regardless of where errors occur.
Alternatively, one can train a process reward model (PRM) to provide dense, token-level feedback during RL. However, acquiring labels for PRM training is prohibitively expensive and difficult to scale.
On-policy distillation works address distribution shift by training on the student’s own samples, but require a separate, often larger, teacher model to provide supervision.
Comparison of training methods for reasoning tasks.
Method
Overview of On-Policy Self-Distillation (OPSD)
Two conditional distributions from the same language model pθ are instantiated by varying the conditioning context. The teacher policy conditions on privileged information: both the problem x and the reference solution y*.

The student policy observes only the problem statement, matching the inference-time condition:

Both policies share the same parameters θ but differ only in their conditioning context. To encourage the teacher to naturally evaluate the student’s generation, a prompt is added asking the teacher to generate a new solution after seeing the reference solution. However, the teacher doesn’t generate tokens; it only does rationalization implicitly through prefilling.
Prompt example for student and teacher policies.
Given a problem x, the student generates an on-policy response:

Both policies then evaluate this student-generated trajectory. At each position n, they induce next-token distributions over yn ∈ V conditioned on the same student prefix:

Given a student-generated sequence ˆy, the trajectory-averaged, token-wise divergence is:

Here, D can be any distribution divergence measure such as the generalized Jensen-Shannon divergence JSDβ , defined for a weight β ∈ [0, 1] as:

where m = βpT + (1 − β)pS is the interpolated mixture distribution.

The expected divergence between teacher and student is minimized over on-policy student samples.

Gradients are back propagated only through the student policy pS.

Per-Token Pointwise Divergence Clipping

In experiments, token-level divergence is highly skewed across vocabulary entries: a small subset of stylistic tokens exhibits much higher divergence than mathematically meaningful tokens. This imbalance causes the training signal to be dominated by stylistic patterns. To address this, pointwise clipping is applied to the vocabulary-level divergence contributions. Let Df (pT ∥pS ) denote an f-divergence. At each token position n and vocabulary entry v, define:

It measures how different the student is from the teacher for token v at position n, weighted by how probable that token is for the teacher.

The clipped divergence is computed as:

Alternative objective: Sampled-token distillation through policy gradient

A sampled-token reward signal (a reverse-KL signal on sampled actions) is formed and optimized with policy gradient. For each position n in a sampled sequence ˆy, the advantage term is defined:

and optimize the policy-gradient-style objective:

Experiments Setup

The Qwen3 model family is used at three scales: Qwen3–1.7B, Qwen3–4B, and Qwen3–8B, utilizing the instruct-tuned versions. For training data, the mathematical reasoning subset of OpenThoughts is used, sampling up to 30K problem-solution pairs with chain-of-thought reasoning. Evaluation is conducted on competition-level mathematics benchmarks including AIME 2024, AIME 2025, and HMMT 2025.

Evaluation
Performance comparison on mathematical reasoning benchmarks for Qwen3 models.
OPSD consistently outperforms SFT and matches or exceeds GRPO across all model scales, achieving these gains with significant token efficiency: a single rollout (1024 tokens) per problem versus GRPO’s 8 rollouts of 16k tokens each.
Token Efficiency of OPSD.
OPSD extracts learning signals more efficiently than both GRPO and SFT, with higher token-level learning efficiency in fewer steps.
Comparison of divergence objectives on AIME25 with Qwen3–1.7B.
Forward KL outperforms reverse KL and JSD, giving notable improvements in accuracy and stability.
Ablation on divergence computation strategies for OPSD on Qwen3–4B with 2048 generation length for distillation.
Full-vocabulary logit distillation outperforms sampled-token distillation, offering richer supervision but at a higher memory cost.
Per-token KL divergence by token category across generation styles.
The best results are achieved when the student is in TM-off mode and the teacher in TM-on, as this setup maximizes KL on math-relevant tokens.
Per-token KL Clipping stabilizes training, prevents performance degradation due to heavy-tailed KL on stylistic tokens, and is important for fast convergence.
Effect of Generation Length on Qwen3–1.7B.
Increasing the student generation length does not give consistent improvements; early tokens are more important for learning, as later tokens become too predictable.

Paper

Self-Distilled Reasoner: On-Policy Self-Distillation for Large Language Models 2601.18734

That’s a wrap!

If you enjoyed this breakdown, follow for more. I publish new paper explanations most weekdays.

More papers in this series, organized by lab and topic, are in the start here guide.

What paper should I cover next? Let me know in the responses.

By Ritvik Rastogi on August 11, 2026.

Canonical link

Exported from Medium on August 22, 2026.
