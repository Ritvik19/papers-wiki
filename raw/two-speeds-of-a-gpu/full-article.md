# Two speeds of a GPU

**Author**: Adam Mainz (@MainzOnX)  
**Date**: July 16, 2026  
**Canonical HTML**: `raw/two-speeds-of-a-gpu/full-article.html`  

## Overview
A first-principles guide to GPU performance limits, arithmetic intensity, and the Roofline Model. The article breaks down why GPUs have two distinct, independent ceilings—compute throughput (FLOP/s) and memory bandwidth (Bytes/s)—and uses a kitchen analogy (fast chef vs slow runner) and concrete mathematical derivations to explain why elementwise vector operations are deeply memory-bound while large matrix multiplications become compute-bound.

## Key Sections
1. **GPUs have two speeds**: Compute speed vs memory bandwidth speed mismatch across modern hardware generations.
2. **A chef, a runner, and a very long wait**: The kitchen analogy explaining memory-bound vs compute-bound bottlenecks.
3. **How much math can a GPU actually do?**: Definition of FLOP, multiply-accumulate conventions, H100 SXM5 BF16 peak (989 TFLOPS), RTX 4090 BF16 peak (165 TFLOPS).
4. **How fast can you feed a GPU?**: Memory bandwidth throughput (H100 3.35 TB/s HBM3, RTX 4090 1 TB/s GDDR6X) and hardware ridge ratios (~300 FLOPs/byte on H100, ~165 FLOPs/byte on 4090).
5. **Why a vector add barely uses the chip**: 1M BF16 vector add takes 1 ns compute vs 1.8 us memory on H100 (~1,800x slower), defining memory-bound workloads.
6. **When the chef finally has enough to do**: Matrix multiplication scaling ($2N^3$ FLOPs vs $6N^2$ bytes) and the 4096x4096 BF16 case (137 GFLOPs vs 96 MB, 138 us compute vs 29 us memory -> compute-bound).
7. **Same op but different shape**: Scaling $N/3$ FLOPs/byte shows $N=64$ (intensity 21) is memory-bound while $N=4096$ (intensity 1365) is compute-bound.
8. **Both roofs on one chart**: The Roofline Model, slanted memory roof, flat compute roof, and machine ridge point.
9. **Summary**: Two ceilings, one ratio.

## Figures
- `images/fig-1.jpg`: Header banner for "Two speeds of a GPU"
- `images/fig-2.jpg`: Kitchen analogy cartoon: Fast chef waiting idle for slow runner (memory-bound).
- `images/fig-3.jpg`: Kitchen analogy cartoon: Busy chef working continuously while runner fetches (compute-bound).
- `images/fig-4.jpg`: Matrix multiplication scaling diagram ($2N^3$ FLOPs vs $6N^2$ bytes).
- `images/fig-5.jpg`: The Roofline Model chart with slanted memory roof, flat compute roof, and ridge point.
