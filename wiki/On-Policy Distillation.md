# On-Policy Distillation

#concept

On-Policy Distillation, or OPD, is a teacher-guided post-training method that samples rollouts from the current student policy and then uses a teacher policy to provide dense token-level learning signal on those same rollouts. It sits between [[Supervised Fine-Tuning]] and [[Reinforcement Learning]]: like RL, it trains on the student's own state distribution, but like [[Model Distillation]], it replaces sparse outcome reward with a teacher-bounded token-level objective.

## Core Idea

The central problem OPD addresses is distribution mismatch. Standard teacher [[Supervised Fine-Tuning]] trains the student on completions sampled from a fixed dataset or teacher distribution. That is cheap and stable, but the student does not learn from the states it actually visits after its own policy changes. [[Reinforcement Learning]] fixes this by sampling current student rollouts, but its signal is often sparse: a whole response may receive only an outcome reward, verifier score, or preference-derived scalar.

OPD combines the two views. For a prompt, the student samples a response from its current policy. A teacher then scores the student-sampled tokens, usually through teacher log probabilities or a reverse-KL-style token advantage. Tokens the teacher would make more likely receive positive pressure; tokens the teacher would make less likely receive negative pressure. The student therefore receives an update that is both on-policy in state coverage and dense in token-level supervision.

In [[On SFT RL and On-Policy Distillation]], OPD is framed as the same-family upgrade to SFT. The page's key distinction is that OPD keeps the compounding property of on-policy training while using teacher likelihoods to avoid the high variance of pure reward learning. The tradeoff is that OPD remains teacher-bounded: it can efficiently transfer what the teacher knows, but it cannot reliably exceed the teacher unless combined with verifier or reward signals.

## Why Same-Family Teachers Matter

OPD works best when teacher and student share tokenizer, vocabulary, chat template, and post-training recipe. If the teacher and student are from different families, per-token probabilities no longer describe the same action space cleanly. The resulting gradient may teach formatting habits, tokenization artifacts, or teacher-specific response style rather than capability.

Same-family teachers make token-level credit more meaningful. In [[Papers Explained 552 - Nemotron Cascade 2]], multi-domain OPD uses teachers selected from the same Cascade RL pipeline, not unrelated external frontier models. The page explicitly notes two advantages: the teachers provide a diverse capability pool while sharing tokenizer and vocabulary with the student, which reduces distribution shift.

This is also why OPD is different from ordinary synthetic-data distillation. A cross-family teacher can still write useful solutions for SFT, but OPD depends on the teacher assigning probabilities to the exact tokens sampled by the student. The closer the teacher and student are as policies, the more the teacher's log-probability differences can be interpreted as a local improvement direction rather than a noisy imitation target.

## Objective Shape

A typical OPD update has three pieces:

- Sample: generate responses from the current student or inference policy on the target prompt distribution.
- Score: evaluate the student-sampled tokens under a teacher policy, often comparing teacher log probability to the student's log probability on the same token.
- Optimize: update the trainable student policy toward tokens the teacher prefers, sometimes with importance weighting when rollout and training policies differ.

The [[Papers Explained 552 - Nemotron Cascade 2]] raw corpus entry gives the clearest concrete form. In its Multi-domain On-Policy Distillation section, each prompt is assigned a domain teacher. The model samples a response, computes a token-level distillation advantage from the teacher-student log-probability difference, and applies the signal only on valid response tokens. Because the inference engine and training engine may not be perfectly identical, truncated importance weighting is used to account for train-infer mismatch.

The important detail is that the objective does not require a full-vocabulary KL at every step. The raw-backed summary says the log-probability difference is computed only on the sampled token. This makes OPD closer to a policy-gradient-style update with a dense teacher-derived advantage than to a heavyweight full-distribution distillation pass.

## Comparison To Nearby Regimes

Compared with SFT, OPD updates on student rollouts rather than fixed demonstrations. SFT is cheaper and often enough when the student is far below the teacher, but its data distribution does not automatically improve as the student improves. OPD lets the student keep sampling its own mistakes, hesitations, and intermediate behaviors, then uses the teacher to shape those states directly.

Compared with RL, OPD is usually lower variance and more sample efficient because every retained response token can carry training signal. RL with verifiable rewards, as in [[Papers Explained 283 - Tulu V3]], [[Papers Explained 381 - AceReason-Nemotron]], and [[Papers Explained 553 - Rubrics as Rewards]], can exceed a teacher when the verifier recognizes better solutions than any teacher demonstration. OPD cannot do that by itself; its ceiling is the teacher's policy. Its advantage is efficiency and stability when a strong same-family teacher exists.

Compared with DPO or offline preference tuning, OPD is on-policy. [[Papers Explained 283 - Tulu V3]] shows the practical importance of on-policy data even for DPO: including completions generated by the current SFT model improves downstream preference tuning. OPD applies that same principle more directly by making the student generate the tokens being distilled.

