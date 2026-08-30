# Papers Explained 476: Klear-Reasoner

Papers Explained 476: Klear-Reasoner

Papers Explained 476: Klear-Reasoner

Klear-Reasoner is a reasoning model with long reasoning capabilities that achieves high performance across multiple benchmarks. The report…

Papers Explained 476: Klear-Reasoner

Klear-Reasoner is a reasoning model with long reasoning capabilities that achieves high performance across multiple benchmarks. The report provides an in-depth analysis of the model’s post-training workflow, including data preparation, long Chain-of-Thought supervised fine-tuning, and reinforcement learning, along with detailed ablation studies. It proposes GPPO to address the clipping issues by gently backpropagating gradients from clipped tokens, enhancing exploration and improving learning from negative samples.

The project is available at GitHub.

Data Curation

Long Chain-of-Thought Supervised Fine-tuning

For mathematical and coding tasks, a quality-centric data construction strategy inspired by OpenThoughts is adopted, prioritizing high-quality data over superficial diversity. This approach is reflected in four key design principles:

Prompts are exclusively curated from high-quality sources: mathematics prompts primarily draw from OpenThoughts, NuminaMath, and AceReason-Nemotron 1.1, while coding prompts are gathered from OpenThoughts, Open-CodeReasoning, AceReason-Nemotron 1.1, TACO, Apps, and Codeforces.
To ensure data uniqueness and prevent contamination, strict deduplication protocols are implemented, including exact match removal of queries and filtering prompts with 9-gram overlap against test samples.
The teacher model employed for response generation is Deepseek-R1–05283, which produces up to 16 responses per prompt through sampling.
After evaluating sample difficulty using Qwen3–8B, all responses are retained since most samples qualify as difficult.

Through this process, a high-quality reasoning dataset containing 1.5 million math and coding samples is constructed. To effectively leverage these high-quality reasoning data, the model is fine-tuned using the standard SFT objective.

Reinforcement Learning

A data collection and validation pipeline integrates prompts from various sources, including Skywork-OR1, Acereason, NuminaMath, and DeepScaleR. A 9-gram filtering mechanism is employed to prevent overlap with common benchmark datasets, and exact deduplication is applied to ensure the uniqueness of each sample. For code problems, multiple filtering strategies are applied to mitigate noisy or low-quality samples that could harm RL training. Examples with fewer than 16 test cases are removed, as these are more susceptible to false positives. For each retained prompt, 16 completions are generated using DeepSeek-R1–0120. Only those prompts for which DeepSeek-R1–0120 achieves a pass@16 greater than 0.5 are kept, reducing noise introduced by faulty or insufficient test cases. For math problems, the focus is on ensuring correctness and clarity, particularly because the raw data, often collected from the web and processed via OCR or parsers, can contain substantial noise (e.g., incorrect questions or answers). To address this, 16 responses per prompt are generated using DeepSeek-R1–0120 and only those for which a majority of completions pass a rule-based validator are retained. After these rigorous filtering steps, a high-quality RL dataset consisting of 88K math samples and 18K code samples is constructed.

Gradient-Preserving Clipping Policy Optimization

Classical PPO Algorithm (Unclipped)

In the classical PPO algorithm without clipping, the gradient of the loss function is given by:

here rt(θ) is the importance sampling ratio, ϕθ(at,st) is the gradient of the logits output by the policy network with respect to θ, and ˆAt is the advantage estimate.

The absence of clipping allows the importance sampling ratio rt(θ) to range from (0, +∞). While this broad range can enhance exploration, it often leads to training instability due to excessively large gradient updates. This can cause oscillating or divergent policy updates, hindering convergence to an optimal policy.

Clipped PPO Algorithm

To address the instability, a common approach is to apply clipping to the importance sampling ratio, constraining its upper and lower bounds (e.g., using 1-ϵ and 1+ϵ).

When ˆAt > 0, gradients are only propagated if rt(θ) is within (0, 1+ϵ).
When ˆAt < 0, gradients are only present if rt(θ) is within (1−ϵ, +∞).

This mechanism restricts the range of gradient updates, preventing over-encouragement for positive advantages and avoiding excessive punishment for negative advantages, thereby stabilizing training.

Issues with Completely Discarding Clipped Token Gradients

Despite stabilizing training, completely discarding gradients for samples outside the clipping range introduces two key problems:

High-Entropy Token Clipping: Clipping indiscriminately suppresses gradients for all tokens whose importance sampling ratios exceed 1+ϵ. This includes “high-entropy tokens” associated with valuable exploratory behaviors, which often lie at crucial decision branches. Clipping out these tokens, severely hampering the model’s capacity to explore.
Delayed Convergence of Negative Samples: When the importance sampling ratio of suboptimal trajectories falls below 1−ϵ, their gradients are forcibly clipped. This prevents the model from updating based on these negative signals. The model must repeatedly sample similar suboptimal trajectories before it can correct its behavior, leading to slower convergence on negative examples and hindering timely policy adjustment.

