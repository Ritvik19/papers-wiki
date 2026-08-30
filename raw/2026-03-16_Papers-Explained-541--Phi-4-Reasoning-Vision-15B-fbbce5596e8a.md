# Papers Explained 541: Phi 4 Reasoning Vision 15B

Papers Explained 541: Phi 4 Reasoning Vision 15B

Papers Explained 541: Phi 4 Reasoning Vision 15B

Phi-4-reasoning-vision-15B is a compact open-weight multimodal reasoning model that balances reasoning power, efficiency, and training data…

Papers Explained 541: Phi 4 Reasoning Vision 15B

Phi-4-reasoning-vision-15B is a compact open-weight multimodal reasoning model that balances reasoning power, efficiency, and training data needs. The model was trained with 200 billion tokens of multimodal data leveraging Phi-4-Reasoning (trained with 16 billion tokens) based on a core model Phi-4 (400 billion unique tokens). This compares to more than 1 trillion tokens used for training multimodal models like Qwen 3 VL, Kimi-VL, and Gemma3.

The model is available on HuggingFace.

Architecture

Early vs. Mid Fusion

In late or mid-fusion models, a vision encoder first converts images into a compact set of visual tokens via a pretrained image encoder, which are then projected into the language embedding space and injected into a pretrained LLM. This approach enables meaningful cross-modal reasoning while preserving the strengths and scalability of large unimodal models. This approach keeps training and inference costs manageable, as it can utilize the power of pretrained components that have typically been trained on trillions of tokens.

Early-fusion models, by contrast, process all image patches and text tokens into a single transformer, allowing unrestricted cross-attention across modalities throughout the network. While this can yield richer joint representations and tighter visual–textual grounding, it significantly increases compute, memory, and data requirements.

Given our goal of creating a highly performant model with less compute and data, a mid-fusion architecture is used.

Vision Encoder and Image Processing
Overview of the Phi-4-reasoning-vision-15B mid-fusion architecture.
The model builds on the SigLIP-2 vision encoder and the Phi-4-Reasoning backbone.

With high-resolution multimodal benchmarks increasing in relevance, several open-source multimodal language models have adapted their methodologies accordingly, e.g. Gemma3 uses pan-and-scan, NVILA uses dynamic S2, and Qwen3-VL uses a bespoke vision encoder which operates at native resolution.

To explore these options, a large-scale ablation of several vision encoder and image processing techniques was conducted, with the goal of understanding and maximizing grounding performance. A smaller (5B) variation of the model was trained on a dataset of 10M image-text pairs, primarily composed of computer-use and GUI grounding data and experimented with several vision encoder configurations:

Dynamic S2: similar to S2, but resizes to a rectangular resolution chosen to minimize distortion while admitting a tiling by 384 ×384 squares.
Multi-crop: crops the image into (potentially overlapping) 384 ×384 squares; sends each through the vision encoder and concatenates features on the token dimension.
Multi-crop with S2: similar to multi-crop but uses S2 to broaden the receptive field, i.e., crops the image into (potentially overlapping) 1536 ×1536 squares, performs S2, and concatenates features on the token dimension.
Dynamic resolution: a natively dynamic resolution vision encoder; particularly NaFlex variant of the SigLIP-2 encoder with the minimum and maximum number of patches adjusted.
Results with different resolution handling approaches.
The primary finding is that dynamic resolution vision encoders with a large number of visual tokens perform uniformly well, and the best on high-resolution datasets. Reinforcing the high-resolution trend, multi-crop with S2 outperforms standard multi-crop despite using fewer visual tokens (i.e., fewer crops overall). It is worth noting that the dynamic resolution technique produces the most tokens on average; due to their tiling subroutine, S2-based methods are constrained by the original image resolution and often only use about half the maximum tokens.

Training Recipe
Training recipe for Phi-4-reasoning-vision-15B.
Phi-4-reasoning-vision-15B is trained in three stages:

Stage 1: MLP Pretraining: Only the cross-modality projector (MLP) is trained while the vision encoder and language model remain frozen. This stage aligns the visual feature space of SigLIP-2 with the text embedding space of Phi-4-Reasoning, establishing a shared representation before any other parameters are updated.
Stage 2: Instruction Tuning: All model components: the MLP, vision encoder, and language model are jointly trained on single-image instruction-tuning data. This stage constitutes the bulk of training and covers the full range of tasks: visual question answering, mathematical and scientific reasoning, grounding, captioning, OCR, and computer-use. The mixture includes both reasoning traces (with <think> tokens) and direct-response samples (with <nothink> tokens)
Stage 3: Long Context, Multi-Image, and RAI: The full model continues training on specialized data: long-document understanding, multi-image and sequential-image tasks, and additional responsible AI (RAI) data. This stage extends the model’s capabilities to handle longer contexts and multi-turn visual interactions while reinforcing safety alignment.
Training hyperparameters by stage.
Training Data

The final data mix consists of data primarily from three sources: open-source vision-language datasets which were meticulously filtered and improved, high-quality domain-specific data from other Microsoft teams, and high-quality data from targeted acquisitions. The overwhelming majority of our data lies in the first category: data which originated as open-source data, after which a significant amount of effort was dedicated to filtering and improving, whether by removing low-quality datasets or records, programmatically fixing errors in data formatting, or using open-source images as seeds to synthetically generate higher-quality accompanying text.

Open-Source Training Data Sources for Stages 1–3.

Data Quality

The process of improving open-source data started with manually reviewing data to classify it into several categories:

