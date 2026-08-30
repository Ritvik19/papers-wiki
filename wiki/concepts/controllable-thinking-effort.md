# Controllable Thinking Effort

**Type**: concept  
**Tags**: #concept

## Overview

Controllable thinking effort is Inkling's product name for continuous [[Reasoning Effort]]: developers set an effort level (roughly 0.2–0.99, or named levels in transformers: `none`, `minimal`, `low`, `medium`, `high`, `xhigh`, `max`) to trade accuracy against tokens, cost, and latency. Training teaches the policy to spend different amounts of thinking by pairing system-message effort with a per-token cost in RL.

## Appearances

- [[Inkling]] — effort sweeps on Terminal-Bench 2.1, HLE, and IFBench; matches Nemotron 3 Ultra Terminal-Bench scores at roughly one-third the tokens; transformers `reasoning_effort` API.
- [[Inkling-Small]] — effort curves sit above Inkling's across Terminal-Bench 2.1, HLE, and IFBench at every budget.
- [[Controlling Reasoning Effort in LLMs]] — surveys Inkling's continuous effort conditioning alongside other open-weight recipes.
- [[Reasoning Effort]] — parent taxonomy of effort labels and token-penalty RLVR.

## Notes

- Effort was trained into the model during large-scale async RL by changing system messages and per-token cost, not only as an inference-time heuristic.
- Output TFLOPs per sample are estimated as 2 × active parameters × mean generated tokens (including reasoning tokens).
- Inkling output pricing: $4.05 / 1M tokens; Inkling-Small: $1.20 / 1M tokens (Thinking Machines Tinker pricing, 2026).
- Effort is a separate axis from model size: Inkling-Small with high effort can be preferable to full Inkling at low effort for cost-sensitive workloads (coding, grading, synthetic data).

## Related

- [[Reasoning Effort]]
- [[Reasoning Budget]]
- [[Think Tokens]]
- [[Inkling]]
- [[Inkling-Small]]
- [[Reasoning Models]]
- [[Model Compression and Efficiency]]
- [[Evaluation and Benchmarks]]
