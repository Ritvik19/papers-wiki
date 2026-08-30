# Tiled MLP

**Type**: concept  
**Tags**: #concept

## Overview

Sequence-dimension sharding of MLP forward/backward passes so activations never materialize the full sequence at once. Enables Unsloth's 500K context length fine-tuning when combined with chunked fused cross-entropy.

## Appearances

- [[Unsloth Long Context Training]]

## Related

- [[Cut Cross Entropy]]
- [[Long Context]]
- [[Unsloth Gradient Checkpointing]]