Excellent-quality data: the text components of the data consist of high-quality questions paired with correct answers.
Good questions with wrong answers: the text components of the data consist of high-quality questions, answerable from the image, with some portion of incorrect answers. This category arises most commonly with diagrams/math/STEM QA.
Low-quality questions: the text components of the data contain some number of low-quality questions, which are either nonsensical or not answerable from the given image.
Low-quality images: the images themselves are too repetitive or have fundamental errors (for example, a synthetic dataset of L A T E X diagrams where text and figures tend to overlap chaotically).
High-quality with formatting errors: the text component of the data contains formatting errors for many records, probably introduced during some processing stage; for example: all answers in a different format than what the prompt requests, misspelled image tags, final answers contained within reasoning blocks, etc.

Data Cleaning and Enhancement:

High-quality data: Mostly left unchanged, with minor formatting improvements.
Low-quality data: Re-generated answers or captions using GPT-4o and o4-mini, with verification and majority-voting pipelines. Datasets with high error rates were excluded.
Low-quality questions: Attempts to improve them using models for generating high-quality questions were largely unsuccessful except in specific cases.
Image quality: Datasets with fundamentally flawed images were excluded. Formatting and logical errors were fixed across open-source datasets.

Data Augmentation Techniques:

Domain-specific data: Detailed image descriptions were generated for math/science/logic datasets, creating multiple records with the same image: one with original QA and one with a caption-style description.
Multi-purpose data: Instruction-following data and domain-specific data were combined by modifying the text portion of data with ground-truth QA pairs to request and provide answers in a specific format.
Multi-image data:
Scrambled captions: 5 images with captions requested in a random order, sometimes with additional images added later.
Caption matching: 5 images with the request to match captions to images.
“What’s changed?” data: Generated from pairs or triples of sequential screenshots to improve the model’s ability to navigate images in real-time.
Robust prompts: Human-generated prompts were used to teach the model robustness and avoid over-reliance on perfectly structured questions.

Mathematics and Science vs. Computer-Use Data Proportion

A suite of experiments was conducted to better understand optimal data scale and ratios for multimodal reasoning tasks of math and science reasoning vs. computer use. A smaller variation of the model (5B parameters) was trained, while varying the amount of mathematics and computer-use data for each run. Each dataset included the same subset of 1M general image-text pairs as a baseline. For mathematics data, the same dataset of 150K multimodal records was used, optionally duplicating each one 3 times. Next, up to 450K computer-use records, and optionally an additional 400K from Phi-Ground were included.
Varying the ratios of math and CUA data.
The finding is that it appears possible for a single model to have uniformly superior performance across multiple reasoning domains. In general, multimodal mathematics performance was not harmed by additional computer-use data, and vice versa. It is also worth noting that increasing mathematics data while keeping computer-use data constant still improves computer-use benchmarks.

Mixed Non-Reasoning and Reasoning

While reasoning traces improve performance in language-only settings, their benefit in multimodal settings is less clear-cut. Reasoning can be unnecessary or even harmful for tasks like image captioning and OCR, but beneficial for mathematical and scientific problem-solving.

Training Approaches for Multimodal Reasoning:

Supervised Fine-Tuning (SFT): Simpler but requires large amounts of reasoning trace data.
Reinforcement Learning (RL): Reduces data requirements but increases training complexity and compute.

Mid-Fusion Architectures: The base language model can be either reasoning or non-reasoning, leading to various training pipelines:

Non-Reasoning LLM → Reasoning Multimodal Training: Reasoning and multimodal capabilities are trained together.
Non-Reasoning LLM → Non-Reasoning Multimodal → Reasoning Multimodal Training: Multimodal capabilities are learned first, then reasoning is added.
Reasoning LLM → Reasoning Multimodal Training: A reasoning base is used, but all multimodal data must include reasoning traces.
Reasoning LLM → Mixed Non-Reasoning / Reasoning Multimodal Training: A reasoning-capable base is trained on a hybrid data mixture, learning when to reason and when to respond directly.

Phi-4-reasoning-vision-15B adopts the fourth approach, balancing reasoning capability, inference efficiency, and data requirements. It inherits a strong reasoning foundation but uses a hybrid approach to combine the strengths of alternatives while mitigating their drawbacks. It defaults to direct inference for perception-focused domains and invokes longer reasoning paths for domains like math and science.

It is trained with SFT, using <think>…</think> sections for reasoning samples and <nothink> tokens for non-reasoning samples. Reasoning data comprises approximately 20% of the total mix.

Evaluation
Accuracy comparisons relative to popular open-weight, non-thinking models.Accuracy comparisons relative to popular open-weight, thinking models.
Phi-4-reasoning-vision-15B shows strong accuracy across diverse multimodal benchmarks.
The model’s default mixed-reasoning behavior (letting it decide when to “think” vs not) generally yields better average accuracy than forcing purely thinking or purely non-thinking modes.
Only a few benchmarks benefit from forcing a specific mode:
Thinking mode improves performance on MathVerse and MMMUVAL.
Non-thinking mode improves performance on ScreenSpotv2.

From the timing experiments, Phi-4-reasoning-vision-15B offers a desirable trade-off between accuracy and cost, where cost is measured via inference time compute and output token counts.
Compared to recent popular open-weight models, it achieves competitive or better accuracy at a reasonable per-query latency, suitable for interactive use.

Paper

Phi-4-reasoning-vision-15B Technical Report 2603.03975

Hungry for more insights?

Don’t miss out on exploring other fascinating threads in this series. Simply click here and uncover the state-of-the-art research!

Do Subscribe for weekly updates!!

By Ritvik Rastogi on March 16, 2026.

Canonical link

Exported from Medium on May 4, 2026.
