# Abliteration

**Type**: concept  
**Tags**: #concept

## Overview

**Abliteration** is a mechanistic technique to remove a model's refusal (or other linearly encoded) behavior without full retraining. It identifies a [[Refusal Direction]] in residual activations and removes the model's ability to represent that direction—either at inference via directional ablation or permanently via [[Weight Orthogonalization]].

## Appearances

- [[Uncensor any LLM with abliteration]] — tutorial on uncensoring Llama-class instruct models; DPO healing after performance drop.

## Notes

Based on Arditi et al. (2024): refusal is mediated by a single direction. Abliteration demonstrates fragility of safety fine-tuning. Can be applied to other behavioral directions (e.g., conversational style). Later tools (Heretic, AutoAbliteration) automate selection; projected/norm-preserving variants aim to reduce capability loss.

## Related

- [[Refusal Direction]]
- [[Weight Orthogonalization]]
- [[Safety and Alignment]]
- [[ITI]]
