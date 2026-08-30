# Mellum

**Type**: tool  
**Tags**: #entity

## Overview

**Mellum** is JetBrains' open-weight code model family. **Mellum** (4B dense) targets low-latency multi-line IDE completion; **Mellum 2** (12B MoE, 2.5B active) extends to agentic coding, tool use, and reasoning.

## Appearances

- [[Papers Explained 582: Mellum]] — 4B from-scratch FIM completion on 4T tokens.
- [[Papers Explained 583: Mellum 2]] — 12B MoE successor with SFT + multi-domain RLVR.

## Notes

Models released on Hugging Face under JetBrains collections. Mellum 4B optimizes for &lt;500 ms completion latency; Mellum 2 trades latency for agentic capability.

## Related

- [[JetBrains]]
- [[Code Models]]
- [[Mixture of Experts]]
