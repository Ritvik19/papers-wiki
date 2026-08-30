# Keep the Tokens Flowing: Lessons From 16 Open-Source RL Libraries

**Source**: `raw/async-rl-training-landscape/full-article.md` (364 KB), `raw/async-rl-training-landscape/full-article.md`
**Ingested**: 2026-07-10
**Tags**: #summary

## Summary

A Hugging Face survey of sixteen open-source asynchronous RL training libraries (AReaL, ART, Atropos, MILES, NeMo-RL, OAT, open-instruct, PipelineRL, PRIME-RL, ROLL, SkyRL, SLIME, TorchForge, Tunix, verl, verifiers-rl), conducted to inform the design of an async trainer for TRL. The motivating problem: in synchronous RL training, autoregressive generation dominates wall-clock time (a single batch of 32K-token rollouts on a 32B model can take hours) while training GPUs sit idle. Value-function-free trainers like GRPO make this worse, since they need G times more rollouts per prompt and the whole batch is gated by the slowest completion (the "straggler problem"), and agentic RL with tools/sandboxes adds highly variable rollout latencies on top. Every surveyed library independently converged on the same fix: disaggregate inference and training onto separate GPU pools connected by a rollout buffer, and sync weights asynchronously so neither side blocks the other.

The survey compares libraries across seven axes. Orchestration & concurrency: 8 of 16 libraries use Ray's distributed actor model (chosen for built-in scheduling, fault tolerance, and a zero-copy object store), while others (PRIME-RL, PipelineRL, AReaL, verifiers-rl) opt for lightweight native-Python asyncio/threading to avoid the Ray dependency; Meta's TorchForge uses a new PyTorch-native actor framework called Monarch. Rollout buffer depth ranges from none (synchronous), through double-buffering (one step of overlap), to bounded async queues and fully unbounded streams (PipelineRL's Redis-stream approach), with deeper buffers trading throughput for more staleness to manage. Weight sync protocol is the most architecturally consequential axis: transport is almost universally NCCL broadcast (with verl adding bucketing for ~20ms latency), but the interrupt model varies from PipelineRL's "never stop" per-forward-pass weight swap (a few ms gap) to per-HTTP-request abort, soft-pause draining, or full per-batch blocking used by most other libraries.

Staleness management combines three orthogonal strategies: per-sample version rejection (hard-drop stale samples), depth bounding (cap buffer capacity so staleness is architecturally limited), and importance-sampling correction (reweight stale samples by the policy ratio, optionally clipped). Production systems (PRIME-RL, AReaL, open-instruct) increasingly combine depth bounding with optional IS correction. LoRA support is the most practically consequential axis for compute-constrained teams: when the inference server is LoRA-aware, only adapter deltas need to sync (~50MB at rank 32, sub-millisecond) instead of a full NCCL broadcast of the base model; 8 of 13 relevant libraries support this adapter-only sync. Distributed training backend and parallelism determine whether a library can handle Mixture-of-Experts models at all; only Megatron-backed libraries (verl, SLIME, MILES, ROLL, NeMo-RL) and PRIME-RL's FSDP2+EP path correctly support Expert Parallelism, while ZeRO-based libraries can load MoE checkpoints but AllGather every expert on every forward pass, negating the sparsity advantage.

The post's forward-looking section flags five stress points for current architectures: critic-free algorithms (GRPO etc.) free memory but increase weight-sync pressure since they need larger group sizes for stable advantage estimates; process reward models introduce a new synchronization barrier since scoring intermediate steps is no longer cheap; multi-agent co-evolution compounds the straggler problem multiplicatively across chained agent invocations; DeepSeek-V3.2's production experience revealed that MoE expert-routing inconsistency between inference and training frameworks (different floating-point rounding leading to different expert selections) and top-p/top-k sampling-mask mismatches are structural training-inference mismatches that importance-sampling correction cannot fix, requiring new inference-server API contracts ("Keep Routing" and "Keep Sampling Mask") that no current library implements; and on-policy distillation is structurally the same async coordination problem as GRPO with the reward function swapped for a teacher forward pass. For TRL's own async trainer, the post commits to three design choices: a bounded queue with per-token `model_version` tagging (not double-buffering) for token-level staleness correction from day one, NCCL weight sync with packed/bucketed transfers (via vLLM's `NCCLWeightTransferEngine` and exploring Awex/Mooncake for cross-engine transfer), and experimental partial-rollout support (prefix-resume or abort-and-retry) for agentic workloads.

