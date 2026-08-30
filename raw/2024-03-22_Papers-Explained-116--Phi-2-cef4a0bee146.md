# Papers Explained 116: Phi-2

Papers Explained 116: Phi-2

Papers Explained 116: Phi-2

Phi-2 is a 2.7B parameter model that follows the phi approach, trained on 1.4T tokens from multiple passes on a mixture of Synthetic and…

Papers Explained 116: Phi-2

Phi-2 is a 2.7B parameter model that follows the phi approach, trained on 1.4T tokens from multiple passes on a mixture of Synthetic and Web datasets for NLP and coding.It is developed to explore whether emergent abilities achieved by large-scale language models can also be achieved at a smaller scale using strategic choices for training, such as data selection.

The model is available on HuggingFace.

Recommended Reading [Papers Explained 114: Phi-1] [Papers Explained 115: Phi-1.5]

Training Details

The training data mixture contains synthetic datasets specifically created to teach the model common sense reasoning and general knowledge, including science, daily activities, and theory of mind, among others. The training corpus is further augmented with carefully selected web data that is filtered based on educational value and content quality.

Phi-2 is a base model, i.e., it has not undergone alignment through RLHF, nor has it been instruction-fine-tuned. Despite this, it achieves better behavior with respect to toxicity and bias compared to existing open-source models that have gone through alignment.

Phi-2 is developed starting from the 1.3B phi-1.5, using innovative techniques to scale up and embed its knowledge in the 2.7B model. This scaled knowledge transfer not only accelerates training convergence but shows clear boost in Phi-2 benchmark scores.

Evaluation

The first model, Phi-1 (1.3B), achieved state-of-the-art performance on Python coding among existing SLMs (specifically on the HumanEval and MBPP benchmarks).

Phi-1.5 (1.3B) extended the focus to common sense reasoning and language understanding with performance comparable to models 5x larger.

Phi-2 (2.7B) demonstrates outstanding reasoning and language understanding capabilities, showcasing state-of-the-art performance among base language models with less than 13 billion parameters.

On complex benchmarks Phi-2 matches or outperforms models up to 25x larger, thanks to new innovations in model scaling and training data curation.
Comparison between Phi-2 (2.7B) and Phi-1.5 (1.3B) models. All tasks are evaluated in 0-shot except for BBH and MMLU which use 3-shot CoT and 5-shot, respectively.
Phi-2 outperforms phi-1.5 in all the mentioned benchmarks.
Safety scores computed on 13 demographics from ToxiGen.
Despite not being aligned, Phi-2 demonstrates better behaviour with respect to toxicity and bias compared to existing open-source models that went through alignment.

Phi-2 is evaluated across various academic benchmarks including Big Bench Hard (BBH), commonsense reasoning, language understanding, math, and coding.
Despite having only 2.7 billion parameters, Phi-2 surpasses the performance of larger models such as Mistral (7B) and Llama-2 (13B).
Phi-2 also outperforms the significantly larger Llama-2–70B model, especially in multi-step reasoning tasks like coding and math.

Phi-2’s performance is comparable or superior to Google Gemini Nano 2, despite Phi-2’s smaller size.
Phi-2 was also evaluated using Microsoft’s internal proprietary datasets and tasks, showing it generally outperforms Mistral-7B and Llama-2 models across various sizes (7B, 13B, and 70B).

Paper

Phi-2: The surprising power of small language models

HuggingFace Model Card

Hungry for more insights?

Don’t miss out on exploring other fascinating threads in this series. Simply click here and uncover the state-of-the-art research!

Do Subscribe for weekly updates!!

By Ritvik Rastogi on March 22, 2024.

Canonical link

Exported from Medium on May 4, 2026.
