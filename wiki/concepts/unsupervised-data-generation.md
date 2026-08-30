# Unsupervised Data Generation

**Type**: concept  
**Tags**: #concept

## Overview

Unsupervised Data Generation (UDG; Wang et al., 2021) synthesizes classification training data by **few-shot prompting** a large LM to generate inputs $\mathbf{x}$ given label $y$ (reverse of standard prediction). A task model trains on synthetic $(\mathbf{x}, \hat{y})$ with **noisy label annealing (NLA)** removing high-confidence disagreements over time.

## Appearances

- [[Learning with not Enough Data Part 3: Data Generation]] — Large gains over few-shot inference; comparable to supervised fine-tuning on several benchmarks.

## NLA filtering rule

At training step $t$, drop $(\mathbf{x}_i, \hat{y}_i)$ if:
- $p(\bar{y}_i|\mathbf{x}_i) > \mu_t$ where $\bar{y}_i = \arg\max_y p(y|\mathbf{x}_i)$
- and $\bar{y}_i \neq \hat{y}_i$ (synthetic label)

$\mu_t$ initialized at 0.9, annealed toward $1/\text{num\_classes}$.

## vs LAMBADA

| | UDG | [[LAMBADA Data Generation]] |
|---|-----|---------------------------|
| LM use | Few-shot prompt, no fine-tune required | Fine-tune LM on train set |
| Direction | Label → text | Label-conditioned generation |
| Filtering | NLA during training | Classifier confidence pre-filter |

## Not UDA

Distinct from **[[Unsupervised Data Augmentation]]** (UDA), which is consistency SSL — different acronym, different method.

## Related

- [[Synthetic Data]]
- [[Active Learning]]
- [[LAMBADA Data Generation]]
- [[Co-teaching]]
