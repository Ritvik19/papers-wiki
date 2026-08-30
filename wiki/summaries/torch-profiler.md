# Profiling in PyTorch (Part 1): A Beginner's Guide to torch.profiler

**Source**: `raw/torch-profiler/full-article.md` (252 KB), `raw/torch-profiler/full-article.md`
**Ingested**: 2026-07-10
**Tags**: #summary

## Summary

The opening post of a three-part Hugging Face series that teaches `torch.profiler` from first principles, using a minimal `torch.add(torch.matmul(x, w), b)` example (mimicking a neuron's weight/bias interaction) and a question-led structure: open a trace, ask why something looks the way it does, and chase the answer. The profiler exports two artifacts: a table (a statistical summary answering "what is taking the most time," with "Self" columns excluding child events and "total" columns including them) and a trace (a temporal view answering "when and why," with separate CPU and GPU lanes plus visible idle gaps).

Running the example at size 64 shows the classic overhead-bound symptom: self CPU time (2.314ms) dwarfs self CUDA time (23.104us), meaning the GPU is idle while the CPU spends its time preparing and launching kernels rather than computing. Scaling to size 4096 flips this: self CUDA time (4.495ms) becomes comparable to self CPU time (4.908ms), moving the workload into the compute-bound regime. Reading the 64x64 trace in Perfetto surfaces several "why" questions the post walks through: a ~228us dead window between entering `record_function` and the actual `aten::matmul` dispatch (cuBLAS heuristics, workspace allocation, lazy module loading, fixed by adding warmup iterations); a ~2.5ms CPU-GPU lane offset traced to the profiler's own "Activity Buffer Request" (confirmed by running 20 iterations and seeing the gap appear only once); an extra `cudaOccupancyMaxActiveBlocksPerMultiprocessor` CUDA runtime call before matmul but not before add, because matmul's dynamic register/shared-memory footprint requires cuBLAS to query hardware occupancy while add's fixed, resource-light footprint needs no such query; and a large `cudaDeviceSynchronize` (~1.78ms) that the profiler emits to flush events at the end of the active window, covering only 26us of real GPU work, a textbook overhead-bound symptom rather than a real cost.

At size 4096, the post shows that identical kernels running on identical data still time differently across iterations (GPU clock boost/idle states, thermals, power management, driver housekeeping), warning readers that reading only the mean average can produce a misleading mental model. The `torch.compile` section shows that Inductor rewrites `torch.add(torch.matmul(x, w), b)` into a single `aten::addmm` dispatcher-level call, but this is not a new fused CUDA kernel: the GPU still runs the same cuBLAS GEMM kernel eager mode used. Counter to the intuitive expectation that compile would halve CUDA launches, the compiled trace actually reveals two kernels per step (a Device-to-Device memcpy plus the GEMM), because `addmm` computes `out = a.A.B + b.C` and cuBLAS's GEMM-with-bias-add epilogue needs the destination buffer pre-seeded with the bias; a truly fused kernel (as FlashAttention-style hand-written kernels or Triton codegen can produce) would skip that memcpy. CPU overhead also goes up (not down) under `torch.compile` for this tiny op, roughly 2x, since every call walks the full Dynamo -> AOTAutograd -> Inductor stack on top of the same `aten::addmm` dispatch; that tax only amortizes over models with many operators. The post closes with a "trace reading cheatsheet" (profiler table patterns, CPU lane patterns, GPU lane patterns, dispatch chain patterns, and `torch.compile` patterns) meant as a standing reference for readers' own traces.

## Key Claims

- At matrix size 64: self CPU time 2.314ms vs self CUDA time 23.104us, an overhead-bound regime where the GPU is under 1% utilized relative to CPU dispatch time.
- At matrix size 4096: self CPU time 4.908ms vs self CUDA time 4.495ms, a compute-bound regime.
- A ~228us "dead window" between `record_function` entry and actual kernel dispatch is cold-start overhead (cuBLAS heuristics, workspace allocation, lazy loading), fixed by adding warmup iterations.
- `cudaOccupancyMaxActiveBlocksPerMultiprocessor` appears before matmul (dynamic, hardware-dependent resource footprint needing an occupancy query) but not before add (fixed, resource-light footprint).
- `torch.compile` fuses `add(matmul(x,w),b)` into a single `aten::addmm` dispatcher call, but the underlying GPU kernel is unchanged (same cuBLAS GEMM); the compiled trace still shows two GPU kernels per step (a DtoD memcpy plus the GEMM) because the bias-add epilogue needs its destination buffer pre-seeded.
- `torch.compile` roughly doubles CPU-side overhead per step for this tiny two-op example (Dynamo/AOTAutograd/Inductor stack tax), which only amortizes over larger multi-op models.
- Kernel runtimes vary run-to-run even for identical code/data/hardware, due to GPU clock boost states, thermals, and driver housekeeping.

## Figures

No figures were extracted for this ingest; the many Perfetto trace screenshots (profiler tables, CPU/GPU lane views, kernel footprint panels) referenced throughout are described inline but not downloaded, per this batch's no-figure-download policy. All comparison tables (occupancy timing, eager-vs-compile step durations, the full trace-reading cheatsheet) are preserved as markdown in the source file.

## Entities

- [[Hugging Face]] — publishes the post and the profiling-pytorch example scripts/dataset.

## Questions & Gaps

- The post explicitly leaves "how to reduce torch.compile's CPU overhead via the `mode` argument" as a reader exercise rather than answering it directly.
- No guidance is given yet on profiling multi-kernel fused attention or full transformer blocks; that is deferred to Parts 2 and 3 of the series.

## Related

- [[Profiling in PyTorch (Part 2): From nn.Linear to a Fused MLP]] — next post in the series, climbing from this matmul-add example to a full MLP block.
- [[Profiling in PyTorch (Part 3): Attention Is All You Profile]] — final post in the series, applying the same reading skills to SDPA attention backends.
- [[What Even Is a Kernel?]] — complementary explainer on GPU kernel dispatches, eager round-trips, and `torch.compile` fusion.
- [[Two Speeds of a GPU]] — foundational breakdown of arithmetic intensity and roofline bounds explaining matmul vs add behavior.
- [[GPU Kernel]]
- [[Torch Compile]]
- [[Kernel Fusion]]
