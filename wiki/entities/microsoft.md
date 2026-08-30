# Microsoft

**Type**: org  
**Tags**: #entity

## Overview

Microsoft Corporation is a global technology company that is a major research and engineering force in modern artificial intelligence. It is particularly renowned for its foundational contributions to distributed training systems (DeepSpeed), memory optimization frameworks (ZeRO), and high-quality small language models (Phi series).

## Appearances

- [[How to Train Really Large Models on Many GPUs?]] — Highlighted as the development organization behind **DeepSpeed** and the **ZeRO** optimization framework.
- [[Papers Explained 577: MAI-Thinking-1]] — MAI-Base-1 / MAI-Thinking-1 trillion-parameter MoE reasoning model trained from scratch.
- [[Differential Transformer V2]] — Microsoft Research's revision of Differential Attention for faster decoding (no custom kernels) and stabler large-scale pretraining.
- [[Open-Source DeepResearch - Freeing Our Search Agents]] — Magentic-One's web-browser and text-inspector tools were adapted (with minimal changes) as the toolset for Hugging Face's open GAIA-agent reproduction.
- [[Sebastien Bubeck]] — Former VP AI and Distinguished Scientist at Microsoft Research leading early research on small models and LLM reasoning.

## Notes

Microsoft's contributions span both advanced systems engineering and model architecture:
1.  **Distributed Systems**: Microsoft's DeepSpeed team designed **ZeRO (Zero Redundancy Optimizer)** to systematically eliminate memory redundancies in data-parallel training, unlocking the ability to train hundreds-of-billions parameter models on standard hardware.
2.  **Small Language Models (SLMs)**: Microsoft Research pioneered the "textbooks are all you need" paradigm with the **Phi** family- [[Papers Explained 114 - Phi-1]], [[Papers Explained 115 - Phi-1.5]], [[Papers Explained 116 - Phi-2]], [[Papers Explained 130 - Phi-3]], [[Papers Explained 192 - Phi-3.5]], [[Papers Explained 278 - Phi-4]], [[Papers Explained 322 - Phi 4 Mini, Phi 4 Multimodal]], [[Papers Explained 358 - Phi-4-Reasoning]], [[Papers Explained 359 - Phi-4-Mini-Reasoning]], [[Papers Explained 541 - Phi 4 Reasoning Vision 15B]] — Comprehensive Phi series of small, highly capable language and multimodal models.
3.  **Infrastructure & Partnerships**: Microsoft Azure serves as the backend hardware orchestrator scaling state-of-the-art foundation models through their deep partnership with OpenAI.
4.  **Unsloth Phi support**: [[Unsloth Model Support 2024]] (Phi-3) and [[Unsloth Model Support 2025]] (Phi-4) day-zero QLoRA.

## Related

- [[DeepSpeed]]
- [[ZeRO]]
- [[Sebastien Bubeck]]
- [[How to Train Really Large Models on Many GPUs?]]
- [[Papers Explained 130 - Phi-3]]
- [[Papers Explained 116 - Phi-2]]
- [[Papers Explained 358 - Phi-4-Reasoning]]
- [[Papers Explained 161 - Orca 2]]
