# Profiling in PyTorch (Part 3): Attention Is All You Profile

**Source**: `raw/torch-attention-profile/full-article.md` (200 KB), `raw/torch-attention-profile/full-article.md`
**Ingested**: 2026-07-10
**Tags**: #summary

## Summary

The closing post of Hugging Face's Profiling in PyTorch series applies the reading skills built in [[Profiling in PyTorch (Part 1): A Beginner's Guide to torch.profiler]] and [[Profiling in PyTorch (Part 2): From nn.Linear to a Fused MLP]] to attention. A hand-written causal attention module (matmul, scale, `masked_fill`, softmax, matmul) reveals an unexpected sixth GPU kernel, a memory copy, traced to `masked_fill`'s out-of-place semantics (it allocates a new tensor rather than modifying in place). Switching to the in-place `masked_fill_` removes that Memcpy kernel entirely, a one-line change that saves both time and memory (safe here because the example runs under `torch.no_grad`, since autograd normally needs the original forward-pass values for backward-pass gradient formulas, which in-place ops would corrupt).

The centerpiece of the post is profiling `F.scaled_dot_product_attention` (SDPA) across its four selectable backends, and the results invert the naive expectation that a single high-level call should be simpler and faster than hand-written code. The math backend (SDPA's dtype-safe, NaN-safe reference implementation) is 3.7x slower than the naive in-place version and launches 20 GPU kernels instead of 5, for three compounding reasons: it upcasts to FP32 and runs on ordinary CUDA cores instead of the Tensor Cores the naive bf16 version used (visible directly in the kernel name, `sgemm` for FP32/CUDA-core versus `s16816` for bf16 Tensor-Core); it materializes a fresh causal mask from scratch on every single call (`aten::ones` -> `aten::tril` -> `aten::where`) rather than reusing a precomputed one; and it calls `aten::_safe_softmax` instead of plain softmax, adding extra kernels to guard against `NaN` outputs on fully-masked rows. The efficient backend (PyTorch's upstreamed version of Meta's xformers memory-efficient attention) and the flash backend (FlashAttention-2, vendored into PyTorch) each collapse the entire pipeline into a single fused kernel (`fmha_cutlassF_...` and `pytorch_flash` respectively) that stays in bf16 on Tensor Cores and never materializes the full `[seq, seq]` score matrix in HBM, instead tiling over K/V with an online-softmax trick and accumulating output incrementally, which is the core idea behind FlashAttention's speed.

A counterintuitive finding: the flash kernel reports only ~13% occupancy in the profiler despite being the fastest backend, because it deliberately uses a large number of per-thread registers and shared memory per block (enough that only 2 of a possible many blocks fit per Streaming Multiprocessor), trading occupancy (how many warps can be resident, which helps hide latency) for on-chip data reuse (keeping attention tiles resident and avoiding HBM traffic). High occupancy and fast execution are not the same thing. The cuDNN backend also fuses into one kernel, but the kernel itself is generated and tuned per-problem by cuDNN's own compiler at runtime (visible in its verbose `cudnn_generated_..._knob_6_128x64x64_...` name) rather than being a fixed, pre-compiled binary like flash or efficient; this lets it skip the metadata transposes flash and efficient each insert (4 apiece), and it launches through the driver-level `cuLaunchKernelEx` rather than the runtime API's `cudaLaunchKernel` (which is also why the profiler reports 0% occupancy for it, a CUPTI measurement gap rather than a real stall). The trade-off shows up on the CPU side: despite having zero transpose ops, cuDNN spends the most CPU time per forward of the three fused backends (214us vs. flash's 138us and efficient's 117us), because its runtime engine has to select and prepare a tuned "knob" configuration on every call; work that disappears from the visible ATen op list doesn't disappear, it just moves somewhere the profiler shows as one opaque bar.

## Key Claims

- SDPA math backend: 20 GPU kernels per forward vs. 5 for naive in-place attention, and 3.7x slower (7.239ms vs 1.955ms CUDA time avg per forward).
- Math backend's slowness stems from three compounding factors: FP32 upcast running on CUDA cores instead of Tensor Cores, rebuilding the causal mask from scratch every call, and `_safe_softmax`'s extra NaN-guarding kernels.
- Efficient (xformers-derived) and flash (FlashAttention-2) backends each collapse attention into one fused kernel that never materializes the full `[seq,seq]` score matrix in HBM.
- The flash kernel achieves only ~13% profiler-reported occupancy despite being the fastest backend, because it deliberately maximizes per-thread register and shared-memory usage per block to keep data on-chip, trading occupancy for reduced HBM traffic.
- cuDNN generates a per-problem-tuned kernel at runtime (no fixed binary) and skips transpose ops other backends need, but spends more CPU time per forward (214us) than flash (138us) or efficient (117us) due to its runtime "knob" selection process; its 0% reported occupancy is a profiler measurement gap (driver-level launch), not a real stall.
- Removing a single out-of-place `masked_fill` (replacing with `masked_fill_`) eliminates an extra Memcpy kernel from naive attention with no downside under `torch.no_grad`.

## Figures

No figures were extracted for this ingest; the CPU/GPU lane traces for each backend and kernel-footprint/occupancy panels are described inline but not downloaded, per this batch's no-figure-download policy. The final "everything we covered, at a glance" comparison table across all six attention variants is preserved as markdown in the source file.

## Entities

- [[Hugging Face]] — publishes the post and the profiling-pytorch example scripts.

## Questions & Gaps

- The post explicitly scopes itself to showing how each optimization looks under the profiler rather than exhaustively covering every attention optimization technique that exists.
- No guidance is given on choosing between flash, efficient, and cuDNN backends for a specific production shape beyond the general note that cuDNN "often wins on other shapes" without further benchmarks in this post.

## Related

- [[Profiling in PyTorch (Part 1): A Beginner's Guide to torch.profiler]] — first post in the series, establishing the profiler-reading fundamentals.
- [[Profiling in PyTorch (Part 2): From nn.Linear to a Fused MLP]] — second post, applying those fundamentals to Linear layers and an MLP block.
