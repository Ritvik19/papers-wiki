# Concept Activation Vectors

**Type**: concept  
**Tags**: #concept

## Overview

Concept Activation Vectors (CAVs), introduced in Testing with Concept Activation Vectors (TCAV), quantify how sensitive a model's predictions for a target class are to user-defined high-level concepts (e.g., "stripes", "curved edges") by training binary classifiers in hidden activation space and measuring the gradient of the class score along the concept direction.

## Appearances

- [[Explainable AI (XAI): A Survey of Recent Methods, Applications and Frameworks]] — numerical XAI method; sensitivity \(S_{C,k,l} = h_{k,l}(\nabla f_l(x) \cdot u_C^l)\) where \(u_C^l\) is the CAV for concept \(C\) at layer \(l\) (Kim et al. 2018).

## Notes

TCAV moves beyond feature attribution to concept-level testing — useful when explanations need to reference human-meaningful abstractions rather than individual pixels. Requires curated positive/negative example sets per concept.

## Related

- [[LIME]]
- [[Explainable AI]]
- [[Evaluation and Benchmarks]]
