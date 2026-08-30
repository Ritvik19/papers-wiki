# Weight Orthogonalization

**Type**: concept  
**Tags**: #concept

## Overview

**Weight orthogonalization** permanently removes a linear feature direction from a language model by adjusting weight matrices so they no longer write to that direction. In abliteration, embedding `W_E`, attention output `W_O`, and MLP `W_out` are orthogonalized with respect to the [[Refusal Direction]].

## Appearances

- [[Uncensor any LLM with abliteration]] — implementation via TransformerLens; converted back to Hugging Face weights for Hub upload.

## Notes

For each matrix, the component parallel to the direction vector is subtracted: $W' = W - \text{proj}_\vec{r}(W)$. This is more permanent than inference-time directional ablation hooks. Causes benchmark degradation that can be partially recovered with light [[Papers Explained 148 - Direct Preference Optimization|DPO]] alignment.

## Related

- [[Abliteration]]
- [[Refusal Direction]]
- [[ITI]]