Compared with [[On-Policy Self-Distillation]], OPD uses a separate teacher policy rather than the student under privileged context. OPSD automatically solves tokenizer mismatch because the teacher path is the same model, but [[On SFT RL and On-Policy Distillation]] warns that privileged-answer conditioning can create dense, biased, concentrated gradients. OPD still has bias from the teacher, but same-family teacher calibration can make the signal more diffuse and easier to control.

## Raw Corpus Anchors

- [[Papers Explained 552 - Nemotron Cascade 2]] is the direct OPD/MOPD source. Its raw file is `raw/2026-03-31_Papers-Explained-552--Nemotron-Cascade-2-1ac869c28c8c.md`. It describes Cascade RL followed by Multi-domain On-Policy Distillation to reduce capability drift, recover benchmark regressions, and rebalance math, code, agentic, and instruction-following capabilities.
- [[Papers Explained 149 - RLHF Workflow]] is an important online-training baseline. Its raw file is `raw/2024-06-12_Papers-Explained-149--RLHF-Workflow-56b4e00019ed.md`. It distinguishes offline DPO from online iterative RLHF, where new responses from intermediate policies are added to the feedback buffer.
- [[Papers Explained 283 - Tulu V3]] contributes the on-policy data lesson. Its raw file is `raw/2025-01-08_Papers-Explained-283--Tulu-V3-fc7758b18724.md`. The preference-tuning section reports that including on-policy SFT-model generations improves downstream DPO relative to only off-policy data.
- [[Papers Explained 381 - AceReason-Nemotron]] contributes the RL contrast. Its raw file is `raw/2025-06-05_Papers-Explained-381--AceReason-Nemotron-0b3bd6495890.md`. It emphasizes strict on-policy RL for stability and argues that RL can surpass distillation-based models when verifiers are reliable.
- [[Papers Explained 417 - Kimi-Researcher]] extends the on-policy argument to long-horizon agents. Its raw file is `raw/2025-07-25_Papers-Explained-417--Kimi-Researcher-baa1c9f4ae68.md`. It treats strict on-policy trajectory generation as essential, disabling tool-call enforcers so trajectories reflect the model's own probability distribution.
- [[Papers Explained - Advancing Search Augmented Language Models]] supplies an agentic search analogue. Its raw file is `raw/draft_Papers-Explained--Advancing-Search-Augmented-Language-Models-bceb21866e26.md`. It applies on-policy GRPO after SFT and uses token-level importance sampling to correct train-inference mismatch.
- [[Papers Explained 553 - Rubrics as Rewards]] broadens the RL side of the comparison. Its raw file is `raw/2026-04-01_Papers-Explained-553--Rubrics-as-Rewards-229ff69f7355.md`. It shows how on-policy GRPO can use instance-specific rubric rewards when direct verifiers are unavailable.
- [[SFT, RL, and On-Policy Distillation Visual Notes]] contributes a visual X-article treatment of SFT, RL, OPD, forward-vs-reverse KL, entropy collapse, and token-category KL concentration. Its readable raw reconstruction is `raw/x-nrehiew-on-policy-distillation/full-article.md`.

## When OPD Is Attractive

OPD is most attractive when the training team has a strong teacher close to the student, enough rollout infrastructure to sample from the current policy, and a domain where token-level teacher preferences are informative. The Nemotron Cascade 2 recipe is a good example: different intermediate RL checkpoints become domain teachers, and MOPD is used after multi-domain RL to rebalance capabilities that drifted during sequential optimization.

It is also attractive when outcome rewards are available but expensive, delayed, or too sparse for fast convergence. OPD can be used as a recovery or consolidation phase after RL: the RL pipeline discovers specialized domain teachers, then OPD transfers their strengths back into a single student without repeatedly paying the full verifier cost.

OPD is less attractive when the only available teacher is from a very different model family, when the teacher's behavior is known to be misaligned with the target task, or when the goal is to exceed the teacher rather than compress it. In those cases, [[Reinforcement Learning]], [[Verifier-Bounded Learning]], or hybrid RL-plus-distillation recipes may be more appropriate.

## Failure Modes

Teacher ceiling is the main conceptual limit. OPD can transfer or consolidate capability, but without reward or verifier feedback it has no independent way to know that a student token is better than what the teacher would prefer.

Teacher drift and domain imbalance can also matter. If different domain teachers encode incompatible styles or reasoning lengths, the student may inherit unstable mixtures. MOPD's domain-teacher selection in [[Papers Explained 552 - Nemotron Cascade 2]] is a practical response: each training example is paired with the teacher most relevant to that capability domain.

Train-inference mismatch is another implementation hazard. If rollouts are generated by one copy of the policy and optimized by another, stale probabilities can bias the update. Nemotron Cascade 2 addresses this with truncated importance weighting, while the search-agent corpus similarly uses token-level importance sampling in on-policy GRPO.

