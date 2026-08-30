# Papers Explained 357: Long-To-Short LLM Reasoning With Model Merging

Papers Explained 357: Long-To-Short LLM Reasoning With Model Merging

Papers Explained 357: Long-To-Short LLM Reasoning With Model Merging

This work presents a comprehensive empirical study on model merging for L2S reasoning, exploring diverse methodologies, including…

Papers Explained 357: Long-To-Short LLM Reasoning With Model Merging

This work presents a comprehensive empirical study on model merging for L2S reasoning, exploring diverse methodologies, including task-vector-based, SVD-based, and activation-informed merging. Furthermore, the study investigates the merged model’s ability to self-critique and self-correct, as well as its adaptive response length based on task complexity.

Experiment Setup

The CoT-based LLM reasoning is divided into two categories: short-CoT (quick-thinking) reasoning and long-CoT (slow-thinking) reasoning. Given an input X, quick-thinking reasoning models directly output the final answer, represented as {θ,X} → A. In contrast, slow-thinking models generate both the extensive thinking process and the final answer, denoted as {θ,X} → [T,A].

The effect of model merging is explored on the most frequently used 7B reasoning models, i.e. Qwen2.5-Math-7B and DeepSeek-R1-Distill-Qwen-7B. Evaluations are conducted on popular reasoning datasets: GSM8K, MATH500, Minerva Math, Olympiadbench, College Math and AIME24.

The quick-thinking models are evaluated with few shots and the slow-thinking models are in a zero-shot setting. For activation-based merging methods, the s1K dataset, which contains the high-quality aligned quick-thinking answer and slow-thinking answer for each question, is adopted. The maximum length for quick-thinking models and slow-thinking models are 8K and 10K, respectively. A training-based baseline is also established using DPO, where DeepSeek-R1–7B is trained on the s1K dataset with the short answers as positive samples.

Apart from the evaluations on Qwen-7B models, the effectiveness of model merging is further investigated across different model scales, including the smaller Qwen-1.5B model and larger models such as Qwen-14B and Qwen-32B. To simplify the evaluation process, only the GSM8K, MATH500 and AIME24 datasets are tested in this section.

Main Results
Evaluations of different model merging methods on Qwen-7B models. The number in () indicates the average response length on the dataset.
Task-Vector Based Merging Works
Task-vector based merging methods, especially like TA and Ties-Merging, can achieve long-to-short reasoning with around 50% length reduction alongside accuracy parity or even marginal gains.
Task-vector based merging methods effectively reduce output length while maintaining or improving accuracy.
Average merging reduces length by 34.6% and improves accuracy by 15.8% compared to the quick-thinking baseline, but slightly underperforms the pure reasoning model.
TA and Ties-Merging achieve 48–53% length reduction while maintaining or slightly improving accuracy (+0.3% on average) compared to the reasoning model. This demonstrates that significant length reduction can be achieved with minimal computational cost.
DARE consistently underperforms other merging methods, likely due to large parameter shifts between models exceeding the effective range of DARE and the potentially detrimental effect of dropping critical task vectors. A lower drop ratio (<0.5) than the recommended 0.9 is found to be more effective.
Accuracy improvements are more pronounced on datasets where the quick-thinking and reasoning models have similar initial performance (e.g., GSM8K, College Math).
Merged models struggle to surpass the reasoning model when there’s a large initial performance gap between base models (e.g., MATH500, OlympiadBench).
Length reduction is greater on more complex datasets (e.g., AIME24, OlympiadBench).

SVD-Based Merging Underperforms
SVD-based merging methods exhibit limited effectiveness, delivering moderate performance and serving as viable alternatives only when task vectors inherently possess low- rank spectral characteristics.
SVD-based merging methods (LoRE-Merging and Twin-Merging) outperform average merging methods in terms of both length compression and reasoning accuracy for long-to-short reasoning tasks.
SVD-based merging methods underperform compared to more advanced task-vector-based methods like TA and Ties-Merging.
The effectiveness of SVD-based methods is likely dependent on the distribution of singular values of the task vectors, which was observed to deviate from the ideal distribution in the candidate base models.
While generally moderate in performance, SVD-based methods show consistent performance on complex tasks like AIME24.
Takeaway: SVD-based merging methods offer only moderate performance and are suitable alternatives only when task vectors have inherent low-rank spectral characteristics.

