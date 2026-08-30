# Synchronized Batch Normalization

**Type**: concept  
**Tags**: #concept

## Overview

Synchronized batch normalization (SyncBN; Zhang et al., 2018) computes [[Batch Normalization]] statistics across **all GPUs/workers** in distributed training rather than per-device. Global mean and variance match what a single process would see with the full minibatch, fixing inaccurate BN estimates when per-GPU batch slices are too small.

## Appearances

- [[In-layer Normalization Techniques for Training Very Deep Neural Networks]] — natural evolution of BN for multi-worker setups; statistics communicated via all-reduce.

## Notes

Essential for semantic segmentation and other tasks where memory limits per-GPU batch size. Implementation computes partial sums of x and x² per device, then reduces globally before normalizing.

## Related

- [[Batch Normalization]]
- [[Group Normalization]]
