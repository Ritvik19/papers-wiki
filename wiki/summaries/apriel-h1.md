# Apriel-H1: The Surprising Key to Distilling Efficient Reasoning Models

**Source**: `raw/apriel-h1/full-article.md` (172 KB), `raw/apriel-h1/full-article.md`
**Ingested**: 2026-07-10
**Tags**: #summary

## Summary

ServiceNow converts its existing 15B reasoning model into a Mamba hybrid via distillation, achieving 2.1x inference throughput with minimal quality loss, and reports that the key to making this work was a counterintuitive choice about which data to distill on. The framing: MiniMax's public post-mortem on abandoning efficient attention at 230B scale (October 2025) briefly suggested "efficient attention is dead," but Kimi Linear's success days later showed it depends on the constraints. ServiceNow's constraint was having a strong existing 15B model with no budget for 20T-token pretraining or day-one architectural co-design, raising the question of whether efficiency can be retrofitted into an existing model purely through distillation.

The release, Apriel-H1, spans seven checkpoints with 25 to 40 Mamba layers (out of 50 total), tracing the full efficiency/quality frontier. The flagship, Apriel-H1-15b-Thinker-SFT (30 Mamba layers, 76.8B total training tokens), reaches 2.1x throughput with quality close to the full-attention teacher (MATH500 0.92 vs 0.90, MTBench 8.58 vs 8.30, GSM8k 0.95 vs 0.97, GPQA 0.55 vs 0.59, AIME24 0.65 vs 0.70); a more aggressive H-40 variant reaches 3.4x throughput at 136.5B tokens. For reference, NVIDIA's Nemotron-Nano-9B-v2 reaches 4.6x throughput at a similar quality score but required training from scratch with far more compute.

The key finding: distilling on pretraining data (even mixed with SFT) failed, sometimes badly, degrading reasoning quality regardless of mix ratio, despite the intuitive assumption that new, never-trained Mamba layers need general-purpose token-mixing signal to learn from scratch. What worked instead was distilling on high-quality reasoning traces from the teacher's own SFT dataset. The team's explanation: distilling a reasoning model isn't really about transferring general next-token prediction (the base model already has that); it's about preserving the teacher's specific, fragile multi-step reasoning patterns, which emerge from attention mechanisms like retrieval and induction heads connecting premises to conclusions many steps later. Replacing attention with Mamba's linear recurrence disrupts those mechanisms, and the hybrid must discover new paths to the same reasoning outcomes, which requires training examples where the reasoning structure is explicit and correct (multi-step math proofs, logically dependent coding tasks, detailed scientific explanatory chains); noisy, diffuse pretraining data doesn't carry a strong enough reasoning signal to survive the transition. The team also found reverse KL divergence (temperature 1) consistently beat forward KL for distillation, reasoning that since training happens on problems where the teacher is confident and structured, reverse KL's mode-seeking behavior pushes the student to commit to those high-confidence predictions rather than spreading probability mass across the teacher's full distribution.

The staged distillation procedure has three phases. First, a Leave-One-Out (LOO) analysis on MMLU (removing each layer, replacing it with identity, measuring the accuracy drop) ranks layers by importance; the 25 least-important are replaced with Mamba-in-Llama (MIL)-initialized mixers and distilled end-to-end, producing checkpoint H-25. Second, past 25 layers, LOO breaks down because layers unimportant in isolation become critical in combination, so a dynamic heuristic (MIL-Mamba-Replacement, MMR) initializes a Mamba mixer for each remaining attention layer, runs 100 training steps, and ranks layers by which converge to lower distillation loss ("easier to replace"); conversion proceeds incrementally (25 -> 27 -> 30 -> 34 -> 37 -> 40 Mamba layers), each checkpoint distilled from the previous one. Third, once the target Mamba-layer count is reached, a final end-to-end SFT pass runs on the reasoning data until performance stabilizes (55.9B distillation tokens plus 20.9B SFT tokens for the flagship checkpoint). The work is built on Fast-LLM, ServiceNow's Apache-2.0 training framework, whose core design treats attention and Mamba as interchangeable implementations of a shared "mixing" interface configurable per block via YAML, and is implemented for production in Hugging Face Transformers (new interchangeable-mixer model class) and vLLM (using Mamba cache operations for continuous batching, prefix caching, and chunked prefill), though the vLLM plugin was pending legal approval to open-source at time of writing.

## Key Claims

- Apriel-H1-15b-Thinker-SFT (30/50 Mamba layers, 76.8B tokens): 2.1x throughput, near-parity with the full-attention teacher on MATH500 (0.92 vs 0.90), MTBench (8.58 vs 8.30), GSM8k (0.95 vs 0.97), GPQA (0.55 vs 0.59), AIME24 (0.65 vs 0.70).
- H-40 variant (136.5B tokens): 3.4x throughput at 0.76 average score, versus NVIDIA Nemotron-Nano-9B-v2's 4.6x throughput at 0.77 score, achieved via from-scratch training with substantially more compute.
- Distilling on pretraining data (pure or SFT-mixed) failed to preserve reasoning quality; distilling on the teacher's own high-quality SFT reasoning traces was the key to success.
- Reverse KL divergence (temperature 1) consistently outperformed forward KL for distillation in this setting.
- Staged conversion: LOO-ranked replacement for the first 25 layers, then a dynamic MMR heuristic (100 training steps per candidate layer, ranked by resulting distillation loss) for incremental conversion up to 40 layers.
- Built on Fast-LLM (Apache 2.0), where attention and Mamba are interchangeable "mixer" implementations configurable per decoder block via YAML.
- Production integration ships in Hugging Face Transformers and vLLM (Mamba cache ops for continuous batching, prefix caching, chunked prefill); the vLLM plugin's open-source release was pending legal approval at publication time.
- RL was explicitly out of scope for this release (a scoping decision to isolate whether reasoning transfers via distillation alone), expected to close remaining quality gaps in future iterations.

## Figures

No figures were extracted for this ingest; the efficiency-vs-quality frontier chart across all seven checkpoints is described inline but not downloaded, per this batch's no-figure-download policy. The benchmark table and Fast-LLM YAML config snippet are preserved as markdown/code in the source file.

## Entities

- [[ServiceNow]] — develops Apriel-H1 and the underlying Fast-LLM training framework.
- [[NVIDIA]] — Nemotron-Nano-9B-v2 is cited as a from-scratch-trained comparison point on the efficiency/quality frontier.
- [[Hugging Face]] — hosts the blog post; Apriel-H1 ships as a new model class in Hugging Face Transformers.

## Questions & Gaps

- The post does not test or report results from combining distillation with RL, framing this as future work to close remaining quality gaps rather than something evaluated here.
- No comparison is given against MOHAWK's multi-stage procedure beyond a stated preliminary finding that it showed no significant advantage over Mamba-in-Llama initialization plus knowledge distillation; details of that comparison aren't included.

## Related

- [[PipelineRL]] — an earlier ServiceNow RL infrastructure post; both reflect ServiceNow's SLAM Lab efficient-training research line.
- [[Mixture of Experts]]
- [[Reasoning Models]]
