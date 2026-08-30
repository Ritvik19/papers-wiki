# Explainable AI

**Type**: concept  
**Tags**: #concept

## Overview

Explainable AI (XAI) encompasses methods that make machine learning model decisions understandable to humans — addressing the black-box problem where complex models (especially deep neural networks) achieve high accuracy but provide no justification for their predictions. Critical in safety-sensitive domains like autonomous driving, healthcare, and finance.

## Appearances

- [[Explainable AI (XAI): A Survey of Recent Methods, Applications and Frameworks]] — AI Summer survey categorizing XAI by explanation modality (visual, textual, numerical); covers CAM, Grad-CAM, LRP, LIME, TCAV, applications, and frameworks (iNNvestigate, explAIner, InterpretML).

## Notes

Papastratis (2021) organizes methods by how explanations are delivered rather than by model architecture. Visual saliency methods (CAM, Grad-CAM, LRP) dominate CNN interpretability; numerical methods (LIME, linear probes, TCAV) generalize across model types. Post-hoc explanation does not guarantee faithfulness — a known open problem not deeply addressed in this survey.

## Related

- [[Grad-CAM]]
- [[LIME]]
- [[Class Activation Mapping]]
- [[Layer-Wise Relevance Propagation]]
- [[Concept Activation Vectors]]
- [[Safety and Alignment]]
- [[Evaluation and Benchmarks]]
