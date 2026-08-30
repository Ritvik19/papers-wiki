Source URL: https://huggingface.co/blog/open-r1
Title: Open-R1: a fully open reproduction of DeepSeek-R1

# Open-R1: a fully open reproduction of DeepSeek-R1

Published January 28, 2025

Elie Bakouch, Leandro von Werra, Lewis Tunstall

If you've ever struggled with a tough math problem, you know how useful it is to think a little longer and work through it carefully. OpenAI's o1 model showed that when LLMs are trained to do the same, by using more compute during inference, they get significantly better at solving reasoning tasks like mathematics, coding, and logic.

However, the recipe behind OpenAI's reasoning models has been a well kept secret. That is, until last week, when DeepSeek released their DeepSeek-R1 model and promptly broke the internet (and the stock market!).

Besides performing as well or better than o1, the DeepSeek-R1 release was accompanied by a detailed tech report that outlined the key steps of their training recipe. This recipe involved several innovations, most notably the application of pure reinforcement learning to teach a base language model how to reason without any human supervision.

However, the DeepSeek-R1 release leaves open several questions about:

- Data collection: How were the reasoning-specific datasets curated?
- Model training: No training code was released by DeepSeek, so it is unknown which hyperparameters work best and how they differ across different model families and scales.
- Scaling laws: What are the compute and data trade-offs in training reasoning models?

These questions prompted the launch of the Open-R1 project, an initiative to systematically reconstruct DeepSeek-R1's data and training pipeline, validate its claims, and push the boundaries of open reasoning models.

## How did they do it?

DeepSeek-R1 is a reasoning model built on the foundation of DeepSeek-V3. This 671B Mixture of Experts (MoE) model performs on par with heavyweights like Sonnet 3.5 and GPT-4o, and was cost-efficient to train (~$5.5M) thanks to architectural changes like Multi Token Prediction (MTP), Multi-Head Latent Attention (MLA), and heavy hardware optimization.

DeepSeek introduced two models: DeepSeek-R1-Zero and DeepSeek-R1, each with a distinct training approach. DeepSeek-R1-Zero skipped supervised fine-tuning altogether and relied entirely on reinforcement learning (RL), using Group Relative Policy Optimization (GRPO) to make the process more efficient. A simple reward system guided the model based on the accuracy and structure of its answers, helping it develop skills like breaking problems into steps and verifying its own outputs. However, its responses often lacked clarity and were difficult to read.

DeepSeek-R1 started with a "cold start" phase, fine-tuning on a small set of carefully crafted examples to improve clarity and readability, then went through more RL and refinement steps, including rejecting low-quality outputs with both human-preference-based and verifiable reward, to create a model that reasons well and produces polished, consistent answers.

## Open-R1: the missing pieces

The release of DeepSeek-R1 is a huge boon for the community, but the datasets and code used to train the model were not released, only the model weights.

The goal of Open-R1 is to build these missing pieces so the whole research and industry community can build similar or better models using these recipes and datasets, in the open, so anybody can contribute. The plan of attack:

- Step 1: Replicate the R1-Distill models by distilling a high-quality reasoning dataset from DeepSeek-R1.
- Step 2: Replicate the pure RL pipeline that DeepSeek used to create R1-Zero, curating new, large-scale datasets for math, reasoning, and code.
- Step 3: Show it is possible to go from base model to SFT to RL via multi-stage training.

The synthetic datasets will let anyone fine-tune existing or new LLMs into reasoning models by fine-tuning on them; the RL training recipes will serve as a starting point for building similar models from scratch and for researchers building more advanced methods on top. The project's scope extends beyond math into code and other reasoning-heavy fields such as medicine.

## Models mentioned in this article

- deepseek-ai/DeepSeek-R1 (685B, Text Generation)
- deepseek-ai/DeepSeek-R1-Zero (685B)
