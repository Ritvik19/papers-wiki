# Sample Packing

**Type**: concept  
**Tags**: #concept

## Overview

Packing multiple variable-length sequences into one batch row without padding tokens, using block-diagonal attention masks. Unsloth's padding-free packing with fused QK RoPE achieves ~3× throughput on heterogeneous SFT data.

## Appearances

- [[Unsloth Training Efficiency and Kernels]]
- [[Unsloth Reinforcement Learning]]

## Related

- [[Gradient Accumulation]]
- [[Long Context]]
