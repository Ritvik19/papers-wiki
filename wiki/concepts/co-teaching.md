# Co-teaching

**Type**: concept  
**Tags**: #concept

## Overview

Co-teaching (Han et al., NeurIPS 2018) trains two networks $f_1, f_2$ in parallel; each epoch each network selects **small-loss** samples from the peer's mini-batch as clean enough to train on. Under the assumption that independent nets memorize different noise subsets, cross-selection avoids fitting mutual label corruption.

## Appearances

- [[Learning with not Enough Data Part 3: Data Generation]] — Beats F-correction at high noise rates or asymmetric corruption matrices.

## Algorithm

1. Each net forward-passes current batch, ranks samples by loss
2. Exchange which samples to use (small-loss = likely clean)
3. Selection fraction $R(T)$ **decreases** over training (less data as overfitting to noise risk grows)
4. Each net backprops on peer-selected subset

## vs MentorNet

| | Co-teaching | MentorNet |
|---|-------------|-----------|
| Architecture | Two equal students | Mentor LSTM + StudentNet |
| Weighting | Hard selection | Soft curriculum weights |
| Noise model | Implicit via disagreement | Explicit $w_i$ prediction |

## Related

- [[Synthetic Data]]
- [[Generalized Cross Entropy]]
- [[MentorNet]]
- [[F-Correction]]
