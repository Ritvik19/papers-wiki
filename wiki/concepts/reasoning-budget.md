# Reasoning Budget

**Type**: concept  
**Tags**: #concept

## Overview

A **reasoning budget** is a hard cap on how many tokens a [[Reasoning Models|reasoning model]] may spend in its thinking trace before producing the final answer. Budgets can be enforced at inference (client closes `</think>` and continues generation) or learned during training.

## Appearances

- [[Controlling Reasoning Effort in LLMs]] — Nemotron 3 Ultra random-budget truncation SFT; Qwen3 emergent behavior after forced stop; Kimi K2.5 Toggle alternates budgeted and unconstrained RL.

## Notes

Learned effort modes (medium vs. regular) determine *how* the model uses tokens; an external budget constrains *how long* thinking may continue. Fixed budgets alone can overfit to short solutions; Toggle addresses this by alternating constrained and unconstrained RL phases.

## Related

- [[Reasoning Effort]]
- [[Papers Explained 580: Nemotron 3 Ultra]]
- [[Think Tokens]]
