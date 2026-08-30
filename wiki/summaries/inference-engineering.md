# Inference Engineering

**Source**: `raw/inference-engineering/Inference Engineering.pdf`  
**Ingested**: 2026-05-18  
**Tags**: #summary

## Summary

*Inference Engineering* by Philip Kiely (Baseten Books, 2026) is a comprehensive 259-page practitioner's guide to serving generative AI models in production. The book defines inference engineering as a distinct discipline spanning runtime optimization, infrastructure scaling, and developer tooling — a field that barely existed before ChatGPT's launch in November 2022 but now underpins every serious AI product.

The book systematically covers the full stack: from the mathematical foundations of neural networks and transformer architectures (Chapter 2), through GPU hardware generations from Hopper to the forthcoming Rubin (Chapter 3), the software ecosystem of CUDA, PyTorch, and inference engines like vLLM, SGLang, and TensorRT-LLM (Chapter 4), to the core optimization techniques that define the field — quantization, speculative decoding, KV cache management, model parallelism, and disaggregated serving (Chapter 5). Chapter 6 extends inference engineering to non-LLM modalities including vision-language models, embedding models, ASR, TTS, and image/video generation. Chapter 7 addresses production concerns: containerization, autoscaling, multi-cloud capacity management, and observability.

A central thesis is that the explosion of open models (2M+ on Hugging Face) — particularly after DeepSeek V3/R1 closed the intelligence gap with closed models in December 2024 — means every AI product company needs its own inference strategy. Open models offer 80%+ cost savings at scale, control over latency and availability, and the ability to fine-tune and customize. The book argues that the most impactful "optimization" is often model selection itself: choosing the smallest model that passes your evals, then applying inference engineering to serve it fast and reliably.

## Key Claims

- Inference is the most valuable category in the AI industry; inference engineering is still in its infancy but growing rapidly.
- The open-closed model gap effectively disappeared with DeepSeek V3/R1 (December 2024), and open models now match closed ones within weeks of release.
- LLM inference has two distinct bottleneck regimes: prefill is compute-bound (determines TTFT), decode is memory-bandwidth-bound (determines TPS). This duality drives all major optimizations.
- Quantization from FP16 to FP8 roughly doubles effective compute and halves memory bandwidth requirements; Blackwell GPUs introduce FP4 and microscaling formats (MXFP8, MXFP4, NVFP4) for further gains.
- EAGLE is the go-to speculative decoding algorithm for production use, offering up to 8 draft tokens per forward pass with high acceptance rates by leveraging hidden states from the target model.
- N-gram speculation outperforms EAGLE specifically for code completion tasks where output closely mirrors input syntax.
- Prefix caching can skip prefill on thousands of tokens for workloads with shared system prompts, multi-turn conversations, or repeated code context.
- Disaggregated serving (separating prefill and decode onto different GPUs) becomes worthwhile at 100M–1B+ tokens/day on models with 100B+ parameters and prefill-heavy traffic.
- Tensor Parallelism is the default strategy for multi-GPU latency optimization within a node; Expert Parallelism improves throughput for MoE models and scales better across nodes.
- Memory bandwidth is the bottleneck for LLM decode; the H200's advantage over the H100 is primarily its higher memory bandwidth (4.8 TB/s vs 3.35 TB/s).
- The B200/B300 represent the new gold standard for inference with ~5 petaFLOPS FP8 compute, 192–288 GB VRAM, and up to 8 TB/s bandwidth.
- Pipeline Parallelism is only recommended for multi-node inference and should be avoided within a single node due to poor latency and utilization.
- FlashAttention is a lossless optimization implemented in tens of thousands of lines of hand-fused CUDA code, tuned per GPU architecture (H100 vs B200 use different code).
- Production inference requires four nines of availability, which is achievable with dedicated open-model deployments but not with closed-model APIs (stuck at two nines).
- The most important decision in inference optimization is model selection — choosing the smallest model that passes your evals.

## Figures

