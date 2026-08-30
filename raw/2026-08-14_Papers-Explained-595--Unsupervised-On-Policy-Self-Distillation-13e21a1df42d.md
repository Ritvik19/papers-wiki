# Papers Explained 595: Unsupervised On-Policy Self Distillation

Papers Explained 595: Unsupervised On-Policy Self Distillation

Papers Explained 595: Unsupervised On-Policy Self Distillation

This work shows that On-Policy Self-Distillation can be achieved using only a model’s own generations via internal consistency…

Papers Explained 595: Unsupervised On-Policy Self Distillation

This work shows that On-Policy Self-Distillation can be achieved using only a model’s own generations via internal consistency. Unsupervised On-Policy Self-Distillation (U-OPSD) first samples multiple rollouts and constructs a pseudo solution by majority vote under a self-consistency threshold. It then conditions a teacher distribution on the shortest pseudo-solution and distills it into prefixes of the model’s longest incorrect completion, allowing the model to correct itself precisely where it is confidently wrong.

Method
Comparison among On Policy Post Training Methods.
Despite on-policy training, most post training methods remain externally supervised. RLVR relies on gold answers for verification, OPD on a stronger teacher, and OPSD and related work on privileged teacher contexts such as GT solutions, demonstrations, or environmental feedback.
Overview of Unsupervised On-policy Self-Distillation (U-OPSD).
U-OPSD removes this dependence by enabling the model to construct its own privileged context through internal consistency, i.e., a majority vote over its own rollouts that identifies a pseudo-solution in place of y⋆, while the resulting conditional teacher distribution is distilled into the student on the disagreeing rollouts.

Sample: For each prompt, draw G rollouts and parse the final answer with normalization and canonicalization.
Vote: Among the valid answers, the pseudo-answer is defined as the plurality vote, with ties broken uniformly at random. This vote partitions the rollouts into agreeing and disagreeing sets. Invalid rollouts belong to neither set, as an incomplete generation provides evidence of neither a correct nor an incorrect belief. Vote confidence is quantified using the self-consistency score c(x) = Number of trajectories in agreeing set / G. If c(x) < τ, the prompt is treated as unlabeled and contributes no gradient in the training step. τ is set to 1/2 for an absolute majority.
Distill: Given a valid majority vote, select an agreeing rollout and distill the teacher into the student on the disagreeing rollouts.

Unlike conventional majority-vote self-training, it does not simply imitate the selected response under teacher-forced prefixes. Instead, it transfers the solution-conditioned next-token distribution along the model’s own disagreeing trajectories, providing dense corrective supervision precisely at the prefixes that lead toward answers inconsistent with the model’s consensus.

Experiment Setup

Models:

Qwen3- 4B and Qwen3–8B (Both non-thinking and thinking modes)
Qwen3–30B-A3B-Instruct-2507 and Qwen3–4B-Instruct-2507.

Training Set:

A 30k subset of OpenThoughts

Baseline:

SFT on their gold solutions.
GRPO with binary outcome rewards verified against the gold answer.
OPSD with the teacher conditioned on the gold solution,

Evaluation Benchmarks:

AIME24, AIME25, and HMMT25 at avg@12
MATH500 and AMC23 at avg@4

Implementation Details:

Forward KL (β=0) over the full vocabulary with per-token pointwise clipping is used as the objective. A teacher fixed to the initial policy rather than the running one is adopted to ensure fair comparison. LoRA of rank 64 (α=128) is applied on all attention and MLP projections, with a learning rate of 5×10−6, gradient-norm clipping at 0.1, and sampling at temperature 1.1 with top-p 0.95 and top-k 20.

For U-OPSD, two unique hyperparameters are introduced: for each prompt, G=8 rollouts are generated independently and filtered by confidence threshold τ =0.5, whereas supervised OPSD uses 32 prompts and a single rollout. The maximum completion length is increased from 1,024 to 4,096 tokens, as U-OPSD requires rollouts to reach a boxed final answer.

