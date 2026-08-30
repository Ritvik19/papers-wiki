# MentorNet

**Type**: concept  
**Tags**: #concept

## Overview

MentorNet (Jiang et al., ICML 2018) uses a mentor network (often LSTM over prediction variance) to predict per-sample curriculum weights $w_i \in [0,1]$ for a StudentNet training on corrupted labels, plus predefined curriculum $G_\lambda(\mathbf{w})$ regularizer.

## Appearances

- [[Learning with not Enough Data Part 3: Data Generation]] — Architecture diagram; alternative to [[Co-teaching]] for noisy generated labels.

## Related

- [[Co-teaching]]
- [[Generalized Cross Entropy]]
- [[Synthetic Data]]
