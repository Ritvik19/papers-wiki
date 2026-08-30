# Papers Explained 594: Teacher-Routed Exploration via Forward KL (TREK)

Papers Explained 594: Teacher-Routed Exploration via Forward KL (TREK)

Papers Explained 594: Teacher-Routed Exploration via Forward KL (TREK)

TREK (Teacher-Routed Exploration via Forward KL) is a simple staged procedure that uses distillation not for imitation but for exploration…

Papers Explained 594: Teacher-Routed Exploration via Forward KL (TREK)

TREK (Teacher-Routed Exploration via Forward KL) is a simple staged procedure that uses distillation not for imitation but for exploration support expansion. It first identifies prompts where the unaided student has very low pass rate, queries a proposal source to produce verified candidate solutions, keeps the top-r proposals ranked by current student likelihood, applies a short forward-KL phase to pull those verified modes into the student’s support, and then returns to standard on-policy GRPO refinement.

Method
Overview of TREK as distillation for exploration support expansion.
Problem Setup and Failure Mode

Standard GRPO optimizes the student from responses sampled from its current policy. The key limitation for GRPO is that it can only reinforce modes that the student already samples. Prompts with low pass rates are hard candidates: the unaided student fails to discover useful trajectories under the current sampling configuration. A hard candidate becomes useful for proposal learning only if the proposal source later produces at least one verified trajectory. This is the setting in which distillation is treated as exploration support expansion rather than denser supervision on already-sampled rollouts.

For a verified teacher trajectory yT, let

be its token-level student NLL. Reachability is measured with a two-sided trimmed length-normalized NLL,

where Iα,β (yT) removes the lowest α fraction and highest β fraction of token losses before averaging. The low-end trim prevents high-confidence boilerplate or formatting tokens from making a trajectory look artificially close, while the high-end trim prevents isolated rare-token outliers from making it look artificially far. The resulting quantity is a reachability score, not yet a training loss: smaller dS(yT | x) indicates a verified trajectory closer to the student’s current support.

Because absolute NLL scales differ across prompts, the prompt-relative form is also used as an analysis variable, where the expectation is estimated from the same student rollouts already drawn for pS (x).

Prompt Routing and Reachability

The proposal policy πT is used to generate candidate solutions for hard prompts. It may be a larger model, but the most deployment-aligned setting is the same student family run with additional inference-time context. Examples include verifier-guided retry, self-consistency, search, environment interaction, reflection, failure lessons, or a longer reasoning budget. This extra context or computation may help discover solutions.

For each routed hard prompt, proposal trajectories that fail the verifier are discarded. Among the verified trajectories, ranking is done by current student likelihood and the top-r student-proximal verified proposals are kept.

This rule makes proposal learning conditional on teacher success while avoiding broad imitation of trajectories far from the student’s current support. The hyperparameter r trades off multi-mode coverage against transfer stability.

Proposal Learning and On-Policy Refinement

On routed hard prompts, Yreach(x) defines the target for a short support-expansion update. If teacher probabilities are available, the retained proposal distribution can be written as:

Explicit teacher probabilities are not required; retained samples are sufficient. At the distributional level, proposal learning minimizes

on selected prompts. The forward direction penalizes missing proposal support and encourages the student to cover the retained solution modes. In black-box or context-only settings, this reduces to teacher-forced negative log-likelihood on retained proposal samples:

This SFT-like update is applied only on the selected proposal dataset.

Experiment Setup

TREK consistently improves performance over direct GRPO baselines across all model scales and benchmarks, especially on harder tasks/prompts.
Math results across Qwen3 scales on AIME 2024 and AIME 2025 (avg@16, %).
TREK using DeepSeek-V4 proposals gains +5.4 to +6.4 points on AIME 2024 and +2.8 to +4.9 on AIME 2025 across Qwen3 scales. Self-context variant also outperforms direct GRPO, and forward-KL consolidation is shown to be superior to OPD-style supervision.
Agentic task final success rate (%) with Qwen2.5–7B-Instruct on ALFWorld and ScienceWorld.Per-task-type ALFWorld success rate (%) for the DeepSeek-V4 TREK variant across all six task types, ordered by GRPO baseline success (lowest first).
On ALFWorld, TREK raises success from 75.8 (GRPO) to 82.8 (DeepSeek-V4 proposals), and to 80.4 (self-context). On ScienceWorld, success more than doubles from 12.5 (GRPO) to 26.7 (TREK, DeepSeek-V4) and reaches 23.4 for self-context.
Gains from TREK concentrate on the hardest task types, supporting the central claim: support-expansion proposals most benefit areas where unaided exploration fails.

Paper

TREK: Distill to Explore, Reinforce to Refine 2607.05339

That’s a wrap!

If you enjoyed this breakdown, follow for more. I publish new paper explanations most weekdays.

More papers in this series, organized by lab and topic, are in the start here guide.

What paper should I cover next? Let me know in the responses.

By Ritvik Rastogi on August 13, 2026.

Canonical link

Exported from Medium on August 22, 2026.
