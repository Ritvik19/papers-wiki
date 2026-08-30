# Papers Explained 600: Rubric Dropout

Papers Explained 600: Rubric Dropout

Papers Explained 600: Rubric Dropout

Rubric Dropout is a one-line fix borrowed from neuron dropout to mitigate reward hacking in Rubric-as-Reward RL. At every step, a subset of…

Papers Explained 600: Rubric Dropout

Rubric Dropout is a one-line fix borrowed from neuron dropout to mitigate reward hacking in Rubric-as-Reward RL. At every step, a subset of the rubric’s criteria is randomly dropped before computing the reward, so the policy never optimizes the same rubric twice. The dropped subset is shared across each rollout group, so GRPO’s group-relative advantages stay comparable, and evaluation always uses the full rubric.

Method

For a query x and response y, a rubric is a set of K criteria indexed by k, each with a weight wk. A single judge call grades all criteria at once, returning a verdict sk(x, y) ∈ {0, 1}.

The protocol uses two judges and an OOD evaluation set. Every 20 training steps, the current policy is evaluated on the OOD evaluation set, and each response is graded twice: once with the training (proxy) judge and once with a stronger, cross-family (gold) judge. Four quantities are tracked:

gold score: the gold judge’s score on the OOD evaluation set;
proxy−gold gap: how much the proxy judge over-rates the policy;
overclaim fraction: the share of criteria the proxy marks satisfied but gold rejects, a per-criterion view of the same failure;
in-domain full-rubric reward: what training itself is optimizing, used to check that a mitigation is not just slowing training.

Rubric Dropout
Rubric Dropout is dropout for rubric criteria.
The method has a single hyperparameter, the dropout fraction f ∈ [0, 1). At each training step, a random f-fraction of the rubric’s positive-weight criteria is dropped, always keeping at least three, and the same reward is computed on the kept criteria only. Writing m ∈ {0, 1}K for the keep-mask (mk = 1 means criterion k is kept).

Dropout never touches a protected set reserved for safety-critical criteria, and evaluation always scores the full rubric.

There is one place where dropout could go wrong. If each rollout drew its own mask, the G responses would be graded on different sub-rubrics, and comparing them within the group would be meaningless. So one mask is drawn per rollout group. Every rollout of a prompt at a given step is scored on the same sub-rubric, and the mask changes from step to step.

Its real effect is the noise it injects, which lands hardest on responses whose advantage hinges on a single criterion and barely touches responses that are broadly better than their group, the same anti-co-adaptation logic as neuron dropout.

Experiment Setup

Qwen3–8B is trained with GRPO (16 rollouts per prompt, learning rate 10^−6) on two independent train→eval pairs: RubricHub-Medical → HealthBench-Hard (1,000 prompts, physician-written rubrics) and RubricHub-Science → ResearchQA (survey-derived rubrics, scored on the 368 validation prompts that never occur in training). The proxy judge is gpt-4o-mini and the gold judge is claude-sonnet-4–6.

Evaluation
OOD gold score on both pairs at both model sizes.Proxy−gold gap and overclaim fraction.
Reward Hacking Emerges with Standard Training: In base runs (no dropout), true quality (gold judge score) increases at first and then collapses despite continued proxy-reward improvement, indicating classic reward hacking.
Dropout Consistently Raises True Quality: Applying 30% or 50% rubric dropout improves average gold judge scores over the comparison window in both domains and model size
Ablations on the Medical pair.
Optimal Dropout Range Is Robust: Across dropout sweeps (20–60%), any fraction in the 30–50% range yields robust and forgiving improvements, the metric is not sensitive, and performance only degrades above 50–60% dropout.

Paper

Rubric Dropout: A Simple Way to Mitigate Reward Hacking in Rubric-as-Reward RL 2608.11669

That’s a wrap!

If you enjoyed this breakdown, follow for more. I publish new paper explanations most weekdays.

More papers in this series, organized by lab and topic, are in the start here guide.

What paper should I cover next? Let me know in the responses.

By Ritvik Rastogi on August 21, 2026.

Canonical link

Exported from Medium on August 22, 2026.
