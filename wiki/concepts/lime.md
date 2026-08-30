# LIME

**Type**: concept  
**Tags**: #concept

## Overview

Local Interpretable Model-Agnostic Explanations (LIME) explains individual predictions of any classifier by learning a simple interpretable surrogate model (e.g., linear model or decision tree) in the neighborhood of the instance being explained, balancing fidelity to the black-box model against surrogate complexity.

## Appearances

- [[Explainable AI (XAI): A Survey of Recent Methods, Applications and Frameworks]] — numerical XAI method; optimizes \(\xi(g) = \arg\min L(f,g) + \Omega(g)\) where \(f\) is the black-box model, \(g \in G\) is an interpretable surrogate, and \(\Omega(g)\) penalizes complexity.

## Notes

Introduced by Ribeiro, Singh & Guestrin (2016). Model-agnostic and local — explanations are valid only near the explained instance. Perturbation sampling strategy and kernel width affect explanation stability; known limitations include sensitivity to superpixel segmentation for images.

## Related

- [[Explainable AI]]
- [[Concept Activation Vectors]]
- [[Evaluation and Benchmarks]]
