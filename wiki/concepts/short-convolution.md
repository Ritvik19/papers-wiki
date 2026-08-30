# Short Convolution

**Type**: concept  
**Tags**: #concept

## Overview

**Short convolution (SConv)** is a local 1D convolution over hidden states that mixes the current token with the previous `W−1` states (window size `W`). In Inkling it sits after key/value projections in attention and on attention/MLP residual branch outputs before they rejoin the main residual stream, handling local structure so attention and MoE modules need not.

## Appearances

- [[Inkling]] — distinctive architectural component alongside hybrid attention and relative position embeddings; diagram in the Hugging Face architecture writeup.

## Notes

Related in spirit to local-context mechanisms in hybrid SSM/attention models, but implemented here as explicit short convolutions on transformer residual paths rather than as a full sequence mixer replacement.

## Related

- [[Inkling]]
- [[Relative Position Embedding]]
- [[Mixture of Experts]]
- [[Large Language Models]]
