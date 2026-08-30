# Catastrophic Forgetting

**Type**: concept  
**Tags**: #concept

## Overview
The tendency of neural networks and language models to abruptly lose previously acquired capabilities and factual knowledge when fine-tuned on new, narrow tasks.

## Appearances
- [[Papers Explained 593: Self-Distillation Fine-Tuning]] — analyzed in post-training SFT vs. SDFT.
- [[Papers Explained: SFT Conflicts, RL Coexists]] — demonstrates that sequential multi-stage SFT collapses performance (-23.1% below base), whereas multi-stage RL accumulates reasoning performance (+24.9%) through orthogonal parameter updates and [[Task Coexistence]].

## Notes
- Mitigated by on-policy self-distillation (SDFT), on-policy reinforcement learning ([[GRPO]]), parameter-efficient fine-tuning, and rehearsal mixtures.

## Related
- [[Task Coexistence]]
- [[Gradient Interference]]
- [[Parallel-RL]]
- [[Self-Distilled Fine-Tuning]]
- [[Continual Learning]]
- [[Supervised Fine-Tuning]]
