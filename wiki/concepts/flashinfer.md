# FlashInfer

**Type**: concept  
**Tags**: #concept

## Overview

Efficient, customizable GPU attention engine for LLM inference serving. Builds metadata to configure and schedule attention kernels for prefill, decode, and verification passes.

## Appearances

- [[Accelerating Sonar Through Speculation]] — Perplexity's inference runtime is shaped around FlashInfer; speculative decoding adds CPU-side metadata work and GPU→CPU sync on accepted token counts.
- [[Inference Engineering]] — attention kernel and serving-stack context.

## Notes

Speculative decoding at Perplexity shares batch scheduling and KV page allocation across draft and target models behind a unified server interface.

## Related

- [[KV Cache]]
- [[Speculative Decoding]]
- [[Inference Engine]]
