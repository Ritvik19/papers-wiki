# Profiling in PyTorch (Part 2): From nn.Linear to a Fused MLP

**Source**: `raw/torch-mlp-fusion/full-article.html` (256 KB), `raw/torch-mlp-fusion/full-article.md`
**Ingested**: 2026-07-10
**Tags**: #summary

## Summary

The second post in Hugging Face's Profiling in PyTorch series, moving from the raw matmul-add example in [[Profiling in PyTorch (Part 1): A Beginner's Guide to torch.profiler]] up to `nn.Linear` and then a three-layer GeGLU MLP block. Profiling a single `nn.Linear(bias=True)` shows an `aten::t` (transpose) op preceding `aten::addmm`, but `aten::t` never launches a GPU kernel: it only rewrites tensor metadata (shape and stride) to produce a transposed view of the weight, with the underlying buffer untouched. There is also no separate `aten::add` for the bias, since `nn.Linear` dispatches straight to `aten::addmm`, which folds the bias-add into the GEMM kernel's writeback as an epilogue (a small computation a GEMM does just before writing its result to HBM, avoiding a second memory round-trip). Because eager `nn.Linear` already uses the fused `addmm` kernel, `torch.compile` has essentially nothing left to fuse for a single Linear: comparing eager and compiled traces shows the identical cuBLAS GEMM kernel and identical `aten::addmm` op, with compile only removing a few CPU-side dispatch rows (the `aten::t` view bookkeeping) by tracing through the view chain once at compile time and hard-coding the resulting strides. The GPU kernel name itself encodes which memory layout it expects (a `tn` suffix meaning transposed/non-transposed inputs), which is how the GEMM "knows" to read the weight in transposed order without a physical transpose kernel ever running.

Stacking three Linears into a GeGLU MLP (`down_proj(gelu(gate_proj(x)) * up_proj(x))`) produces exactly 5 GPU kernels per forward as predicted: three GEMMs (two of them, gate and up, sharing an identical `128x128` tile shape and CUDA time; down_proj gets a different `128x256` tile with a deeper pipeline stage and runs about 10% faster despite having the same FLOP count, since cuBLAS picks a different tile for the different output shape) plus separate pointwise GeLU and multiply kernels. The pointwise ops skip the `cudaOccupancyMaxActiveBlocksPerMultiprocessor` occupancy query that GEMMs need, since their resource footprint is fixed rather than shape-dependent. Compiling the MLP collapses the entire dispatcher chain (`aten::linear` -> `aten::t` -> `aten::transpose` -> `aten::matmul` -> `aten::reshape` -> `aten::mm`) down to three bare `aten::mm` calls with byte-for-byte identical GEMM kernel names to eager, and more importantly fuses the GeLU, multiply, and an intervening reshape into a single Triton kernel (`triton_poi_fused__unsafe_view_gelu_mul_0`). This fusion is the actual win of compiling an MLP: in eager mode the ~50MB intermediate `gelu(gate)` tensor makes a full round-trip through HBM (written by GeLU, read back by multiply); the fused Triton kernel reads gate and up once, computes `gelu(gate) * up` in registers, and writes the result once.

Swapping in a hand-tuned kernel (`LigerGEGLUMLP` from the `kernels-community/liger-kernels` Hub package, fetched via the `kernels` library which downloads pre-built, version-pinned binaries rather than requiring local compilation) achieves the same fusion (a single Triton kernel computing `gelu(gate) * up`) without any `torch.compile` overhead: no Dynamo cache-lookup guards, no compile latency, no recompilation risk. The raw numbers show the Liger kernel (92.8us) is technically slightly slower than Inductor's compiled kernel (89.4us), but the comparison is not apples-to-apples: Inductor's kernel is specialized for one exact input shape and must retrace and recompile if the shape changes, while Liger's kernel uses one set of launch parameters that works for any shape with zero recompilation cost. The real trade-off is a fast generic kernel versus a kernel specialized for one particular input shape, not "slow human kernel vs. fast compiled kernel."

## Key Claims

- `aten::t` (transpose) inside `nn.Linear` never launches a GPU kernel; it only rewrites shape/stride metadata to produce a view, with zero CUDA time in the profiler table.
- `nn.Linear`'s bias-add is folded into the GEMM kernel's writeback as an epilogue via `aten::addmm`, so eager mode already uses one fused kernel with no separate add operation.
- `torch.compile` has nothing to fuse for a single Linear (identical cuBLAS kernel, identical `addmm` op); it only removes CPU-side view-dispatch overhead by hard-coding strides at compile time.
- A 3-linear GeGLU MLP launches exactly 5 GPU kernels in eager mode: 3 GEMMs (gate/up share a `128x128` tile, down_proj gets a `128x256` tile and runs ~10% faster on identical FLOPs) plus separate GeLU and multiply kernels.
- Compiling the MLP fuses GeLU, multiply, and a reshape into one Triton kernel (`triton_poi_fused__unsafe_view_gelu_mul_0`), eliminating a ~50MB HBM round-trip for the intermediate tensor; the three GEMMs remain byte-for-byte identical to eager.
- The hand-tuned `LigerGEGLUMLP` kernel (via the Hugging Face `kernels` library) achieves the same fusion as compile (92.8us vs. compile's 89.4us) but with zero Dynamo/guard/recompilation overhead, trading a few microseconds of shape-specific speed for shape-agnostic robustness.

## Figures

No figures were extracted for this ingest; the Perfetto trace screenshots for eager/compiled/Liger dispatch chains are described inline but not downloaded, per this batch's no-figure-download policy. The GEMM tile-shape comparison table and the final "what changed / what stayed the same" summary table are preserved as markdown in the source file.

## Entities

- [[Hugging Face]] — publishes the post and maintains the `kernels` library used to fetch the Liger MLP kernel.

## Questions & Gaps

- The post does not test whether `torch.compile`'s recompilation actually triggers (vs. an error) when input strides violate compile-time assumptions; a reader comment raises this and it is left unresolved in the source text.
- No benchmark is given for the Liger kernel's robustness across a wider range of shapes beyond the one tested configuration.

## Related

- [[Profiling in PyTorch (Part 1): A Beginner's Guide to torch.profiler]] — prior post establishing the profiler-reading fundamentals this post builds on.
- [[Profiling in PyTorch (Part 3): Attention Is All You Profile]] — next post, applying the same approach to SDPA attention backends.
- [[Kernel Fusion]] — concept page on operator fusion mechanics.
- [[Torch Compile]] — concept page on automated graph compilation in PyTorch.
- [[What Even Is a Kernel?]] — explainer on intermediate memory traffic and fusion benefits.