Existing methods like DAPO’s clip-higher operation, which elevates the clip upper bound, still inherently truncate gradient signals from certain samples and fail to resolve the underlying issue.

Gradient-Preserving Clipping Policy Optimization (GPPO)

The core motivation of GPPO is to propose a balanced approach that bridges unclipped and clipped methodologies. It aims to incorporate gradient signals from samples beyond clip boundaries while constraining these out-of-bound gradient signals within a defined range to safeguard training stability.

Unlike traditional techniques that completely discard gradients outside the clipping range, GPPO introduces an innovative truncation mechanism that incorporates previously clipped tokens into the computational graph. This ensures valuable learning signals are retained while maintaining stable policy updates.

Here, δ = r(j)t(θ) is the importance sampling ratio, and sg(·) denotes the stop-gradient operation. The term δ/sg(δ) is numerically 1, so the forward computation remains unchanged.

GPPO decouples gradient propagation from the clipping constraint. This means its backward computation differs from standard clipping, which directly discards gradients of samples falling outside the clipping bounds.

GPPO Gradient Expression:

RL Training with SFT Loss

Similar to other works, GPPO incorporates a Supervised Fine-Tuning (SFT) loss into the RL training process.

where Φ is the index set of correct samples from examples in the rollout.

Benefits of SFT Loss:

Improved Utilization of Positive Examples: The SFT loss enhances the efficiency of using positive examples.
Training Anchor: It serves as an anchor during training, constraining the policy model’s output to maintain a reasonable distribution.
Mitigates Reward Hacking: This helps to mitigate reward hacking behavior.
Enhances Training Stability: It contributes to overall training stability.

Final Combined Loss: The final loss L(θ) is a weighted sum of the GPPO loss and the LLM loss:

where α is a hyperparameter balancing the weighting between the two losses.

Reward Design for Math and Code RL

For mathematical tasks, a binary reward system is used where solutions receive either positive or negative rewards based on final correctness. Responses that fail to encapsulate their reasoning process within designated <think>…</think> tags are penalized.

In terms of code tasks, RL often struggles with sparse rewards, particularly in code generation where models may produce largely correct solutions that fail only on corner cases. Traditional approaches label such samples as entirely negative, disregarding their partial correctness. Partially correct solutions contain valuable learning signals. To overcome this challenge, a soft reward mechanism based on test case pass rates is introduced. For example, if generated code passes 4 out of 16 test cases, it receives a proportional reward of 0.25 (4/16). The soft pass@k reward system provides granular feedback that mitigates sparse rewards, preserves learning signals from partially correct solutions, and encourages incremental quality improvement.

Experiment Setup

Klear-Reasoner-8B is based on the Qwen3–8B-Base model. It is first fine-tuned with long CoT SFT and then trained using RL on math and coding tasks.

DeepSeek-R1–0528 was used to generate responses for the long CoT SFT data. Maximum training length of 32K, maximum learning rate of 8e-5 (cosine decay to 4e-5), trained for 4 epochs.

RL training was conducted jointly with SFT loss (α=0.1), utilizing GPPO, token-level policy gradient loss, and Clip-Higher with ϵh = 0.28, without using KL loss and a global batch size of 128 per step, Sampled 8 responses per prompt. Math RL used a constant learning rate of 1e-6 with a mini-batch size of 16. Coding RL used a constant learning rate of 5e-7 with a mini-batch size of 32.

Evaluation

SFT Model Performance: The Klear-Reasoner-8B-SFT model achieved performance comparable to Qwen3–8B, demonstrating the effectiveness of the long CoT SFT approach, which relies solely on data distillation.
RL Model Performance (32K Inference Budget): Klear-Reasoner-8B, after RL fine-tuning, matched the performance of community SOTA models operating at larger 64K/96K inference budgets.
RL Model Performance (64K Inference Budget): When the inference budget was expanded to 64K (using the YaRN method with a scaling factor of 2.5), Klear-Reasoner-8B achieved optimal performance.

Paper

Klear-Reasoner: Advancing Reasoning Capability via Gradient-Preserving Clipping Policy Optimization 2508.07629

Hungry for more insights?

Don’t miss out on exploring other fascinating threads in this series. Simply click here and uncover the state-of-the-art research!

Do Subscribe for weekly updates!!

By Ritvik Rastogi on October 16, 2025.

Canonical link

Exported from Medium on May 4, 2026.
