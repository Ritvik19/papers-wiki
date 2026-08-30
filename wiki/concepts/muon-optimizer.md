# Muon Optimizer

**Type**: concept  
**Tags**: #concept

## Overview

The Muon optimizer is a modern deep learning optimizer designed for improved training efficiency and stability compared to AdamW. It is used in the pretraining of large-scale language models and is noted for high efficiency in large MoE settings.

## Appearances

- [[Introducing Composer 2.5]] — **sharded Muon** with distributed Newton–Schulz orthogonalization per attention head and per MoE expert; async all-to-all for sharded expert matrices; 0.2s optimizer step on a 1T model; paired with dual-mesh HSDP (narrow non-expert, wide expert groups).
- [[Papers Explained: Arcee Trinity]] — used to train Trinity Large (400B/13B active), where it is described as providing "high efficiency and stability" during pretraining.
- [[Inkling]] — hybrid pretraining: Muon for large matrix weights, Adam for other parameters; weight decay coupled to LR².

## Notes

- The Trinity technical report does not include explicit ablation comparisons of Muon vs. AdamW, but its use marks the first adoption of Muon in the Arcee model family.
- Muon has also been adopted in other frontier model training efforts as an alternative to Adam-family optimizers.

## Related

- [[Introducing Composer 2.5]]
- [[Mixture of Experts]]
- [[Papers Explained: Arcee Trinity]]
- [[Inkling]]
- [[Large Language Models]]
