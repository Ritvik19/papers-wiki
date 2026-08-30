# Papers Explained 579: Policy-Aware Rubric Reward (POW3R)

Papers Explained 579: Policy-Aware Rubric Reward (POW3R)

Papers Explained 579: Policy-Aware Rubric Reward (POW3R)

Rubric-based reinforcement learning for language models often aggregates multi-criteria rewards using static human-assigned weights, but…

Papers Explained 579: Policy-Aware Rubric Reward (POW3R)

Rubric-based reinforcement learning for language models often aggregates multi-criteria rewards using static human-assigned weights, but this approach misallocates training pressure because many criteria are saturated or unreachable and thus provide no learning signal; human importance and current learnability are uncorrelated. The proposed POW3R framework dynamically reallocates training focus toward rubric criteria that currently distinguish model outputs, while preserving original human weights and category balance, resulting in substantially faster and more effective policy improvement across multiple models and datasets.

Method

For a prompt 𝑞, the rubric set is 𝑅(𝑞) = (𝑐𝑗, 𝑤𝑗, 𝜅𝑗)

𝑐𝑗 : Each criterion for evaluating the response.
𝑤𝑗 : Human-assigned static weight for criterion (how important it is).
κ𝑗 : Category label indicating which category 𝑐𝑗 belongs to.

An LLM judge scores the response: 𝑠𝑗(𝑜,𝑞) ∈ [0, 1 ]. If 𝑠𝑗(𝑜, 𝑞) = 1, the response fully satisfies 𝑐𝑗.

Standard Rubric Reward is a weighted sum of scores but it assumes:

Categories have similar number of criteria.
Criteria in a category are equally informative.
𝑤𝑗 reflects both importance and current training utility.

POW3R relaxes these by dynamically reallocating category weight to criteria that are most helpful for current learning. Importantly, it does not alter the rubric, judge scores, or human weights.

Category-Normalized Baseline

Category-Normalized Reward ensures every category contributes equally to the reward, regardless of size or weight. It normalizes within categories and across categories.

K_q = number of non-empty categories for prompt 𝑞.
𝐶_𝑘(𝑞) = set of criteria in category 𝑘.
𝑊_𝑘(𝑞) = ∑𝑗∈𝐶_𝑘(𝑞) 𝑤𝑗 = total weight in category 𝑘.

Inside each category, the weighted sum is normalized by 𝑊_𝑘(𝑞)

Policy-Aware Factors

Policy-aware factors are dynamic adjustments applied to each rubric criterion during reward calculation.

Each criterion’s factor 𝛼_𝑗^(𝑡) starts at 1 for epoch 𝑡, and is applied to all 𝐺 rollouts.

After the epoch, judge calls yield each criterion’s pass rate and variance:

where 𝑠𝑗(𝑜𝑖, 𝑞) is the score for rollout 𝑖 on criterion 𝑗 and 𝑉𝑗 is the set of rollouts with valid scores.

Smooth the variance (add 𝜖 for stability) and Category-normalize (Average 𝑔_𝑗^(𝑡) across all criteria 𝑗 in the category (weighted by their static weights))

For each criterion 𝑗, compute the ratio of its smoothed variance to the category average and then Blend between 1 and this ratio using parameter 𝜆 (trade-off between prior and rollout contrast), and clip to [𝛼_min, 𝛼_max]

Update 𝛼𝑗^(𝑡+1) with exponential moving average (speed set by 𝛽_ema), and clip to the allowed range:

Criteria with too few valid verdicts (< 0.75G rollouts) retain their previous factor.
If all valid signals in a category vanish, set ^𝛼_𝑗^(𝑡) = 1.

POW3R reward

At epoch t, set w˜ (t) j = wjα (t) j and W˜ (t) k (q) = ∑j∈Ck (q) w˜ (t) j , then compute

then keeps category mass uniform and uses wj as prior.

Experimental setup

Datasets:

HealthBench (HB): English-language prompts only, using native physician-authored point-valued criteria. The 500-task “hard” split is used for testing and 10% of the remaining English training prompts as dev set.
MM (Multimodal): 10k-task dataset pairing images with prompts and rubric sets spanning six quality categories. Images include charts, diagrams, photos, screenshots, and natural scenes. Each rubric criterion is anchored to specific visual or textual instructions.

Models:

MM (multimodal) models: Qwen3-VL-4B-Instruct, Qwen3-VL-8B-Instruct, Gemma 3 4B-IT.
HB (text-only) models: Qwen3–4B-Instruct-2507, Qwen3–8B, Gemma 3 4B-IT.

Reward Judging:

Each (prompt, rollout, criterion) triple gets a reasoning-then-verdict call from a reward judge, giving a one-sentence rationale and a binary {0,1} decision.
Training rewards use GPT-5.4-nano with medium-effort reasoning/explanations.
Held-out evaluations are re-scored by GPT-5.4-mini for judge–training disentanglement.
Both judges use T=1.0 and up to 2048 completion tokens.

Results
Held-out evaluation on MM test and selected external VLM benchmarks.HealthBench English test split.
POW3R outperforms other rewards: POW3R achieves the best score on 24 of 30 base-policy/metric comparisons.
Main result visual summary.
Dominance in two-objective space: POW3R Pareto-dominates other reward constructions on both mean quality and strict all-criteria satisfaction, emphasizing that high mean scores don’t always mean full rubric compliance.
Cross-setting consistency: the ordering of test gains is consistent between multimodal and text-only settings, and POW3R’s smallest improvement is still a substantial +3.7 percentage points; this indicates POW3R’s robustness and its independence from dataset-specific rubric conventions.
Per-category validation reward trajectories (Qwen3-VL-4B, MM).
Consistent gains across categories: POW3R shows consistent improvement over static baselines, particularly in contrastive categories like Visual Perception, Visual Reasoning, Truthfulness, Content, and Instruction Following. Gains are less pronounced for Writing Style, which is mostly handled by the base policy

Paper

Not Every Rubric Teaches Equally: Policy-Aware Rubric Rewards for RLVR 2605.20164

Hungry for more insights?

Don’t miss out on exploring other fascinating threads in this series. Simply click here and uncover the state-of-the-art research!

Do Subscribe for weekly updates!!

View original.

Exported from Medium on June 13, 2026.