For reasoning-mode experiments, following OPSD, the teacher is kept in reasoning mode and its behavior is distilled into a student in non-reasoning mode, while the resulting model is evaluated in reasoning mode. For non-reasoning experiments, both the teacher and student are in non-reasoning mode during training, and evaluation is likewise conducted in non-reasoning mode.

Evaluation

Non-thinking mode
Performance comparison on math reasoning benchmarks for Qwen3 models with nonthinking mode.
U-OPSD improves Qwen3–4B and Qwen3–8B by 8.5 and 10.7 points, respectively.
Outperforms all supervised baselines (SFT, GRPO, OPSD) and label-free RL baselines, exceeding OPSD by 3.2 and 2.3 points.
Achieves best results on four of five benchmarks for both models, indicating robust performance.
In contrast, label-free RL baselines offer only minor gains (up to 1.5 points), highlighting the advantage of consensus-based distillation.

Thinking mode
Thinking mode, per benchmark at step 150.
Gains are smaller: U-OPSD improves base models by 2.2 and 1.9 points.
Matches or slightly exceeds supervised OPSD and consistently outperforms GRPO.
Conclusions: Consensus-based distillation is most effective when base models are relatively weak (with lots of room for improvement); strong models leave less room, so improvements are smaller.

Instruction-tuned models
Qwen3–30B-A3B-Instruct-2507, non-thinking, scored as pass@1 rather than average@n.
U-OPSD achieves the highest average performance on both Qwen3–30B-A3B-Instruct-2507 and Qwen3–4B-Instruct-2507, with gains of 1.69 and 1.78 points over base models and also surpassing supervised OPSD in average.
Demonstrates recipe transferability to larger mixture-of-expert models without hyperparameter tuning.

Ablations
Configuration ablations, on Qwen3–8B non-thinking with longest-1.
Self-consistency Threshold (τ): Lowering the threshold (accepting more prompts for supervision) monotonically increases accuracy; filtering out prompts based on higher thresholds reduces performance more due to data loss than due to label noise.
Rollouts per Prompt (G): Increasing the number of rollouts improves performance but with diminishing returns; G=8 is cost-effective, while G=12 is slightly better if computational budget allows.
Teacher Update Policy: Updating the teacher with EMA (exponential moving average) yields a 2.4–4.1 point gain over a frozen teacher.
Performance under combinations of the teacher-reference selection and the distillation target selection, on Qwen3–8B non-thinking, G=8, τ=0.5, k=1.
Reference/Distillation Target: Conditioning the teacher on the longest agreeing rollout (i.e., using complete reasoning traces) is significantly better than conditioning on only the final answer; only using the boxed pseudo-label drops performance by 11–16 points
Ablation of the disagreeing-rollout selection policy (matched decay schedule).
Disagreeing Rollout Selection: Capping the number of disagreeing rollouts used in distillation (to 1–3) outperforms using all rollouts, with “disagree-1” being the most stable. Unlimited cap (“disagree-all”) sometimes yields results even below the base model.
Comparison of divergence computation strategy.
Vocabulary Truncation in Divergence: Truncating to the top 50–200 vocabulary entries suffices and does not hurt performance, while saving computational cost. Sampled-token distillation lags behind by 13–16 points.
Divergence family Dβ under U-OPSD, on Qwen3–8B non-thinking, longest-1, G=8, τ=0.5.
Divergence Measure: Forward KL is clearly favored; Jensen–Shannon and reverse KL perform much worse, with JSD matching the untrained model and reverse KL causing loss of reasonable termination in generations.

Paper

On-Policy Self-Distillation without Any Supervision 2608.06296

That’s a wrap!

If you enjoyed this breakdown, follow for more. I publish new paper explanations most weekdays.

More papers in this series, organized by lab and topic, are in the start here guide.

What paper should I cover next? Let me know in the responses.

By Ritvik Rastogi on August 14, 2026.

Canonical link

Exported from Medium on August 22, 2026.
