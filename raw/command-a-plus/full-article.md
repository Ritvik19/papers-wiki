# Introducing Command A+: Making sovereign agentic capabilities available to all

**Source URL**: https://cohere.com/blog/command-a-plus  
**Companion press release**: https://cohere.com/blog/cohere-releases-command-a-plus (saved as `press-release.html`)

Command A+. Our fastest, most powerful language model yet - available open-source.

May 20, 2026

## Introducing Command A+: Making sovereign agentic capabilities available to all

Our fastest and most powerful language model yet. Command A+ is an open-source enterprise workhorse built for complex reasoning, multimodal and multilingual agentic tasks — all while running on as little as two H100 GPUs.

Today, we're releasing Command A+ open-source. A mixture-of-experts (MoE) model, Command A+ is an efficient, versatile, and privately deployable LLM built for high-performance agentic tasks with minimal compute overhead.

Born from a year of deploying North with our customers, it surpasses every previous generation in the Command series and unifies their capabilities into a single scalable model.

Now freely available under an Apache 2.0 license, Command A+ advances Cohere's mission to make sovereign AI a technological reality — giving developers direct access to enterprise-grade agentic capabilities across experimentation, deployment, and production workflows.

### Snapshot

| Model | command-a-plus-05-2026 |
| --- | --- |
| License | Apache 2.0 |
| Architecture | Sparse / MoE |
| Model size | 218B total; 25B active |
| Context length | 128K input context; 64K max generation |
| Input modalities | Text, image, tool use |
| Output modalities | Text, reasoning, tool use |
| Languages | Supports 48 languages |
| Optimized for | Reasoning, agentic workflows, RAG, multilingual, multimodal document processing |
| Supported frameworks | vLLM, Transformers |
| Hardware (minimum) | 1× B200 @ W4A4; 2× H100s @ W4A4 |

### Northwards

For the past year, North — Cohere's integrated enterprise workspace for building and deploying agentic AI — has been the driving force behind much of our innovation. Through that work, we set out to build a unified model for customers that simplifies deployment, can run locally, and synthesizes capabilities from across the Command family.

### Command, consolidated

Command A+ outperforms previous Command A models in key dimensions of enterprise workloads, including multimodal understanding, retrieval, long-horizon, and complex reasoning.

| Command A+ | Command A | Command A Reasoning | Command A Vision | Command A Translate |
| --- | --- | --- | --- | --- |
| Size | 218B A25B | 111B | 111B | 112B | 111B |
| Reasoning | ✓ | — | ✓ | — | — |
| Multimodal | ✓ | — | — | ✓ | — |
| Tool use | ✓ | ✓ | ✓ | — | — |
| Multilingual | 48 | 23 | 23 | 6 | 23 |

Compared with Command A Reasoning, τ²-Bench Telecom scores improved from 37% to 85%, with agentic coding performance on Terminal-Bench Hard reaching 25% from 3%. Gains were also achieved on non-agentic reasoning, instruction following, and other code generation tasks.

Command A+ performs strongly within North applications. Agentic Question Answering accuracy and spreadsheet analysis quality improved by 20% and 32% over Command A Reasoning, respectively. Memory performance scored 54% with Command A+ compared to 39% with Command A Reasoning.

For multimodal understanding and reasoning, Command A+ achieved 63% on MMMU Pro and 75.1% on MMMU (compared with 65.3% for Command A Vision for the latter). MathVista scores increased from 73.5% to 80.6%, and CharXiv reasoning improved from 46.9% to 52.7%.

Command A+ significantly expands multilingual capability, broadening language coverage from 23 to 48 languages and recording gains in machine translation and multilingual reasoning.

Command A+ achieved a score of 37 on the Artificial Analysis Intelligence Index, outperforming other leading open models.

### Efficiency at scale

Command A+ is available on Hugging Face in 16-bit (BF16), 8-bit (FP8), and 4-bit (W4A4) quantizations, with imperceptible differences in quality. In practice, this enables Command A+ to run on as little as two NVIDIA H100s or a single NVIDIA Blackwell GPU.

At the same quantization and concurrency levels, it delivers up to 63% higher Output Tokens per Second (TOPS), and reduces Time To First Token (TTFT) by up to 17%. The W4A4 quantization contributes an additional 47% increase in speed and a further 13% reduction in latency.

Cohere uses speculative decoding optimized for the model's MoE architecture, delivering an additional 1.5–1.6× inference speedup for both text and multimodal inputs.

Command A+ is the first model to use Cohere's latest tokenizer, delivering substantial compression improvements. Tokenization efficiency improved by 20% for Arabic, 16% for Korean, and 18% for Japanese.

### Getting started

Command A+ is available on Hugging Face, through Model Vault, Cohere API, and a free Space.
