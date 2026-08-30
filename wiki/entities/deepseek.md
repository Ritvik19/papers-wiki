# DeepSeek

**Type**: org  
**Tags**: #entity

## Overview

DeepSeek is an artificial intelligence research company and organization focused on building advanced open-source foundation models. The company is recognized for its major contributions to reinforcement learning post-training, Mixture-of-Experts (MoE) architectures, and inference optimization. Among its notable innovations are the Group Relative Policy Optimization (GRPO) training method, Multi-head Latent Attention (MLA), and highly competitive model families like DeepSeek-V (dense and MoE) and DeepSeek-R1 (reasoning).

## Appearances

- [[GRPO++: Tricks for Making RL Actually Work]] — pioneer of the Group Relative Policy Optimization (GRPO) algorithm, which serves as the core RL training engine for DeepSeek-R1.
- [[Reward Hacking in Reinforcement Learning]] — discussion of DeepSeek post-training, reasoning models, and alignment paradigms.
- [[Papers Explained - Composer 2]] — DeepSeek V3.2 is evaluated as a base candidate alongside GLM-5 and Kimi K2.5 for Cursor's Composer coding agent.
- [[DeepSeek-V4: A Million-Token Context That Agents Can Actually Use]] — V4-Pro (1.6T/49B active) and V4-Flash (284B/13B active); Compressed/Heavily Compressed Sparse Attention (CSA/HCA) hybrid, 1M context at ~2% the KV cache of standard GQA, agent-focused post-training (interleaved thinking across tool calls, DSML tool schema, DSec RL sandbox).
- [[Open-R1: A Fully Open Reproduction of DeepSeek-R1]] and its four updates ([[Open R1: Update #1]] through [[Open R1: Update #4]]) — Hugging Face's project reconstructing DeepSeek-R1's training data and RL pipeline; Update #4 covers the DeepSeek-V3-0324 base-model refresh.
- [[Mini-R1: Reproduce Deepseek R1 "Aha Moment", a RL Tutorial]] — small-scale GRPO reproduction of DeepSeek-R1's self-reflective "aha moment" behavior on the Countdown Game.
- [[Keep the Tokens Flowing: Lessons From 16 Open-Source RL Libraries]] — DeepSeek-V3.2's production RL experience surfaces MoE expert-routing and sampling-mask training-inference mismatches ("Keep Routing", "Keep Sampling Mask") that no surveyed async RL library yet implements.
- [[One Year Since the "DeepSeek Moment"]], [[Architectural Choices in China's Open-Source AI Ecosystem: Building Beyond DeepSeek]], [[The Future of the Global Open-Source AI Ecosystem: From DeepSeek to AI+]] — Hugging Face's three-part retrospective on China's open-source AI ecosystem in the year since R1's release; covers R1's adoption barriers, MoE/domestic-hardware architectural convergence across Chinese labs, and DeepSeek's standing as the most-followed org on the Hub.
- [[State of Open Source on Hugging Face: Spring 2026]] — R1 cited as the model that displaced Meta's Llama family atop the Hub's most-liked-models ranking over the past year.
- [[Inkling]] — MoE design (256 routed + 2 shared experts, top-6, aux-loss-free load balancing) largely follows the DeepSeek-V3 recipe.
- [[Unsloth Model Support 2025]] — day-zero DeepSeek R1/V3 GRPO, dynamic 1.58-bit quant, and MoE QLoRA.
- [[Unsloth Model Support 2026]] — DeepSeek V4 local run and fine-tune guide.

## Notes

- DeepSeek MoE architectures (like DeepSeekMoE) leverage fine-grained experts with specialized routing, reducing active parameter count while scaling capacity.
- DeepSeek's pioneering of GRPO (eliminating the value model / critic network in RL training by estimating advantages within a sample group) has become the default RL paradigm for training modern reasoning models.

## Related

- [[GRPO]]
- [[GRPO++: Tricks for Making RL Actually Work]]
- [[Reward Hacking in Reinforcement Learning]]
- [[DeepSeek Sparse Attention]]
- [[Mixture of Experts]]
- [[Large Language Models]]
- [[Reasoning Models]]
- [[Long Context]]
