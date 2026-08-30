# Reinforcement Learning from Human Feedback

**Source**: `raw/reinforcement-learning-from-human-feedback/Reinforcement Learning from Human Feedback.pdf`  
**Book**: [arXiv 2504.12501](https://arxiv.org/abs/2504.12501) · [rlhfbook.com](https://rlhfbook.com)  
**Author**: Nathan Lambert  
**Ingested**: 2026-05-19  
**Tags**: #summary

## Summary

Nathan Lambert's *Reinforcement Learning from Human Feedback* is a 229-page open textbook (May 2026) that treats RLHF as the central method for preference-driven post-training of language models, while situating it inside the broader pipeline of instruction tuning, preference optimization, and [[Reinforcement Learning with Verifiable Rewards]] (RLVR). The book's stated goal is to make industrial post-training practice legible: why ChatGPT-era RLHF drew so much attention, what it actually changes in model behavior, and how modern recipes (InstructGPT, Tülu 3, DeepSeek R1) combine SFT, reward modeling, rejection sampling, RL optimizers, and direct-alignment algorithms.

The canonical RLHF pipeline has three steps: (1) instruction / supervised fine-tuning so the model can follow prompts, (2) training a Bradley–Terry-style reward model on human preference pairs, and (3) optimizing the policy with an RL method (PPO, GRPO, etc.) that scores on-policy generations against that reward model. Lambert argues RLHF's distinctive value is less about raw capability gains than about **style and subtle preference**: tone, format, helpfulness, harmlessness, and response-level contrastive learning that generalizes better across domains than per-token SFT alone. The book contrasts base-model completion behavior (verbose, web-metadata continuations) with post-trained models that answer concisely and in user-facing chat format.

Beyond the core loop, the book covers reward-model variants (outcome vs. process reward models, generative judges), policy-gradient implementations (REINFORCE, RLOO, PPO, [[GRPO]], GSPO, CISPO), **direct-alignment algorithms** ([[Direct Preference Optimization]] and relatives), rejection sampling, preference-data collection interfaces, synthetic-data distillation paths toward on-policy distillation, tool-use post-training, over-optimization and reward hacking, KL and implicit regularization ("SFT memorizes, RL generalizes"), evaluation pitfalls, and product-facing character training. A full chapter on RLVR connects verifier-reward training for reasoning to the same post-training stack that RLHF popularized.

## Key Claims

- RLHF solves **hard-to-specify objectives** by optimizing from coarse preference signals rather than hand-written reward functions.
- Modern post-training has **three optimization layers**: instruction tuning (IFT/SFT), preference fine-tuning (RLHF and DAAs), and RLVR on verifiable domains.
- RLHF optimizes at the **completion level** with contrastive feedback; SFT optimizes **per-token imitation** on fixed demonstrations — different inductive biases with different failure modes.
- Reward models are **proxy objectives**; without regularization (especially KL to a reference policy), RLHF runs risk **over-optimization** where training reward rises but downstream quality plateaus or degrades.
- **Rejection sampling** is a practical middle ground: generate many completions, filter by reward, fine-tune on winners — often cheaper and more stable than full RL.
- **DPO and other DAAs** reparameterize the RLHF objective to avoid an explicit RL loop, but trade-offs around online data, numerical stability, and synthetic preferences remain active research areas.
- **GRPO** and related group-relative methods remove the critic network, making RL cheaper at scale for reasoning-style training; the book documents PPO → GRPO → GSPO/CISPO as an evolving implementation stack.
- **RLVR** (verifiable rewards for math, code, instruction-following constraints) is the newest post-training stage and complements preference-based RLHF rather than replacing it.
- Lambert cites evidence that **online/on-policy RL forgets less** than offline SFT on new tasks because KL-regularized RL biases toward policies close to the base model ("RL's razor").
- External benchmark leaderboards **saturate quickly**; internal eval loops and contamination control matter more than public score chasing for real model improvement.

## Figures

| Figure | Caption | Page |
|--------|---------|------|
| ![fig-1](../assets/reinforcement-learning-from-human-feedback/fig-1.png) | Early three-stage RLHF pipeline: SFT, reward model, then optimization. | 7 |
| ![fig-2](../assets/reinforcement-learning-from-human-feedback/fig-2.png) | Timeline of RLHF-related research from origins through the ChatGPT era. | 18 |
| ![fig-3](../assets/reinforcement-learning-from-human-feedback/fig-3.png) | Core RLHF loop from Christiano et al. (2017): learned reward predictor in the RL loop. | 19 |
| ![fig-4](../assets/reinforcement-learning-from-human-feedback/fig-4.png) | Standard RL agent–environment loop. | 22 |
| ![fig-5](../assets/reinforcement-learning-from-human-feedback/fig-5.png) | Thermostat control as an intuitive RL example. | 22 |
| ![fig-6](../assets/reinforcement-learning-from-human-feedback/fig-6.png) | CartPole as a classic RL benchmark illustration. | 23 |
| ![fig-7](../assets/reinforcement-learning-from-human-feedback/fig-7.png) | Standard RLHF loop with policy, reward model, and reference model. | 26 |
| ![fig-8](../assets/reinforcement-learning-from-human-feedback/fig-8.png) | Early three-stage RLHF process (duplicate of fig-1 context). | 28 |
| ![fig-9](../assets/reinforcement-learning-from-human-feedback/fig-9.png) | Tülu 3 multi-stage post-training recipe overview. | 29 |
| ![fig-10](../assets/reinforcement-learning-from-human-feedback/fig-10.png) | Detailed Tülu 3 training stages and model versions. | 29 |
| ![fig-11](../assets/reinforcement-learning-from-human-feedback/fig-11.png) | Reward model as a learnable environment returning preference-based rewards. | 37 |
| ![fig-12](../assets/reinforcement-learning-from-human-feedback/fig-12.png) | Bradley–Terry preference loss equivalence formulations. | 39 |
| ![fig-13](../assets/reinforcement-learning-from-human-feedback/fig-13.png) | Outcome reward model token-level scoring intuition. | 44 |
| ![fig-14](../assets/reinforcement-learning-from-human-feedback/fig-14.png) | ORM training with masked binary cross-entropy on token logits. | 44 |
| ![fig-15](../assets/reinforcement-learning-from-human-feedback/fig-15.png) | Process reward models scoring chain-of-thought steps. | 45 |
| ![fig-16](../assets/reinforcement-learning-from-human-feedback/fig-16.png) | RLHF training loop: policy generates, reward model scores, KL anchors to initial policy. | 52 |
| ![fig-17](../assets/reinforcement-learning-from-human-feedback/fig-17.png) | REINFORCE policy-gradient with baseline advantage. | 58 |
| ![fig-18](../assets/reinforcement-learning-from-human-feedback/fig-18.png) | REINFORCE Leave-One-Out (RLOO) multi-sample baseline architecture. | 60 |
| ![fig-19](../assets/reinforcement-learning-from-human-feedback/fig-19.png) | PPO clipped surrogate objective over token log-probability ratios. | 61 |
| ![fig-20](../assets/reinforcement-learning-from-human-feedback/fig-20.png) | PPO clipping behavior for positive and negative advantages. | 62 |
| ![fig-21](../assets/reinforcement-learning-from-human-feedback/fig-21.png) | Value-function training for PPO advantage estimation. | 65 |
| ![fig-22](../assets/reinforcement-learning-from-human-feedback/fig-22.png) | GRPO architecture with group-relative advantage normalization. | 67 |
| ![fig-23](../assets/reinforcement-learning-from-human-feedback/fig-23.png) | Asynchronous / distributed RL system with actor–learner queues. | 78 |
| ![fig-24](../assets/reinforcement-learning-from-human-feedback/fig-24.png) | Example distributed RL system using Ray-style synchronization. | 79 |
| ![fig-25](../assets/reinforcement-learning-from-human-feedback/fig-25.png) | RLVR role in reasoning post-training with verifiable checkers. | 91 |
| ![fig-26](../assets/reinforcement-learning-from-human-feedback/fig-26.jpeg) | DPO as closed-form solution to the KL-constrained RLHF objective. | 103 |
| ![fig-27](../assets/reinforcement-learning-from-human-feedback/fig-27.png) | Preference displacement: DPO vs discriminator-guided DPO (D2PO). | 109 |
| ![fig-28](../assets/reinforcement-learning-from-human-feedback/fig-28.png) | Rejection sampling overview: generate, score, filter, fine-tune. | 113 |
| ![fig-29](../assets/reinforcement-learning-from-human-feedback/fig-29.png) | Timeline integrating subfields into modern RLHF. | 120 |
| ![fig-30](../assets/reinforcement-learning-from-human-feedback/fig-30.png) | Early Anthropic preference-collection interface (Bai et al. 2022). | 126 |
| ![fig-31](../assets/reinforcement-learning-from-human-feedback/fig-31.png) | Arena-style pairwise preference interface. | 127 |
| ![fig-32](../assets/reinforcement-learning-from-human-feedback/fig-32.png) | Early ChatGPT Arena preference UI example. | 128 |
| ![fig-33](../assets/reinforcement-learning-from-human-feedback/fig-33.png) | Allen AI up/down arrow preference interface. | 129 |
| ![fig-34](../assets/reinforcement-learning-from-human-feedback/fig-34.png) | Text-to-image preference collection UI. | 130 |
| ![fig-35](../assets/reinforcement-learning-from-human-feedback/fig-35.png) | Preference data sourcing and pipeline integration considerations. | 134 |
| ![fig-36](../assets/reinforcement-learning-from-human-feedback/fig-36.png) | Synthetic data scale growth in fine-tuning datasets. | 138 |
| ![fig-37](../assets/reinforcement-learning-from-human-feedback/fig-37.png) | Distillation as a post-training data engine across stages. | 139 |
| ![fig-38](../assets/reinforcement-learning-from-human-feedback/fig-38.png) | Sketch of RL over-optimization: healthy training reward vs flat downstream eval. | 160 |
| ![fig-39](../assets/reinforcement-learning-from-human-feedback/fig-39.png) | Train vs test reward-model divergence under over-optimization (Bai et al. 2022). | 164 |
| ![fig-40](../assets/reinforcement-learning-from-human-feedback/fig-40.png) | Over-optimization qualitative patterns. | 164 |
| ![fig-41](../assets/reinforcement-learning-from-human-feedback/fig-41.png) | SFT vs RL objective: forward KL vs reverse KL perspectives. | 171 |
| ![fig-42](../assets/reinforcement-learning-from-human-feedback/fig-42.png) | KL-minimal RL solutions retain more base-model capability (forgetting mitigation). | 173 |
| ![fig-43](../assets/reinforcement-learning-from-human-feedback/fig-43.png) | Epoch AI plot of benchmark saturation over time. | 181 |
| ![fig-44](../assets/reinforcement-learning-from-human-feedback/fig-44.png) | Persona vector extraction and intervention pipeline. | 188 |
| ![fig-45](../assets/reinforcement-learning-from-human-feedback/fig-45.png) | Assistant axis in persona-vector PCA space. | 190 |
| ![fig-46](../assets/reinforcement-learning-from-human-feedback/fig-46.png) | Discussion figure on PPO vs capability trade-offs in DPO-era training. | 225 |

The early pipeline ![three-stage RLHF](../assets/reinforcement-learning-from-human-feedback/fig-1.png) and modern Tülu-scale recipe ![Tülu 3 stages](../assets/reinforcement-learning-from-human-feedback/fig-10.png) bracket how post-training grew from three clean stages into many iterative model versions. The GRPO diagram ![GRPO architecture](../assets/reinforcement-learning-from-human-feedback/fig-22.png) is the book's reference implementation for critic-free group-relative RL now standard in reasoning training.

## Entities

- [[Nathan Lambert]] — author; RLHF researcher and educator behind rlhfbook.com and this textbook.
- [[GRPO]] — group-relative policy optimization covered in depth with PPO/RLOO comparisons and implementation notes.
- [[Direct Preference Optimization]] — DPO chapter derives the closed-form preference objective and discusses weaknesses/alternatives.
- [[Reinforcement Learning with Verifiable Rewards]] — RLVR chapter on reasoning models, verifiable checkers, and inference-time scaling.
- [[Supervised Fine-Tuning]] — instruction-tuning foundation stage before preference optimization.
- [[KL Regularization]] — central tool for controlling proxy-reward over-optimization.
- [[Reward Hacking]] — related failure mode when optimizing imperfect reward or rubric signals.
- [[Papers Explained 148 - Direct Preference Optimization]] — existing wiki page on the DPO paper; this book provides a pedagogical treatment.
- [[Papers Explained 149 - RLHF Workflow]] — complementary focus on online iterative RLHF implementation.
- [[GRPO++: Tricks for Making RL Actually Work]] — practical GRPO engineering guide that extends the algorithms chapter here.

## Questions & Gaps

- The book is a moving target (arXiv v9, May 2026); industrial recipes evolve faster than any static textbook.
- How much of the "RL generalizes / SFT memorizes" claim holds across model scales and mixture-of-tasks post-training?
- When should teams prefer rejection sampling over full RL vs DPO/online DPO — the book discusses trade-offs but offers no universal decision rule.
- RLVR is growing quickly; the book's treatment may lag frontier practice (e.g., rubric-based RL, agentic RL environments).
- Persona/character training (Chapter 17) is newer and less benchmarked than core RLHF.

## Related

- [[Reinforcement Learning Topic]] — primary topic hub for RLHF/RLVR papers in this wiki.
- [[Reinforcement Learning]] — general on-policy RL concept used throughout the book.
- [[Safety and Alignment]] — harmlessness/helpfulness framing central to early RLHF motivation.
- [[Reasoning Models]] — RLVR and GRPO-heavy reasoning post-training.
- [[On SFT RL and On-Policy Distillation]] — complementary perspective on SFT vs RL vs distillation trade-offs.
- [[Papers Explained 283 - Tulu V3]] — open recipe the book cites as a canonical modern post-training stack.
- [[Papers Explained 60 - Llama 2]] — earlier multi-iteration RLHF + rejection sampling recipe.
