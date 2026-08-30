# Granite 4.0 Nano: Just How Small Can You Go?

**Source**: `raw/granite-4-nano/full-article.md` (205 KB)
**Ingested**: 2026-07-10
**Tags**: #summary

## Summary

IBM's launch post for Granite 4.0 Nano, the smallest models in the Granite 4.0 family, aimed at edge and on-device deployment. The release comprises four instruct models (plus base counterparts): Granite 4.0 H 1B and Granite 4.0 H 350M, both dense LLMs using Granite 4.0's hybrid-SSM architecture, and Granite 4.0 1B / Granite 4.0 350M, traditional (non-hybrid) transformer versions of the same two sizes, released specifically to support runtimes like llama.cpp where hybrid architectures may not yet have optimized kernel support. All variants are Apache 2.0, trained on the same 15T+ token corpus and training pipeline as the larger Granite 4.0 models, and carry IBM's ISO 42001 certification for responsible model development.

The post frames sub-1B to ~1B parameter models as an active, competitive space (citing Qwen, LiquidAI's LFM, and Gemma as comparison points) and reports that Granite 4.0 Nano shows a meaningful capability jump over similarly sized peers on general benchmarks spanning knowledge, math, code, and safety, as well as on agentic-workflow-relevant tasks: instruction following (IFEval) and tool calling (BFCL v3).

## Key Claims

- Granite 4.0 Nano models (0.2B-2B range) show higher average accuracy than comparably sized competitor models across combined Knowledge, Math, Code, and Safety benchmarks (chart-based comparison, no baseline numbers included in the archived text).
- Granite Nano models outperform several similarly sized models on IFEval and BFCL v3, the two benchmarks the post highlights as most relevant to agentic workflows (instruction following and tool calling).
- Native runtime support across vLLM, llama.cpp, and MLX from release.
- Four size/architecture variants released, each with base and instruct checkpoints: Granite 4.0 H 1B (hybrid-SSM, ~1.5B), Granite 4.0 H 350M (hybrid-SSM, ~350M), Granite 4.0 1B (traditional transformer), and Granite 4.0 350M (traditional transformer).

## Figures

No figures were extracted for this ingest; the post's two benchmark charts (average accuracy across Knowledge/Math/Code/Safety, and IFEval/BFCL v3 accuracy) are referenced but not downloaded, per this batch's no-figure-download policy, and contain no numeric axis labels recoverable from the archived text.

## Entities

- [[IBM]] — releasing organization; Granite model family.
- [[Hugging Face]] — hosts the blog and model weights.

## Questions & Gaps

- The archived post's charts are image-only with no accompanying data table, so the specific accuracy numbers behind the "significant increase in capabilities" claim could not be extracted; only the qualitative claim is captured here.
- No architectural detail is given for the hybrid-SSM design beyond "Granite 4.0's new, efficient hybrid architecture." Full specification is deferred to the Hugging Face model cards, which were not part of this ingest.
- Exact parameter counts for the base transformer variants (1B / 350M) versus their hybrid-SSM counterparts (H 1B / H 350M) are approximate ("~1.5B", "~350M") in the source text.

## Related

- [[Granite 4.1 LLMs: How They're Built]] — sibling post covering the larger 3B/8B/30B dense Granite 4.1 models and the shared training pipeline/data recipe.
- [[IBM]]
- [[Large Language Models]]
- [[Model Compression and Efficiency]]
