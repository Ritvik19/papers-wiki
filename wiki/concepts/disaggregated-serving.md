# Disaggregated Serving

**Type**: concept  
**Tags**: #concept

## Overview

Disaggregated serving separates the prefill and decode phases of LLM inference onto independent GPU workers, allowing each phase to be optimized and scaled independently. Prefill is compute-bound and determines TTFT; decode is memory-bandwidth-bound and determines TPS.

## Mechanism

In a disaggregated setup, inference follows three steps:
1. The **prefill engine** processes the input sequence, generating the KV cache and the first token.
2. The KV cache is transferred over the hardware interconnect to the **decode engine**.
3. The **decode engine** generates all subsequent tokens.

Conditional disaggregation first checks if the input sequence is already cached or short enough for local handling, only routing to the prefill engine when needed.

The ratio of prefill to decode engines is expressed as **xPyD** (e.g., 5P3D = 5 prefill, 3 decode engines). This ratio can be adjusted at runtime to match changing traffic patterns — a capability called dynamic disaggregation.

## When to Use

Disaggregation becomes worthwhile when:
1. Serving 100M–1B+ tokens per day
2. Running models with 100B+ parameters
3. Traffic is prefill-heavy with long input sequences

A textbook use case is serving a frontier LLM in a code editor, where many developers simultaneously pass large varied code chunks as context.

## Appearances

- [[Inference Engineering]] — Chapter 5.5 covers disaggregated serving, conditional disaggregation, and NVIDIA Dynamo's production-ready support.

## Notes

The primary bottleneck in disaggregated systems is prefill queue size. NVIDIA Dynamo provides NIXL-based KV transfer with kernel support for transposing KV blocks between different TP configurations on prefill and decode engines.

## Related

- [[KV Cache]]
- [[Inference Engineering]]
- [[Large Language Models]]
