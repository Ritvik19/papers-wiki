# Open R1: Update #4

**Source**: `raw/open-r1-update-4/full-article.md` (200 KB), `raw/open-r1-update-4/full-article.md`
**Ingested**: 2026-07-10
**Tags**: #summary

## Summary

Fourth [[Open-R1: A Fully Open Reproduction of DeepSeek-R1]] update, covering DeepSeek's quiet release of DeepSeek-V3-0324, an updated version of the base model underlying DeepSeek-R1. The refreshed model kept V3's architecture but switched to an MIT license (from V3's original custom license) and showed clear benchmark gains: MMLU-Pro 75.9 to 81.2, GPQA 59.1 to 68.4, AIME 39.6 to 59.4, LiveCodeBench 39.2 to 49.2. DeepSeek's model card cited targeted improvements in front-end web development, Chinese writing proficiency, multi-turn rewriting, translation, and function-calling accuracy. Since no technical report accompanied the release, the post speculates the gains likely came from continual pretraining on newer/better-curated data and/or improved post-training, rather than an architecture change.

The bulk of the post is a practical "how to use it" and "is it safe?" guide, reflecting the intense scrutiny DeepSeek models were receiving at the time. Usage options covered: Hugging Face Inference Providers (Fireworks, Hyperbolic, Novita), Text Generation Inference 3.2.1, SGLang (with Multi-Head Latent Attention and Data Parallelism), and Unsloth's Dynamic Quantizations for running the model with roughly half the compute of one H100 node via llama.cpp. On safety, the post separates two questions: is downloading/running the model safe (yes, given `safetensors` weight storage, visible modeling code requiring explicit `trust_remote_code=True`, and Hub malicious-code scanning), and are the model's outputs safe to use unsupervised (the standard LLM caveats apply regardless of provider: alignment is opaque and can shift, code generation can reproduce known vulnerabilities, and agentic use needs sandboxing, scoped credentials, and human-in-the-loop review for high-stakes actions).

## Key Claims

- DeepSeek-V3-0324 benchmark deltas over the original V3: MMLU-Pro +5.3 (75.9 to 81.2), GPQA +9.3 (59.1 to 68.4), AIME +19.8 (39.6 to 59.4), LiveCodeBench +10.0 (39.2 to 49.2).
- License changed from a custom DeepSeek license to MIT for the 0324 update.
- Downloading and running the model is safe due to `safetensors` weight format (no arbitrary code execution risk) plus visible, `trust_remote_code`-gated, Hub-scanned modeling code.
- Unsloth's Dynamic Quantizations let DeepSeek-V3-0324 run with roughly half the compute of one H100 node via llama.cpp with limited benchmark degradation.
- Open-model output-safety risks fall into three buckets: alignment mismatch (opaque, can shift, fixable via fine-tuning as with Perplexity's R1 1776), code generation (may reproduce known vulnerabilities from training data), and agentic use (needs sandboxing, scoped credentials, human-in-the-loop for high-stakes actions).

## Figures

No figures were extracted for this ingest; the benchmark comparison chart and refusal-frequency comparison (DeepSeek vs Perplexity's R1 1776) are described inline but not downloaded, per this batch's no-figure-download policy.

## Entities

- [[Hugging Face]] — publishes the update and runs the open-r1 project.
- [[DeepSeek]] — releases the DeepSeek-V3-0324 model covered here.

## Questions & Gaps

- No technical report accompanied DeepSeek-V3-0324; the continual-pretraining vs. improved-post-training explanation is explicitly speculative.
- The post doesn't quantify how much of the accuracy gain, if any, comes from the license change enabling wider community fine-tuning/evaluation versus the base model update itself.

## Related

- [[Open R1: Update #3]] — prior update, covering the CodeForces-CoTs dataset and OlympicCoder models.
- [[Open-R1: A Fully Open Reproduction of DeepSeek-R1]] — project this update reports on.
- [[DeepSeek]]
- [[Large Language Models]]
