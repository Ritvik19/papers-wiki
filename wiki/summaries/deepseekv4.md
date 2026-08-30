# DeepSeek-V4: A Million-Token Context That Agents Can Actually Use

**Source**: `raw/deepseekv4/full-article.html` (181 KB), `raw/deepseekv4/full-article.md`
**Ingested**: 2026-07-10
**Tags**: #summary

## Summary

DeepSeek released V4 as two MoE checkpoints: DeepSeek-V4-Pro (1.6T total / 49B active) and DeepSeek-V4-Flash (284B total / 13B active), both with a 1M-token context window. The Hugging Face blog post argues the headline benchmark numbers are "competitive, but not SOTA" and that the real story is architectural: V4 is built specifically to make long-context inference cheap enough for agentic workloads, where every tool-call round trip appends to the context and every subsequent token pays full attention cost against everything that came before.

The efficiency gain comes from splitting attention into two interleaved mechanisms across layers. Compressed Sparse Attention (CSA) pools KV entries 4x along the sequence dimension via softmax-gated pooling with a learned positional bias, then a lightning indexer (FP4, ReLU-scored multi-head dot product) selects top-k compressed blocks per query, inheriting the sparse-selection idea from [[DeepSeek Sparse Attention]] in V3.2 but running it over an already-4x-shorter sequence. Heavily Compressed Attention (HCA) compresses KV entries 128x and drops sparse selection entirely, since the compressed stream is short enough for cheap dense attention. In V4-Pro's 61-layer stack, layers 0-1 are HCA, layers 2-60 alternate CSA/HCA, and the trailing MTP block runs sliding-window only. Both paths store most KV entries in FP8 (BF16 only for RoPE dimensions), and residual connections use manifold-constrained hyper-connections (mHC) instead of standard residuals.

At 1M tokens, V4-Pro needs 27% of V3.2's single-token inference FLOPs and 10% of its KV cache memory; V4-Flash needs 10% of the FLOPs and 7% of the cache. Against a standard 8-head GQA baseline in bf16, V4's cache footprint is roughly 2%.

Beyond the architecture, three post-training/infra choices target agents directly: reasoning traces are now preserved across user-turn boundaries whenever the conversation contains tool calls (previously flushed on every new user message in V3.2), a new `|DSML|` XML-based tool-call schema separates string from structured parameters to cut JSON-escaping failures, and DSec (a Rust sandbox platform exposing function calls, containers, microVMs via Firecracker, and full VMs via QEMU behind one Python SDK) runs hundreds of thousands of concurrent RL rollout sandboxes with preemption-safe trajectory replay.

## Key Claims

- Terminal Bench 2.0: V4-Pro-Max 67.9, ahead of GLM-5.1 (63.5) and K2.6 (66.7); behind GPT-5.4-xHigh (75.1) and Gemini-3.1-Pro (68.5).
- SWE-bench Verified: V4-Pro-Max 80.6, within a point of Opus-4.6-Max (80.8) and Gemini-3.1-Pro (80.6).
- MCPAtlas Public: V4-Pro-Max 73.6, second only to Opus-4.6-Max (73.8).
- Toolathlon: V4-Pro-Max 51.8, ahead of K2.6 (50.0), GLM-5.1 (40.7), Gemini-3.1-Pro (48.8).
- Internal R&D coding benchmark (30 curated PyTorch/CUDA/Rust/C++ tasks): V4-Pro-Max 67% pass rate vs. Sonnet 4.5 (47%) and Opus 4.5 (70%).
- Developer survey (n=85 DeepSeek engineers using V4-Pro daily): 52% said it was ready to replace their primary coding model, 39% leaned toward yes.
- MRCR 8-needle retrieval accuracy stays above 0.82 through 256K tokens and holds at 0.59 at 1M.
- Four checkpoints released: `DeepSeek-V4-Pro`, `DeepSeek-V4-Flash`, `DeepSeek-V4-Pro-Base`, `DeepSeek-V4-Flash-Base`. Instruct models use FP4 for MoE expert weights and FP8 elsewhere; base models are FP8 throughout. Three reasoning modes (Non-think, Think High, Think Max); Think Max needs at least a 384K context window. Recommended sampling: `temperature=1.0, top_p=1.0`.
- Three reasoning-effort specialists (different context windows and length penalties) are distilled into one checkpoint per [[Controlling Reasoning Effort in LLMs]] §6.1.

## Figures

No figures were extracted for this ingest, per this batch's no-figure-download policy. The post's benchmark comparison chart, per-token FLOPs/KV-cache-vs-sequence-length plot, CSA/HCA architecture diagrams, and MRCR retrieval curve are referenced inline above but not downloaded; the underlying technical report is cited as `DeepSeek_V4.pdf`. Benchmark numbers are preserved as prose/tables above.

## Entities

- [[DeepSeek]] — releasing organization.
- [[Hugging Face]] — hosts the blog post and model weights.

## Questions & Gaps

- No official technical report link was resolved in the post beyond a bare filename (`DeepSeek_V4.pdf`); architectural details (mHC, exact CSA/HCA layer schedule beyond V4-Pro) are taken as reported without independent verification.
- The post doesn't explain how "V4-Pro-Max" (used in benchmark tables) relates to the four released Hub checkpoints (`V4-Pro`, `V4-Flash`, and their base variants); it may be an internal eval configuration (e.g., Think Max mode) rather than a distinct checkpoint.
- No comparison against DeepSeek's own V3.2 is given for the headline knowledge/reasoning benchmarks, only for FLOPs/cache efficiency.

## Related

- [[DeepSeek Sparse Attention]] — CSA's lightning-indexer top-k selection is a direct descendant of DSA from V3.2.
- [[Multi-Head Latent Attention]] — DeepSeek's prior KV-cache compression mechanism, superseded here by CSA/HCA's block compression.
- [[GLM-5.2: Built for Long-Horizon Tasks]] — GLM-5.2 is benchmarked directly against DeepSeek-V4-Pro on long-horizon coding/agentic tasks and independently pursues 1M-context efficiency via IndexShare.
- [[DeepSeek]]
- [[Long Context]]
- [[Agentic AI]]
- [[Mixture of Experts]]
- [[Controlling Reasoning Effort in LLMs]]
- [[Reasoning Effort]]
- [[On-Policy Distillation]]
