# NVIDIA Releases 6 Million Multi-Lingual Reasoning Dataset

**Source**: `raw/multilingual-reasoning-v1/full-article.html`, `raw/multilingual-reasoning-v1/full-article.md`
**Ingested**: 2026-07-10
**Tags**: #summary

## Summary

NVIDIA releases the Nemotron Post-Training Dataset v2, a 6-million-example multilingual reasoning dataset, continuing from the Nemotron Post-Training Dataset v1 (used to train the Llama Nemotron Super model) and the earlier Llama Nemotron Post-Training Dataset. V2 takes the previously released English reasoning data and translates the user prompt and model response into five target languages (French, German, Italian, Japanese, Spanish), while deliberately preserving the original English reasoning chain, on the premise that this better exploits English-dominant pretraining knowledge than translating the reasoning trace itself.

NVIDIA's preliminary studies found that LLMs used for translation are more prone to hallucination on SFT-style data than on standard machine-translation test sets (e.g. FLORES), and that translation quality/hallucination rate for open models degrades noticeably as input length grows. To manage this, the translation pipeline breaks text into lines and translates line-by-line (skipping non-translatable lines such as pure whitespace or code), enforces a bracket-wrapped output format to make correctly-formed translations mechanically extractable, and runs fastText language identification on translated prompts to discard off-target-language outputs, filtering out 55,567 examples (1.1% of all multilingual examples) on that basis. After benchmarking, NVIDIA selected `Qwen2.5-32B-Instruct-AWQ` for German and `Qwen2.5-14B-Instruct` for the other four languages, chosen for translation quality, single-A100 inference feasibility, broad training-domain coverage, and an Apache-2.0 license.

Alongside the dataset, the post highlights NVIDIA Nemotron Nano 2 9B, which brings these multilingual reasoning capabilities to edge deployment via a hybrid Transformer-Mamba (Mamba-2 plus a small number of attention layers) architecture with a configurable "thinking budget" that lets developers trade off accuracy, throughput, and reasoning cost. NVIDIA reports up to 6x higher token-generation throughput than other leading models in its size class, and up to 60% lower reasoning cost via the thinking-budget control. This model corresponds to the architecture covered in [[Papers Explained 454 - Nemotron Nano 2]].

## Key Claims

- The Nemotron Post-Training Dataset v2 contains ~6 million multilingual reasoning examples, translating English post-training data (prompt + response only, reasoning chain kept in English) into French, German, Italian, Japanese, and Spanish.
- Enforcing a bracket-delimited translation output format and fastText-based language-ID filtering discarded 55,567 examples (1.1% of all multilingual examples); per-language/domain discard rates varied substantially:

| Language | Code | QA | Math |
|---|---|---|---|
| German | 2.28% | 1.11% | 2.47% |
| Spanish | 26.14% | 5.15% | 6.38% |
| French | 11.01% | 1.37% | 1.96% |
| Italian | 4.94% | 1.36% | 0.75% |
| Japanese | 7.68% | 2.51% | 3.86% |
- `Qwen2.5-32B-Instruct-AWQ` was used for German translation and `Qwen2.5-14B-Instruct` for French/Spanish/Italian/Japanese, selected for quality, single-A100 feasibility, domain coverage, and Apache-2.0 licensing.
- NVIDIA Nemotron Nano 2 9B (highlighted alongside the dataset) is a hybrid Transformer-Mamba model claiming up to 6x higher throughput than similarly-sized peers and up to 60% lower reasoning cost via a configurable thinking budget.
- The dataset and model both ship under the `nvidia-open-model-license`, with weights on Hugging Face, a hosted endpoint on build.nvidia.com, and planned NVIDIA NIM availability.

## Figures

No figures were extracted for this ingest, per this batch's no-figure-download policy; the discard-rate table (Table 1) is preserved inline above as markdown.

## Entities

- [[NVIDIA]] — publishes the dataset and the Nemotron Nano 2 9B model.
- [[Hugging Face]] — hosts the dataset and the blog post.
- [[Qwen]] — `Qwen2.5-32B-Instruct-AWQ` and `Qwen2.5-14B-Instruct` are the translation models used to build the dataset.

## Questions & Gaps

- No downstream evaluation is given showing that models fine-tuned on the translated data actually perform better on multilingual reasoning benchmarks than models trained on English-only data; the post focuses on data-construction methodology rather than measured downstream gains.
- The post does not explain why Spanish shows a substantially higher code-domain discard rate (26.14%) than the other four languages, beyond attributing discards generally to format-compliance and language-ID filtering.

## Related

- [[Papers Explained 454 - Nemotron Nano 2]] — the hybrid Mamba-Transformer model architecture highlighted in this post.
- [[Nemotron-Personas-India: Synthesized Data for Sovereign AI]] — another NVIDIA multilingual/localization-focused data release from the same era.
- [[Data for Agents]]