Finally, dense token-level signals can over-regularize exploration. A teacher may penalize rare but useful actions before a verifier would have a chance to reward them. This is the mirror image of RL's high-variance problem: OPD is stable because it is dense and biased, but that same bias can suppress novel strategies.

## Relationship To Hybrid Recipes

Modern post-training pipelines increasingly combine OPD with RL rather than treating them as substitutes. A likely pattern is:

1. Use SFT to establish instruction following, format, safety, and task priors.
2. Use on-policy RL to discover or sharpen capabilities under verifier, reward, or rubric feedback.
3. Use OPD/MOPD to consolidate strengths from specialized teachers and reduce regressions across domains.

[[Papers Explained 552 - Nemotron Cascade 2]] is the clearest instance in this wiki: Cascade RL improves capabilities, while Multi-domain On-Policy Distillation rebalances them. [[Papers Explained 149 - RLHF Workflow]] and [[Papers Explained - Advancing Search Augmented Language Models]] provide adjacent online-learning recipes where on-policy sampling, importance correction, and reward design carry the training loop.

## Appearances in product training

- [[Inkling-Small]] — post-trained from an Inkling-Small (preview) checkpoint using on-policy distillation with [[Inkling]] as the same-family teacher, before two weeks of agentic coding RL.

- [[Papers Explained 581: Rubric-Guided Self-Distillation]] — RGSD: frozen rubric-conditioned teacher distills per-token clipped JS divergence into an unconditioned student on on-policy rollouts; removes LLM judge from rubric training loop while matching GRPO quality.
- [[Introducing Composer 2.5]] — Cursor uses on-policy distillation KL loss for **targeted textual feedback**: a hint-conditioned teacher (same policy with inserted hint) vs. the original-context student on a single problematic turn, localizing credit assignment inside long agent rollouts while keeping trajectory-level RL.
- [[Sasha Rush Explains Targeted On-Policy Self-Distillation]] — Sasha Rush explains OPD's role in the three-regime progression (sequence KD → OPD → OPSD) and provides an intuitive tennis analogy: sequence KD is watching Nadal play; OPD is having Nadal correct your swing over your shoulder on your own strokes. Also clarifies that OPD integrates cheaply with RL because the student is already generating rollouts and computing log-probs for the RL loss.
- [[Papers Explained: On-policy Distillation with Verifiable Reward]] — OPDVR introduces ReLU gating on sampled-token log-probability ratios to align dense OPD implicit rewards with verifiable trajectory outcomes ($R \in \{-1, +1\}$), and GRPD extends it to group-relative advantage settings like GRPO.

## Related

- [[Inkling-Small]]
- [[Inkling]]
- [[Introducing Composer 2.5]]
- [[Sasha Rush Explains Targeted On-Policy Self-Distillation]]
- [[Targeted Textual Feedback]]
- [[SFT, RL, and On-Policy Distillation Visual Notes]]
- [[On SFT RL and On-Policy Distillation]]
- [[Model Distillation]]
- [[Supervised Fine-Tuning]]
- [[Reinforcement Learning]]
- [[Policy Gradient]]
- [[KL Regularization]]
- [[Verifier-Bounded Learning]]
- [[On-Policy Self-Distillation]]
- [[OPDVR]]
- [[GRPD]]
- [[Reinforcement Learning Topic]]
- [[Papers Explained Corpus]]
- [[Papers Explained 149 - RLHF Workflow]]
- [[Papers Explained - Advancing Search Augmented Language Models]]
- [[Papers Explained 283 - Tulu V3]]
- [[Papers Explained 381 - AceReason-Nemotron]]
- [[Papers Explained 417 - Kimi-Researcher]]
- [[Papers Explained 552 - Nemotron Cascade 2]]
- [[Papers Explained 553 - Rubrics as Rewards]]
- [[Papers Explained 581: Rubric-Guided Self-Distillation]]
- [[Rubric-Guided Self-Distillation]]

### Ingested Additions (2026-08-23 & 2026-08-30)
- [[Papers Explained 589: Weak-to-Strong On-Policy Distillation]] — weak-to-strong student-teacher capacity disparity and mode-seeking reverse KL.
- [[Papers Explained 591: Generalized Knowledge Distillation]] — GKD foundational formulation.
- [[Papers Explained 592: Self-Distilled Reasoner]] — On-Policy Self-Distillation (OPSD).
- [[Papers Explained 593: Self-Distillation Fine-Tuning]] — SDFT in-context teacher fine-tuning.
- [[Papers Explained 594: Teacher-Routed Exploration via Forward KL (TREK)]] — teacher routing and reachability recovery.
- [[Papers Explained 595: Unsupervised On-Policy Self-Distillation]] — label-free self-distillation.
- [[Papers Explained: Kimi K3]] — multi-teacher on-policy distillation.
- [[Papers Explained: On-policy Distillation with Verifiable Reward]] — [[OPDVR]] and [[GRPD]] combining OPD with verifiable rewards.
