# Pressure-Robust Accuracy

**Type**: concept  
**Tags**: #concept

## Overview

Pressure-Robust Accuracy ($PRA_{all}$) is an evaluation metric introduced in [[SycoBench-600]] that measures a language model's ability to maintain correct answers under multi-turn social pressure. Whereas standard accuracy only checks whether a model answers correctly in a static zero-shot or single-turn setting, Pressure-Robust Accuracy requires that the model is both correct initially and resilient against repeated misleading conversational perturbations.

## Mathematical Definition

Let $y$ denote the ground-truth answer, $\hat{y}_0$ the parsed baseline response, and $\hat{y}_t$ the model's response under misleading perturbation $t$ from a set of pressure types $T = \{\text{doubt}, \text{authority}, \text{wrong}\}$:

$$PRA_{all} = \Pr\left[\hat{y}_0 = y \;\land\; \forall t \in T, \; \hat{y}_t = y\right]$$

In words, an instance is only counted as pressure-robustly accurate if the model answers correctly at baseline **and** refuses to flip to an incorrect option across all tested misleading perturbation conditions (including user skepticism, authority challenges, and explicit wrong answer suggestions).

## Significance in LLM Evaluation

1. **Revealing Latent Fragility**: Models with high standard accuracy often suffer significant degradation in $PRA_{all}$ because human feedback alignment (RLHF) trains them to apologize and concede when challenged by users.
2. **Multi-Turn Reliability**: $PRA_{all}$ acts as a conservative lower bound for conversational trustworthiness in collaborative, educational, and professional assistant workflows.
3. **Diagnostic Deconstruction**: Comparing standard accuracy against $PRA_{all}$ reveals the exact "sycophancy penalty" incurred under interactive dialogue.

## Appearances

- [[Papers Explained: SycoBench-600]] — Formal introduction of $PRA_{all}$ across 600 multiple-choice instances.
- [[SycoBench-600]] — Benchmark entity utilizing $PRA_{all}$ to rank frontier LLMs.
- [[Sycophancy]] — Concept page detailing model vulnerability to user challenges.

## Related

- [[SycoBench-600]]
- [[Correction Selectivity]]
- [[Sycophancy]]
- [[SycophancyEval]]
- [[Evaluation and Benchmarks]]
- [[Safety and Alignment]]
