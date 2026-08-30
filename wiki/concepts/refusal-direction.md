# Refusal Direction

**Type**: concept  
**Tags**: #concept

## Overview

The **refusal direction** is a vector in a transformer layer's residual stream that encodes a model's tendency to refuse requests. Arditi et al. (2024) showed that blocking this direction removes refusals; artificially adding it can cause refusals on harmless prompts.

## Appearances

- [[Uncensor any LLM with abliteration]] — estimated as normalized mean difference of harmful vs. harmless prompt activations at the last token, per layer and residual position (pre/mid/post).

## Notes

Selection involves running candidate directions through inference-time ablation hooks and choosing the layer that best removes refusals without obvious quality collapse. The direction is architecture- and alignment-dependent. Related but distinct from [[ITI]]'s truthfulness direction.

## Related

- [[Abliteration]]
- [[Weight Orthogonalization]]
- [[Safety and Alignment]]
