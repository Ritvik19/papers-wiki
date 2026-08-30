# Papers Explained: On-policy Distillation with Verifiable Reward

Papers Explained: On-policy Distillation with Verifiable Reward

Papers Explained: On-policy Distillation with Verifiable Reward

On-policy Distillation with Verifiable Reward combines OPD and RLVR. The implicit reward of sampled-token OPD is reformulated based on…

Papers Explained: On-policy Distillation with Verifiable Reward

On-policy Distillation with Verifiable Reward combines OPD and RLVR. The implicit reward of sampled-token OPD is reformulated based on trajectory correctness, then a ReLU gating mechanism is applied to ensure that correct trajectories receive non-negative rewards and incorrect ones receive non-positive rewards, thereby aligning the distillation signal with task success while preserving the teacher’s distributional guidance.

Method

Begin with the sampled-token OPD loss:

For a sampled response o ∼ πθ(· | q), the per-token loss is:

The gradient of the sequence-level loss with respect to θ is:

The RLVR loss for a trajectory with reward R is:

Its gradient is:

The sampled-token OPD gradient shares the same form as the RLVR gradient, where the log-ratio term corresponds to the reward coefficient. By matching the coefficients of ∇θ log πθ(ot|q, o<t), the correspondence becomes evident.

This observation allows to reinterpret the log-ratio term as an implicit token-level reward ROPD(ot):

However, unlike RLVR, where the reward sign is determined by the verifier outcome, the sign of Ropd is solely determined by the teacher-student probability ratio. To analyze their alignment, consider two cases based on trajectory correctness:

The sign of log (πT /πθ) is determined by whether πT > πθ or πT < πθ, which is independent of trajectory correctness. This creates two failure cases: correct trajectories can receive negative rewards when πT < πθ, and incorrect trajectories can receive positive rewards when πT > πθ. Both violate the RL principle.

OPDVR: A Simple Gated Mechanism

OPDVR method.

The solution is extremely simple: apply a ReLU gate to enforce RLVR compliance on the sampled token while preserving the teacher’s distributional guidance:

The corresponding loss is:
Overview of OPDVR.
This gated mechanism ensures that:

Correct trajectories receive non-negative rewards, and incorrect trajectories receive non-positive rewards, aligning the reward sign with trajectory correctness.
For tokens on correct trajectories, the reward magnitude is larger when the teacher is more confident than the student, i.e., log (πT /πθ) is larger. This encourages the model to reinforce choices that are both correct and reliable according to the teacher.
For tokens on incorrect trajectories, the penalty magnitude is larger when the student is more confident than the teacher, i.e., log (πθ/πT ) is larger. This forces the model to suppress overconfident mistakes.

Group Relative Policy Distillation (GRPD)

GRPO computes a group-relative advantage ˆAi,t for each token position t in response oi:

Apply the same ReLU gating logic, but with the binary correctness sign R replaced by the group-relative advantage ˆAi,t:

Equivalently, this can be written compactly as:

The corresponding loss is:

Experiments

Same-architecture setting: Qwen3–4B-nonthinking is used as the student model and is distilled from a teacher model of the same architecture, which is obtained by training Qwen3–4B with GRPO on the filtered subset of the DeepMath dataset consisting of 57k samples with difficulty level ≥ 6.
Cross-architecture setting: The DAPO-Math-17k dataset is used. The teacher model is Qwen3–4B-base, fine-tuned with GRPO for 3 epochs on the same dataset. The student model is Qwen3–1.7B-base. The distillation training runs for 3 epochs.
Benchmarks: AIME24, AIME25, AMC, MATH500, Minerva, and OlympiadBench.
Results on same-architecture distillation.Results on cross-architecture distillation.
OPDVR consistently outperforms both standard sampled-token OPD and top-64 OPD across all six benchmarks and settings.
In the same-architecture setup, OPDVR surpasses the teacher on AIME24 and achieves significant improvements on AIME24 (+2.7) and AIME25 (+2.1) over standard OPD.
In cross-architecture distillation, OPDVR demonstrates robustness with substantial gains (e.g., +5.5 AMC, +1.7 MATH500 over OPD).
Results on Group Relative Policy Distillation.
GRPD (OPDVR with group-relative advantages) outperforms both GRPO and vanilla OPD, especially on AIME24 (+6.5) and AIME25 (+10.9), showing the advantage of combining group-relative estimation with ReLU-gated signals.

Paper

On-policy Distillation with Verifiable Reward 2608.24696

That’s a wrap!

If you enjoyed this breakdown, follow for more. I publish new paper explanations most weekdays.

More papers in this series, organized by lab and topic, are in the start here guide.

What paper should I cover next? Let me know in the responses.

View original.

Exported from Medium on August 30, 2026.
