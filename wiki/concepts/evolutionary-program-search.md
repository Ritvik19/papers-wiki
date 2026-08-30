# Evolutionary Program Search

**Type**: concept  
**Tags**: #concept

## Overview

**Evolutionary program search** applies mutation, evaluation, and selection to populations of programs, prompts, or harnesses. It fits domains where the search space is large and fitness is cheap to measure but gradients are unavailable—common in agent and harness design.

## Appearances

- [[Harness Engineering for Self-Improvement]] — STOP, AlphaEvolve, ShinkaEvolve, Darwin Gödel Machine, ADAS, AFlow, Promptbreeder, GEPA.

## Notes

AlphaEvolve marks evolvable code regions with `# EVOLVE-BLOCK-START/END` and co-evolves meta-prompts. Darwin Gödel Machine lets a coding agent edit its own harness repository. ADAS and AFlow search over agentic workflow **code** and **graphs** respectively. Works best for kernel optimization, contests, and other auto-verifiable tasks; weak evaluators and diversity collapse are risks.

## Related

- [[Self-Improving Harness]]
- [[Recursive Self-Improvement]]
- [[Reward Hacking]]
