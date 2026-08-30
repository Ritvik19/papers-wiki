# LAMBADA Data Generation

**Type**: concept  
**Tags**: #concept

## Overview

LAMBADA (Anaby-Tavor et al., AAAI 2020) augments text classification by fine-tuning a language model on the training set, then generating new samples by continuing from `y[SEP]` until EOS. A baseline classifier filters synthesized data by correctness and confidence; top 10% of a 10× oversampled pool are retained.

## Appearances

- [[Learning with not Enough Data Part 3: Data Generation]] — Outperforms other generative augmentation approaches in surveyed experiments.

## Pipeline

1. $h = \mathcal{A}(\mathcal{D}_\text{train})$ — train classifier
2. Fine-tune LM $\mathcal{M}$ on $\mathcal{D}_\text{train}$ → $\mathcal{M}_\text{tuned}$
3. Generate $\mathcal{D}^*$ from class-conditioned prompts
4. Filter: $h(x)=y$ and top confidence → $\mathcal{D}_\text{syn}$
5. Train on $\mathcal{D}_\text{syn} \cup \mathcal{D}_\text{train}$ (repeat optional; diminishing returns possible)

## Related

- [[Unsupervised Data Generation]]
- [[Synthetic Data]]
- [[Large Language Models]]
