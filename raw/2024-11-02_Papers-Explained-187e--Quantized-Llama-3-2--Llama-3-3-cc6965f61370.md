# Papers Explained 187e: Quantized Llama 3.2, Llama 3.3

Papers Explained 187e: Quantized Llama 3.2, Llama 3.3

Papers Explained 187e: Quantized Llama 3.2, Llama 3.3

Llama 3 is a new set of foundation models, designed for multilinguality, coding, reasoning, and tool usage.

Papers Explained 187e: Quantized Llama 3.2, Llama 3.3

Llama 3 is a new set of foundation models, designed for multilinguality, coding, reasoning, and tool usage.

This article covers the Quantized Lightweight Llama models, introduced in October 2024. The models are available on HuggingFace.

Further it covers Llama 3.3, introduced in December 2024, available on HuggingFace.

Refer the Part A of this article to read about the models released in April 2024: [Papers Explained 187a: Llama 3]
Refer the Part B of this article to read about the models released in July 2024: [Papers Explained 187b: Llama 3.1]
Refer the Part C of this article to read about the initial experiments of adding multimodal capabilities to Llama3: [Papers Explained 187c: Llama 3.1 — Multimodal Experiments]
Refer the Part D of this article to read about the 3.2 models which consists of 11B and 90B vision language models and 3B and 1B small language models: [Papers Explained 187d: Llama 3.2]

Quantized Llama 3.2

Quantized Llama have been optimized for use on resource-constrained devices like mobile phones.

These models are developed using Quantization-Aware Training with LoRA adaptors to optimize performance in low-precision environments and SpinQuant, a technique that enables us to determine the best possible combination for compression while retaining the most possible quality.

The Quantization Setup

The quantization scheme involves three parts.

All linear layers in all transformer blocks are quantized to a 4-bit groupwise scheme (with a group size of 32) for weights and 8-bit per-token dynamic quantization for activations.
The classification layer is quantized to 8-bit per-channel for weight and 8-bit per-token dynamic quantization for activation.
Additionally, an 8-bit per-channel quantization is employed for embedding.

Quantization-Aware Training and LoRA

Quantization-Aware Training (QAT) is used to simulate the effects of quantization during the training of Llama 3.2 models, enabling optimization of their performance in low-precision environments. To initialize QAT, BF16 Llama 3.2 model checkpoints are used after supervised fine-tuning (SFT), followed by an additional full round of SFT training with QAT. The backbone of the QAT model is then frozen and another round of SFT training is performed with low-rank adaptation (LoRA) adaptors applied to all layers within the transformer block, while maintaining LoRA adaptors’ weights and activations in BF16. Finally, the resulting model (both backbone and LoRA adaptors) is fine-tuned using direct preference optimization (DPO).

SpinQuant

Although QAT gives the best results, some people might want to quantize their fine-tuned 1B and 3B models or quantize the models for different targets with different quantization settings. For this reason, a state-of-the-art technique for post-training quantization called SpinQuant is used.

While the method is less accurate than QAT + LoRA, a key advantage of SpinQuant is its portability and ability to operate without requiring access to training datasets, which are often private. It’s an attractive solution for applications where data availability or computational resources are limited.

In experiments, WikiText, a small calibration dataset, is utilized to learn rotation matrices in SpinQuant. These matrices enable the smoothing of outliers and facilitate more effective quantization. After this, best practices in quantization such as range setting and generative post-training quantization are applied. The SpinQuant matrices are optimized for the quantization scheme similar to QAT + LoRA.

Results

Llama 3.3

The Meta Llama 3.3 multilingual large language model (LLM) is an instruction-tuned generative model in 70B. The LLM is optimized for multilingual dialogue use cases and outperforms many of the available open source and closed chat models on common industry benchmarks.

This model uses an auto-regressive language architecture, specifically an optimized transformer architecture. The tuned versions employ supervised fine-tuning (SFT) and reinforcement learning with human feedback (RLHF) to align with human preferences for helpfulness and safety.

The Llama 3.3 model supports eight languages: English, German, French, Italian, Portuguese, Hindi, Spanish, and Thai. Token counts refer to pretraining data only, and all model versions use Grouped-Query Attention (GQA) for improved inference scalability.

Llama 3.3 was pretrained on approximately 15 trillion tokens of data from publicly available sources. The fine-tuning data includes publicly available instruction datasets, as well as over 25 million synthetically generated examples. The pretraining data has a cutoff of December 2023.

The fine-tuning data is collected through a multi-faceted approach, combining human-generated data with synthetic data to mitigate potential safety risks. Many large language model (LLM)-based classifiers are used to thoughtfully select high-quality prompts and responses, enhancing data quality control.

Paper

Introducing quantized Llama models with increased speed and a reduced memory footprint

Recommended Reading [LLaMA Models]

Hungry for more insights?

Don’t miss out on exploring other fascinating threads in this series. Simply click here and uncover the state-of-the-art research!

Do Subscribe for weekly updates!!

By Ritvik Rastogi on November 2, 2024.

Canonical link

Exported from Medium on May 4, 2026.
