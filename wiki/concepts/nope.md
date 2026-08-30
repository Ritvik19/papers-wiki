# NoPE

**Type**: concept  
**Tags**: #concept

## Overview
No Position Encoding (NoPE); the finding and architectural design (Kazemnejad et al., 2023) showing that causal attention masking implicitly encodes position, enabling autoregressive transformers to learn positional relationships and extrapolate context length without explicit positional encodings.

## Appearances
- [[Papers Explained: No Position Encoding (NoPE)]] — foundational study.
- [[Papers Explained Review 06 - Position Encodings]] — survey.

## Notes
- Effective for causal decoder-only models; does not apply to bidirectional encoders.

## Related
- [[Positional Encoding]]
- [[ALiBi]]
- [[Long Context]]
