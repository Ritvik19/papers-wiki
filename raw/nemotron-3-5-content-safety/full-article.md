Source URL: https://huggingface.co/blog/nvidia/nemotron-3-5-content-safety
Title: Nemotron 3.5 Content Safety: Customizable Multimodal Safety for Global Enterprise AI

# Nemotron 3.5 Content Safety: Customizable Multimodal Safety for Global Enterprise AI

Published June 4, 2026

Varun Singh, Isabel Hulseman, Anuj Doshi, Shyamala Prayaga (NVIDIA)

The last two years have seen NVIDIA's content safety stack grow from a focused English text classifier into a family of specialized models, each extending coverage to new modalities, languages, and inference modes. Nemotron 3 Content Safety, released in March 2026, combined multimodal and multilingual capabilities for the first time in a single 4B-parameter model. Nemotron 3.5 Content Safety completes that arc: a single model that unifies multimodal input, multilingual reach, custom enterprise policy enforcement, and auditable reasoning into one inference call.

## What's New in Nemotron 3.5 Content Safety

### 1. Unified Multimodal Evaluation

Nemotron 3 introduced image understanding; Nemotron 3.5 deepens the multimodal integration. The model takes a user prompt, an optional image, and an optional assistant response as a single context window and produces a coherent safety verdict over the combined input. Evaluating all three together, rather than scoring each independently, closes a gap in multimodal safety: policy violations that only emerge from the interaction between text and image, or between request and response, are caught in a single pass.

### 2. Global Language Coverage

Nemotron 3.5 maintains the 12-language explicit training coverage of its predecessors (English, French, Spanish, German, Chinese, Japanese, Korean, Arabic, Hindi, Russian, Portuguese, Italian) while inheriting zero-shot generalization across roughly 140 languages from the Gemma 3 base model, benefiting deployments in markets with sparse training data (Southeast Asian, Scandinavian, less-resourced African languages).

### 3. Custom Policy Enforcement

The most significant architectural addition relative to Nemotron 3. Production deployments rarely operate under a single universal safety taxonomy: a healthcare platform has a different risk profile than a financial chatbot, a developer tools IDE, or a children's education app. Nemotron 3.5 accepts a custom policy specification alongside the input and reasons over that policy when producing its verdict, rather than deferring entirely to the built-in taxonomy. This extends work first introduced in Nemotron Content Safety Reasoning 4B to the full multimodal, multilingual setting. Supports category suppression (disabling irrelevant categories, e.g. preventing a "violence" trigger when a DevOps tool handles "terminate a process") and custom category injection (proprietary risk categories per organization).

### 4. Reasoning Traces (THINK Mode)

Every verdict can be accompanied by an auditable reasoning trace via an optional think mode, outputting step-by-step reasoning before a final `safe`/`unsafe` label and, optionally, violated categories:

```
<think>
The user prompt asks for guidance on acquiring a controlled substance without a prescription.
The assistant response provides specific sourcing steps and references an online marketplace.
This interaction violates the Criminal Planning/Confessions and Controlled Substances categories.
The image (a pharmacy exterior) provides locational context but does not alter the verdict.
</think>

User Safety: unsafe
Response Safety: unsafe
Safety Categories: Criminal Planning/Confessions, Controlled Substances
```

THINK mode can be disabled to return to the same low-latency binary verdict available in Nemotron 3, when latency is the primary constraint.

### 5. Safety Dataset

NVIDIA is releasing its safety dataset alongside the model, an important milestone since most open-source safety models don't provide training/evaluation sets, particularly for multimodal artifacts (images, videos) often derived from restrictively-licensed sources. The dataset is multimodal, multilingual, and includes the safety reasoning traces used to train the model, generated in a 2-step process for conciseness.

## Model Architecture

Built on Google Gemma 3 4B IT (4B parameters), providing a 128K context window, vision-language reasoning, and multilingual coverage. NVIDIA fine-tunes this base with a LoRA adapter installing safety classification behavior while keeping the model compact enough for real-time deployment on 8GB+ VRAM GPUs.

Three inference output modes:
- **Mode 1** — low-latency binary verdict (`User Safety: safe` / `Response Safety: unsafe`)
- **Mode 2** — binary verdict with categories
- **Mode 3** — THINK mode (reasoning trace + verdict + categories)

