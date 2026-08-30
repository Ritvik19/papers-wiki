Source URL: https://huggingface.co/blog/tngtech/llm-performance-prefill-decode-concurrent-requests
Title: Prefill and Decode for Concurrent Requests - Optimizing LLM Performance

# Prefill and Decode for Concurrent Requests - Optimizing LLM Performance

Team Article. Published April 16, 2025

Benjamin Merkel (TNG Technology Consulting)

Handling load from multiple users in parallel is crucial for the performance of LLM applications. In a previous part of this series on LLM performance, TNG discussed queueing strategies for prioritizing different users. This second part focuses on the concurrent processing of requests, and how it impacts latency, throughput, and GPU resource utilization. At TNG, the team self-hosts numerous LLMs on a cluster of 24 H100 GPUs, supporting 50 different applications, handling over 5,000 inferences per hour, and generating more than ten million tokens every day.

## The Two Stages of Token Generation: Prefill and Decode

Most LLMs generate text token by token in an auto-regressive manner: every new token is computed from all preceding tokens. Computing a new token requires key, value, and query vectors for each preceding token, but results from prior tokens can be reused via the key-value (KV) cache, so only one new set of key/value vectors needs to be added per output token. For the very first output token, the KV cache starts empty and all input-prompt tokens' key/value vectors must be computed, but since all input tokens are known from the start, this can be parallelized. This motivates the distinction between the prefill phase (computing the first output token, parallel over prompt tokens) and the decode phase (computing any later output token, sequential per token).

## Metrics

Two key metrics reflect the prefill/decode distinction: time to first token (the prefill phase's latency) and time per output token (a single decode step's latency). Even though prefill also produces only one token, it takes much longer than a single decode step because it must process every input token; conversely, prefill is much faster per input token than decode is per output token (which is why commercial LLM APIs charge input tokens at a lower rate than output tokens). Typical interactive-application latency targets are 100-300ms per output token (3-10 tokens/second) and a time to first token of 3 seconds or less; both can be challenging depending on model size, hardware, prompt length, and concurrent load. Non-interactive use cases (e.g. batch translation, repository summarization) instead care about total token throughput (tokens/second summed across all concurrent requests). There is generally a trade-off between maximizing total throughput and minimizing per-request latency.

## Resource Utilization

The prefill phase is very GPU compute-intensive due to parallelized computation across all input tokens. The decode step for a single output token uses very little computational power and is typically memory-bandwidth-limited (loading weights and activations, including KV vectors). Token throughput can be increased until GPU compute utilization saturates: in prefill, even a single long-prompt request can saturate the GPU; in decode, GPU utilization is increased via batching multiple requests. As a result, plotting token throughput against concurrent request count shows an almost linear increase at low concurrency (memory-bound regime benefiting from larger batch sizes), then a plateau once the GPU becomes compute-bound. (Measured for vLLM with Llama-3.1-8B on an H100, at 3000/1500 input tokens and 100 output tokens: shorter prompts mean lower prefill compute utilization, so throughput saturates at a higher request rate.)

## Concurrent Processing

Both prefill and decode phases can use batching to apply the same operations to different requests, but running prefill and decode of different requests simultaneously has consequences worth examining.

### Static Batching vs. Continuous Batching

Static batching is the most naive approach: start with an empty batch, fill it with as many waiting items as fit, process the batch until all items finish, then repeat with a new empty batch. All requests in a batch start prefill simultaneously (since prefill is a single, heavily parallelized matrix multiplication, all concurrent prefills finish together), then all decode phases start simultaneously; shorter requests finish earlier but the next waiting request cannot start until the entire batch (including the longest request) finishes. This optimizes time per output token (uninterrupted decode) at the cost of very inefficient resource utilization: prefill saturates compute regardless of parallel handling, while decode tends to underutilize the GPU, and the biggest disadvantage is a potentially long time to first token, since even short finished requests don't let a new queued request start its prefill until the longest decode in the batch completes. Because of this, inference engines typically implement continuous batching, where any completed request is immediately removed from the batch and replaced by the next queued request; every continuous batching strategy therefore has to manage concurrency between prefill and decode phases.

### Prefill-First

Inference engines such as vLLM and TGI schedule new requests' prefill as soon as they arrive and fit in the batch, running it in parallel with a single decode step for each already-running request; since this is one GPU operation dominated by prefill's duration, in-flight decodes only advance by a single output token during that time. This minimizes time to first token but interrupts the decode phase of already-running requests; in a chat application, users can experience this as the streamed token generation pausing when other users submit long prompts.

### Chunked Prefill

Chunked prefill distributes the prompt across multiple prefill chunks instead of processing it all at once, allowing as many concurrent decode steps during prefill as there are chunks (rather than only one decode step for the entire prefill). Each chunked prefill step still takes longer than an isolated decode step, but for small chunk sizes users experience only a slowdown rather than a full pause, reducing average time per output token at a small cost to time to first token (due to chunking overhead). Chunk size becomes a tuning knob for prioritizing either metric; typical chunk sizes range 512-8192 tokens (vLLM's default was 512 when chunked prefill was first implemented, later raised).

The biggest advantage of chunked prefill is that it maximizes resource efficiency: since prefill is compute-intensive and decode is memory-bound, running both in parallel increases overall throughput without being limited by either resource alone, though maximum efficiency depends on chunk size, which in turn depends on the load pattern. In a standard vLLM deployment with evenly sized requests, TNG observed chunked prefill increasing total token throughput by +50%; it is now enabled for every vLLM deployment of TNG's self-hosted LLMs, and TNG considers it a good default strategy for most use cases (though tuning chunk size is difficult under unpredictable load, so TNG sticks with defaults). Regardless of exact chunk size configuration, concurrent processing with chunked prefill comes with two further challenges to be addressed in the next article in the series.
