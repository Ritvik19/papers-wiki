Source URL: https://huggingface.co/blog/nvidia/multilingual-reasoning-v1
Title: NVIDIA Releases 6 Million Multi-Lingual Reasoning Dataset

# NVIDIA Releases 6 Million Multi-Lingual Reasoning Dataset

Published August 20, 2025

Jane Polak Scowcroft, Dhruv Nathawani, Shuoyang Ding, Oleksii Kuchaiev, Vitaly Lavrukhin (NVIDIA)

NVIDIA continues releasing permissive datasets in support of the open ecosystem with a 6 Million Multilingual Reasoning Dataset. Continuing the success of the Nemotron Post-Training Dataset v1 release (used in the Llama Nemotron Super model) and the Llama Nemotron Post-Training Dataset released earlier in the year, NVIDIA releases the reasoning dataset translated into five target languages: French, Spanish, German, Italian, and Japanese.

Alongside the dataset, the post highlights the newly released NVIDIA Nemotron Nano 2 9B, which brings these multilingual reasoning capabilities to the edge with a hybrid Transformer-Mamba architecture and a configurable "thinking budget" letting developers dial accuracy, throughput, and cost to match real-world needs.

## Model Highlights (TL;DR) — NVIDIA Nemotron Nano 2 9B

- Model size: 9B parameters
- Architecture: Hybrid Transformer-Mamba (Mamba-2 + a small number of attention layers) for higher throughput at similar accuracy to Transformer-only peers
- Throughput: up to 6x higher token generation than other leading models in its size class
- Cost: thinking budget lets you control how many "thinking" tokens are used, saving up to 60% lower reasoning costs
- Target: agents for customer service, support chatbots, analytics copilots, and edge/RTX deployments
- Availability: model weights on Hugging Face, hosted endpoint on build.nvidia.com, and planned NVIDIA NIM availability
- License: nvidia-open-model-license

## What's in the Dataset and How It Was Built

The Nemotron Post-Training Dataset V2 takes the previously released English reasoning data and translates it into five target languages (French, German, Italian, Japanese, Spanish). To take advantage of English knowledge instilled during pretraining, only the user prompt and model response are translated, while the original English reasoning chain is preserved.

Per the WMT 2024 general translation shared task, LLMs achieve state-of-the-art results on machine translation benchmarks. However, NVIDIA's preliminary studies for synthetic post-training data translation found:

- LLMs are more prone to hallucination when translating SFT datasets compared to translating common machine-translation test sets (e.g. FLORES).
- Translation quality and hallucination rate of open-source LLMs deteriorate significantly as input length increases.

To maintain translation quality and enable hallucination detection, the pipeline:

- Breaks sentences down by newline and translates line-by-line; non-translatable lines (e.g. only tabs, or part of a code block) are left untranslated.
- Enforces a specific output format ("wrap the translated text in brackets 〘〙") and uses the matching bracket to extract translations, discarding examples that don't conform.
- Runs fastText language ID on translated prompt inputs to filter out off-target-language data points, discarding 55,567 examples (1.1% of all multilingual examples) on this basis.

| Language | code (discarded) | qa (discarded) | math (discarded) |
|---|---|---|---|
| de | 2.28% | 1.11% | 2.47% |
| es | 26.14% | 5.15% | 6.38% |
| fr | 11.01% | 1.37% | 1.96% |
| it | 4.94% | 1.36% | 0.75% |
| ja | 7.68% | 2.51% | 3.86% |

*Table 1: ratio of discarded data (measured by bytes) from enforcing the output format, by language and domain.*

After benchmarking, NVIDIA selected `Qwen2.5-32B-Instruct-AWQ` (for German) and `Qwen2.5-14B-Instruct` (for the other four languages) to perform the translation, based on: robust translation quality, ability to fit on a single A100 GPU for inference, wide domain coverage in training data, and an open (Apache 2.0) license.

## Usage

```python
from datasets import load_dataset
ds = load_dataset("nvidia/Nemotron-Post-Training-Dataset-v2")
```
