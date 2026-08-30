# Activation Recomputation

**Type**: concept  
**Tags**: #concept

## Overview

Activation Recomputation (also known as **Activation Checkpointing** or **Gradient Checkpointing**) is a memory-saving technique that trade-offs computation time to reduce the GPU memory footprint of intermediate activation tensors. During standard backpropagation, a model must store all intermediate layer activation tensors in memory from the forward pass until they are needed to compute gradients in the backward pass. Activation Recomputation eliminates this excessive $O(\ell)$ memory scaling (for a network of $\ell$ layers) by saving only a sparse subset of activations at partition boundaries (checkpoints) and recomputing intermediate activations on the fly during the backward pass.

## Appearances

- [[How to Train Really Large Models on Many GPUs?]] — *How to Train Really Large Models on Many GPUs?* (Sep 25, 2021): Details the sublinear memory cost derivation, partition optimizations, and memory-saving trade-offs.

## Notes

*   **Sublinear $O(\sqrt{\ell})$ Memory Cost Derivation**:
    Originally formulated by Chen et al. (2016), Activation Recomputation reduces the activation memory footprint to a sublinear cost. 
    Let an $\ell$-layer network be divided into $d$ equal partitions:
    1.  During the forward pass, only the activation tensors at the boundaries of these $d$ partitions are stored in memory. The memory cost of storing these "checkpoint" activations is $O(d)$.
    2.  Intermediate activations *within* each partition are discarded.
    3.  During the backward pass, when backpropagation reaches partition $i$ (which contains $\ell/d$ layers), the worker starts from the stashed boundary activation of partition $i-1$ and performs a local forward pass across the partition's $\ell/d$ layers to re-generate the intermediate activations.
    4.  These temporary intermediate activations are used to compute the partition's gradients and are then immediately discarded.
    
    The total memory cost $M(\ell)$ of this scheme is:
    $$M(\ell) = \max_{i=1,\dots,d} \text{cost-of-one-partition}(i) + \text{cost-of-storing-checkpoints} = O\left(\frac{\ell}{d}\right) + O(d)$$
    Applying calculus to find the optimal partition size that minimizes memory, we set the derivative with respect to $d$ to zero:
    $$\frac{d}{d(d)} \left(\frac{\ell}{d} + d\right) = 0 \implies -\frac{\ell}{d^2} + 1 = 0 \implies d = \sqrt{\ell}$$
    Substituting $d = \sqrt{\ell}$ back into the equation, the minimum memory cost scales at:
    $$M(\ell) = O(\sqrt{\ell})$$
*   **Compute-Memory Trade-off**:
    Activation Recomputation represents a classic trade-off: it saves massive amounts of GPU memory at the cost of performing **one additional forward pass** per mini-batch (approximately a $33\%$ computational overhead). However, at extreme scale, this memory saving is what enables fitting significantly larger models or larger batch sizes on existing hardware, yielding net training throughput gains.
*   **Partitioned Activation Recomputation (ZeRO-R)**:
    Advanced systems like **ZeRO-R** (Rajbhandari et al. 2019) optimize this further by sharding the boundary activations across data-parallel processes. Rather than duplicating stashed checkpoint activations on every GPU, they are sharded and gathered on the fly via `AllGather` communication right before the local forward recomputation pass, eliminating activation redundancy.

*   **Selective Recomputation**:
    Full recomputation (recomputing every intermediate activation) can be expensive. A refinement called **Selective Recomputation** only recomputes activations that are cheap to compute but expensive to store — such as attention softmax outputs and dropout masks — while retaining activations for computationally expensive operations like large GEMMs. This reduces the recomputation overhead from ~33% to closer to ~5–10% while still achieving significant memory savings.

*   **Activation Memory in Transformer Models**:
    For a transformer layer with hidden size $h$, sequence length $s$, and batch size $b$, the activation memory per layer (without recomputation) is approximately:
    $$M_\text{act} \approx 10 \times b \times s \times h \text{ bytes (in FP16)}$$
    For a 175B GPT-3 model ($h=12288$, 96 layers, $s=2048$, batch 1), this amounts to approximately 3 TB of activation memory per training step — far exceeding GPU memory capacity without recomputation.

*   **Integration with Pipeline Parallelism**:
    In [[Pipeline Parallelism]] (GPipe), each microbatch stage must store its intermediate activations until the corresponding backward microbatch reaches that stage. Activation Recomputation is therefore almost always used alongside GPipe to cap the per-stage memory cost. Without it, GPipe's memory usage scales as $O(m 	imes \text{activations per layer})$ where $m$ is the number of microbatches, which quickly becomes prohibitive.

    See [[How to Train Really Large Models on Many GPUs?]] fig-15 for a comparison of activation sharing, in-place operations, and recomputation memory profiles.

## Related

- [[Pipeline Parallelism]]
- [[ZeRO]]
- [[Mixed Precision Training]]
- [[How to Train Really Large Models on Many GPUs?]]
