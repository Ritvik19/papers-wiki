# Speculative Decoding

**Type**: concept  
**Tags**: #concept

## Overview

Speculative decoding is an inference optimization technique that generates and validates multiple draft tokens per forward pass, reducing the total number of expensive forward passes needed to produce a complete output sequence. It trades spare compute cycles for higher tokens-per-second during the memory-bandwidth-bound decode phase.

## Mechanism

During standard autoregressive decoding, each forward pass produces exactly one token. Speculative decoding introduces a lightweight draft mechanism that proposes multiple candidate tokens, which the target model then verifies in a single batched forward pass. Accepted draft tokens are output immediately; rejected tokens trigger normal decoding from the rejection point.

Three factors govern effectiveness:
1. **Draft model overhead** — compute and memory cost of generating draft tokens.
2. **Draft sequence length** — number of draft tokens per forward pass (typically 4–8).
3. **Token acceptance rate** — percentage of draft tokens validated by the target model; decays deeper in the sequence.

Higher temperatures and unpredictable subject matter reduce acceptance rates. Speculative decoding is most useful at low batch sizes where spare compute cycles exist; at high batch sizes it must be dynamically disabled.

## Variants

- **Draft-target** — uses a separate small model (typically 10x smaller) as the draft model; simplest to set up but highest overhead.
- **Medusa** — grafts 2–4 additional decoder heads onto the target model via fine-tuning; inspired EAGLE but limited in draft length.
- **EAGLE** — purpose-built draft model trained on hidden states from early, middle, and late target model layers; generates up to 8 draft tokens with high acceptance; the go-to algorithm for production inference.
- **Gemma 4 MTP** — coupled 4-layer drafter that cross-attends the target KV cache with **no independent draft KV**; shared embeddings and target-activation reuse; clustered LM head on edge sizes ([[Gemma 4 MTP Overview]], [[Gemma4 Assistant Docs]]).
- **N-gram speculation** — constructs a dictionary of observed token sequences during prefill; no draft model needed; excels at code completion where output mirrors input syntax.
- **Lookahead Decoding** — generates n-grams during inference to fill the dictionary; more general than n-gram speculation but requires extra compute.

## Appearances

- [[Accelerating Sonar Through Speculation]] — Perplexity production draft-target (Llama-1B), EAGLE exploration, and MTP single-token schedules on FlashInfer; tree EAGLE not deployed due to attention-mask overhead.
- [[Gemma 4 Multi-Token Prediction]] — Google MTP drafters for Gemma 4; shared KV cache; up to 3× speedup with zero quality degradation.
- [[Papers Explained 586: Gemma 4]] — 4-layer autoregressive MTP drafters with clustered vocab projection heads for E2B/E4B edge models.
- [[Inference Engineering]] — Chapter 5.2 provides a systematic comparison of all speculation algorithms with production deployment guidance.
- [[Inkling]] — open-weights multimodal MoE released with MTP drafter layers for speculative decoding.

## Notes

EAGLE can be attached to the same PyTorch module as the target model, eliminating the CPU round-trips needed to orchestrate separate draft-target models. Adopting EAGLE for improved latency requires reduced batch sizes, lowering throughput and increasing cost — a fundamental tradeoff in speculation.

**Gemma 4 MTP vs EAGLE/Medusa:** Gemma 4's drafter does not build its own KV cache over drafted tokens—it cross-attends the target's already-computed KV with constant `position_ids` and tracks the draft trajectory only via projected activations between steps ([[Gemma4 Assistant Docs]], [[Gemma 4 MTP Explained in 5 Minutes]]). This eliminates drafter prefill entirely. MoE targets (26B-A4B) may see limited speedup at batch size 1 because different drafted tokens can route to different experts ([[Gemma 4 MTP Overview]]).

## Related

- [[Multi-Token Prediction]]
- [[FlashInfer]]
- [[Sonar]]
- [[EAGLE (Speculative Decoding)]]
- [[Inference Engineering]]
- [[Large Language Models]]
- [[Model Compression and Efficiency]]
- [[Introducing Command A+]] — Cohere reports MoE-optimized speculative decoding yielding 1.5–1.6× speedup on Command A+ text and multimodal generation.
