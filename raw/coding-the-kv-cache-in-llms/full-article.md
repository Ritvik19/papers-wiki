Source URL: https://magazine.sebastianraschka.com/p/coding-the-kv-cache-in-llms
Title: Understanding and Coding the KV Cache in LLMs from Scratch
Author: Sebastian Raschka, PhD
Date: Jun 17, 2025

# Understanding and Coding the KV Cache in LLMs from Scratch

KV caches are one of the most critical techniques for efficient inference in LLMs in production. This article explains how they work conceptually and in code with a from-scratch, human-readable implementation.

## Overview

In short, a KV cache stores intermediate key (K) and value (V) computations for reuse during inference (after training), which results in a substantial speed-up when generating text. The downside of a KV cache is that it adds more complexity to the code, increases memory requirements (the main reason I initially didn't include it in the book), and can't be used during training. However, the inference speed-ups are often well worth the trade-offs in code complexity and memory when using LLMs in production.

## What Is a KV Cache?

Imagine the LLM is generating some text. Concretely, suppose the LLM is given the following prompt: "Time". As you may already know, LLMs generate one word (or token) at a time, and the two following text generation steps may look as illustrated in the figure below:

The diagram illustrates how an LLM generates text one token at a time. Starting with the prompt "Time", the model generates the next token "flies." In the next step, the full sequence "Time flies" is reprocessed to generate the token "fast".

Note that there is some redundancy in the generated LLM text outputs, as highlighted in the next figure:

This figure highlights the repeated context ("Time flies") that must be reprocessed by the LLM at each generation step. Since the LLM does not cache intermediate key/value states, it re-encodes the full sequence every time a new token (e.g., "fast") is generated.

The following figure shows an excerpt of an attention mechanism computation that is at the core of an LLM. Here, the input tokens ("Time" and "flies") are encoded as 3-dimensional vectors (in reality, these vectors are much larger, but this would make it challenging to fit them into a small figure). The matrices _W_ are the weight matrices of the attention mechanism that transform these inputs into key, value, and query vectors.

The figure below shows an excerpt of the underlying attention score computation with the key and value vectors highlighted:

This figure illustrates how the LLM derives key (`k`) and value (`v`) vectors from token embeddings during attention computation. Each input token (e.g., "Time" and "flies") is projected using learned matrices `W_k` and `W_v` to obtain its corresponding key and value vectors.

As mentioned earlier, LLMs generate one word (or token) at a time. Suppose the LLM generated the word "fast" so that the prompt for the next round becomes "Time flies fast". This is illustrated in the next figure below:

This diagram shows how the LLM recomputes key and value vectors for previously seen tokens ("Time" and "flies") during each generation step. When generating the third token ("fast"), the model recomputes the same `k(1)/v(1)` and `k(2)/v(2)` vectors again, rather than reusing them. This repeated computation highlights the inefficiency of not using a KV cache during autoregressive decoding.

As we can see, based on comparing the previous 2 figures, the keys and value vectors for the first two tokens are exactly the same, and it would be wasteful to recompute them in each next-token text generation round.

Now, the idea of the KV cache is to implement a caching mechanism that stores the previously generated key and value vectors for reuse, which helps us to avoid these unnecessary recomputations.

## How LLMs Generate Text (Without and With a KV Cache)

After we went over the basic concept in the previous section, let's go into a bit more detail before we look at a concrete code implementation. If we have a text generation process _without_ KV cache for "Time flies fast", we can think of it as follows:

Notice the redundancy: tokens "Time" and "flies" are recomputed at every new generation step. The KV cache resolves this inefficiency by storing and reusing previously computed key and value vectors:

1. Initially, the model computes and caches key and value vectors for the input tokens.
2. For each new token generated, the model only computes key and value vectors for that specific token.
3. Previously computed vectors are retrieved from the cache to avoid redundant computations.

The benefits here are that `"Time"` is computed once and reused twice, and `"flies"` is computed once and reused once. (It's a short text example for simplicity, but it should be intuitive to see that the longer the text, the more we get to reuse already computed keys and values, which increases the generation speed.)

The following figure illustrates generation step 3 with and without a KV cache side by side.

Comparing text generation with and without a KV cache. In the top panel (without cache), key and value vectors are recomputed for each token step, which results in redundant operations. In the bottom panel (with cache), previously computed keys and values are retrieved from the KV cache to avoid recomputation for faster generation.

So, if we want to implement a KV cache in code, all we have to do is compute the keys and values as usual but then store them so that we can retrieve them in the next round. The next section illustrates this with a concrete code example.

## Implementing a KV Cache from Scratch

There are many ways to implement a KV cache, with the main idea being that we only compute the key and value tensors for the newly generated tokens in each generation step.

I opted for a simple one that emphasizes code readability. There are two files shared on GitHub, which are self-contained Python scripts that implement an LLM with and without KV cache from scratch:

1. gpt_ch04.py: Self-contained code taken from Chapters 3 and 4 of my _Build a Large Language Model (From Scratch)_ book to implement the LLM and run the simple text generation function
2. gpt_with_kv_cache.py: The same as above, but with the necessary changes made to implement the KV cache.

### 1. Registering the Cache Buffers

Inside the `MultiHeadAttention` constructor, we add two buffers, `cache_k` and `cache_v`, which will hold concatenated keys and values across steps:

```
self.register_buffer("cache_k", None)
self.register_buffer("cache_v", None)
```

### 2. Forward pass with `use_cache` flag

Next, we extend the `forward` method of the `MultiHeadAttention` class to accept a `use_cache` argument. When `use_cache=True`, newly computed keys/values are concatenated onto the cache and the full cached tensors are used for attention.

### 3. Clearing the Cache

When generating text, we have to remember to reset both the keys and value buffers between two separate text-generation calls. Otherwise, the queries of a new prompt will attend to stale keys left over from the previous sequence. We add a `reset_kv_cache` method to the `MultiHeadAttention` class.

### 4. Propagating `use_cache` in the Full Model

We add `self.current_pos = 0` to `GPTModel` to track how many tokens have been cached during incremental generation. With `use_cache=True`, positional IDs start at `current_pos` and advance by `seq_len` each forward pass so new queries align with stored keys/values.

### 5. Using the Cache in Generation

With caching enabled, the generation loop feeds only the new token on each decode step (`model(next_idx, use_cache=True)`) after an initial full-prompt prefill. Without caching, the full running sequence is re-fed each step.

## A Simple Performance Comparison

On a Mac Mini with M4 chip (CPU), a 124M parameter untrained GPT model generating 200 new tokens from a 4-token prompt shows ~5× speedup with KV cache vs without. Both implementations produce identical output, validating correctness.

## KV cache Advantages and Disadvantages

- **[Good] Computational efficiency increases**: Without caching, cumulative attention work scales as O(n²). With a cache, each key/value is computed once and reused, reducing per-step complexity to O(n).
- **[Bad] Memory usage increases linearly**: Each new token appends to the KV cache; long sequences and large models can make cache memory prohibitive. Truncation (e.g., sliding window) adds complexity.

## Optimizing the KV Cache Implementation

Production deployments require more than the educational `torch.cat` approach:

- **Pre-allocate memory** for keys/values up to `max_seq_len` and write into slices.
- **Sliding-window truncation** keeps only the last `window_size` tokens in cache.

An optimized reference is in `gpt_with_kv_cache_optimized.py`. On tiny models and CUDA GPUs, device-transfer overhead can dominate, erasing KV-cache gains.

## Bonus: KV Caches in Qwen3 and Llama 3

Raschka added KV caches to from-scratch Qwen3 (0.6B) and Llama 3 (1B) implementations. KV cache gives the largest speedups on CPU; `torch.compile` boosts further. On GPU, compiled models without pre-allocated KV tensors can win on small models because memory allocation and transfer dominate.
