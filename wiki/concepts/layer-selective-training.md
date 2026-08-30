# Layer-Selective Training

**Type**: concept  
**Tags**: #concept

## Overview
A compute- and memory-efficient fine-tuning method (LST) where low-contribution early transformer layers are frozen during post-training, reducing backward-pass memory and compute by ~50% with negligible loss in reasoning performance.

## Appearances
- [[Papers Explained: Is One Layer Enough?]] — systematic study.

## Notes
- Recovers 90%+ of full-parameter gains by training only high-impact middle-to-deep layers.

## Related
- [[Layer-Adaptive Learning Rate]]
- [[Model Compression and Efficiency]]
