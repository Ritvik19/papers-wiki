Source URL: https://huggingface.co/blog/nvidia/nemotron-3-nano-evaluation-recipe
Title: The Open Evaluation Standard: Benchmarking NVIDIA Nemotron 3 Nano with NeMo Evaluator

# The Open Evaluation Standard: Benchmarking NVIDIA Nemotron 3 Nano with NeMo Evaluator

Published December 17, 2025

Seph Mard, Isabel Hulseman, Besmira Nushi, Piotr Januszewski, Grzegorz Chlebus, Vivienne Zhang, Wojciech Prazuch, Pablo Ribalta, Nik Spirin, Ferenc Galko (NVIDIA)

An NVIDIA post arguing that it has become increasingly hard to tell whether a model's reported improvements reflect genuine advances or just variation in evaluation conditions, dataset composition, or benchmark-contaminated training data — and addressing this for Nemotron 3 Nano 30B A3B by publishing the complete evaluation recipe used to generate its reported results, built on NVIDIA's open-source NeMo Evaluator library, so anyone can rerun the pipeline, inspect the artifacts, and independently verify the numbers.

NeMo Evaluator is framed as a unifying orchestration layer rather than a new standalone benchmark runner: it integrates and coordinates benchmarks from multiple existing evaluation harnesses (NeMo Skills for instruction-following/tool-use/agentic evals, LM Evaluation Harness for base-model/pretraining benchmarks, and others), letting each harness retain its native logic, datasets, and scoring semantics while NeMo Evaluator standardizes how they're configured, executed, and logged. This gives two practical properties beyond convenience: methodology independence from inference backend (the same config can run against hosted endpoints, local deployments, or third-party providers, so infrastructure changes don't confound comparisons), and default production of structured, inspectable artifacts (per-task `results.json` files and execution logs) so a score's provenance can be audited rather than trusted blindly.

The post publishes the exact published YAML configuration used for Nemotron 3 Nano 30B A3B's model-card evaluation (model inference/deployment settings, benchmark/task selection, per-benchmark parameters like sampling and prompt templates, runtime controls, output paths) and walks through reproducing it end-to-end via the `nemo-evaluator-launcher` CLI against a hosted build.nvidia.com endpoint, including running the full suite, individual benchmarks via `-t` flags, and monitoring/inspecting results. It's explicit that reproduction is not expected to be bit-for-bit identical — decoding settings, repeated trials, judge-based scoring, parallel execution, and serving-infrastructure differences all introduce legitimate run-to-run variance — and frames the goal as methodological consistency with clear provenance rather than deterministic output matching.

## Key Claims

- NeMo Evaluator is an orchestration layer unifying multiple existing evaluation harnesses (NeMo Skills, LM Evaluation Harness, others) under one config/execution/logging interface, rather than a new standalone benchmark runner.
- Evaluation methodology is decoupled from inference backend: the same config can target hosted endpoints, local deployments, or third-party providers (HuggingFace, build.nvidia.com, OpenRouter), enabling infrastructure-independent comparison.
- NVIDIA publishes the exact YAML configuration used to produce Nemotron 3 Nano 30B A3B's model-card benchmark numbers, plus structured per-task `results.json` artifacts and execution logs for every run, by default.
- Published benchmark results for Nemotron 3 Nano 30B A3B: BFCL v4 53.8 (function calling), LiveCodeBench 68.3 (coding), MMLU-Pro 78.3 (knowledge), GPQA 73.0 (science), AIME 2025 89.1 (math), SciCode 33.3 (scientific coding), IFBench 71.5 (instruction following), HLE 10.6 (Humanity's Last Exam).
- The post explicitly frames evaluation reproducibility as methodological consistency with legitimate run-to-run variance (from decoding settings, repeated trials, judge-based scoring, parallelism, serving differences), not bit-wise identical outputs.
- An enterprise-grade NeMo Evaluator microservice, built on the same principles, is mentioned as a separate offering for organizations needing automated/large-scale evaluation pipelines.

## Figures

No figures were extracted for this ingest, per this batch's no-figure-download policy; the article is primarily text, a benchmark table, and CLI code examples.

## Entities

- [[NVIDIA]] — develops NeMo Evaluator and the Nemotron 3 Nano model line being benchmarked.
- [[Hugging Face]] — hosts the model weights and Enterprise blog post; the evaluation workflow also targets HuggingFace-hosted endpoints as one of its supported inference targets.

## Questions & Gaps

- No comparison is given against other models' scores on the same benchmark suite; the post focuses entirely on the reproducibility methodology for Nemotron 3 Nano's own numbers rather than competitive positioning.
- The post does not quantify the actual observed variance across repeated runs (e.g. a reported standard deviation on AIME 2025 or HLE), only that variance is expected and explained.

## Related

- [[NVIDIA Nemotron 3 Nano Omni: Long-Context Multimodal Intelligence for Documents, Audio and Video Agents]]
- [[Data for Agents]]
