# Papers Explainedv377: Fathom-R1

Papers Explainedv377: Fathom-R1

Papers Explainedv377: Fathom-R1

Fathom-R1–14B is a 14-billion-parameter reasoning language model derived from Deepseek-R1-Distilled-Qwen-14B, fine-tuned for mathematical…

Papers Explainedv377: Fathom-R1

Fathom-R1–14B is a 14-billion-parameter reasoning language model derived from Deepseek-R1-Distilled-Qwen-14B, fine-tuned for mathematical reasoning by Fractal.

The models and datasets are available at HuggingFace.

Training Dataset

We begin by curating a high-quality mathematical corpus from the following open-source datasets:

Open-R1 — default subset
Numina — Olympiads & AOPS_forum (word problems, float type answers)

After rigorous deduplication and decontamination, approximately ~100K unique problems are consolidated forming the initial corpus for all subsequent trainings.

Training Recipes

Training Recipe for Fathom-R1–14B-v0.6

SFT on difficult questions and their reasoning chains has proven effective for enhancing reasoning ability. Building on this, this training stage aims to improve the model’s performance on challenging mathematical problems using an iterative curriculum learning strategy, with a maximum sequence length of 16k. Curriculum learning (CL) is a well-established method for training LLMs, where the model is gradually exposed to increasingly difficult tasks. This approach helps scaffold more complex reasoning, enhancing generalization and reducing overfitting. In this case, CL is implemented iteratively, meaning multiple iterations of CL are performed.

For dataset preparation, each question’s difficulty is annotated using OpenAI’s o3mini model. Only questions rated above average are retained and further filtered to include those with solve rates between 0.2 and 0.7. This process results in the Iterative Curriculum Learning dataset, comprising 5K examples.

Training Recipe for Fathom-R1–14B-v0.4-RS

The strategy for creating this checkpoint involves a two-stage pipeline:

First Stage (Leveraging RL for efficient test-time thinking):

Curate a seed dataset ensuring minimal reward but room for growth, comprising questions with solve rates within a specific range, forming a 7.7K question RL Compression dataset.
Train the base model, DeepSeek-R1-Distill-Qwen-14B, using the GRPO algorithm with a 6k token sequence length limit.
The model learns to generate concise responses, showing improved performance at lower token limits.

Second Stage (Leveraging SFT to improve reasoning efficiently at higher sequence length):

Build upon the RL checkpoint and perform SFT with a 16K context window to enhance detailed reasoning for complex problems.
Curate a dataset of hard problems with lower solve rates, forming a 9.5K example SFT Shortest Chains dataset.
Supervised fine-tuning on this dataset stabilizes the model’s reasoning at up to 16K sequence length.

The resulting model, Fathom-R1–14B-v0.4, is optimized for concise yet accurate mathematical reasoning.

Training Recipe for Fathom-R1–14B-v0.4

Given the performance improvement noticed during the second fine-tuning stage of developing Fathom-R1–14B-v0.4-RS and in an attempt to further reduce the cost, an experiment was conducted by eliminating RL and directly performing second stage SFT on Deepseek-R1-Distilled-Qwen-14B base model.

Model Merging

Given v0.6 and v0.4 models have been developed by following different training methodologies, linear merging is performed to combine the strengths to obtain final 2 checkpoints.

Fathom-R1–14B: Obtained via merging Fathom-R1–14B-V0.6 (Iterative Curriculum SFT) and Fathom-R1–14B-V0.4 (SFT-Shortest-Chains)
Fathom-R1–14B-RS: Obtained via merging Fathom-R1–14B-V0.6 (Iterative Curriculum SFT) and Fathom-R1–14B-V0.4 (RL-compression + SFT-Shortest-Chains)

Evaluation

Fathom‑R1–14B demonstrates highly competitive performance across all datasets, improving over the original R1-distilled models while closely matching or surpassing other strong baselines in several settings.
On both AIME 25 and HMMT 25, our model shows the highest pass@1 as well as cons@64 scores among all the open-source models (including the bigger R1-Distilled-32B model), with R1–670B being the only exception.
Fathom-R1–14B is superior to the first two generations of OpenAI’s mini-reasoning models, including o1-mini and o3-mini-low- and its performance closely matches that of newly released o4-mini-low (self-consistency decoding).

Paper

Fathom-R1: $499 Training Recipe for Unlocking Math Reasoning at o4-mini level with just 14B parameters under 16K context

Hungry for more insights?

Don’t miss out on exploring other fascinating threads in this series. Simply click here and uncover the state-of-the-art research!

Do Subscribe for weekly updates!!

By Ritvik Rastogi on May 30, 2025.

Canonical link

Exported from Medium on May 4, 2026.
