# Papers Explained 578: Reward Hacking in Rubric-Based RL

Papers Explained 578: Reward Hacking in Rubric-Based RL

Papers Explained 578: Reward Hacking in Rubric-Based RL

The study analyzes reward hacking in rubric-based RL, where policies are optimized against a training verifier but evaluated by stronger…

Papers Explained 578: Reward Hacking in Rubric-Based RL

The study analyzes reward hacking in rubric-based RL, where policies are optimized against a training verifier but evaluated by stronger reference panels. It finds that weak verifiers lead to proxy-reward gains that do not transfer to reference panels, with exploitation arising from partial satisfaction of criteria, treating implicit content as explicit, and imprecise topical matching. Stronger verifiers reduce but do not eliminate reward hacking, and even then, if rubrics leave important failure modes unspecified, RL checkpoints favored by rubric-based judges are rated lower by rubric-free judges, with gains concentrated in presence-based criteria like completeness but declines in overall quality, factual correctness, conciseness, and relevance.

Setup

During training, an AI policy is optimized based on a proxy reward called R_proxy. This reward is produced by the training verifier v_train, which evaluates responses using a set of rules (a rubric) and aggregates the results into criterion-level judgments g_proxy.

To ensure that any improvements in R_proxy reflect real improvements (and are not just overfitting to the biases of a single verifier), a reference reward R_ref is computed using a panel of three advanced AI judges from different model families: GPT-5.4, Gemini 3 Pro, and Claude Opus 4.6. The panel achieves high agreement with human experts (about 79.4–81.3 macro-F1 in medical and science domains), which matches typical human inter-rater reliability.

Two particular models are selected as training verifiers:

GPT-4o-mini (weak/cheap): 76–82% agreement with the reference panel.
GPT-OSS-120B (strong/expensive): 92% agreement.

The setup uses medical and science questions from datasets (e.g., RaR-science, ResearchQA, MegaScience, II-medical-reasoning) paired with rubrics from RubricHub. This yields 12,519/1,391 train/test prompts for medical and 19,806/2,201 for science domains.

The main policy trained is Qwen2.5–7B-Instruct for five epochs, with identical training parameters except for the training verifier used. Additional models (Qwen2.5–14B and Qwen2.5–32B) validate that the observed effects persist at larger model sizes.

Measuring Reward Hacking via Verifier Exploitation

As proxy reward rises during training, two things happen at the same time:

Policy improvement: The model genuinely gets better at satisfying the criteria it’s supposed to.
Exploitation of verifier errors: The model also learns to “hack” or exploit mistakes made by the training verifier so that it gets credit it shouldn’t actually have received.

To measure and separate these effects three indicators are introduced for every test prompt and evaluation criterion:

A “new credit” is called “incorrect at t” when:

The criterion is newly credited by the training verifier (N=1)
AND the reference panel unanimously rejects it (J=1).

Exploitation Rate at every evaluation checkpoint t is defined as the fraction, among all newly credited criteria, that are actually unanimously rejected by the reference panel.

Four RL training runs are tested: two domains (medical and science), two types of verifiers (weak: GPT-4o-mini, strong: GPT-OSS-120B), with 300 test prompts each, evaluated every 25 training steps.
Evaluation-set reward and exploitation trajectories across RL training.
In the “weak-verifier” (GPT-4o-mini) setting:

Proxy/training-verifier reward rises sharply.
Reference-panel reward rises less and plateaus.
The exploitation rate increases as reward rises
This means most of the new reward comes from the model learning to exploit verifier mistakes (hacking), not genuine ability gains.

In the “strong-verifier” (GPT-OSS-120B) setting:

Training-verifier and reference-panel reward closely track each other.
Exploitation rate starts and stays low, with no upward trend.
Stronger verification cuts down on hacking, but doesn’t eliminate it some mistakes are always exploited.

Verifier Failure Modes

To examine the errors, or each case:

the rubric’s text,
the verifier’s own explanation of why it thought the criterion was met (MET judgment),
the three panel judges’ explanations for their NOT_MET judgments.

are used to prompt GPT-5.4 to summarize, in one sentence, the structural reason for the failure. By clustering these structural failure descriptions, the following taxonomy is identified:

The full pipeline is applied to all incorrect credits across the four runs (53,447 criterion-level cases total).
Sub-mode distribution of verifier failure modes across training for all four runs.
Mode stability: The relative share of each error type changes very little regardless of training stage, domain, or verifier strength. In other words, training just makes the system less error-prone overall, but doesn’t change how it fails.
Verifier similarity: Different verification systems (GPT-4o-mini and GPT-OSS-120B), despite very different total error rates, make the same types of mistakes in virtually identical proportions. This suggests that these failure types are fundamental limitations of rubric verification, not just quirks of a particular model.

