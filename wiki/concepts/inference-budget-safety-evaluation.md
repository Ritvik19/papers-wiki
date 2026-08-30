# Inference-Budget Safety Evaluation

**Type**: concept  
**Tags**: #concept

## Overview

**Inference-Budget Safety Evaluation** is an AI safety evaluation methodology proposed to address the gap between standard pre-deployment model evaluations and the compute resources available to well-funded threat actors. In traditional safety evaluations, models are tested against misuse benchmarks (e.g. cyber exploitation, biological synthesis, chemical weapon design) under modest per-task inference budgets (typically $100 to $10,000 across small batches). However, state actors or well-capitalized adversaries can deploy upwards of $10 million in parallel [[Test-Time Compute]] to achieve a single catastrophic goal. Inference-Budget Safety Evaluation requires AI developers to evaluate capability curves over multiple compute budgets and project expected capabilities into high-spend regimes using empirical scaling models with stated uncertainty bounds.

## Core Principles

1. **2D Safety Frontier**: Capability thresholds in [[Preparedness Framework|Preparedness Frameworks]] and [[Responsible Scaling Policy|Responsible Scaling Policies (RSPs)]] cannot be treated as static binary flags. Misuse risk is a function of inference spend: $\text{Risk} = f(\text{Model}, \text{Inference Budget}, \text{Scaffolding})$.
2. **Empirical Measurement with Extrapolation**: Because running thousands of red-teaming rollouts at $10M+ each is computationally intractable, labs must empirically measure capability curves at low-to-medium budgets and extrapolate projected performance to actor budgets, explicitly modeling uncertainty bands.
3. **Runtime Scaffolding Transparency**: Model cards and system cards must evaluate base models across diverse inference scales so that downstream users and safety auditors understand the capabilities achievable through multi-agent scaffolding, parallel search, and extended execution.
4. **Horizon vs. Development Cycle Dilemma**: Verifying long-horizon agent alignment (e.g., assessing covert misalignment over a 1-year operational lifetime) requires year-long evaluations that outlast frontier model release cycles. Overcoming this bottleneck requires developing accelerated proxy environments and validated short-horizon extrapolation techniques.

## Appearances

- [[Implications of Large-Scale Test-Time Compute]] — foundational proposal by [[Noam Brown]] outlining the necessity of compute-budgeted safety curves, using [[Gemini 3 Deep Think]] and [[GPT-5.5]] case studies.
- [[Preparedness Framework]] — OpenAI's framework evaluated under this methodology.
- [[Responsible Scaling Policy]] — industry governance commitments requiring compute-conditioned thresholds.

## Notes

- Highlighted by the [[AI Security Institute]]'s long-horizon cyber evaluations ("The Last Ones"), where severe multi-stage exploits (M1–M9) only manifest after tens of millions of cumulative tokens.
- Addresses controversies such as Google DeepMind's [[Gemini 3 Deep Think]] release, emphasizing that high-compute runtime scaffolds inherit and amplify the latent capabilities of base models.

## Related

- [[Test-Time Compute]] — underlying compute mechanism driving capability expansion.
- [[Preparedness Framework]] — safety governance process requiring compute-budget integration.
- [[Responsible Scaling Policy]] — commitment protocol for catastrophic risk mitigation.
- [[Noam Brown]] — author of the evaluation framework.
- [[Safety and Alignment]] — parent domain.
- [[AI Security Institute]] — evaluation institute running compute-scaled cyber benchmarks.
