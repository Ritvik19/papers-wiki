# Hugging Face

**Type**: org
**Tags**: #entity

## Overview

Hugging Face is the open-source AI platform (Hub, `transformers`, `sentence-transformers`, `datasets`, Inference Endpoints/Providers) that hosts most of the open-weight model ecosystem and publishes the `huggingface.co/blog` technical blog used throughout this batch of ingests. Posts on the blog are written both by Hugging Face staff (integration guides, Sentence Transformers releases) and by partner labs and companies announcing models on the platform (Google, IBM, NVIDIA, JHU CLSP, etc.).

## Appearances

- [[Ettin Suite: SoTA Paired Encoders and Decoders]] — JHU CLSP encoder/decoder pair, HF blog post.
- [[Introducing the Ettin Reranker Family]] — Sentence Transformers CrossEncoder rerankers.
- [[Introducing RTEB: A New Standard for Retrieval Evaluation]] — MTEB team benchmark launch.
- [[Granite Embedding Multilingual R2]] — IBM ModernBERT-based multilingual embedding release.
- [[Build a Domain-Specific Embedding Model in Under a Day]] — NVIDIA embedding fine-tuning recipe.
- [[Papers Explained 471 - mmBERT]] — JHU CLSP multilingual encoder; the HF blog post is a cross-reference on this existing page rather than a separate summary.
- [[Papers Explained 465 - EmbeddingGemma]] — Google embedding model; the HF blog post is a cross-reference on this existing page rather than a separate summary.
- [[DeepSeek-V4: A Million-Token Context That Agents Can Actually Use]] — HF launch/technical-deep-dive post on DeepSeek's agent-focused MoE release.
- [[Welcome Llama 4 Maverick & Scout on Hugging Face]] — HF's day-one integration and architecture writeup for Meta's Llama 4.
- [[GLM-5.2: Built for Long-Horizon Tasks]] — Z.ai's own post on the HF blog announcing GLM-5.2.
- [[Granite 4.1 LLMs: How They're Built]] — IBM's technical deep-dive on the Granite 4.1 dense model family, posted on the HF blog.
- [[Granite 4.0 Nano: Just How Small Can You Go?]] — IBM's edge/on-device Granite 4.0 Nano launch, posted on the HF blog.
- [[StarCoder2 and The Stack v2]] — BigCode (co-led by Hugging Face) launch of the StarCoder2 code model family and The Stack v2 dataset.
- [[StarCoder2-Instruct: Fully Transparent and Permissive Self-Alignment for Code Generation]] — BigCode's self-aligned instruction-tuning follow-up to StarCoder2.
- [[Open-R1: A Fully Open Reproduction of DeepSeek-R1]] and its four updates ([[Open R1: Update #1]], [[Open R1: Update #2]], [[Open R1: Update #3]], [[Open R1: Update #4]]) — HF's project to reconstruct DeepSeek-R1's training data and RL pipeline in the open.
- [[Mini-R1: Reproduce Deepseek R1 "Aha Moment", a RL Tutorial]] — Philipp Schmid's GRPO/Countdown Game tutorial, cross-posted on the Open-R1 blog.
- [[Putting RL Back in RLHF]] — introduces the RLOO Trainer in TRL as a cheaper, faster alternative to PPO.
- [[Keep the Tokens Flowing: Lessons From 16 Open-Source RL Libraries]] — survey of 16 async RL libraries informing TRL's own async trainer design.
- [[OpenEnv in Practice: Evaluating Tool-Using Agents in Real-World Environments]] — joint post with Turing on the OpenEnv framework and its Calendar Gym environment.
- [[DeepMath: A Lightweight Math Reasoning Agent With Smolagents]] — Intel's GRPO-trained math agent, posted on the HF blog.
- [[Kimina-Prover: Applying Test-Time RL Search on Large Formal Reasoning Models]] and [[Kimina-Prover-RL]] — Numina/Kimi's Lean 4 theorem provers, posted on the HF blog.
- [[PipelineRL]] and [[Apriel-H1: The Surprising Key to Distilling Efficient Reasoning Models]] — ServiceNow's RL infrastructure and Mamba-hybrid distillation posts, posted on the HF blog.
- [[Profiling in PyTorch (Part 1): A Beginner's Guide to torch.profiler]], [[Profiling in PyTorch (Part 2): From nn.Linear to a Fused MLP]], and [[Profiling in PyTorch (Part 3): Attention Is All You Profile]] — three-part series teaching `torch.profiler`-driven optimization.
- [[Tricks From OpenAI gpt-oss You Can Use With Transformers]] — engineering deep-dive on the `transformers` upgrades (kernels, MXFP4, TP/EP, sliding-window cache) shipped for gpt-oss.
- [[Native-Speed vLLM Transformers Modeling Backend]] — `torch.fx`-based runtime fusion making the `transformers` vLLM backend match native throughput.
- [[Efficient MultiModal Data Pipeline]] — nanoVLM's knapsack-packing rewrite of its multimodal data loading pipeline.
- [[Beyond LoRA: Can You Beat the Most Popular Fine-Tuning Technique?]] — PEFT team benchmark suite comparing 40+ fine-tuning techniques against LoRA on equal footing.
- [[Introducing SynthID Text]] — joint post with Google DeepMind integrating SynthID Text watermarking into `transformers`.
- [[Introducing the Synthetic Data Generator - Build Datasets with Natural Language]] — no-code Argilla/`distilabel`-backed dataset generation tool.
- [[Open-Source DeepResearch - Freeing Our Search Agents]] — 24-hour open reproduction of OpenAI's Deep Research agent on the GAIA benchmark, via `smolagents`' code-agent design.
- [[Harness, Scaffold, and the AI Agent Terms Worth Getting Right]] — glossary formalizing agent/harness/scaffold/policy/rollout terminology.
- [[Differential Transformer V2]] — Microsoft Research's post on the HF Enterprise blog.
- [[AprielGuard: A Guardrail for Safety and Adversarial Robustness in Modern LLM Systems]] and [[Nemotron 3.5 Content Safety: Customizable Multimodal Safety for Global Enterprise AI]] — ServiceNow and NVIDIA safety-guardrail model posts on the HF Enterprise blog.
- [[NVIDIA Cosmos Reason 2 Brings Advanced Reasoning to Physical AI]] — NVIDIA's open reasoning VLM for physical AI, posted on the HF Enterprise blog.
- [[Data for Agents]], [[Nemotron-Personas-India: Synthesized Data for Sovereign AI]], [[NVIDIA Releases 6 Million Multi-Lingual Reasoning Dataset]] — NVIDIA Nemotron open-data posts on the HF Enterprise blog.
- [[Introducing NVIDIA Nemotron 3 Nano Omni: Long-Context Multimodal Intelligence for Documents, Audio and Video Agents]] and [[The Open Evaluation Standard: Benchmarking NVIDIA Nemotron 3 Nano with NeMo Evaluator]] — NVIDIA's omni-modal model release and its companion evaluation-reproducibility post, both on the HF Enterprise blog.
- [[State of Open Source on Hugging Face: Spring 2026]] — HF's own team retrospective on the open-source AI ecosystem's growth, geography, and sub-communities.
- [[Gemma4 Assistant Docs]] — `Gemma4AssistantForCausalLM` Transformers docs for Gemma 4 MTP speculative decoding (`assistant_model=` in `generate()`).
- [[One Year Since the "DeepSeek Moment"]], [[Architectural Choices in China's Open-Source AI Ecosystem: Building Beyond DeepSeek]], [[The Future of the Global Open-Source AI Ecosystem: From DeepSeek to AI+]] — HF's three-part retrospective series on China's open-source AI ecosystem one year after DeepSeek R1.
- [[Inkling]] — day-0 transformers / Inference Providers integration and architecture blog for Thinking Machines Lab’s open multimodal MoE; Hub weights `thinkingmachines/Inkling` and `Inkling-NVFP4`.
- [[Unsloth Model Support 2024]] — official HF blog post `unsloth-trl` documenting TRL + Unsloth integration for SFT/DPO.

## Notes

Most posts in this batch were archived from `huggingface.co/blog/<slug>` with both `full-article.html` (canonical) and `full-article.md` (readability aid) saved under `raw/<slug>/`. No figures were downloaded for this batch; benchmark tables are preserved inline as markdown instead. Two URLs in this batch (mmBERT, EmbeddingGemma) turned out to already have dedicated Papers Explained pages and were downgraded to cross-reference notes rather than full ingests, with no raw archival.

## Related

- [[Model Compression and Efficiency]]
- [[Embedding and Retrieval]]
- [[Large Language Models]]
