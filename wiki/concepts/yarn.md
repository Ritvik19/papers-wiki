# YaRN

**Type**: concept  
**Tags**: #concept

## Overview
Yet another RoPE extensioN method (Peng et al., 2023); a context window extension technique combining NTK-by-parts frequency interpolation with attention temperature scaling to extend RoPE context windows to 128k+ tokens with negligible fine-tuning compute.

## Appearances
- [[Papers Explained: Yet another RoPE extensioN method (YaRN)]] — foundational paper.
- [[Papers Explained Review 06 - Position Encodings]] — survey.

## Notes
- Splits RoPE dimensions into non-interpolated high-frequency, interpolated low-frequency, and ramped mid-frequency bands.

## Related
- [[RoPE]]
- [[Long Context]]
- [[Positional Encoding]]
