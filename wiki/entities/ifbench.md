# IFBench

**Type**: benchmark  
**Tags**: #entity

## Overview

IFBench is a benchmark and training/evaluation paradigm for precise instruction following under unseen, verifiable output constraints. It expands beyond IFEval by adding 58 held-out test constraints, 29 IFTrain constraints, strict and loose accuracy metrics, and both single-turn and multi-turn rewrite settings.

## Appearances

- [[Inkling]] — scores 79.8% on IFBench at effort=0.99; [[Inkling-Small]] scores 82.2%.
- [[Papers Explained: IFBench]] - central source describing the benchmark, IFTrain, and IF-RLVR training setup.
- [[Papers Explained 544 - GEPA]] - uses IFBench as one of the benchmark tasks for comparing prompt optimization against GRPO.
- [[Papers Explained 518 - Nemotron Cascade]] - mentions IF-Bench-Train taxonomies as part of instruction-following RL.

## Notes

IFBench is especially useful because its constraints have Python verification functions. That makes it a bridge between [[Evaluation and Benchmarks]], [[Safety and Alignment]], and [[Reinforcement Learning Topic]]: instruction following becomes a verifier-scored behavior that can be optimized directly.

## Related

- [[Verifiable Instruction Following]]
- [[GRPO]]
- [[Evaluation and Benchmarks]]
- [[Safety and Alignment]]
