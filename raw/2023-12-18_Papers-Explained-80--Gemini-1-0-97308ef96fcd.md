# Papers Explained 80: Gemini 1.0

Papers Explained 80: Gemini 1.0

Papers Explained 80: Gemini 1.0

Gemini is a family of highly capable multi-modal models developed at Google, trained jointly across image, audio, video, and text data for…

Papers Explained 80: Gemini 1.0

Gemini is a family of highly capable multi-modal models developed at Google, trained jointly across image, audio, video, and text data for the purpose of building a model with both strong generalist capabilities across modalities alongside cutting-edge understanding and reasoning performance in each respective domain.

Gemini 1.0 comes in three sizes:

Ultra for highly-complex tasks.
Pro for enhanced performance and deployability at scale.
Nano for on-device applications.
An overview of the Gemini 1.0 model family.
Gemini Ultra is the first model to achieve human-expert performance on MMLU.

Recommended Reading: [Flamingo]

Architecture

Gemini models are built on top of Transformer decoders with enhancements to enable stable training at scale and optimized inference on Google’s Tensor Processing Units. They are trained to support 32k context length, employing efficient attention mechanisms (for e.g. multi-query attention).

Gemini models are trained to accommodate textual input interleaved with a wide variety of audio and visual inputs, such as natural images, charts, screenshots, PDFs, and videos, and they can produce text and image outputs. The visual encoding of Gemini models is inspired by the foundational work on Flamingo, CoCa, and PaLI, with the important distinction that the models are multimodal from the beginning and can natively output images using discrete image tokens.

Video understanding is accomplished by encoding the video as a sequence of frames in the large context window. The models can handle variable input resolution in order to spend more computation on tasks that require fine-grained understanding. In addition, Gemini can directly ingest audio signals at 16kHz from Universal Speech Model (USM) features. This enables the model to capture nuances that are typically lost when the audio is naively mapped to a text input.

Training Dataset

The pretraining dataset uses data from web documents, books, and code, and includes image, audio, and video data. The SentencePiece tokenizer is used.

Quality filters are applied to all datasets, using both heuristic rules and model-based classifiers. Safety filtering is also performed to remove harmful content. We filter our evaluation sets from the training corpus.

Evaluation

Academic Benchmarks
Gemini performance on text benchmarks.
Gemini outperforms inference-optimized models like GPT-3.5 and competes equally with several top models.
Ultra surpasses all current models, while Pro outperforms many existing ones.
Gemini Ultra achieves a 90.04% accuracy on MMLU, exceeding human expert performance (89.8%).
Specialized knowledge across diverse domains, coupled with reading comprehension and reasoning, contributes to this high accuracy.
Utilizes a chain-of-thought prompting approach to handle model uncertainty, employing k samples to reach a consensus or revert to a greedy sample.
Strong performance in grade-school math benchmarks (GSM8K) with 94.4% accuracy using specific prompting techniques.
Success in tackling increasingly difficult math problems from middle- and high-school competitions, surpassing all competitors.
Outperforms competitors in American Mathematical Competitions with a solve rate of 32%.
Excels in coding tasks, achieving high scores in code completion benchmarks and python code generation tasks.
Evaluations performed on conventional benchmarks and complex reasoning systems, showing high correctness rates, such as 74.4% and 74.9%, respectively.

Trends in Capabilities
Language understanding and generation performance of Gemini model family across different capabilities (normalized by the Gemini Pro model).
Consistent quality gains with increased model size, particularly evident in reasoning, math/science, summarization, and long-context tasks.
Gemini Nano 1 (1.8B) and Nano 2 (3.2B5) models, designed for on-device deployments, excel in summarization and reading comprehension tasks. Despite their smaller size, they perform exceptionally well in factuality, reasoning, STEM, coding, and multilingual tasks.

Multilingual

Machine Translation:
Performance of Gemini models on WMT 23 translation benchmark. All numbers with 1-shot.
Gemini Ultra excels in translating from English to various languages, surpassing other language models.
Achieves highest BLEURT scores in out-of-English translation tasks across different language pairs in WMT 23 benchmark.
Outperforms GPT-4 and PaLM 2 in translation quality on average across all language pairs and directions.
Successfully translates very low-resource languages with commendable chrF scores.

Multilingual Math and Summarization:
Performance of Gemini models on multilingual math and summarization.
Gemini Ultra demonstrates strong performance in multilingual tasks:
Achieves higher accuracy in the MGSM math benchmark compared to PaLM 2-L across multiple languages.
Shows promising results in summarization benchmarks (XLSum and WikiLingua), though trailing behind PaLM 2 in one instance.

Long Context
Negative log likelihood as a function of token index across 32K context length on a held-out set of long documents.
Gemini models, trained with a sequence length of 32,768 tokens, effectively utilize their context length.
Synthetic retrieval tests confirm the effective use of context: Key-value pairs placed at the context’s start show Ultra model retrieves correct values with 98% accuracy across the entire context length.
Investigation through NLL plotting across held-out long documents reveals a decreasing trend in NLL concerning token index, emphasizing the effective use of context length.

Human Preference Evaluations
Win rate of Gemini Pro over PaLM 2 (text-bison@001) with 95% confidence intervals.
Instruction-tuned Gemini Pro models showcase significant improvements across Creative Writing, Instruction Following and Safety.

Image Understanding
Image understanding
Gemini Ultra consistently outperforms existing approaches even in zero-shot, especially for OCR-related image understanding tasks for natural images, text, documents, and figures without using any external OCR engine (‘pixel only’).
Many existing approaches fine-tune on the respective tasks, highlighted in gray, which makes the comparison with 0-shot not apples-toapples.
Multilingual image understanding
Gemini models outperform existing models in captioning images in many languages when benchmarked on a subset of languages in XM-3600 dataset.

Video Understanding
Few-shot video understanding across tasks and languages
Gemini Ultra achieves state-of-the-art results in few-shot video captioning and zero-shot video question answering tasks.
Demonstrates strong temporal reasoning across multiple frames.

Image Generation

Native Image Output: Gemini has a unique capability to generate images directly without relying on descriptive text as an intermediate step, allowing prompt-based image and text creation.
Interleaved Image and Text Generation: The model can create images based on prompts that involve sequences of both images and text, enabling it to suggest visual concepts aligned with given prompts.

Audio Understanding
Speech evaluation results on selected benchmarks for ASR and AST.
Gemini Pro outperforms USM and Whisper models across all ASR and AST tasks for both English and multilingual test sets.
Particularly strong performance shown in FLEURS due to training with the FLEURS dataset, achieving lower WER (Word Error Rate).
Gemini Nano-1 also outperforms USM and Whisper on most datasets, except FLEURS, showcasing competitive performance in various tasks.
Gemini Pro demonstrates superior performance in producing more understandable responses, especially with rare words and proper nouns compared to USM.
Gemini Ultra’s performance in audio tasks remains unexplored but anticipated to perform better due to increased model scale, hinting at potential improvements in speech-related tasks with larger-scale models.

Recommended Reading: [Papers Explained 81: An In-depth Look at Gemini’s Language Abilities]

Paper

Gemini

Hungry for more insights?

Don’t miss out on exploring other fascinating threads in this series. Simply click here and uncover the state-of-the-art research!

Do Subscribe for weekly updates!!

By Ritvik Rastogi on December 18, 2023.

Canonical link

Exported from Medium on May 4, 2026.
