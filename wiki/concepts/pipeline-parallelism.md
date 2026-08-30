# Pipeline Parallelism

**Type**: concept  
**Tags**: #concept

## Overview

Pipeline Parallelism (PP) is an advanced vertical model-parallel paradigm designed to reduce the compute-idle "bubbles" of naive model parallelism. PP partitions a neural network vertically into sequential stages across multiple devices, and splits each training mini-batch into smaller units called **microbatches**. By pipelining these microbatches sequentially through the vertical stages, multiple devices can compute forward and backward passes simultaneously, significantly improving hardware utilization.

## Appearances

- [[How to Train Really Large Models on Many GPUs?]] — *How to Train Really Large Models on Many GPUs?* (Sep 25, 2021): Synthesizes pipeline-parallel paradigms, microbatch schedules, bubble fraction derivations, and parameter synchronization models.

## Notes

*   **GPipe (Synchronous Pipelining)**:
    Developed by Google (Huang et al. 2019), **GPipe** aggregates and applies gradients synchronously at the end of each mini-batch, guaranteeing learning consistency identical to standard training. In GPipe, a mini-batch is split into $m$ microbatches and pipelined across $d$ devices.
    Assuming the forward and backward passes of a single microbatch each take one unit of time, the idle **bubble fraction** is mathematically formulated as:
    $$\text{Bubble Fraction} = 1 - \frac{2md}{(2m + 2(d-1))d} = \frac{d-1}{m+d-1}$$
    As the number of microbatches $m$ increases relative to the pipeline depth $d$ ($m \gg d$), the bubble fraction asymptotically approaches zero. Empirically, the bubble overhead is negligible when $m > 4d$ (especially when combined with [[Activation Recomputation]]).
    
    See [[How to Train Really Large Models on Many GPUs?]] fig-3 for the GPipe microbatch scheduling timeline.
    
*   **GPipe Memory Cost**:
    GPipe's synchronous approach requires storing all $m$ microbatch activations simultaneously (to feed the backward pass), making memory usage proportional to:
    $$\text{Memory}_{\text{GPipe}} = O(m \times \text{activation size per layer})$$
    This is why GPipe is almost always deployed with [[Activation Recomputation]], which drops intermediate activations and recomputes them on the fly during the backward pass.

*   **PipeDream (Asynchronous Pipelining & 1F1B)**:
    Unlike GPipe's end-of-batch global barrier, **PipeDream** (Narayanan et al. 2019) adopts an asynchronous **1F1B (One Forward, One Backward)** scheduling pattern. Once the pipeline is filled, each worker alternates between executing a single forward microbatch and a single backward microbatch.
    Because workers compute asynchronously, an unmodified 1F1B schedule would cause learning instability since the forward pass and backward pass of the same microbatch could execute using different parameter versions (due to intermediate step updates). PipeDream solves this via:
    -   **Weight Stashing**: Each worker maintains multiple stashed versions of its model weights, ensuring that the exact same parameter version used during the forward pass of a microbatch is re-applied during its backward pass.
    -   **Vertical Synchronization (Asynchronous)**: Model weight version metadata flows along with activations and gradients between stages to keep version alignment.
    
    See [[How to Train Really Large Models on Many GPUs?]] fig-4 for the PipeDream 1F1B scheduling timeline, and fig-5 for VGG16 speedup comparisons across BSP, ASP, and PipeDream.

*   **Pipeline Memory Reductions**:
    To minimize the excessive GPU memory footprint of storing stashed parameter versions under PipeDream, two variations were developed:
    -   **PipeDream-Flush**: Re-introduces a periodic pipeline flush (similar to GPipe) to discard stashed weights and perform a global update. This sacrifices a small amount of throughput to maintain only a single version of model weights in memory. See [[How to Train Really Large Models on Many GPUs?]] fig-6.
    -   **PipeDream-2BW (Double-Buffered Weights)**: Limits the stashed parameter footprint to exactly two weight versions. It generates a new model version every $k$ microbatches ($k > d$), retaining the old version only for active, in-flight backward passes before discarding it. See [[How to Train Really Large Models on Many GPUs?]] fig-7.

*   **Interleaved 1F1B (PTD-P, Narayanan et al. 2021)**:
    Narayanan et al. (2021) further improved the pipeline schedule by assigning each device **multiple non-contiguous model chunks** rather than one contiguous stage. If there are $v$ model chunks per device, the bubble fraction is reduced by a factor of $v$:
    $$\text{Bubble Fraction}_{\text{interleaved}} = \frac{1}{v} \cdot \frac{d-1}{m+d-1}$$
    For example, with $v=4$ chunks and $d=8$ stages, the bubble overhead is reduced to just $\frac{7}{4(m+7)}$ — roughly 4× less idle time than vanilla 1F1B. The trade-off is that each device must perform an additional `AllReduce` per model chunk boundary, increasing communication volume by $v\times$.
    
    See [[How to Train Really Large Models on Many GPUs?]] fig-9 for the PTD-P interleaved pipeline schedule.

*   **Summary Comparison**:

    | Strategy | Update | Bubble Fraction | Memory | Weight Versions |
    |---|---|---|---|---|
    | Naive MP | Sync | $(d-1)/1$ | Low | 1 |
    | GPipe | Sync | $(d-1)/(m+d-1)$ | High (all microbatch activations) | 1 |
    | PipeDream | Async | Low (1F1B) | High (weight stashing) | $d$ |
    | PipeDream-Flush | Sync-ish | $(d-1)/(m+d-1)$ | Medium | 1 |
    | PipeDream-2BW | Near-sync | Low | Low | 2 |
    | PTD-P Interleaved | Sync | $\frac{1}{v}\cdot\frac{d-1}{m+d-1}$ | Moderate | 1 |

## Related

- [[Model Parallelism]]
- [[Tensor Parallelism]]
- [[GPipe]]
- [[Megatron-LM]]
- [[Activation Recomputation]]
- [[How to Train Really Large Models on Many GPUs?]]
