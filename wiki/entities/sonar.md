# Sonar

**Type**: tool  
**Tags**: #entity

## Overview

Perplexity's family of language models served via the Perplexity product and API. Production inference uses speculative decoding (draft-target and MTP heads) to reduce inter-token latency.

## Appearances

- [[Accelerating Sonar Through Speculation]] — draft-target (Llama-1B) and MTP acceleration in Perplexity's FlashInfer-based runtime.
- [[Papers Explained 529 - DR Tulu]] — compared against Claude Sonnet Search and Perplexity Sonar (high-reasoning mode).

## Notes

Distinct from the sonar *sensor* or unrelated "Sonar" model names in other papers; in this wiki, [[Sonar]] refers to Perplexity's LLM line unless otherwise noted.

## Related

- [[Perplexity AI]] — parent org.
- [[Speculative Decoding]] — primary latency optimization for Sonar serving.
- [[Multi-Token Prediction]] — MTP draft heads for single-token speculation.