Activation-Based Merging Is The Future
Activation-based merging methods demonstrate superior performance in terms of both reasoning accuracy and response length compression rates; however, their effectiveness is certainly dependent on the choice of the calibration dataset.
Activation-based merging methods (AIM and Sens-Merging) outperform the baseline model (DeepSeek-R1–7B) in terms of overall performance and response length reduction.
Applying AIM to a model merged using Ties-Merging further improves performance by 0.2 points and increases the compression ratio to 55.3%.
Sens-Merging achieves comparable reasoning performance to DPO while significantly reducing response length by about 50%.
Sens-Merging requires gradient computation, impacting efficiency, while AIM relies solely on forward pass activations, making it more efficient.
The performance of both methods is sensitive to the choice of calibration data; alternative datasets resulted in inferior performance.

Analysis On Models With Different Scales

Smaller Models Struggle To Learn From Model Merging
Evaluations of various model merging methods on Qwen-1.5B models. The number in [] indicates the number of reflective responses on the datasetModel merging methods applied to 1.5B-scale models, such as TA, Ties-Merging and Sens-Merging, remain effective on simple tasks. Smaller models struggle to learn long CoT reasoning ability through model merging.
Model merging is less effective for smaller (1.5B) models compared to larger (7B) models, especially on complex tasks.
Activation-based merging (Sens-Merging) generally outperforms task-vector-based methods (TA and Ties-Merging). While task vector methods maintain reasoning performance with shorter responses.
The number of “reflective responses” (instances where the model revisits or corrects its reasoning steps) is negatively correlated with performance in smaller merged models, suggesting these reflections are often incorrect (“false reflections”).
Smaller models struggle to learn effective long CoT reasoning from larger models through merging, potentially due to limitations in capacity or architectural differences.

Length Reduction Is Challenging On Large-Scale Models
The merging of large-scale models poses significant challenges in simultaneously main- taining reasoning performance while substantially reducing response length. The substantial performance gaps between the merging models likely contribute to this difficulty.Evaluations of various model merging methods on Qwen-14B models. The number A in [A;B] indicates the number of reflective responses on the dataset and number B indicates the average frequency of reflection keywords appearing in each response.Evaluations of various model merging methods on Qwen-32B models.
Model merging methods struggle to significantly reduce response length in large-scale models (14B and 32B) compared to smaller models.
Some merging methods, like average merging and Sens-Merging, can even increase response length in large models, though Sens-Merging generally improves reasoning accuracy.
While significant length reduction can be achieved by aggressively tuning hyperparameters (e.g., TA merging with a coefficient of 0.3 achieving 58.6% reduction), this often leads to a substantial drop in reasoning performance.
Performance on the GSM8K benchmark remained relatively stable or even slightly improved after merging in most cases, likely due to the small performance variation among the base models on this benchmark.
Merged models generally did not outperform R1-distilled models on complex mathematical tasks (MATH500, AIME), likely due to the large performance gap between the general-purpose base models and the specialized R1 models. This suggests that merging struggles to add informative knowledge to already strong models.
Evaluations of average merging on Qwen-32B models.
Merging QwQ-32B (a System 2 reasoning model) often resulted in excessively long responses, especially when merged with another System 2 model (R1–32B). This highlights challenges in merging models with significantly different training strategies (reinforcement learning vs. fine-tuning) and parameter disparities.
Introducing an intermediate base model during the merging process can improve the performance of merged models involving QwQ-32B, emphasizing the importance of a pre-trained model in facilitating effective merging.

Further Analysis
Changes in response length and the ratios of reflective responses corresponding to different difficulty levels on the Math500 dataset.
Response length correlates with question difficulty: Longer responses are generated for more challenging questions across all models (System 1, System 2, and merged).
Ratios (%) of responses containing reflective content across various datasets. Scores for Qwen2.5-Math-7B are not reported, as it produces almost no reflective responses.
Merged models retain self-critique and self-correction abilities: While the “System 2” model (DeepSeek-R1–7B) exhibited a high rate of reflective responses (99.3%), the merged models also showed this ability, albeit to varying degrees. The reflection ratio did not directly correlate with reasoning accuracy but did correlate with response length and question difficulty.

Paper

Unlocking Efficient Long-to-Short LLM Reasoning with Model Merging 2503.20641

Hungry for more insights?

Don’t miss out on exploring other fascinating threads in this series. Simply click here and uncover the state-of-the-art research!

Do Subscribe for weekly updates!!

By Ritvik Rastogi on May 2, 2025.

Canonical link

Exported from Medium on May 4, 2026.
