# Papers Explained: Is One Layer Enough

Papers Explained: Is One Layer Enough

Papers Explained: Is One Layer Enough

This work presents a systematic layer-wise study of RL training and finds that, training a single transformer layer can recover most of the…

Papers Explained: Is One Layer Enough

This work presents a systematic layer-wise study of RL training and finds that, training a single transformer layer can recover most of the gains achieved by full-parameter RL training. Across seven models spanning two model families (Qwen3, Qwen2.5), three RL algorithms (GRPO, GiGPO, Dr. GRPO), and multiple task domains including mathematical reasoning, code generation, and agentic decision-making, it is observed that RL gains are highly concentrated in a small subset of layers concentrated in the middle of the transformer stack, while layers near the input and output ends contribute substantially less.

Experimental Setup

Models and training configurations
Summary of all models and training configurations.
Training Datasets

NuminaMath-CoT: A large-scale collection of ~860K competition-level math problems with chain-of-thought solutions, sourced from Chinese high school exams, US and international mathematics olympiads, and online mathematics forums. To improve training efficiency, the dataset is randomly downsampled to 50K problems.
DeepScaleR: A curated mathematics dataset containing approximately 40K reasoning-intensive problems, compiled from sources including AIME, AMC, and other competition archives. The same binary answer-matching reward is applied.
DeepCoder: A coding dataset containing approximately 24K programming problems with test cases, compiled from LiveCodeBench and Codeforces. The reward is based on execution correctness: 1 if the generated code passes all test cases, 0 otherwise.
Skywork-OR1: A mathematics dataset containing approximately 48K problems. The same binary answer-matching reward is applied.
ALFWorld: An environment-based agentic benchmark consisting of 2,435 household tasks across six categories. Each task requires the agent to interact with a simulated environment through text commands to achieve a goal (e.g., placing a heated object on a surface). The reward is binary: 1 if the task is completed successfully, 0 otherwise.

Evaluation Datasets

Math (in-domain):

MATH500: 500 competition-level math problems spanning algebra, geometry, number theory, and more.
GSM8K: 8.5K grade-school math word problems requiring multi-step arithmetic reasoning.
OlympiadBench: Olympiad-level mathematics problems.
AMC: Problems from the American Mathematics Competitions.

Code (out-of-distribution):

HumanEval+: Function-level code generation with augmented test cases.
MBPP: Mostly Basic Python Programs, testing basic programming ability.
LiveCodeBench: Recent competitive programming problems collected after model training cutoff dates.

Reasoning (out-of-distribution):

GPQA-Diamond: Graduate-level science questions curated by domain experts.
MMLU-Pro: An enhanced version of MMLU with harder, more discriminative questions.

Language (out-of-distribution):

C-Eval: A comprehensive Chinese evaluation benchmark covering diverse subjects.
IFEval: Instruction-following evaluation measuring the model’s ability to follow specific formatting and content constraints.
MGSM: Multilingual Grade School Math evaluates multilingual mathematical reasoning.

Fair comparison of training methods

A key effort in the study is to ensure that when comparing single-layer training and full-parameter training, any observed differences reflect genuine layer-level variation rather than artifacts of suboptimal hyperparameters or premature convergence.

For each model, the learning rate is tuned for the full-parameter baseline and the value that yields the best performance is selected; this ensures that the full-parameter reference is as strong as possible.
This full-parameter-tuned learning rate is applied to all single-layer training runs, so that no layer receives an unfair advantage or disadvantage from the learning rate choice.
All configurations, including full-parameter and single-layer, use identical hyperparameters for every other setting (batch size, KL coefficient, clip range, number of epochs) and are trained to convergence under the same training steps.
For a number of settings that have publicly available results using the same model, dataset, and methods, such as Dr. GRPO and GiGPO, the best publicly available results are also reported, so as to best anchor full-parameter experiments and the performance achieved by layer-training.

Since the learning rate was tuned only for full-model training and not for layer-wise training, it is investigated whether low-contribution layers could benefit from a higher learning rate, or whether the contribution of high-performing layers could be further improved, through an ablation study and shows that varying the learning rate does not alter the relative ranking of layer contributions.

Single Layer Training Contribution

To quantify each layer’s capacity to capture RL-induced improvement, the concept of layer contribution is defined. Let Sk denote the in-domain performance of the model trained on layer k, measured as the average score across in-domain benchmarks. Sbase denotes the performance of the original pretrained model without any RL training, and Sfull denotes the performance of the model after standard full-parameter GRPO training. The layer contribution of layer k is defined as follows:

Qwen3 Experiments: Layer Contribution Varies Dramatically

Layer contribution C(k) across model scales.

Per-layer training results on the three Qwen3 models.
Layer contributions vary dramatically: some layers individually capture the entire benefit of full training, with up to fourfold differences between the best and worst layers.
Some single layers’ training can surpass full-parameter training, suggesting that joint training may dilute individual layer improvements.
Layers with low contribution (<0.5) show limited capacity to learn from RL signals in isolation, and one layer even yielded negative contribution, degrading performance below the base model (Layer 0 in Qwen3–8B-Base, C = -0.51).
Middle layers consistently show higher contribution, while those near input/output ends contribute less.
High-contribution layers not only improve in-domain capabilities but also enhance out-of-distribution tasks (coding, reasoning, language), indicating genuine capability improvement rather than overfitting.
Layer contribution is a general property, layers strong on math tend to be strong on other tasks too, with a high Pearson correlation (r>0.6) between math and overall scores.

