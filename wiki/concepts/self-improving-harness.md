# Self-Improving Harness

**Type**: concept  
**Tags**: #concept

## Overview

A **self-improving harness** is an [[Agent Harness]] that edits its own configuration or source code based on rollout feedback, subject to validation and permission boundaries. Optimization targets include system prompts, tool descriptions, middleware, skills, sub-agent configs, and memory policies.

## Appearances

- [[Harness Engineering for Self-Improvement]] — surveys Self-Harness (weakness mining → bounded proposal → regression validation), AHE (observability-driven component edits), and STOP (recursive improver improvement).

## Notes

Key design constraints: explicit editable surfaces, held-in/held-out regression tests, evaluators and verifiers **outside** the edit loop (prevents disabling the verifier or swapping models). Harness-updating ability is relatively flat across model sizes; benefiting from an updated harness requires strong tool use and long-horizon instruction following.

## Related

- [[Recursive Self-Improvement]]
- [[Agentic Context Engineering]]
- [[Reward Hacking]]
- [[Continually Improving Our Agent Harness]]
