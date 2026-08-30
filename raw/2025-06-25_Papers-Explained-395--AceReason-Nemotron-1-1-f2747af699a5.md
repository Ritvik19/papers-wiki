# Papers Explained 395: AceReason-Nemotron 1.1

Papers Explained 395: AceReason-Nemotron 1.1

Papers Explained 395: AceReason-Nemotron 1.1

AceReason-Nemotron-1.1 7B is a reasoning model developed by leveraging the synergy between supervised fine-tuning (SFT) and reinforcement…

Papers Explained 395: AceReason-Nemotron 1.1

AceReason-Nemotron-1.1 7B is a reasoning model developed by leveraging the synergy between supervised fine-tuning (SFT) and reinforcement learning (RL).

This work suggests that scaling the number of prompts and the number of generated responses per prompt during SFT training leads to substantial improvements in reasoning performance. Scaling the number of prompts yields more significant gains.

The research further investigates the relationship between SFT and RL, finding that a stronger SFT model generally leads to better final performance after RL training, provided effective RL training is conducted.

The models and data are available on HuggingFace.
Training Pipeline of AceReason-Nemotron 1.1.
Supervised Fine-Tuning

Prompts are collected from AceMath dataset, NuminaMath, and OpenMathReasoning for math. For coding, prompts are collected from TACO, APPs, OpenCoder-Stage2, and OpenCodeReasoning. Dataset deduplication is conducted to ensure that each prompt is unique. After that, data decontamination is conducted and the sample that has a 9-gram overlap with any test sample in math and coding benchmarks is filtered. DeepSeek-R1 is used to generate responses for the collected prompt set. Intuitively, longer model responses often correspond to more difficult questions. Based on this observation a subset of the prompts whose responses around or below 2,000 tokens in length is randomly filtered out and the proportions of other difficulty levels are adjusted through additional random sampling. This resulted in a final dataset of 247K math prompts and 136K code prompts, totaling 383K prompts.

Reinforcement Learning

The stage-wise RL approach is applied on math-only and code-only prompts in sequence, to SFT models utilizing the high-quality math and code RL data from AceReason-Nemotron-1.0. Specifically, the GRPO algorithm is employed and on-policy training is strictly adhered to by generating 𝐺= 8 or 16 rollouts for each question 𝑞in a global batch of 128 prompts, followed by a single policy gradient update. The token-level policy gradient loss is utilized, which assigns greater rewards to longer samples when the answer is correct and harsher penalties when it is incorrect. The intuition is that learning to generate longer samples plays a more critical role in enhancing reasoning capabilities. The KL divergence term is removed as well. As a result, the GRPO objective can be reduced to:

where a question-answer pair (𝑞, 𝑎) is sampled from the training dataset 𝒟, {𝑜𝑖} are responses generated for 𝑞 by the current policy 𝜋𝜃(· | 𝑞), and token-level advantages 𝐴𝑖,𝑡 are estimated as:

Training process

Math-only Stage-1 (8K): This initial stage with 8K response length budget serves as a warm-up phase for RL training. Relatively simple questions sampled from a collected RL dataset are used for training. Most of these questions elicit responses from DeepSeek-R1 with token lengths predominantly between 2K and 4K. During this stage, an initial decline in model performance is observed, followed by a recovery to nearly the original level. Although this stage does not yield a net performance gain by itself, experiments show that it is essential — skipping directly to Stage-2 (16K) results in suboptimal outcomes. It is hypothesized that the model uses this stage to facilitate the transition from imitation learning (SFT) to reinforcement learning.
Math-only Stage-2 (16K): At this stage of training, the proportion of more challenging questions is increased compared to Stage 1. As a result, the model’s average response length gradually increases, and a substantial performance improvement is observed — similar to what was seen in AceReason-Nemotron-1.0, even though starting from a much stronger SFT model.
Math-only Stage-3 (24K): Most of the simple questions are filtered out and around 2500 hard ones are kept for the training of this stage. The model shows a significant performance improvement on math benchmarks in this stage.
Code-only Stage-I (24K): False positive and false negative rewards are generally more prevalent in the code domain than math domain due to the nature and lower quality of test cases. Conducting math-only RL beforehand helps to enhance the model’s reasoning capabilities, facilitates generalization from math to code, and better prepares the model for the relatively “noisier” code-only RL training that follows.
Code-only Stage-II (32K): In this stage, the epoch-wise filtering strategy is applied — starting after the first epoch — as in AceReason-Nemotron-1.0. Specifically, easy problems that can be fully solved by the previous epoch’s checkpoint are removed, i.e., problems for which every rollout passes all test cases.
Math-only Stage-4 (32K): As in the math-only Stage-3 (24K) setup, most of the simple questions — those that can be solved by every rollout — are filtered out and only the challenging ones are retained for training in this final stage.

Evaluation

Main Results
Evaluation of reasoning models primarily based on Qwen2.5-Math 7B and Llama-3.1 8B to disentangle the impact of pretraining.
The SFT model achieves slightly better results than Llama-Nemotron-Nano-8B-v1 and much better performance compared to Light-R1 and DeepSeek-R1-Distill-Qwen-7B.
Applying the AceReason RL training recipe to the SFT model substantially improves performance, yielding significant score gains on AIME24, AIME25, LiveCodeBench v5, and LiveCodeBench v6.
The RL model, AceReason-Nemotron-1.1–7B, achieves the highest accuracy among 7B-scale models on AIME25 and LiveCodeBench v6.
A well-curated RL recipe can significantly boost a model’s reasoning capability, even when starting from a strong SFT model.

