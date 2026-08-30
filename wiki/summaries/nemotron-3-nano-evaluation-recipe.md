# The Open Evaluation Standard: Benchmarking NVIDIA Nemotron 3 Nano with NeMo Evaluator

**Source**: `raw/nemotron-3-nano-evaluation-recipe/full-article.html`, `raw/nemotron-3-nano-evaluation-recipe/full-article.md`
**Ingested**: 2026-07-10
**Tags**: #summary

## Summary

An NVIDIA post arguing it has become increasingly hard to tell whether a model's reported gains reflect genuine advances or just variation in evaluation conditions, dataset composition, or benchmark-contaminated training data. NVIDIA addresses this for [[Papers Explained 506 - Nemotron 3 Nano]] by publishing the complete evaluation recipe used to generate its model-card results, built on the open-source NeMo Evaluator library, so anyone can rerun the pipeline, inspect the artifacts, and independently verify the numbers.

NeMo Evaluator is framed as a unifying orchestration layer rather than a new standalone benchmark runner: it integrates and coordinates hundreds of benchmarks from existing evaluation harnesses (NeMo Skills for instruction-following/tool-use/agentic evals, LM Evaluation Harness for base-model/pretraining benchmarks, and others), letting each harness retain its native logic, datasets, and scoring semantics while NeMo Evaluator standardizes configuration, execution, and logging. This gives two practical properties beyond convenience: methodology independence from inference backend (the same config can run against hosted endpoints, local deployments, or third-party providers like HuggingFace, build.nvidia.com, or OpenRouter, so infrastructure changes don't confound comparisons), and default production of structured, inspectable artifacts (per-task `results.json` files plus execution logs) so a score's provenance can be audited rather than trusted blindly.

The post publishes the exact YAML configuration used for Nemotron 3 Nano 30B A3B's model-card evaluation (inference/deployment settings, benchmark/task selection, per-benchmark sampling and prompt-template parameters, runtime controls, output paths) and walks through reproducing it end-to-end via the `nemo-evaluator-launcher` CLI against a hosted build.nvidia.com endpoint, covering running the full suite, individual benchmarks via `-t` flags, and monitoring/inspecting results. It is explicit that reproduction is not expected to be bit-for-bit identical: decoding settings, repeated trials, judge-based scoring, parallel execution, and serving-infrastructure differences all introduce legitimate run-to-run variance. The stated goal is methodological consistency with clear provenance (using the same config, benchmark selection, inference target, and execution settings) rather than deterministic output matching.

## Key Claims

- NeMo Evaluator is an orchestration layer unifying multiple existing evaluation harnesses (NeMo Skills, LM Evaluation Harness, others) under one config/execution/logging interface, rather than a new standalone benchmark runner.
- Evaluation methodology is decoupled from inference backend: the same config can target hosted endpoints, local deployments, or third-party providers (HuggingFace, build.nvidia.com, OpenRouter), enabling infrastructure-independent comparison.
- NVIDIA publishes the exact YAML configuration used to produce Nemotron 3 Nano 30B A3B's model-card benchmark numbers, plus structured per-task `results.json` artifacts and execution logs for every run, by default.
- Published benchmark results for Nemotron 3 Nano 30B A3B:

| Benchmark | Accuracy | Category |
|---|---|---|
| BFCL v4 | 53.8 | Function Calling |
| LiveCodeBench (v6, 2025-08–2025-05) | 68.3 | Coding |
| MMLU-Pro | 78.3 | Knowledge |
| GPQA | 73.0 | Science |
| AIME 2025 | 89.1 | Mathematics |
| SciCode | 33.3 | Scientific Coding |
| IFBench | 71.5 | Instruction Following |
| HLE | 10.6 | Humanity's Last Exam |
- The post explicitly frames evaluation reproducibility as methodological consistency with legitimate run-to-run variance (from decoding settings, repeated trials, judge-based scoring, parallelism, serving differences), not bit-wise identical outputs.
- An enterprise-grade NeMo Evaluator microservice, built on the same principles, is offered separately for organizations needing automated/large-scale evaluation pipelines.

## Figures

No figures were extracted for this ingest, per this batch's no-figure-download policy; the article is primarily text, a benchmark table, and CLI code examples (both fully preserved above/in the raw markdown).

## Entities

- [[NVIDIA]] — develops NeMo Evaluator and the Nemotron 3 Nano model line being benchmarked.
- [[Hugging Face]] — hosts the model weights and the Enterprise blog post; the evaluation workflow also targets HuggingFace-hosted endpoints as one of its supported inference targets.

## Questions & Gaps

- No comparison is given against other models' scores on the same benchmark suite; the post focuses entirely on the reproducibility methodology for Nemotron 3 Nano's own numbers rather than competitive positioning.
- The post does not quantify the actual observed variance across repeated runs (e.g. a reported standard deviation on AIME 2025 or HLE), only that variance is expected and explained.

## Related

- [[Papers Explained 506 - Nemotron 3 Nano]] — the base model whose model-card results this evaluation recipe reproduces.
- [[Introducing NVIDIA Nemotron 3 Nano Omni: Long-Context Multimodal Intelligence for Documents, Audio and Video Agents]] — the omni-modal extension of the same Nemotron 3 Nano line.
- [[Data for Agents]]
