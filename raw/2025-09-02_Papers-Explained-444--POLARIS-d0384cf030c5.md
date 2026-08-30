# Papers Explained 444: POLARIS

Papers Explained 444: POLARIS

Papers Explained 444: POLARIS

POLARIS is a post-training recipe focused on calibrated data difficulty, enhanced data diversity, inference-time length scaling, and…

Papers Explained 444: POLARIS

POLARIS is a post-training recipe focused on calibrated data difficulty, enhanced data diversity, inference-time length scaling, and efficient training, designed to scale reinforcement learning on advanced reasoning models.

POLARIS-4B-Preview is fine-tuned from Qwen3–4B and POLARIS-7B-Preview is fine-tuned from Deepseek-R1-Distill-Qwen-7B .

Data Difficulty

Previous RL training methods, while effective for smaller models (e.g., 1.5B parameters), showed only marginal improvements or even performance decline when applied to more advanced models like Qwen3. The core issue identified was that existing datasets, such as DeepScaleR, were often too simple for larger models. For instance, a 7B model quickly achieved high rewards, indicating the training set lacked sufficient challenge to drive further learning.

Deepseek-R1-Distill-Qwen-7B and its 1.5B version are used to evaluate the DeepScaleR dataset. For each problem, 8 solutions were generated, and the pass rate served as a proxy for difficulty. A “mirror effect” was noted:

The 1.5B model showed a “mirrored J-shaped” (Ⴑ) distribution, with most problems being extremely difficult.
The 7B model showed a “standard J-shaped” distribution, with the vast majority of problems being far too easy.

This confirmed that the dataset, while challenging for a smaller model, was insufficient for a larger one.

Using the Deepseek-R1-Distill-Qwen-7B model,distinct training sets are created by altering difficulty:

Full Dataset (40K samples): Original J-shaped, dominated by easy samples.
Removal of Perfect Scores (26K samples): Created a mirrored J-shaped distribution by removing problems with 8/8 correct solutions.
Aggressive Filtering (19K samples): Focused only on the hardest problems (pass rate > 4/8 filtered out).
Model performance across the three above mentioned conditions.
Removing the easiest samples led to consistent performance improvements. Both the unfiltered (too easy) and aggressively filtered (overly difficult) datasets hindered training progress.

POLARIS’s Data Curation Strategy

For each potential training problem, the specific model being trained generates 8 rollouts. The pass rate of these rollouts determines the problem’s difficulty relative to that model.

To achieve the desired mirrored J-shape, all samples that the model solves perfectly (8/8 correct) are removed.

For Deepseek-R1-Distill-Qwen-7B, filtering DeepScaleR and AReaL datasets resulted in a 53K sample training set.
For the Qwen3–4B model, an additional filtering pass on this 53K set was performed, yielding a 30K sample dataset specifically calibrated to its difficulty level.

Dynamically drop easy data during training

As RL training progresses, the model’s capabilities improve, and the proportion of difficult questions naturally decreases, causing the distribution to shift back towards a J-shape.
Data Difficulty Distribution Shifts (Left: Before Training, Right: After-Training; Top: Qwen3–4B, Bottom: Deepseek-R1-distill-Qwen-7B)
During training, each sample’s accuracy is dynamically updated after reward computation. At the end of each training phase, samples with an accuracy greater than 0.9 are removed. This dynamic filtering ensures the model continuously faces appropriately challenging samples, preventing the learning signal from degrading due to an overabundance of mastered problems.

Diversity-based Rollout Sampling

In GRPO training, diversity among sampled trajectories is crucial for several reasons:

Enhanced Trajectory Contrast: High diversity encourages the model to generate both positive and negative trajectories within a single rollout, which is essential for effective trajectory contrast.
Wider Exploration: It allows the model to explore a broader range of potential reasoning paths, preventing it from becoming overconfident in a narrow set of patterns.

While top-p and top-k are typically set to maximize diversity (1.0 and -1 respectively), the sampling temperature remains the primary adjustable hyperparameter for controlling diversity.
Rollout diversity with sampling temperature on R1-Distill-Qwen and Qwen3 across different model sizes.
Higher sampling temperatures generally lead to better diversity in generated rollouts. However, different models exhibit varying diversity performance at the same temperature.
Model performance with sampling temperature on R1-Distill-Qwen and Qwen3 across different model sizes.
Model accuracy typically follows a “low-high-low” trend as temperature increases. Each model has a unique optimal temperature range, highlighting the need for model-specific calibration.

To guide temperature selection, POLARIS categorizes temperature settings into three zones:

Robust Generation Zone (RGZ): Where the model’s performance is optimal and stable. Recommended decoding temperatures usually fall here, but they often result in low diversity.
Controlled Exploration Zone (CEZ): Leads to a slight, acceptable performance degradation but significantly increases rollout diversity. This zone is crucial for exploration during training.
Performance Collapse Zone (PCZ): In this zone, the temperature is too high, causing the model to output noisy tokens and leading to a drastic drop in performance, making it unsuitable for training or decoding.

POLARIS implements a dynamic temperature adjustment strategy:

