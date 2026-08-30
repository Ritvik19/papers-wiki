# Self-Summarization

**Type**: concept  
**Tags**: #concept

## Overview

**Self-summarization** is an agent capability where a coding model compresses its own long trajectory into a useful summary when the context window fills, then continues working from that summary—potentially repeating the cycle on hard tasks. Cursor introduced the technique in [[Introducing Composer 1.5]] and trains it with reinforcement learning by requiring a helpful summary at context limits during rollouts.

## Appearances

- [[Introducing Composer 1.5]] — first public description: RL-trained summaries when context runs out; recursive triggers on hard examples; accuracy stable across varying context lengths.
- [[Papers Explained - Composer 2]] — extends the idea to multi-generation training chains where final trajectory reward applies to all tokens including summaries; good summaries upweighted, lossy summaries downweighted.

## Notes

- Distinct from harness-level transcript summarization at model-switch time ([[Agent Harness]]); self-summarization is a model behavior trained end-to-end inside RL.
- Composer 2 reports that self-summarization also reduces overlong-rollout masking issues in practice.

## Related

- [[Introducing Composer 1.5]]
- [[Papers Explained - Composer 2]]
- [[Agent Harness]]
- [[Long Context]]
- [[Dynamic Context]]
