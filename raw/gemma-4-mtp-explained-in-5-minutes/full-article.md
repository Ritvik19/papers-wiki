# Gemma 4 MTP Explained in 5 minutes

**Source URL**: https://tianhaozhou.medium.com/gemma-4-mtp-explained-in-5-minutes-0b12ad381240  
**Author**: Jackson MZ (ex DeepMind, ex Google)

## What is MTP?

MTP (a.k.a. speculative decoding) is the technique to make a model predict more than one token at the same time. The most common way is to let a lightweight fast model guess multiple tokens and use the heavy main model to verify the guessed tokens in batch.

## What is new about Gemma 4 MTP?

Compared with DeepSeek v3 and EAGLE-3, the biggest differences are:

- Gemma 4 MTP uses shared weights to do autoregressive token generation instead of one token per MTP module.
- Gemma 4 MTP attends to the main model KV cache, not hidden states (which are the attention result of the KV cache).

## How is it implemented?

The drafter selects the latest layers' KV cache from the main model (assumed to contain the richest features) and supplies them to drafter layers together with the draft token embedding for autoregressive generation.

**Key detail**: the drafter does not maintain any KV cache. Every draft token depends only on the last draft token, not all previous draft tokens.

Inside a single drafter layer:

- Pre-projection and post-projection shrink/expand dimension from main model size to draft model size.
- A bidirectional attention mask (implementation convenience so all draft tokens attend to all main-model KV cache; not a seq2seq model).

**Hierarchical LM head**: clusters the full vocabulary into a second-level vocab and only computes the LM head for top-K clusters.

## Final thoughts

- Extremely efficient due to KV cache sharing; not having to prefill and maintain its own KV cache is a huge boost.
- Suggests draft steps contain so little information compared with main-model KV cache that maintaining a separate draft KV may not be worth it.
