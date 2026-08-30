# Probabilistic Context-Free Grammars

**Type**: concept  
**Tags**: #concept

## Overview

Probabilistic Context-Free Grammars (PCFGs) extend traditional context-free grammars (CFGs) by assigning probabilities to each production rule. This allows them to model the variability and ambiguity of natural language in a quantitative way. A PCFG generates parse trees by probabilistically sampling and applying rules from a start symbol until all nodes are terminal tokens (actual vocabulary items).

Key parameters that control PCFG complexity:
- **Number of terminals** — the vocabulary size (actual tokens)
- **Number of non-terminals** — the number of syntactic categories
- **Max RHS length** — maximum number of symbols on the right-hand side of a production rule
- **Max productions per non-terminal** — how many alternative rules each non-terminal can have

Increasing any of these parameters increases syntactic complexity, producing data that is harder to compress and requires more compute to model.

## Appearances

- [[gzip Predicts Data-dependent Scaling Laws]] — PCFGs are used to generate synthetic datasets with precisely controlled complexity, enabling controlled experiments on how data complexity shifts neural scaling laws.

## Notes

- In the gzip scaling laws paper, terminals are represented as integers serving as token IDs; sentences end with a special token 0. This makes the PCFG outputs directly usable as language model training data.
- The Python `PCFG` package (built on NLTK) is used to instantiate and sample from the grammars.
- Gzip compressibility is used as a grammar-agnostic complexity proxy: it does not require knowing the grammar and applies equally to real-world datasets.

## Related

- [[Scaling Laws]] — the context in which PCFGs were used as a data complexity control mechanism.
- [[Kolmogorov Complexity]] — the information-theoretic concept that gzip compressibility approximates.
- [[gzip Predicts Data-dependent Scaling Laws]] — primary source for this use of PCFGs.