## Key Claims

- A GRPO training step with G=8 completions x 64 prompts (512 rollouts) at 32K tokens/rollout takes an estimated ~45 min on 1xH100 for a 7B model and ~3.7 hours for a 32B model; even at 8 inference GPUs, 32K-token rollouts on a 32B model still take ~28 min/step.
- 8 of 16 surveyed libraries use Ray for orchestration; the rest use native Python concurrency, pub/sub message buses, or HTTP microservices.
- PipelineRL is the only library with a "never stop" weight-sync interrupt model, swapping weights between individual token decode steps (~1-10ms gap); every other library pauses generation at a coarser boundary (per-request, per-batch drain, or full block).
- Only Megatron-backed libraries (verl, SLIME, MILES, ROLL, NeMo-RL) plus PRIME-RL's FSDP2+EP path correctly support Expert Parallelism for MoE training; ZeRO-based libraries can load MoE checkpoints but AllGather every expert per forward pass, losing the sparsity benefit.
- LoRA adapter-only weight sync (when supported) reduces a full-model NCCL broadcast (~100-500ms) to a sub-millisecond transfer at rank 32 (~50MB); 8 of 13 relevant libraries support this.
- DeepSeek-V3.2 identified two structural, IS-correction-resistant sources of training-inference mismatch in MoE RL: expert-routing inconsistency between inference and training frameworks, and truncation-mask mismatch between sampling-time (top-p/top-k) and training-time (full vocabulary) distributions.
- TRL's planned async trainer will use a bounded queue with per-token `model_version` tags (skipping double-buffering entirely), NCCL weight sync with packed/bucketed transfers, and experimental prefix-resume/abort-retry partial rollout handling.

## Figures

No figures were extracted for this ingest; the synchronous-training-timeline diagram and colocated-vs-disaggregated topology diagrams are described inline but not downloaded, per this batch's no-figure-download policy. All comparison tables (libraries surveyed, orchestration types, rollout buffer patterns, weight-sync transport/interrupt tiers, staleness-management matrix, LoRA-support matrix, training-backend/parallelism matrix, and the full 16-library overview table) are preserved as markdown in the source file.

## Entities

- [[Hugging Face]] — publishes the survey and maintains TRL, the library this survey's findings will inform.
- [[ServiceNow]] — develops PipelineRL, the outlier library with the finest-grained ("never stop") weight-sync interrupt model.
- [[DeepSeek]] — DeepSeek-V3.2's production RL training surfaced the MoE routing/sampling-mask mismatch problems discussed in the forward-looking section.

## Questions & Gaps

- The post explicitly frames itself as a snapshot ("as of March 2026"); several features/backends are flagged as rapidly evolving, and some claims (e.g. "no current library implements Keep Routing") were contested in the comments (a reader asked whether Megatron already supports router replay, without the authors giving a definitive answer in the source text).
- No quantitative benchmark is given comparing end-to-end training throughput across the 16 libraries; the comparison is architectural/qualitative rather than empirical.

## Related

- [[PipelineRL]] — ServiceNow's library, singled out in this survey for its unique never-stop weight-sync design.
- [[Putting RL Back in RLHF]] — earlier TRL post on RLOO, an example of the critic-free algorithm trend this survey discusses as increasing weight-sync pressure.
- [[GRPO]]
- [[Reinforcement Learning Topic]]