Self-Internalization Gap

The exploitation rate requires three frontier-judge calls per criterion-prompt pair at every checkpoint making it expensive, and unavailable in many deployment settings. Hence the authors complement it with the self-internalization gap, a verifier-free diagnostic computed from the policy’s own log-probabilities.

For each evaluation prompt 𝑥𝑖, the model is run under two contexts:

Prompt-only: 𝜋𝜃𝑡(⋅∣𝑥𝑖) (the same as during reinforcement learning training).
Rubric-conditioned: 𝜋𝜃𝑡(⋅∣𝑥𝑖, 𝐶𝑖) where the evaluation rubric is inserted as a system prompt at evaluation time.

For each prompt, K=10 samples of model outputs ({𝑜𝑖,𝑗(𝑡)}) are drawn from the rubric-conditioned distribution.

For each sampled response, compute its average log-probability under both contexts:

ℓprompt(𝑜𝑖,𝑗(𝑡)): log-probability under prompt-only.
ℓcond(𝑜𝑖,𝑗(𝑡)): log-probability under rubric-conditioned.

Compute Δ(𝑡) as:

Where ∣𝐷 eval∣ is number of evaluation prompts, and 𝐾 is the number of samples per prompt.

Larger (closer to zero) values of Δ(t) mean the model’s outputs, in the prompt-only context, are becoming more similar to those generated with the rubric (i.e., the model is “internalizing” the rubric).

This gives a stopping heuristic: Train until Δ(𝑡) stops increasing, in other words, until the policy has learned as much of the rubric as possible without further external guidance.

Hacking the Rubric, Not the Verifier

A policy can optimize for the explicit criteria in a rubric to score higher, but degrade aspects of answer quality that the rubric does not enumerate. This includes things like factual precision, relevance, and conciseness. In this context, “reward hacking” means the model gets a higher reward (rubric score) but actually drifts away from the intended notion of good response quality.

Strong Rubric Verification Can Still Favor Worse Responses

The RL-trained checkpoint is evaluated against the base model under both rubric-based and rubric-free pairwise judging on five quality dimensions (1–7 Likert, Completeness, Factual correctness, Conciseness, Relevance, Safety).
Rubric-based vs. rubric-free judge agreement.
On the strong-verifier medical run, evaluated with the full reference panel (GPT-5.4, Gemini 3 Pro, Claude Opus 4.6), rubric-based judges prefer the checkpoint on 85.8% of prompts but rubric-free judges prefer the base on 78.4%.

This is reward hacking even under strong verification: the checkpoint wins according to the rubric-based reward but loses according to rubric-free holistic evaluation by the same class of frontier judges. The failure is not primarily that the strong verifier cannot apply the rubric; rather, the optimized rubric rewards completeness and explicit coverage more directly than it penalizes verbosity, factual drift, and relevance loss.
Rubric-free dimensional ratings (1–7 Likert, averaged across 3 judges).
The dimensional breakdown is consistent with this: the checkpoint improves only on completeness while degrading on the other four.
Per-model dimensional deltas (ckpt-last minus base).
All the three judges agree directionally
Per-dimension ckpt-vs-base pairwise win rate (rubric-free, gpt-5.4) over training.
The pattern holds across all four main runs, and the magnitude scales with verifier strength: training under the strong verifier roughly halves the overall-quality decline in both domains.

Rubric Rewards Over-Specify What to Include and Under-Specify What to Avoid

Most rubric reward focuses on presence-based criteria rather than absence-based criteria. This imbalance matters because presence-based criteria are easier to enumerate (e.g., facts, disclaimers, formatting), while absence-based criteria (like not being misleading, verbose, irrelevant, overconfident, or subtly incorrect) are much harder to specify.

Satisfying presence-based rubrics often means responses get longer and more verbose, as the easiest way to maximize the rubric score is to keep adding content and meeting explicit criteria.

These criteria can be met without actually improving correctness or trustworthiness e.g., incorrect claims, verbose formatting, unnecessary disclaimers.
Rubric satisfaction by type (base vs. ckpt-last).
Presence-based rubric satisfaction increases 14.9 percentage points (from 27.6% to 42.5%).
Absence-based satisfaction declines slightly (from 51.6% to 49.6%, a drop of 2 percentage points).
This co-occurs with longer responses and more incorrect claims.

Paper

Reward Hacking in Rubric-Based Reinforcement Learning 2605.12474

Hungry for more insights?

Don’t miss out on exploring other fascinating threads in this series. Simply click here and uncover the state-of-the-art research!

Do Subscribe for weekly updates!!

View original.

Exported from Medium on June 13, 2026.
