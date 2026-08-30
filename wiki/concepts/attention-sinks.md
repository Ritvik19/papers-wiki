# Attention Sinks

**Type**: concept  
**Tags**: #concept

## Overview

Dedicated sink tokens in attention that absorb excess probability mass, stabilizing long-context and sliding-window attention. GPT-OSS uses sinks with 128-token sliding windows; Unsloth moves sink position to index 0 for training stability with Flex Attention.

## Appearances

- [[Unsloth Long Context Training]]

## Related

- [[Flex Attention]]
- [[Sliding Window Attention]]
- [[KV Cache]]
