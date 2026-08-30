# Agentic Context Engineering

**Type**: concept  
**Tags**: #concept

## Overview

**Agentic Context Engineering (ACE)** treats the model's context as an evolving structured playbook rather than a monolithic growing prompt. Three roles maintain it: a **Generator** (task trajectories), a **Reflector** (insights from successes/failures), and a **Curator** (incremental bullet-point updates with deterministic merge logic).

## Appearances

- [[Harness Engineering for Self-Improvement]] — ACE (Zhang et al. 2025); extensions include Meta Context Engineering (MCE: bi-level skill/context evolution) and Meta-Harness (optimizes harness code itself).

## Notes

ACE avoids context collapse by never rewriting the full prompt blob. MCE instantiates context as files (`skill.md` plus dynamic rollouts) and evolves skills via agentic crossover. Meta-Harness pushes optimization one level deeper: the object is the code that builds context.

## Related

- [[Self-Improving Harness]]
- [[Dynamic Context]]
- [[Agent Harness]]
- [[Long Context]]
