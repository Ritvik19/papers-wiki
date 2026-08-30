# Easy Data Augmentation

**Type**: concept  
**Tags**: #concept

## Overview

Easy Data Augmentation (EDA; Wei & Zou, EMNLP-IJCNLP 2019) applies four cheap lexical operations to text classification training data: **synonym replacement (SR)**, **random insertion (RI)**, **random swap (RS)**, and **random deletion (RD)**. Hyperparameters $p=\alpha$ and $n=\alpha \times \text{sentence\_length}$ control noise intensity.

## Appearances

- [[Learning with not Enough Data Part 3: Data Generation]] — Performance lift largest on smaller training sets; each operation helps at different optimal $\alpha$.
- [[Contrastive Representation Learning]] — Also covered in contrastive-learning survey.

## Operations

| Op | Action |
|----|--------|
| SR | Replace $n$ random non-stopwords with WordNet synonyms |
| RI | Insert random synonym of random word at random position |
| RS | Swap two random words, repeat $n$ times |
| RD | Delete each word with probability $p$ |

## Related

- [[Synthetic Data]]
- [[Contrastive Representation Learning]]
- [[SimCSE]]
