# Noam Brown

**Type**: person  
**Tags**: #entity

## Overview

**Noam Brown** is an AI researcher at [[OpenAI]] known for foundational breakthroughs in game theory, multi-agent reinforcement learning, heuristic search, and test-time compute scaling. Prior to OpenAI, Brown was a research scientist at Meta AI (FAIR) and completed his PhD at Carnegie Mellon University under Tuomas Sandholm. His landmark systems include **Libratus** (first AI to beat top humans in heads-up no-limit Texas hold'em), **Pluribus** (first to beat elite humans in six-player poker), and **Cicero** (first AI to achieve human-level play in the natural language strategy game Diplomacy). At OpenAI, Brown's research has centered on scaling inference-time search, reasoning models (o1, o3, GPT-5.x reasoning lines), and evaluating model capability as a function of compute.

## Appearances

- [[Implications of Large-Scale Test-Time Compute]] — author of the June 2026 essay arguing that LLM benchmark evaluations and safety frameworks (Preparedness Frameworks, RSPs) must replace scalar scores with 2D performance-vs-compute curves and projected capability bounds for high-budget actors.

## Notes

- Brown's work connects classical tree search and equilibrium finding in imperfect-information games to modern LLM test-time reasoning.
- Advocated early for the "third scaling law" (scaling test-time compute in addition to model parameters and pre-training data), leading into OpenAI's o-series reasoning architectures.
- Emphasizes that because capability plateaus are pushed out into millions of tokens and thousands of rollout experiments, single-number benchmark grids fail to measure true model progress.

## Related

- [[OpenAI]] — current research affiliation.
- [[Test-Time Compute]] — core research area spanning search, Monte Carlo methods, and reasoning tokens.
- [[Inference-Budget Safety Evaluation]] — proposed safety evaluation methodology.
- [[Reasoning Models]] — architectural class leveraging test-time inference scaling.
- [[Gemini 3 Deep Think]] — analyzed in Brown's essay as a runtime model scaffolding case study.
- [[GPT-5.5]] — case study demonstrating how token-budget-controlled evals reveal step-changes missed by scalar grids.
