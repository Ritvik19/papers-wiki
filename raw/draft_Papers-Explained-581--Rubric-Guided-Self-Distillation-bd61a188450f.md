# Papers Explained 581: Rubric Guided Self Distillation

Papers Explained 581: Rubric Guided Self Distillation

Papers Explained 581: Rubric Guided Self Distillation

Rubric-Guided Self-Distillation (RGSD) is a verifier-free training method in which the base policy, conditioned on the rubric, serves as…

Papers Explained 581: Rubric Guided Self Distillation

Rubric-Guided Self-Distillation (RGSD) is a verifier-free training method in which the base policy, conditioned on the rubric, serves as the teacher for the unconditioned student. RGSD distills the rubric-conditioned teacher distribution into the student token-by-token, replacing sparse trajectory-level rewards with dense per-token learning signals and removing the LLM judge from the training loop entirely.

Method

A training instance for rubric-graded open-ended generation is a tuple (q, R), where q is a prompt and R = {(ci, wi)}K i=1 is a rubric set: a list of criteria ci with weights wi describing what an ideal response should contain. Let MJ denote an LLM judge. Given a candidate response y, the judge produces a binary satisfaction verdict vi(q, ci, y) ∈ {0, 1} for each criterion ci (criterion ci is met or not). These verdicts are aggregated into the rubric score:

The per-criterion verdicts can be elicited either as K separate judge calls (one criterion per call) or as a single batched call that returns the full K-element verdict for one rollout. The batched variant is used throughout this paper. The rubric-RL objective optimizes a policy πθ to maximize expected rubric score:

GRPO instantiates this by drawing G rollouts per prompt, scoring each via sJ, and updating πθ with a group-relative advantage estimate. Every optimizer step thus requires G batched judge calls per prompt (and G × K under per-criterion grading), which dominates training cost.

Rubric-Guided Self-Distillation

Method overview

RGSD removes the judge from the training loop. Rather than grading student rollouts with the judge model MJ, the rubric is used to condition the teacher whose distribution the student is trained to match. RGSD instantiates two copies of the base model from the same checkpoint θbase: a student with trainable weights θS (initialized to θbase) and a teacher with frozen weights θT = θbase. The student conditions on only the prompt q and defines a policy πS(· | q) from which on-policy rollouts are sampled during training. The teacher conditions on the prompt q, the rubric set R, and the student’s prefix y<t at each token position t, and defines a per-token distribution πT (· | q, R, y<t) that is used as a distillation target.

The training step proceeds as follows: Sample an on-policy rollout from the student, y ∼ πS(· | q), then forward (q, R, y) through the frozen teacher to obtain the per-token distribution πT (· | q, R, y<t) at every position t ∈ {1, . . . , T}. The student is then updated to match the teacher token-by-token under a clipped Jensen–Shannon divergence:

Where Dclip β is a clipped Jensen–Shannon divergence interpolating between forward KL (β = 0) and reverse KL (β = 1); β = 0.5 is used throughout. Only θS receives gradients; θT is held fixed for the entire training run.

When the base policy is a reasoning model, the teacher’s reasoning trace might subtly refer to specific rubric criteria even when the system prompt explicitly asks it not to. Distilling those positions into a student that never sees the rubric could introduce noise or bias. In order to prevent such leakage, mask the tokens between and out of the loss, so only final response tokens contribute to the loss.

Experiment Setup

RGSD is compared against judge-based GRPO on the medical and science domains of RubricHub. Each instance consists of a free-form prompt q and a per-prompt rubric set R of weighted criteria. Qwen-2.5–3B/7B-Instruct and Qwen3–4B/8B-Thinking are trained on the full train splits (12,519 medical and 19,806 science prompts) and evaluated on 300-prompt subsets of each domain’s held-out RubricHub validation split, plus 300-prompt subsets of HealthBench for medical and ResearchQA for science as out-of-distribution benchmarks. At evaluation time, all responses are graded against rubrics by gpt-5.4 at temperature 1.0.
Hyperparameters across methods.
Results and Discussion
Main results.
RGSD and GRPO achieve very similar score improvements over their base models: in medical, +6.1pp for RGSD vs. +5.9pp for GRPO; in science, +4.9pp for RGSD vs. +4.5pp for GRPO.
In per-model results, the lead alternates, suggesting quality parity rather than a clear performance advantage for either.
RGSD eliminates all judge queries during training, offering substantial efficiency advantages over the judge-heavy GRPO.

Training dynamics on RubricHub-med-300.Training dynamics on RubricHub-sci-300.

RGSD produces shorter responses while maintaining peak rubric satisfaction, especially pronounced on Qwen-2.5 models where GRPO responses can be 1.4–2.3 times longer with no consistent score advantage.
On Qwen3-Thinking models, the effect is family-dependent due to their inherently longer responses from reasoning traces.

Paper

Rubric-Guided Self-Distillation: Post-Training Without Rubric Verifiers 2606.12507

Hungry for more insights?

Don’t miss out on exploring other fascinating threads in this series. Simply click here and uncover the state-of-the-art research!

Do Subscribe for weekly updates!!

View original.

Exported from Medium on June 21, 2026.