| Figure | Caption | Page |
|--------|---------|------|
| ![Inference stack](../assets/inference-engineering/fig-0.1-inference-stack.webp) | A complete inference stack: runtime and infrastructure layers | 20 |
| ![Speculation diagram](../assets/inference-engineering/fig-0.2-speculation-diagram.webp) | Speculative decoding improving inference latency | 22 |
| ![Multi-cloud serving](../assets/inference-engineering/fig-0.3-multi-cloud-serving.webp) | Unifying capacity across multiple cloud providers | 23 |
| ![Matmul](../assets/inference-engineering/fig-2.2-matmul.webp) | Matrix Multiply: y = Wx + b | 46 |
| ![Prefill vs decode](../assets/inference-engineering/fig-2.6-autoregressive-token-gen.webp) | Autoregressive prefill and decode phases | 50 |
| ![Transformer block](../assets/inference-engineering/fig-2.7-transformer-block.webp) | Transformer block architecture | 53 |
| ![MoE architecture](../assets/inference-engineering/fig-2.9-moe-architecture.webp) | Mixture of Experts model architecture | 56 |
| ![Roofline](../assets/inference-engineering/fig-2.13-prefill-roofline.webp) | Prefill roofline model: compute vs memory bound | 66 |
| ![GPU cache hierarchy](../assets/inference-engineering/fig-3.2-gpu-sm-cache.webp) | GPU SMs, Tensor Cores, and L1/L2 cache hierarchy | 79 |
| ![NVLink topology](../assets/inference-engineering/fig-3.4-nvlink-infiniband.webp) | NVLink, NVSwitch, and InfiniBand interconnects | 87 |
| ![vLLM architecture](../assets/inference-engineering/fig-4.4-vllm-architecture.webp) | vLLM inference engine architecture | 109 |
| ![Number formats](../assets/inference-engineering/fig-5.1-number-formats.webp) | FP32, FP16, FP8, FP4 number format comparison | 125 |
| ![Speculative decoding](../assets/inference-engineering/fig-5.3-speculative-decoding.webp) | Speculative decoding: draft generation, validation, prefix acceptance | 132 |
| ![EAGLE](../assets/inference-engineering/fig-5.5-eagle-hidden-states.webp) | EAGLE takes hidden states as input, produces draft tokens | 136 |
| ![Prefix caching](../assets/inference-engineering/fig-5.7-prefix-cache-match.webp) | Prefix caching reusing KV cache across requests | 138 |
| ![Tensor parallelism](../assets/inference-engineering/fig-5.12-tensor-parallelism.webp) | Tensor Parallelism splitting weights across GPUs | 146 |
| ![Expert parallelism](../assets/inference-engineering/fig-5.13-expert-parallelism.webp) | Expert Parallelism: each expert within a single GPU | 147 |
| ![Disaggregation](../assets/inference-engineering/fig-5.16-disaggregation.webp) | Disaggregated serving: separate prefill and decode workers | 151 |
| ![Autoscaling](../assets/inference-engineering/fig-7.3-autoscaling.webp) | Autoscaling inference replicas based on load | 186 |
| ![Multi-cloud](../assets/inference-engineering/fig-7.7-multi-cloud.webp) | Multi-cloud capacity management | 195 |

## Entities

- [[Philip Kiely]] — author; VP of AI at Baseten, wrote the book based on 4 years of experience.
- [[Baseten]] — inference platform company; publisher of the book; powers inference for companies like Cursor, Clay, Gamma, and Mercor.
- [[NVIDIA]] — dominant GPU vendor; Hopper, Blackwell, and Rubin architectures are central to the book.
- [[vLLM]] — open-source inference engine; one of three primary engines covered alongside SGLang and TensorRT-LLM.
- [[FlashAttention]] — series of optimized attention kernels; key lossless optimization for compute-bound operations.
- [[DeepSeek]] — open-model lab; their V3/R1 release marked the closing of the open-closed model gap.
- [[EAGLE (Speculative Decoding)]] — purpose-built draft model trained on hidden states; the recommended speculation algorithm for production inference.
- [[Accelerating Sonar Through Speculation]] — Perplexity production draft-target and MTP schedules on FlashInfer (complements book's algorithm survey with serving details).
- [[Prefill and Decode for Concurrent Requests - Optimizing LLM Performance]] — TNG's production analysis of chunked prefill and continuous batching, a practitioner's complement to the book's engine-internals chapters.
- [[Native-Speed vLLM Transformers Modeling Backend]] — `transformers`' runtime fusion into vLLM's optimized kernels, closing the gap between reference model code and hand-tuned inference implementations.

## Questions & Gaps

- The book has a January 2026 knowledge cutoff — Blackwell software support was still maturing at time of writing; how have Blackwell-optimized kernels and engines evolved since?
- Disaggregation is presented as powerful but complex; what are the failure modes and operational costs in practice?
- The book focuses heavily on NVIDIA; how competitive are alternative accelerators (Cerebras, Groq, TPUs) in practice for production inference?
- How does inference engineering change for agentic workloads with many chained model calls vs. single-request serving?
- The interplay between reasoning models (extended thinking tokens) and inference optimization (much longer decode sequences) is not deeply explored.

## Related

- [[Model Compression and Efficiency]] — quantization, distillation, and small-model techniques covered in Ch. 1 and Ch. 5.
- [[Model Distillation]] — the book covers distillation as a model selection strategy (§1.3.3).
- [[Mixture of Experts]] — MoE architectures and Expert Parallelism are central to Ch. 2 and Ch. 5.
- [[Large Language Models]] — the book's primary subject; inference mechanics for autoregressive token generation.
- [[Understanding and Coding the KV Cache in LLMs from Scratch]] — pedagogical from-scratch PyTorch KV cache; complements Ch. 5.3 production techniques with readable `torch.cat` baseline and correctness checks.
- [[Vision Language Models]] — Ch. 6 extends inference engineering to VLMs and omni-modal models.
- [[Papers Explained 01 - Transformer]] — the foundational architecture underlying all models discussed.
- [[Papers Explained 145 - LoRA]] — LoRA fine-tuning and weight offloading are referenced for specialized inference.
- [[Papers Explained 95 - Mixtral 8x7B]] — a specific MoE model used to illustrate Expert Parallelism concepts.
- [[Papers Explained 449 - Switch Transformers]] — early MoE architecture relevant to the expert routing discussion.
- [[Papers Explained 448 - Sparsely-Gated Mixture-of-Experts Layer]] — foundational MoE paper referenced in the parallelism discussion.
- [[DiffusionGemma]] — shifts local decode from memory-bandwidth-bound (autoregressive) to compute-bound (parallel 256-token canvas denoising); complements the prefill-compute / decode-bandwidth duality in Key Claims.
- [[Two Speeds of a GPU]] — pedagogical explainer deriving arithmetic intensity and the Roofline Model, formalizing prefill compute-bound vs decode memory-bound dynamics.
- [[Arithmetic Intensity]] — ratio of FLOPs to bytes moved across memory.
- [[Roofline Model]] — performance model bounding execution time by memory bandwidth and peak compute.
