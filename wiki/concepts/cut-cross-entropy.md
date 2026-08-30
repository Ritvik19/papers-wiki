# Cut Cross Entropy

**Type**: concept  
**Tags**: #concept

## Overview

Apple's memory-efficient cross-entropy that avoids materializing full `[batch, seq, vocab]` logits by computing loss on vocabulary slices. Integrated into Unsloth for Llama 3.3 long-context fine-tuning.

## Appearances

- [[Unsloth Long Context Training]]
- [[Unsloth Model Support 2024]]

## Related

- [[Long Context]]
- [[Model Compression and Efficiency]]
