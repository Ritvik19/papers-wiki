# Cursor Router

**Type**: tool  
**Tags**: #concept

## Overview

**Cursor Router** is Cursor's intelligent per-request model router for Teams and Enterprise plans. Before a model runs, a classifier analyzes the request — query, context, task complexity, domain, and per-model behavior — and routes to the best model in the pool. Simple work goes to price-efficient models; UI updates to models with strong taste; complex long-horizon problems to frontier reasoning models.

## Appearances

- [[Introducing Cursor Router]] — Jul 2026 launch post: classifier trained on 600k+ live requests, cache-aware training/evaluation, three Auto modes (Intelligence, Balance, Cost), 30–60% cost savings at frontier quality, admin controls per team.

## Notes

- Optimizes for user satisfaction (AFC) as reward, evaluated via online A/B tests across millions of production requests — not offline benchmarks alone.
- **Cache-aware**: training data includes routing-induced cache misses; reported savings account for model-switching overhead.
- Quality signals mirror harness evaluation: user-response satisfaction classification and [[Keep Rate]].
- Admin controls: per-team rollout, mode defaults, allow/block specific models.
- Draws from an expanding model pool including [[Grok Models|Grok 4.5]] (harder tasks) and [[Introducing Composer 2.5|Composer]] (everyday path).

## Related

- [[Cursor]]
- [[Agent Harness]]
- [[Continually Improving Our Agent Harness]]
- [[Keep Rate]]
- [[Dynamic Tool Calling]]
- [[Evaluation and Benchmarks]]
- [[Code Models]]