SFT Analyses

The investigation explores the impact of scaling the Supervised Fine-Tuning (SFT) dataset on model performance, focusing on two key aspects:

Increasing the number of unique prompts: This expands the coverage of different problem types and topics.
Increasing the number of responses per prompt: This allows the model to learn from diverse reasoning paths for the same input.

Seven SFT datasets (v1 to v7) are created, ranging in size from 36K samples (v1) to 2.2M samples (v7), while maintaining a similar distribution of response token lengths. Datasets v1 to v4 primarily focused on increasing unique prompts with a single response per prompt. Datasets v5 onwards scaled both the number of unique prompts and the number of responses per prompt.
Log-scaled data statistics for the number of math and code prompts and the average number of responses per prompt.

Accuracies on AIME24, AIME25, and LiveCodeBench V5 and V6 for different SFT datasets.

To determine the relative importance of each scaling factor, a multiple linear regression analysis is performed. The model related overall accuracy (z) to the number of unique prompts (x) and the number of responses per prompt (y) using the equation:

The least squares method is used to fit the model using the seven data points. Before fitting, x and y are transformed to a log base-2 scale and standardized. The dependent variable z is defined as the average accuracy across AIME24, AIME25, and LiveCodeBench V5 and V6.

The resulting estimates were:

a = 4.831
b = 2.635
R² = 0.989

The high R² value indicates a strong fit. The larger value of ‘a’ compared to ‘b’ suggests that increasing the number of unique prompts has a greater impact on SFT model performance than increasing the number of responses per prompt.
Accuracies over different epochs of training for SFT dataset v6 and v7.
The model’s performance gradually improves from the 1st to the 5th epoch and begins to plateau around the 5th to 6th epoch. This pattern is consistent across different versions of the SFT dataset. A certain degree of ‘overfitting’ may actually enhance test accuracy in long chain-of-thought (CoT) generation, likely due to exposure bias in autoregressive models.

RL Analyses

RL starting from different SFT models
Math-only RL training starting from different SFT (distillation) models.
Significant performance gains are generally observed at stage-2 (16K) and stage-3 (24K). The performance begins to plateau at stage-4 (32K) for the model initialized from SFT-7B v7, as further gains become more challenging on top of an already strong model.
While some SFT models show substantial performance gaps (e.g., between SFT-7B v5 and v7), these differences become much smaller after applying RL training over more steps.

How training temperature affects the progress of RL

Impact of varying temperatures for inference and RL training.

Importance of Temperature Tuning: The temperature parameter in RL training needs careful tuning to balance exploration and exploitation.
Low Temperature (e.g., 0.6): Leads to over-exploitation, limited exploration, and sub-optimal performance.
High Temperature (e.g., 1.0): Causes excessive exploration, low initial rewards, reduced entropy, and hindered learning progress.
Rule of Thumb: Setting the training temperature such that the temperature-adjusted entropy remains around 0.3 typically leads to effective RL training.
Moderate Temperature: A temperature of 0.85 starts with an entropy of approximately 0.26, which gradually increases to around 0.38 during training.
Inference Temperature: A temperature of 0.6 is consistently better for inference.

RL improves upon the SFT model in terms of pass@K even when K is large
Comparison of pass@K scores between AceReason-Nemotron-1.1–7B and the SFT-7B v7 model it is trained from.
AceReason-Nemotron’s pass@K results suggest that Reinforcement Learning (RL) improves pass@K as K increases.
Experiments on math and code benchmarks show that RL training consistently improves pass@k accuracy from K = 8 to K = 128.
These findings are consistent with AceReason-Nemotron, even though the RL model was initialized from a stronger SFT baseline (SFT-7B v7) compared to the DeepSeek-R1-Distill-Qwen-7B model used in their study.
For the AIME25 math benchmark, the improvement from RL decreases as K increases (e.g., from 8.3% at K = 8 to 1.2% at K = 128) because AIME’s answer space is limited to positive integers with a maximum value in the hundreds.
The gains on coding benchmarks like LiveCodeBench V5 and V6 remain significant, with LiveCodeBench V6 still showing a 5% improvement at K = 128.

RL improves over strong SFT model by solving hard problems
Comparison of problem-level solving rates between AceReason-Nemotron1.1–7B and the SFT-7B v7 model it is trained from.
AceReason-Nemotron found that Reinforcement Learning (RL) training helps solve hard coding problems that the initial Supervised Fine-Tuned (SFT) model, DeepSeek-R1-Distill-Qwen-7B, couldn’t solve even with many attempts.
RL training significantly improves performance on problems where the SFT model’s accuracy is below 20%.
This finding remains valid even with a stronger initial SFT model than the one used in AceReason-Nemotron-1.0.
AceReason-Nemotron-1.1–7B can solve a long tail of difficult coding problems on LiveCodeBench that the SFT model fails to solve within 128 attempts.
This leads to over ten additional problems solved on both LiveCodeBench V5 and V6.

Paper

AceReason-Nemotron 1.1: Advancing Math and Code Reasoning through SFT and RL Synergy 2506.13284

Hungry for more insights?

Don’t miss out on exploring other fascinating threads in this series. Simply click here and uncover the state-of-the-art research!

Do Subscribe for weekly updates!!

By Ritvik Rastogi on June 25, 2025.

Canonical link

Exported from Medium on May 4, 2026.