Initial Temperature Setting: The initial sampling temperature is set based on the model’s Controlled Exploration Zone (CEZ). This ensures a balance between maintaining performance and maximizing diversity from the outset. For example, POLARIS-4B-Preview starts at 1.4, and POLARIS-7B-Preview at 0.7.
Dynamic Temperature Updates: As RL training progresses, the model’s exploration space tends to narrow, and its Robust Generation Zone (RGZ) and Controlled Exploration Zone (CEZ) shift towards higher temperatures. To counteract this and maintain sufficient diversity, POLARIS dynamically increases the sampling temperature across training stages. This ensures the model continues to explore new patterns effectively.
The temperature increase interval is determined by the decrease in entropy from the previous stage (e.g., 0.05 interval for slight entropy decrease, larger for significant).
The RGZ and CEZ shift towards the high-temperature region following 800 steps of RL training.
Inference-Time Length Scaling

A significant challenge in developing advanced reasoning models is the cost of long-context training:

Long-context training is resource-intensive.
Even with increased training length (e.g., 52K), the proportion of samples trained at the maximum length remains low (clip_ratio below 10%).
Models struggle to generate effective long CoTs beyond their original pre-training length, even after RL training.
Analysis of Polaris-4B-Preview showed a significant performance drop for responses exceeding the 32K pre-training limit.

Training-free Length Extrapolation

Polaris incorporates a “train shorter, test longer” approach. It uses Rotary Position Embeddings (RoPE) adjustment to enable the model to maintain performance on sequences longer than those seen during training.

Significant accuracy boost on responses longer than 32K (e.g., from 26% to over 50% for Polaris-4B-Preview).
No retraining is required; Yarn is applied at inference time.
Accuracy improvements are concentrated on more difficult problems.
The model’s potential to scale its reasoning abilities to much longer contexts is unlocked, overcoming limitations imposed by practical RL training constraints.
Polaris-4B-Preview with Yarn significantly outperforms its base model, Qwen3–4B, once the context length exceeds 48K, and its performance continues to grow as the length increases toward 96K.

Exploration Efficiency

Training long CoT models with Reinforcement Learning (RL) is slow due to excessively long outputs. POLARIS incorporates multi-stage training, starting with shorter context windows in earlier stages and increasing the context length as the model’s performance converges.

Model-Specific Token Efficiency: Not all models are equally token-efficient. For instance, a small response length (e.g., 24K) worked for DeepSeek-R1-Distill-Qwen-7B but caused irreversible performance degradation for Qwen3–4B.
“Think Longer” from the Start: For models like Qwen3–4B, it was safer and more effective to directly start training with a longer response length (e.g., 40K) from the beginning, rather than gradually increasing it from a very short length.
Takeaway: When computational resources permit, it is recommended to start directly with the maximum decoding length suggested by the official repository for the base model.

Rollout Rescue Mechanism

POLARIS uses a small rollout size (8) for cost savings, but this raises the chance of zero-reward batches on hard prompts. To balance positive examples with minimal engineering, a per-example offline buffer (“sink”) is maintained:

If all 8 rollouts fail (accuracy 0/8) and a correct rollout was observed in earlier epochs, store that response in the sink (evicting the previous one).
In later epochs, whenever a new batch yields 0/8 for that example, randomly swap one failed rollout with the buffered response.

This lightweight strategy reduces zero-reward data dramatically and speeds up convergence, without retry loops.
An illustration of Rollout Rescue Mechanism.
Intra-Batch Informative Substitution

In GRPO, examples with all-correct or all-incorrect rollouts produce no advantage. Rather than complex dynamic sampling, a simple in-batch swap is applied:

Within each batch, select samples that have a mix of correct and incorrect rollouts (nonzero advantage).
Randomly duplicate these informative samples to replace those that yield zero advantage.

This ensures every training example contributes a learning signal, matching DAPO dynamic sampling’s benefits but requiring only a few tensor index operations — no extra rollouts or data-pipeline changes.

From DAPO and GRPO+

No Entropy Loss (from GRPO+): The entropy loss term is removed to prevent training instability. While intended to encourage exploration, it can cause entropy to grow uncontrollably, leading to a training collapse. The primary motivation is to ensure a more stable and reliable training process.
No KL Loss (from DAPO): The KL loss is eliminated to allow the model to explore beyond the constraints of the original SFT model. This also speeds up training, as there is no longer a need to compute log probabilities for a reference model.
Clip High (from DAPO): The upper clipping bound in the surrogate loss function is increased to encourage more aggressive exploration. This adjustment helps stabilize entropy and has been shown to improve model performance by allowing the policy to take larger, more beneficial update steps.

Reward Function

The reward function used in this work is the same as DeepscaleR. The selection of an Outcome Reward Model (ORM) over a Process Reward Model (PRM) is a deliberate countermeasure against reward hacking.

1 — If the LLM’s answer passes basic LaTeX/Sympy checks.
0 — If the LLM’s answer is incorrect or formatted incorrectly (e.g. missing <think>, </think> delimiters).

Evaluation

Paper

POLARIS: A POst-training recipe for scaling reinforcement Learning on Advanced ReasonIng modelS

Hungry for more insights?

Don’t miss out on exploring other fascinating threads in this series. Simply click here and uncover the state-of-the-art research!

Do Subscribe for weekly updates!!

By Ritvik Rastogi on September 2, 2025.

Canonical link

Exported from Medium on May 4, 2026.
