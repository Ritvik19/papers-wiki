# Numina

**Type**: org
**Tags**: #entity

## Overview

Numina (Project Numina, published under the AI-MO organization on Hugging Face) is a research group focused on AI for mathematics, known for the NuminaMath dataset (winning entry in the first AIMO Progress Prize) and the Kimina-Prover family of Lean 4 automated theorem provers, the latter developed jointly with Kimi's team at Moonshot AI.

## Appearances

- [[Kimina-Prover: Applying Test-Time RL Search on Large Formal Reasoning Models]] — Kimina-Prover-72B and distilled 8B/1.7B variants, reaching 92.2% pass rate on miniF2F via Test-Time Reinforcement Learning Search and an error-fixing capability.
- [[Kimina-Prover-RL]] — slimmed-down, open-source Verl-compatible training pipeline reproducing the core Kimina-Prover methodology at 0.6B-1.7B scale.

## Notes

- Kimina-Prover models are trained on NuminaMath 1.5's olympiad-reference subset and verified against Lean 4 via `kimina-lean-server`.

## Related

- [[Paper Explained 316 - NuminaMath]]
- [[Reasoning Models]]
- [[Reinforcement Learning Topic]]
