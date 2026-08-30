# Grouped-Query Attention

**Tags**: #concept

Grouped-query attention (GQA) is an attention variant that shares key-value projections across multiple query heads while keeping a larger set of query heads. Introduced in *GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints* (Ainslie et al., 2023), it reduces [[KV Cache]] memory and traffic versus classic [[Multi-Head Attention]] with modest architectural change.

## Overview

In standard MHA every head has its own \(W_k, W_v\) projections—modeling-friendly but cache-heavy at long context. GQA groups query heads so several queries reuse the same K/V head, shrinking per-token cache footprint. At the extreme (one shared K/V group) the design approaches multi-query attention (MQA), which is cheaper still but can hurt quality more noticeably. Production models typically pick an intermediate group count.

GQA became the pragmatic dense-model default in 2023–2026 because it is robust, easier to implement and train than [[Multi-Head Latent Attention]], and pairs naturally with [[Sliding Window Attention]] (e.g., Gemma 3, Mistral). Raschka notes newer releases like MiniMax M2.5 and Nanbeige 4.1 deliberately stayed on classic GQA; Sarvam 30B uses GQA while the 105B variant switches to MLA.

## Appearances

- [[A Visual Guide to Attention Variants in Modern LLMs]] — visual comparison to MHA/MLA, KV-cache savings curves, and example architectures (Llama 3, Qwen3, Gemma 3, Mistral, SmolLM3, Sarvam 30B).
- [[Understanding and Coding the KV Cache in LLMs from Scratch]] — notes GQA/MQA as common modern cache layouts not covered in the from-scratch MHA tutorial.
- [[Mistral 7B]] — early influential GQA + SWA open model.

## Notes

- Cache savings grow with sequence length; GQA's benefit is most visible on long contexts.
- MLA may offer better quality-per-byte at very large scale, but GQA remains easier to tune below ~100B parameters.

## Related

- [[Multi-Head Attention]]
- [[Multi-Head Latent Attention]]
- [[KV Cache]]
- [[Sliding Window Attention]]
- [[Model Compression and Efficiency]]
