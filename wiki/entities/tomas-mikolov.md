# Tomas Mikolov

**Type**: person  
**Tags**: #entity

## Overview

Tomas Mikolov is a researcher who led development of **Word2Vec** and related efficient word representation methods at Google. His 2013 papers introduced skip-gram, CBOW, [[Negative Sampling]], and training heuristics that made billion-token embedding training practical.

## Appearances

- [[Learning Word Embedding]] — Skip-gram/CBOW architectures; negative sampling; soft window, subsampling, phrase learning practices.

## Key publications (cited in source)

| Paper | Venue | Contribution |
|-------|-------|--------------|
| Efficient estimation of word representations in vector space | arXiv:1301.3781 (2013) | Skip-gram, CBOW, subsampling, architecture |
| Distributed representations of words and phrases and their compositionality | NIPS 2013 | Phrase vectors, larger-scale training |
| (Same arXiv:1301.3781 listed twice in Weng refs [5],[9]) | — | Core Word2Vec reference |

## Technical legacy

- **Negative sampling** as default large-vocab training (vs full softmax).
- **Subsample frequent words** with √(t/f) rule.
- **Phrase detection** score (C(w_i w_j) − δ) / (C(w_i) C(w_j)).
- Demonstrated **vector arithmetic** analogies at scale.

Later work extended to sentence representations and language modeling; Word2Vec remains the canonical citation for static embeddings in industry and academia.

## Related

- [[Word2Vec]]
- [[Skip-Gram]]
- [[Negative Sampling]]
- [[Distributed Representations]]
- [[Learning Word Embedding]]
