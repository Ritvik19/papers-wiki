# OpenCode

**Type**: tool  
**Tags**: #entity

## Overview

**OpenCode** is an open-source coding-agent harness (github.com/anomalyco/opencode) that exposes fine-grained typed tools (`edit`, `grep`, `todowrite`, `task`, etc.) returning structured JSON—contrasting with SWE-Agent's rich CLI and mini-SWE-agent's single-`bash` modality.

## Appearances

- [[Introducing North Mini Code]] — North Mini Code trained and human-evaluated in OpenCode via Harbor; +10% eval gain from multi-harness SFT.
- [[Papers Explained: Arcee Trinity]] — agentic harness trajectories from OpenCode supply coding SFT data.
- [[Components of A Coding Agent]] — referenced alongside other harness designs in Sebastian Raschka's agent-component taxonomy.

## Notes

- Cohere specifically trained North Mini Code for OpenCode compatibility while optimizing across multiple harnesses.
- Distinct from the **OpenCodeReasoning** synthetic dataset family (NVIDIA/Hugging Face).

## Related

- [[Agent Harness]] — harness layer around coding models.
- [[Components of A Coding Agent]] — six-component coding-agent reference.
- [[North Mini Code]] — model trained for OpenCode robustness.
- [[Code Models]] — topic hub.
