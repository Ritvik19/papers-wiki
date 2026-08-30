# Unsloth Gradient Checkpointing

**Type**: concept  
**Tags**: #concept

## Overview

Unsloth's async gradient checkpointing overlaps activation recompute with the backward pass during long-context training, reducing step time ~30% at 32K+ sequence lengths versus synchronous checkpointing.

## Appearances

- [[Unsloth Long Context Training]]

## Related

- [[Long Context]]
- [[KV Cache]]