Qwen3 Experiments: Layer Contribution is Consistent Across Datasets and Tasks
Cross-dataset consistency of layer contribution on Qwen3–1.7B-Base.
The per-layer contribution rankings are strongly correlated between the two math datasets (Spearman ρ = 0.76, p < 0.001), indicating that the relative importance of layers is consistent despite differences in data composition and difficulty.
This consistency also extends to cross-domain tasks, with a strong correlation (Spearman ρ = 0.59, p < 0.001) between math and code datasets, suggesting that the same layers tend to have the highest contribution regardless of the specific training task.
The findings establish that layer contribution is an intrinsic property of the pretrained model, governed primarily by its weights rather than the nature of the training data or objective.
Practical implication: Layer selections based on small or accessible datasets can be reliably transferred to guide training on other datasets, enabling efficient transfer of training strategies.

Generalization Across Model Families, Algorithms, and Tasks
Layer contribution C(k) for Qwen2.5-Math-1.5B (28 layers) trained with Dr. GRPO.Per-layer training results on Qwen2.5-Math-1.5B (Dr. GRPO).Layer contribution C(k) on the agentic task ALFWorld, trained with GiGPO.Per-layer training results on Qwen2.5–1.5B-Instruct (GiGPO, ALFWorld).Per-layer training results on Qwen2.5–3B-Instruct (GiGPO, ALFWorld).Layer contribution C(k) for DeepSeek-Distilled-Qwen-7B (28 layers) trained with GRPO on the Skywork mathematics dataset.Per-layer training results on DeepSeek-Distilled-Qwen-7B (GRPO, Skywork).
The highest-contribution layers are consistently in the middle of the network, while layers near the input and output contribute much less.
The best single layer often matches or even surpasses the performance of full-parameter RL training.
This pattern holds across significant changes in model family, RL algorithm, training data, model architecture (including distilled models), and even when the task domain shifts from mathematical reasoning to agentic, multi-step interactive tasks.
Middle-layer concentration and large RL gains persist even when the absolute size of the gain varies greatly between tasks (agentic RL gain ≫ mathematical RL gain, but pattern is unchanged.

Layer contribution summary across all seven models.

This result is robust: In all seven tested models, high contribution is concentrated in the middle layers, weak at the network ends, and a single layer can often recover the full RL improvement.

Guiding Full-Parameter RLVR by Layer Contribution

Since different layers vary in their capacity to absorb RL training signals, differentiating across layers according to their contribution should yield better outcomes than uniform treatment. To address this, three strategies are explored:

Adjusting per-layer learning rates based on layer contribution.
Selectively training only the highest-contribution layers.
A heuristic method for selective training based on layer position.

Layer contribution-guided training strategies across model scales.

Layer-Adaptive Learning Rate

The best k layers ranked by layer contribution (denoted Bk) are selected, and their learning rate is increased to 1 × 10−5, while all remaining layers are trained at the default rate of 5 × 10−6. As a control experiment, the worst k layers (denoted Wk) are also boosted. Experiments are conducted with k ∈ {5, 10} across all three model scale.

Across models and configurations, boosting high-contribution layers consistently improves math performance over the uniform-lr baseline
In contrast, boosting the lowest-contribution layers (Boost Wk) leads to a decline in performance across all three models.
This asymmetry confirms that the improvement is driven by the contribution-guided selection rather than the learning rate adjustment itself.

Layer-Selective Training

Only the best k layers are trained while all remaining layers are kept frozen, with k ∈ {5, 10} across all three model scales.

On Qwen3–1.7B-Base, training only the best layers already exceeds the full-parameter baseline.
On larger models, the improvement is more pronounced.
In both cases, selective training surpasses not only full-parameter training but also the adaptive learning rate strategy.
This suggests that at larger scales, updates to low-contribution layers may not contribute positively to training, and freezing them yields a cleaner optimization.

Heuristic Layer Selection

The preceding strategies require layer contribution rankings derived from per-layer training, which is expensive and impractical for routine use. Since layer contribution consistently exhibits a pattern of higher values in middle layers and lower values near the input and output ends across all three model scales, a simple heuristic is tested: select the middle k layers by position, without any profiling at all. Specifically, for a model with L layers, layers in the range [⌊L/2 − k/2⌋, ⌊L/2 + k/2⌋) are selected and the same selective training setup is applied.

Across all three scales, the heuristic surpasses the full-parameter baseline without any per-layer profiling, and achieves a substantial portion of the improvement of contribution-guided selection.
This result has a practical implication: when even a single round of per-layer profiling is unavailable, simply training the middle layers provides a strong default strategy that captures a meaningful portion of the benefit of contribution-guided selection.

Paper

Is One Layer Enough? Training A Single Transformer Layer Can Match Full-Parameter RL Training 2607.01232

That’s a wrap!

If you enjoyed this breakdown, follow for more. I publish new paper explanations most weekdays.

More papers in this series, organized by lab and topic, are in the start here guide.

What paper should I cover next? Let me know in the responses.

For a complementary look at component-level reasoning localization in LLMs, check out the breakdown of Who Reasons in LLMs?.

View original.

Exported from Medium on August 22, 2026.