The safety taxonomy follows the Aegis 2.0 framework: 13 core categories aligned with the MLCommons safety taxonomy, plus 10 fine-grained subcategories, allowing direct comparison with other guard systems benchmarked on Aegis-taxonomy datasets.

## Reasoning as a "Supercharger"

Reasoning provides context, customization, and accountability for production safety systems:
- **Custom and contextual policy enforcement**: dynamically interprets and enforces domain-specific policies defined in natural language at inference time.
- **Auditable, documented justification**: reasoning traces support compliance/audit logging, human review of edge-case errors, and iterative policy-language refinement.
- **Latency mitigation**: reasoning chains are condensed into concise summaries via a 2-step teacher process (Qwen 397B generates chain-of-thought traces given ground-truth labels; Qwen 80B rephrases them to fit within 3 sentences), keeping most traces under 3 sentences.

## Training Data

- Multilingual text safety data from Nemotron Safety Guard Dataset v3, sampled from culturally nuanced subsets with proportional representation across safety categories and safe/unsafe splits.
- Human-annotated multimodal data collected in English, translated into 12 languages; 99% of training images are real photographs, not synthetic generations — addressing a known weakness where benchmarks like VLGuard and MM-SafetyBench rely heavily on SDXL-generated images lacking cultural texture and adversarial complexity. A subset of Wikimedia and synthetic images is released due to licensing constraints on the rest.
- Safe multimodal data from Nemotron VLM Dataset v2 (scanned documents, charts, papers, diagrams) to prevent over-flagging benign professional content.
- Reasoning traces from Qwen 397B (chain-of-thought) shortened via Qwen 80B.
- Topic-following data from the CantTalkAboutThis dataset: policy-specification/verdict pairs across enterprise deployment scenarios (healthcare, finance, banking, education).
- Synthetic data (~10% of total volume) to diversify jailbreak patterns, rare policy violations, and multimodal adversarial cases.

## Benchmarking

Evaluated across VLGuard, MM-SafetyBench, PolyGuard, RTP-LX, Aya Redteaming, XSafety, MultiJail, Aegis, Dynaguardrail, and CoSA. Nemotron 3 set a baseline of 84% average accuracy on multimodal harmful-content tests at roughly half the latency of LlamaGuard-4-12B; Nemotron 3.5 maintains that 4B efficiency while adding custom policy support and reasoning traces, averaging about 85% across the evaluated benchmark set.

| Benchmark | Result |
|---|---|
| Multilingual Aegis (12 languages) | 96.5% average harmful-f1 |
| RTP-LX (12 languages) | 88.8% average harmful-f1 |
| Combined Aegis + RTP-LX | 92.7% average |
| Latency vs. an alternative multimodal safety model | 3x lower end-to-end latency |
| Token generation (reasoning enabled) vs. another reasoning safety model | up to 50% fewer tokens |

(Note: figures/charts referenced in the article — benchmark bar charts for Multilingual Aegis and RTP-LX per-language accuracy, and latency comparison charts — were not extracted; numbers above are transcribed from the article text.)

## Latency

Default (no THINK) mode latency is unchanged from Nemotron 3. THINK mode adds inference time proportional to trace length; this overhead is predictable and can be budgeted separately, e.g. running THINK-mode evaluation asynchronously in an audit pipeline while the default mode handles real-time decisions.

## Addressing the Benchmark Gap

Development encountered gaps documented in the broader multimodal safety literature:
- **Text-only coverage**: widely-cited benchmarks (WildGuard, XSTest, HarmBench) are text-only; multimodal performance cannot be inferred from them.
- **Synthetic image quality**: most multimodal benchmarks use AI-generated (typically SDXL) images rather than real photographs, understating real-world difficulty.
- **Real-image licensing**: stock photo licenses prohibit redistribution in AI datasets, creating a structural gap between research and production conditions.

NVIDIA's multimodal training data (real images, culturally nuanced multilingual prompts) is designed to fill some of these gaps for training; the evaluation-side benchmark gap remains an open problem for the broader research community.

## Getting Started

Available on Hugging Face under the NVIDIA Open Model License for research and commercial use, along with the training dataset. Supports `transformers`, vLLM, and SGLang; also available as a production-grade NVIDIA NIM on build.nvidia.com, and through inference platforms including Baseten, Eigen AI, DeepInfra, OpenRouter, and Vultr. NVIDIA provides a Claude- and Codex-compatible skill for generating custom policies, plus cookbooks for using the model.
