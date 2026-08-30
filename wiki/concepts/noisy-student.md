# Noisy Student

**Type**: concept  
**Tags**: #concept

## Overview

Noisy Student (Xie et al., CVPR 2020) scales **self-training** to web-scale vision: a teacher EfficientNet labels 300M unlabeled images; a **larger** student trains on true labels plus soft pseudo labels with explicit **training noise** (RandAugment, dropout, stochastic depth). The student must be noisier than the teacher to generalize beyond the teacher's errors.

## Appearances

- [[Learning with not Enough Data Part 1: Semi-Supervised Learning]] — ImageNet pipeline; adversarial robustness to FGSM without adversarial training; SentAugment for low in-domain text.
- [[Best Deep CNN Architectures and Their Principles: from AlexNet to EfficientNet]] — iterative teacher–student loop on 300M unlabeled images atop EfficientNet; 88.4% Top-1 with EfficientNet-L2.

## Requirements for student > teacher

| Requirement | Rationale |
|-------------|-----------|
| Student larger than teacher | Capacity to fit more (noisy) data |
| Noise on student only | Teacher produces clean pseudo labels |
| Class-balanced pseudo data | Avoid majority-class collapse |
| Soft pseudo labels | Better than hard one-hot |
| Data balancing | Per-class pseudo image counts |

## Iterative loop

1. Train teacher on labeled data (no noise for pseudo generation)
2. Generate pseudo labels on unlabeled corpus
3. Train larger student on labeled + pseudo with noise
4. Student can become next teacher (iterate)

## Related

- [[Semi-Supervised Learning]]
- [[Self-Supervised Representation Learning]]
- [[Synthetic Data]]
- [[Meta Pseudo Labels]]
