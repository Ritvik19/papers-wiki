# Flex Attention

**Type**: concept  
**Tags**: #concept

## Overview

PyTorch 2.5+ block-sparse attention API (`torch.nn.attention.flex_attention`) enabling custom mask patterns without materializing full attention matrices. Unsloth uses Flex Attention for GPT-OSS long-context training with sliding-window + full-attention alternation.

## Appearances

- [[Unsloth Long Context Training]]

## Related

- [[PyTorch]]
- [[Attention Sinks]]
- [[Sliding Window Attention]]
- [[Long Context]]
