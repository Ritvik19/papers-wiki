# Layer-Adaptive Learning Rate

**Type**: concept  
**Tags**: #concept

## Overview
A post-training optimization technique (LALR) that scales learning rates across transformer layers proportionally to their empirical contribution profile, accelerating convergence in full-parameter RLVR and SFT.

## Appearances
- [[Papers Explained: Is One Layer Enough?]] — introduced by Liu et al. (2026).

## Notes
- Assigns higher learning rates to plastic middle-to-deep layers and lower rates to early feature extraction layers.

## Related
- [[Layer-Selective Training]]
- [[Model Compression and Efficiency]]
