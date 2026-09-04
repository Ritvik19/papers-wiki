# DeepMind

**Type**: org  
**Tags**: #entity

## Overview

Google DeepMind (formerly Google DeepMind and Google Brain) is a leading artificial intelligence research laboratory. It is renowned for breakthroughs in reinforcement learning (AlphaGo, DQN), structural biology (AlphaFold), and key representation learning frameworks. From Nov 2025 through Jun 2026 it shipped the Gemini 3 model family, Gemma 4 open weights, and Nano Banana image models documented in this batch.

## Appearances

### Gemma 3n (Jun 2025)

- [[Gemma 3n fully available in the open-source ecosystem!]] — natively multimodal (image/text/audio/video) on-device Gemma variant with MatFormer nested sub-models and Per-Layer Embeddings; predates the Gemini 3 era below.

### Gemini 3 era (Nov 2025 – Jul 2026)

- [[Gemini 3]] — Nov 2025 flagship launch: Gemini 3 Pro, Deep Think, Antigravity, generative UI, 1M context.
- [[Gemini 3 Flash]] — Dec 2025 Flash tier: frontier speed at $0.50/$3 per M tokens; SWE-bench 78%.
- [[Gemini Deep Research]] — Dec 2025 autonomous research agent via Interactions API; DeepSearchQA benchmark.
- [[Agentic Vision in Gemini 3 Flash]] — Jan 2026 Think-Act-Observe vision loop with code execution.
- [[Gemini 3 Deep Think]] — Feb 2026 science update: 84.6% ARC-AGI-2, 48.4% HLE.
- [[Gemini 3.1 Pro]] — Feb 2026 reasoning upgrade: 77.1% ARC-AGI-2.
- [[Gemini 3.1 Flash Lite]] — Mar 2026 cost tier: $0.25/$1.50 per M tokens.
- [[Gemini 3.1 Flash Live]] — Mar 2026 real-time voice: ComplexFuncBench 90.8%.
- [[Gemini 3.1 Flash TTS]] — Apr 2026 TTS: 70+ languages, Elo 1211 on TTS Arena.
- [[Gemini 3.5 Flash]] — May 2026 I/O agentic/coding Flash; Terminal-Bench 2.1 76.2%.
- [[Introducing Gemini 3.6 Flash, 3.5 Flash-Lite, and 3.5 Flash Cyber]] — Jul 2026: 3.6 Flash workhorse, 3.5 Flash-Lite throughput tier, 3.5 Flash Cyber in CodeMender; Gemini 4 pre-training started.
- [[Gemini 3.7 Flash]] — Aug 2026 workhorse: DeepSWE 65.3%, FrontierCode 43.6%; Spark update; $0.75/$3.75 intro pricing.
- [[Gemini 3.8 Flash and 3.8 Flash Cyber]] — Sep 2026: third Flash in six weeks; HLE-Verified 54.9%; 3.8 Flash Cyber via [[Fairwind Program]].
- [[Gemini Omni Flash]] — May 2026 I/O omni-modal video generation from any input.
- [[Nano Banana Pro]] — Nov/Dec 2025 Gemini 3 Pro Image generation and editing.
- [[How Nano Banana Got Its Name]] — Jan 2026 origin of the Nano Banana codename.
- [[Nano Banana 2]] — Feb 2026 Gemini 3.1 Flash Image at Flash speed.
- [[Gemma 4]] — Apr 2026 open models on Gemini 3 stack; 140+ languages, vision+audio.
- [[Gemma 4 Multi-Token Prediction]] — May 2026 MTP drafters for speculative decoding.
- [[Gemma 4 12B]] — Jun 2026 encoder-free multimodal 12B for laptop deployment.
- [[Gemma 4 QAT]] — Jun 2026 quantization-aware training checkpoints for edge GPUs.
- [[DiffusionGemma]] — Jun 2026 experimental open text-diffusion MoE on Gemma 4 backbone; 4× local GPU decode via 256-token parallel canvas.
- [[T5Gemma 2]] — Dec 2025 encoder-decoder from Gemma 3; multimodal, 128K context.
- [[FunctionGemma]] — Dec 2025 Gemma 3 270M function-calling model for edge agents.
- [[TranslateGemma]] — Jan 2026 open translation models distilling Gemini.
- [[A Framework for Frontier AI and the Dawning of a New Age]] — Jul 2026: CEO Demis Hassabis proposes a FINRA-style public-private Standards Body for frontier AI testing, pre-release review, and coordinated development slowdowns.
- [[Implications of Large-Scale Test-Time Compute]] — Jun 2026: [[Noam Brown]] analyzes the safety governance of [[Gemini 3 Deep Think]] as a case study for runtime model scaffolding and test-time compute evaluation.
- [[Introducing SynthID Text]] — Oct 2024 text-watermarking technique (tournament sampling over a pseudo-random g-function), integrated into `transformers` v4.46.0 jointly with Hugging Face; predates the Gemini 3 era but underlies later SynthID applications across Gemini image/voice/TTS outputs.

### Earlier corpus

- [[Asynchronous Advantage Actor-Critic]] — Released A3C (2016): parallel asynchronous actor-critic workers with a global shared network.
- [[Self-Supervised Representation Learning]] — Developed CPC/InfoNCE bounds and key robotic state-representation architectures like TCN, Grasp2Vec, and RIG.

## Technical highlights in Weng series

- **Contrastive Predictive Coding (CPC)**: Proposed a general self-supervised framework to extract representations from high-dimensional sequence data by predicting future latents using the InfoNCE objective.
- **Time-Contrastive Networks (TCN)**: Multi-camera state representation learning leveraging synchronized multi-view sequence alignment.
- **Grasp2Vec & RIG**: Unsupervised visual representation and goal-conditioned robotic control frameworks.

## Related

- [[Google DeepMind]] — current branding for the merged Google Brain + DeepMind laboratory.
- [[Demis Hassabis]] — CEO and co-founder.
- [[Gemini 3 Deep Think]] — parallel reasoning mode.
- [[Implications of Large-Scale Test-Time Compute]] — test-time compute safety analysis of Deep Think.
- [[Standards Body for Frontier AI]]
- [[Contrastive Predictive Coding]]
- [[Time-Contrastive Networks]]
- [[Reinforcement Learning with Imagined Goals]]
- [[Self-Supervised Representation Learning]]
- [[Contrastive Learning]]
