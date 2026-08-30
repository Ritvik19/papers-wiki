# Tricks From OpenAI gpt-oss You Can Use With Transformers

**Source**: `raw/faster-transformers/full-article.html` (256 KB), `raw/faster-transformers/full-article.md`
**Ingested**: 2026-07-10
**Tags**: #summary

## Summary

A Hugging Face engineering post cataloging the transformers-library upgrades built to ship OpenAI's gpt-oss models on day one, framed as general-purpose features that benefit any current or future model in the library rather than one-off gpt-oss-specific hacks. The centerpiece is the `kernels` package: rather than bundling every community-optimized kernel (Flash Attention, Liger RMSNorm, Megablocks MoE) as a compiled dependency (which would mean dependency bloat and system-specific build requirements), `kernels` downloads pre-built, version-pinned binaries from the Hub on first use, matched to the caller's system. gpt-oss uses this for `LigerRMSNorm`, `MegaBlocksMoeMLP` (both opt-in via `use_kernels=True`, incompatible with mxfp4 so they force bfloat16), and Flash Attention 3 with attention-sink support (set via `attn_implementation="kernels-community/vllm-flash-attn3"`, Hopper-only).

MXFP4 quantization is covered as gpt-oss's headline memory trick: a 4-bit E2M1 float format (1 sign, 2 exponent, 1 mantissa bit) that compensates for its coarseness with blockwise scaling (32-element blocks, each with a shared scale restoring dynamic range). This is the difference between gpt-oss-20B fitting in ~16GB VRAM and gpt-oss-120B in ~80GB versus not being loadable at all on a single GPU. `transformers` natively detects `'quant_method': 'mxfp4'` in a model's config and dispatches automatically to Hub-fetched Triton MXFP4 kernels (no `use_kernels=True` needed, unlike the RMSNorm/MoE kernels); if requirements aren't met (`triton>=3.4`, NVIDIA compute capability >= 7.5), it falls back to a bfloat16 path needing roughly 4x the memory. The post also covers Tensor Parallelism (`tp_plan="auto"` in `from_pretrained`, splitting tensors inside a layer across GPUs via all-gather/all-reduce, best on single-node fast interconnects) and Expert Parallelism (sharding MoE experts across ranks via `DistributedConfig(enable_expert_parallel=True)`, which also activates TP automatically), both implemented directly in `transformers` rather than requiring a separate serving framework.

Two further infrastructure pieces round out the release. A new `DynamicSlidingWindowLayer` and config-aware `DynamicCache` stop KV cache growth past the attention window for sliding-window layers (rather than growing indefinitely with sequence length regardless of layer type); for gpt-oss, which alternates sliding and global attention layers, this roughly halves total KV cache memory as sequence length grows, with no code changes required since it is the default behavior. And `transformers` gained a "pre-stock the pantry" model-loading optimization (via a PR referenced as #36380): rather than requesting GPU memory once per layer during loading (thousands of tiny allocations for multi-billion-parameter models), it inspects the `device_map` up front and pre-allocates one large block per GPU, so layer weights simply slot into pre-reserved space as they're copied in, speeding up loading for any model using `device_map="auto"` or `tp_plan="auto"`. The post also covers `transformers`' native continuous-batching API (`generate_batch`), positioned as useful for evaluation/experimentation rather than production serving (where vLLM/SGLang remain the recommended choice), benchmarked as faster than static batching on a 100-sample test.

## Key Claims

- MXFP4: 4-bit E2M1 format with 32-element blockwise scaling; enables gpt-oss-20B in ~16GB VRAM and gpt-oss-120B in ~80GB, versus ~4x more memory on the bfloat16 fallback path.
- gpt-oss custom kernels (via the `kernels` Hub package): Liger RMSNorm, Megablocks MoE, and Flash Attention 3 with attention sinks (Hopper-only); RMSNorm/MoE kernels benefit larger batch sizes most and are incompatible with mxfp4 (force bfloat16).
- Tensor Parallelism and Expert Parallelism are both implemented directly in `transformers`' `from_pretrained` (`tp_plan="auto"`, `DistributedConfig(enable_expert_parallel=True)`); enabling EP also activates TP.
- `DynamicSlidingWindowLayer` + config-aware `DynamicCache` halts KV cache growth past the sliding-window size for sliding layers; for gpt-oss's alternating sliding/global layers this roughly halves total KV cache memory at longer sequence lengths, on by default with no code changes.
- A model-loading optimization (PR #36380) pre-allocates one large GPU memory block per device from the `device_map` up front, instead of many small per-layer allocations, speeding up loading for `device_map="auto"` and `tp_plan="auto"` setups.
- `transformers`' native `generate_batch` continuous-batching API is positioned for evaluation/experimentation, not production serving, and benchmarked faster than static batching on a 100-sample test.

## Figures

No figures were extracted for this ingest; the kernel benchmark charts (with/without custom kernels, MXFP4 kernel benchmark, quantized-vs-dequantized memory, sliding-window cache memory, continuous-vs-static-batching throughput) are described inline but not downloaded, per this batch's no-figure-download policy.

## Entities

- [[Hugging Face]] — publishes the post and builds the `transformers` upgrades described.
- [[OpenAI]] — releases the gpt-oss model family that motivated these `transformers` upgrades.

## Questions & Gaps

- The post frames itself as "a one-time snapshot of a process we repeatedly iterate on," so several features (linear-attention support in the vLLM-style fused backend, a promised deep-dive on the fusion internals) are explicitly flagged as ongoing/future work rather than finished here.
- No head-to-head benchmark is given between `transformers`' native continuous batching and production serving frameworks (vLLM/SGLang) beyond the static-batching comparison.

## Related

- [[Native-Speed vLLM Transformers Modeling Backend]] — later post showing the `transformers` modeling backend reaching native vLLM inference speed via `torch.fx`-based layer fusion, a direct continuation of the kernels/parallelism themes here.
- [[Prefill and Decode for Concurrent Requests - Optimizing LLM Performance]] — related deep dive on continuous batching and chunked prefill from TNG's production serving experience.
- [[Papers Explained 428 - gpt-oss]]
- [[Mixture of Experts]]
