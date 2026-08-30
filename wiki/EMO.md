# EMO

EMO is a mixture-of-experts pretraining method that induces emergent modularity by constraining all tokens in a document to route within a shared document-level expert pool.

## Overview

EMO uses document boundaries as weak supervision for expert specialization. Instead of relying on human-labeled domains, it averages token routing distributions within a document, selects a top-d expert pool, and masks token routing to that pool so expert subsets become more coherent and usable in isolation.

## Appearances

- [[Papers Explained: EMO]] - primary source page describing EMO, its document expert pools, global load balancing, randomized pool sizes, and selective expert-use results.

## Notes

EMO extends the standard [[Mixture of Experts]] promise from conditional compute to deployable modularity. The source's key claim is that a full EMO model remains competitive with a standard MoE while task-specific expert subsets retain much more performance under pruning.

## Related

- [[Mixture of Experts]]
- [[Model Compression and Efficiency]]
- [[Papers Explained 270 - OLMoE]]

#concept
