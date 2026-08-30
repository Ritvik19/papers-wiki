# Code World Models

**Tags**: #concept

Code world models (CWM) are code-focused LLMs trained to simulate program execution—predicting how variable states and program behavior evolve step by step when code changes—rather than learning only static syntax and token co-occurrence patterns from raw source text.

## Overview

Traditional code LLMs (e.g., Qwen3-Coder) optimize next-token prediction on static repositories. CWM (32B dense decoder, 131k context, Meta/Facebook open weights) adds a **mid-training** phase on Python execution traces and agentic Docker trajectories (observation-action pairs from real repo environments), teaching the model to anticipate runtime outcomes. At inference it remains autoregressive but can emit structured execution traces encoding state after each line.

Raschka describes CWM as a "world-model-augmented LLM": still a transformer generator, but with internal simulation of code dynamics. Reported results place 32B CWM on par with gpt-oss-20b (mid reasoning) and, with best@k test-time scaling using generated unit tests, slightly above gpt-oss-120b (high reasoning) at 4× smaller size on SWE-bench—though latency comparisons across different scaling strategies are not provided.

## Appearances

- [[Beyond Standard LLMs]] — accessible introduction contrasting CWM with regular code LLMs and summarizing SWE-bench results.
- [[Papers Explained 538 - Code World Model]] — detailed paper ingest in the corpus.

## Notes

- Training requires executable traces and repository-scale environment setup (RepoAgent, Activ/CI pipelines)—more complex than static code corpora.
- Complements reasoning-focused post-training (CoT, RL) by grounding code understanding in simulated execution.

## Related

- [[Code Models]]
- [[Papers Explained 538 - Code World Model]]
- [[Reasoning Models]]
- [[Beyond Standard LLMs]]
