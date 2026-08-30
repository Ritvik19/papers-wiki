# Prefill and Decode for Concurrent Requests - Optimizing LLM Performance

**Source**: `raw/llm-performance-prefill-decode-concurrent-requests/full-article.html` (156 KB), `raw/llm-performance-prefill-decode-concurrent-requests/full-article.md`
**Ingested**: 2026-07-10
**Tags**: #summary

## Summary

The second post in a TNG Technology Consulting series on LLM serving performance, drawn from operating a self-hosted cluster of 24 H100 GPUs serving 50 applications, over 5,000 inferences per hour, and more than ten million tokens daily. The post's foundation is the prefill/decode split inherent to autoregressive generation: prefill computes the first output token by processing every prompt token in parallel (since they're all known up front), while decode computes each subsequent token sequentially, one at a time, reusing cached key/value vectors from all prior tokens. This gives prefill a much higher per-token compute cost overall but a lower per-input-token cost than decode's per-output-token cost (the basis for commercial APIs charging less for input than output tokens), and explains the two headline latency metrics: time to first token (prefill latency) and time per output token (a single decode step's latency), against which typical interactive targets are 100-300ms per output token and 3 seconds or less to first token.

Resource-utilization patterns follow directly from this split: prefill is GPU compute-intensive (a single long prompt can already saturate the GPU), while a single decode step is memory-bandwidth-limited and lightly loaded, needing batching across many concurrent requests to reach good utilization. Plotting throughput against concurrency shows a roughly linear increase at low concurrency (memory-bound, benefits from bigger batches) that plateaus once GPU compute saturates, with the plateau point shifting based on prompt length (shorter prompts need more concurrent requests to saturate compute).

The post's core argument concerns how inference engines schedule prefill and decode work when requests arrive at different times. Static batching (fill a batch, run it to completion, then start the next) wastes GPU cycles on both ends: prefill saturates compute regardless, decode underutilizes, and the biggest cost is a potentially very long time to first token, since a new request cannot start until every request in the current batch (including the longest) finishes. Continuous batching, used by engines like vLLM and TGI, instead swaps a finished request out for a new one immediately, but this creates a scheduling choice at the point a new request arrives: prefill-first scheduling runs the new request's full prefill (a single GPU operation) in parallel with just one decode step for every already-running request, minimizing time to first token for the new request but pausing already-streaming users' token generation for the prefill's full duration, an effect visible to end users as a stutter when someone else submits a long prompt. Chunked prefill instead splits a new prompt's prefill into multiple smaller chunks, interleaving one decode step per chunk rather than one decode step per entire prefill; this trades a small increase in average time to first token (chunking overhead) for a much smaller per-step slowdown to in-flight decodes, with chunk size (typically 512-8192 tokens; vLLM's original default was 512) as the tuning knob balancing the two metrics. TNG reports chunked prefill increased total token throughput by +50% on their standard vLLM deployment with evenly sized requests, and now enables it as the default strategy for every self-hosted deployment, while acknowledging chunk-size tuning is hard under unpredictable real-world load, so they stick with framework defaults. The post ends by flagging two further scheduling challenges that chunked prefill introduces, to be addressed in the series' next installment.

## Key Claims

- Prefill is GPU compute-bound (parallel over all prompt tokens); a single decode step is memory-bandwidth-bound and needs batching across requests to use the GPU efficiently.
- Typical interactive latency targets: 100-300ms per output token (3-10 tokens/sec) and 3 seconds or less time to first token.
- Static batching's main cost is a potentially very long time to first token, since a new request can't start until the entire current batch (including its longest member) finishes.
- Prefill-first continuous batching (vLLM, TGI default behavior) minimizes time to first token for new requests but pauses in-flight decode generation for the full duration of any new prefill.
- Chunked prefill interleaves prefill chunks with decode steps, trading a small time-to-first-token increase for a much smaller per-step slowdown to in-flight decode, with chunk size (512-8192 tokens typical) as the tuning knob.
- TNG measured +50% total token throughput from enabling chunked prefill on a standard vLLM deployment with evenly sized requests, and made it the default for all self-hosted LLM deployments.

## Figures

No figures were extracted for this ingest; the throughput-vs-concurrency saturation chart (vLLM, Llama-3.1-8B, H100, varying prompt lengths) and the prefill-first vs. chunked-prefill timeline diagrams are described inline but not downloaded, per this batch's no-figure-download policy.

## Entities

- [[TNG Technology Consulting]] — writes the post from its own production LLM-serving cluster.

## Questions & Gaps

- The post explicitly defers "two further challenges" of concurrent chunked-prefill processing to the next article in TNG's series, not detailed here.
- No guidance is given on how to choose a chunk size for unpredictable, bursty production load beyond noting that TNG relies on framework defaults rather than manual tuning.

## Related

- [[Tricks From OpenAI gpt-oss You Can Use With Transformers]] — covers `transformers`' own native continuous-batching API as a related but non-production-focused alternative.
- [[Native-Speed vLLM Transformers Modeling Backend]] — related vLLM performance post from Hugging Face.
- [[KV Cache]]
