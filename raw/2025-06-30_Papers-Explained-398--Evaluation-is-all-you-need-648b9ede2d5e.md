# Papers Explained 398: Evaluation is all you need

Papers Explained 398: Evaluation is all you need

Papers Explained 398: Evaluation is all you need

This study reveals that the benchmark evaluation results of reasoning models are subject to significant fluctuations caused by various…

Papers Explained 398: Evaluation is all you need

This study reveals that the benchmark evaluation results of reasoning models are subject to significant fluctuations caused by various factors. Subtle differences in evaluation conditions can lead to substantial variations in results, making their claimed performance improvements difficult to reproduce reliably.

To address this, the community should adopt a rigorous evaluation paradigm:

Use dynamic seeds, document all settings transparently, and report confidence intervals rather than peak scores.
Calibrate N-sampling theoretically for stability, considering both model scale and benchmark characteristics.
Promote standardized evaluation frameworks to ensure fair and reproducible model comparisons.

Experiment Setup

Popular reasoning models on Hugging Face with more than 500 total downloads (as of April 26, 2025) are selected as evaluation targets. These include:

32B scale: DeepSeek-R1-Distill-Qwen-32B, QwQ-32B , Skywork-OR1–32B-Preview, TinyR1–32B-Preview
14B scale: DeepSeek-R1-Distill-Qwen-14B, DeepCoder-14B-Preview, Light-R1–14B-DS
7B scale: DeepSeek-R1-Distill-Qwen-7B, Light- R1–7B-DS, Skywork-OR1-Math-7B
1.5B scale: DeepSeek-R1-Distill-Qwen-1.5B, DeepScaleR-1.5B-Preview, Open-RS1, Open-RS2, Open-RS3, DeepCoder-1.5B-Preview, ZR1–1.5B, OpenRS-GRPO, FastCuRL-1.5B-Preview, STILL-3–1.5B-preview

All the models are evaluated on three benchmarks:

AIME24
AIME25
GPQA Diamond

All experiments adopt the following control group configuration:

N: 64.
Seed: Dynamic seed.
Instruction position: Instruction placed after the question.
Option and answer bias in GPQA Diamond: Options ordered as (A → B → C → D), with the correct answer placed at A.
Tensor Parallelism setting: 1 for model sizes no larger than 14B and 2 for 32B models.

Evaluation dataset version:

AIME24: simplescaling/aime24_figures
AIME25: simplescaling/aime25_figures
GPQA Diamond: Idavidrein/gpqa

Evaluation

Average N

To investigate how the number of independent inferences (N) influences evaluation outcomes of language models.

Model performance is evaluated with different values of N (number of independent inferences). The result obtained with N = 64 is treated as the approximate ground truth. The absolute deviation (fluctuation) between evaluation results at smaller N values and the ground truth is calculated.

Fluctuations generally approach 1 percentage point at N = 32 across all four model variants.
Over 75% of experiments still exhibit deviations beyond the baseline fluctuation range.
Performance fluctuation is influenced by N, model size, and the benchmark dataset.
Deepseek-R1-Distill-Qwen-1.5B model shows the largest fluctuation.
GPQA Diamond exhibits relatively smaller fluctuation.

Seed

To investigate the influence of the random seed parameter on the stability of model evaluation results.

A “fixed-seed N-times inference setup” (1-Seed-N) is designed, where each sample is inferred N times using the same fixed seed. 16 random seeds are selected, and N is set to 16.

Evaluation results fluctuate significantly based on the seed used, much more than baseline fluctuations. Small models can outperform larger models with specific seeds.

Evaluation Dataset Version

To investigate the extent to which differences between AIME dataset versions affect evaluation results of reasoning models.

Performance variation for the same reasoning model across different versions of evaluation datasets is substantial, often exceeding the baseline reference fluctuation. The maximum observed discrepancy reached up to 3.9 percentage points.

Instruction Position

To investigate how the position of an instruction (prompt) relative to a question affects model performance on AIME tasks.

Two experimental groups are used: one with the instruction placed before the question and another with the instruction placed after the question. The instruction used is: “Let’s think step by step and output the final answer within \boxed{}.”

The position of the instruction has a relatively minor impact on evaluation outcomes (less than 2 percentage points difference).
Placing the instruction after the question generally yields slightly better performance, potentially due to the model’s training data format.
Instruction position can affect evaluation stability, with some model-benchmark combinations performing slightly better when the instruction is placed before the question.

Option and Answer Bias in GPQA Diamond

To investigate whether option order and the position of the correct answer in multiple-choice questions (MCQs) influence the performance of reasoning models on the GPQA Diamond benchmark.

Created four experimental groups: Control Group, Option Bias Group, Answer Position Bias Group, and Randomized Group, each manipulating option order and correct answer position.

Control Group: Uses a fixed option order (A → B → C → D), with the correct answer always placed as option A.

Option Bias Group: The correct answer is always the first option, but the order is permuted as follows:

(B → A → C → D)
(C → A → B → D)
(D → A → B → C)

Answer Position Bias Group: The option order remains (A → B → C → D), but three subgroups are constructed where the correct answer is placed in option B, C, or D, respectively.

Randomized Group: Options are ordered as (A → B → C → D), but the correct answer is randomly placed in one of the four positions.

Changes in option order and answer position caused consistent and significant performance fluctuations (mostly above 5 percentage points).
Scores in the Randomized Group were generally lower than in the Control Group, suggesting that randomizing option order may reduce model stability.
The Control Group (correct answer always in the first position) consistently outperformed other groups in the Answer Position Bias experiments, suggesting that placing the correct answer directly after the question might improve model performance.

Tensor Parallelism

To investigate how Tensor Parallelism (TP) influences the evaluation results of reasoning models.

The evaluation results of DeepSeek-R1-Distill-Qwen-1.5B, DeepSeek-R1-Distill-Qwen-7B and DeepSeek-R1-Distill-Qwen-14B models are compared with TP=1 (default) to those with TP=2.

Changing the TP setting has a limited impact on evaluation performance, with fluctuations of less than 2 percentage points across benchmarks.
67% of the experimental groups exhibited fluctuation ranges that exceeded the baseline reference.

Paper

Evaluation is All You Need: Strategic Overclaiming of LLM Reasoning Capabilities Through Evaluation Design 2506.04734

Hungry for more insights?

Don’t miss out on exploring other fascinating threads in this series. Simply click here and uncover the state-of-the-art research!

Do Subscribe for weekly updates!!

By Ritvik Rastogi on June 30, 2025.

Canonical link

Exported from Medium on May 4, 2026.
