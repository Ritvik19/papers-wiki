# Reasoning in LLMs: A Literature Review

This document synthesizes the literature on reasoning in large language models, sourced from the Hugging Face Papers API / arXiv. It traces the field from prompting tricks through the RLVR ("R1 moment") era to test-time scaling, verification, efficiency, agentic reasoning, and open questions about what these models are actually doing when they "think."

Eleven of the papers cited below are themselves surveys/literature reviews. Each thematic section also includes a **"Further methods surveyed in the literature"** block that pulls in landmark papers those surveys reviewed in their own taxonomies — verified against each survey's bibliography and cited with the survey that covers it. Section 12 collects benchmark papers surfaced by those surveys.

---

## 1. Scope and taxonomy: System 1 vs. System 2

The field frames the shift as moving LLMs from fast, intuitive "System 1" pattern-matching toward slower, deliberate "System 2" reasoning. [From System 1 to System 2: A Survey of Reasoning Large Language Models](https://huggingface.co/papers/2502.17419) (Feb 2025) uses this framing explicitly, tracing how o1/o3 and DeepSeek-R1 "closely mimic the deliberate reasoning of System 2." [LLM Post-Training: A Deep Dive into Reasoning Large Language Models](https://huggingface.co/papers/2502.21321) (Feb 2025) complements this with a systematic map of post-training methodology — fine-tuning, RL, and test-time scaling — as the three levers used to build reasoning models, while flagging catastrophic forgetting, reward hacking, and inference-time trade-offs as the field's recurring failure modes.

A useful organizing principle that recurs across surveys: reasoning research splits into what happens **during training** (teaching a model to produce better reasoning traces) and what happens **at inference** (spending more compute per query to reason better without changing weights). The rest of this review follows that split, then covers verification, efficiency, agentic extensions, and faithfulness/safety as cross-cutting concerns.

---

## 2. Prompting-era foundations (2022–2023)

Before any specialized training, reasoning was elicited purely through prompting:

- [Chain-of-Thought Prompting Elicits Reasoning in Large Language Models](https://huggingface.co/papers/2201.11903) (Jan 2022, Wei et al.) is the foundational result: showing intermediate reasoning steps before the final answer, via a handful of exemplars, substantially improves performance on arithmetic, commonsense, and symbolic reasoning for sufficiently large models.
- [Self-Consistency Improves Chain of Thought Reasoning in Language Models](https://huggingface.co/papers/2203.11171) (Mar 2022) replaces greedy decoding with sampling many reasoning paths and taking a majority vote over final answers — a striking +17.9 points on GSM8K, +12.2 on AQuA, and gains across StrategyQA and ARC-Challenge, establishing "sample-and-vote" as a cheap, training-free upgrade that persists as a baseline throughout the field.
- [Least-to-Most Prompting Enables Complex Reasoning in Large Language Models](https://huggingface.co/papers/2205.10625) (May 2022) and [Decomposed Prompting: A Modular Approach for Solving Complex Tasks](https://huggingface.co/papers/2210.02406) (Oct 2022) attack compositional generalization by explicitly breaking a hard problem into an ordered sequence of easier subproblems, rather than relying on a single CoT pass.
- [Program of Thoughts Prompting: Disentangling Computation from Reasoning for Numerical Reasoning Tasks](https://huggingface.co/papers/2211.12588) (Nov 2022) offloads arithmetic execution to a Python interpreter, separating "what to compute" (language model) from "how to compute it" (executable code) — an idea that reappears constantly in later code-reasoning and tool-use work.
- [Tree of Thoughts: Deliberate Problem Solving with Large Language Models](https://huggingface.co/papers/2305.10601) (May 2023) generalizes CoT into a search over a tree of intermediate "thoughts," with self-evaluation, lookahead, and backtracking — enabling GPT-4 to solve Game of 24 far more reliably than plain CoT by allowing exploration instead of a single left-to-right pass.

An open dispute from this era concerns whether the improvements from scale are genuinely qualitative jumps. [Emergent Abilities of Large Language Models](https://huggingface.co/papers/2206.07682) (Jun 2022) documents sudden capability jumps (including on reasoning benchmarks) at certain scale thresholds, while [Are Emergent Abilities of Large Language Models a Mirage?](https://huggingface.co/papers/2304.15004) (Apr 2023) argues these "emergent" jumps are largely artifacts of discontinuous (e.g., exact-match) metrics rather than genuine phase transitions in the underlying model — a methodological caution that anticipates later debates about whether RL training genuinely creates new reasoning capacity (Section 3).

By 2024–2025, the field had shifted to models that reason with much longer, more exploratory chains than these early prompting techniques used. [Towards Reasoning Era: A Survey of Long Chain-of-Thought for Reasoning Large Language Models](https://huggingface.co/papers/2503.09567) (Mar 2025) formalizes this transition, introducing a taxonomy that separates "Short CoT" (the prompting-era style above) from "Long CoT," characterized by deep reasoning, extensive exploration, and reflection — the style that o1 and DeepSeek-R1 popularized.

**Further methods surveyed in the literature**
- [Large Language Models are Zero-Shot Reasoners](https://huggingface.co/papers/2205.11916) - appending "Let's think step by step" alone (no exemplars) elicits CoT-style reasoning (via System1to2, Post-Training, Reinforced Reasoning, Multimodal CoT surveys).
- [Automatic Chain of Thought Prompting in Large Language Models](https://huggingface.co/papers/2210.03493) - Auto-CoT clusters questions and auto-generates diverse exemplar chains, removing manual prompt engineering (via Post-Training, Reinforced Reasoning, Multimodal CoT surveys).
- [Complexity-Based Prompting for Multi-Step Reasoning](https://huggingface.co/papers/2210.00720) - selects and votes over the most complex (most reasoning-step) chains among sampled exemplars (via Post-Training, Long CoT surveys).
- [Measuring and Narrowing the Compositionality Gap in Language Models](https://huggingface.co/papers/2210.03350) - Self-Ask has the model explicitly pose and answer its own follow-up sub-questions before the final answer (via Implicit Reasoning survey).
- [Graph of Thoughts: Solving Elaborate Problems with Large Language Models](https://huggingface.co/papers/2308.09687) - generalizes Tree of Thoughts to an arbitrary graph of interdependent "thoughts" with merging and refinement operations (via System1to2, Post-Training, Reinforced Reasoning, Long CoT, Test-Time Scaling, Stop Overthinking, Multimodal CoT surveys).
- [PAL: Program-aided Language Models](https://huggingface.co/papers/2211.10435) - has the LLM generate a program whose execution (not the LLM) produces the final answer, closely related to Program of Thoughts (via System1to2, Long CoT, Implicit Reasoning surveys).
- [Large Language Models as Analogical Reasoners](https://huggingface.co/papers/2310.01714) - prompts the model to self-generate relevant exemplars/knowledge before solving, instead of using fixed few-shot demonstrations (via Reinforced Reasoning survey).

---

## 3. Learning to reason: training-time methods

### 3.1 Bootstrapping reasoning from the model itself

[STaR: Bootstrapping Reasoning With Reasoning](https://huggingface.co/papers/2203.14465) (Mar 2022, Zelikman et al.) is the conceptual ancestor of the entire self-improvement line: generate rationales, keep only the ones that reach a correct answer (using rationalization — regenerating a rationale given the correct answer — for the ones that failed), fine-tune on the successes, and repeat. STaR matched a 30x larger fine-tuned model on CommonsenseQA using only this bootstrapping loop, previewing the idea that a model's own filtered outputs can be a training signal. [Quiet-STaR: Language Models Can Teach Themselves to Think Before Speaking](https://huggingface.co/papers/2403.09629) (Mar 2024) generalizes this from question-answering to *every* token prediction, having the model learn to generate silent rationales throughout generic text before predicting the next token — an early bridge toward the "think before you answer" default behavior of later reasoning models.

**Further methods surveyed in the literature**
- [Reinforced Self-Training (ReST) for Language Modeling](https://huggingface.co/papers/2308.08998) - grows a dataset from the model's own samples (Grow step) then repeatedly fine-tunes on the best-scoring subset (Improve step), decoupling data generation from policy updates (via System1to2, Reinforced Reasoning, Long CoT, Reasoning Economy surveys).
- [Beyond Human Data: Scaling Self-Training for Problem-Solving with Language Models](https://huggingface.co/papers/2312.06585) - ReST\\(^{EM}\\) shows self-generated, filtered training data can match or beat human-curated data for math and code reasoning (via System1to2 survey).
- [Self-Rewarding Language Models](https://huggingface.co/papers/2401.10020) - the model acts as its own reward model via LLM-as-judge, iteratively improving both instruction-following and reward-judging ability (via System1to2, Post-Training, Long CoT surveys).
- [rStar-Math: Small LLMs Can Master Math Reasoning with Self-Evolved Deep Thinking](https://huggingface.co/papers/2501.04519) - a small model bootstraps its own step-by-step verified training data via MCTS, reaching frontier math performance without distillation from a larger teacher (via System1to2, Long CoT surveys).

### 3.2 The RLVR / "R1 moment"

The decisive shift came from applying large-scale reinforcement learning with verifiable, rule-based rewards (RLVR) directly to reasoning, rather than distilling from a stronger teacher:

- [DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning](https://huggingface.co/papers/2501.12948) (Jan 2025) is the field's inflection point. DeepSeek-R1-Zero was trained via large-scale RL with **no SFT step at all** and still developed reasoning behaviors like reflection and re-verification "naturally," though with readability and language-mixing problems; DeepSeek-R1 fixed this with a small cold-start SFT stage before RL and reached performance comparable to OpenAI's o1-1217, while the team also released six distilled dense models (1.5B–70B) — making frontier-style reasoning openly reproducible for the first time.
- [OpenAI o1 System Card](https://huggingface.co/papers/2412.16720) (Dec 2024) is OpenAI's own documentation of the model that started the race, describing o1's training to "think before it answers" via a long internal chain of thought, together with safety evaluations.
- [Kimi k1.5: Scaling Reinforcement Learning with LLMs](https://huggingface.co/papers/2501.12599) (Jan 2025) documents Moonshot AI's parallel effort, covering RL training techniques, multimodal data recipes, and infrastructure for scaling RL-trained reasoning.
- [DAPO: An Open-Source LLM Reinforcement Learning System at Scale](https://huggingface.co/papers/2503.14476) (Mar 2025) is one of the most-cited open recipes for making GRPO-style RL work reliably at scale (decoupled clipping, dynamic sampling, token-level loss), addressing instabilities that plagued naive reproductions of R1-style training.
- [Towards Large Reasoning Models: A Survey of Reinforced Reasoning with Large Language Models](https://huggingface.co/papers/2501.09686) (Jan 2025) frames this whole line as models learning to generate "thought" token sequences via trial-and-error RL, positioning train-time RL and test-time scaling as two combined axes defining a "Large Reasoning Model."

**Further methods surveyed in the literature**
- [Training language models to follow instructions with human feedback](https://huggingface.co/papers/2203.02155) - InstructGPT, the RLHF recipe (SFT → reward model → PPO) that all later RLVR pipelines adapt by swapping the learned reward model for verifiable rewards (via System1to2, Post-Training, Reinforced Reasoning, Reasoning Economy surveys).
- [Proximal Policy Optimization Algorithms](https://huggingface.co/papers/1707.06347) - PPO, the clipped-objective policy-gradient algorithm underlying most RLHF/RLVR pipelines before GRPO-style critic-free alternatives (via Post-Training, Reinforced Reasoning, Long CoT, Stop Overthinking, Reasoning Economy surveys).
- [Direct Preference Optimization: Your Language Model is Secretly a Reward Model](https://huggingface.co/papers/2305.18290) - DPO reframes preference alignment as a single supervised classification-style loss, removing the separate reward model and RL loop (via System1to2, Post-Training, Reinforced Reasoning, Long CoT, Reasoning Economy, Multimodal CoT surveys).
- [DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models](https://huggingface.co/papers/2402.03300) - introduces GRPO, which estimates advantage from group-relative rewards instead of a learned critic, now the default RL algorithm for RLVR reasoning training (via System1to2, Post-Training, Reinforced Reasoning, Long CoT, Implicit Reasoning, Stop Overthinking surveys).
- [Constitutional AI: Harmlessness from AI Feedback](https://huggingface.co/papers/2212.08073) - has models critique and revise their own outputs against a written set of principles, then trains a preference model on the results (RLAIF), an early template for reward signals that don't require human labels (via Post-Training, Reinforced Reasoning, Long CoT surveys).

### 3.3 Data efficiency: how little supervision is actually needed?

A surprising counter-current showed that RLVR/SFT gains don't require massive datasets:

- [LIMO: Less is More for Reasoning](https://huggingface.co/papers/2502.03387) (Feb 2025) achieves strong math reasoning with only 817 carefully curated training examples, arguing that the *foundation* for reasoning is already latent in pretrained models and needs only a small, high-quality "activation" set.
- [LIMR: Less is More for RL Scaling](https://huggingface.co/papers/2502.11886) (Feb 2025) makes the analogous claim for the RL stage rather than SFT.

### 3.4 Does RL actually teach new reasoning, or just resurface it?

This is one of the sharpest open controversies in the literature:

- [Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?](https://huggingface.co/papers/2504.13837) (Apr 2025) argues RLVR mainly biases sampling toward reward-aligned paths the base model could already produce (measurable via pass@k with large k), rather than creating genuinely new reasoning capacity.
- [Spurious Rewards: Rethinking Training Signals in RLVR](https://huggingface.co/papers/2506.10947) (Jun 2025) provides striking supporting evidence: RLVR on Qwen2.5-Math-7B improved MATH-500 by +21.4 points with a *random* reward, +13.8 with a reward for the *wrong* label, and +27.1 with majority-voting rewards — nearly matching the +29.1 gained from ground-truth rewards. Critically, this only worked for Qwen models, not Llama3 or OLMo2, and coincided with a jump in "code reasoning" behavior (thinking in code without executing it) from 65% to over 90% of responses — suggesting RL is often surfacing latent pretraining behaviors specific to a model family rather than teaching a general skill.
- [ProRL: Prolonged Reinforcement Learning Expands Reasoning Boundaries in Large Language Models](https://huggingface.co/papers/2505.24864) (May 2025) argues the opposite conclusion for *sufficiently long* RL runs, claiming prolonged RL training uncovers genuinely novel reasoning strategies not accessible to the base model — directly contesting the "RL only reweights existing capacity" narrative and suggesting duration/scale of RL matters for the conclusion.
- [Reasoning with Sampling: Your Base Model is Smarter Than You Think](https://huggingface.co/papers/2510.14901) (Oct 2025) pushes further in the "capacity is already latent" direction, showing better sampling procedures alone can unlock much of what RL post-training achieves.
- [Part I: Tricks or Traps? A Deep Dive into RL for LLM Reasoning](https://huggingface.co/papers/2508.08221) (Aug 2025) is a systematic ablation of the many small implementation choices (clipping, KL terms, advantage normalization, etc.) that make or break RLVR training runs — useful as a "trust but verify" companion to the papers above, since much of the disagreement in this literature traces back to sensitive, under-reported hyperparameter choices.

### 3.5 Distilling reasoning into small models

- [Small Models Struggle to Learn from Strong Reasoners](https://huggingface.co/papers/2502.12143) (Feb 2025) identifies the "Small Model Learnability Gap": models ≤3B parameters do not reliably benefit from long CoT distilled from much larger teachers, and instead need shorter, simpler chains matched to their capacity; their proposed Mix Distillation blends long/short and large/small-model traces to fix this.
- [Phi-4-Mini-Reasoning: Exploring the Limits of Small Reasoning Language Models in Math](https://huggingface.co/papers/2504.21233) (Apr 2025) is a concrete recipe addressing that gap for a 3.8B model — mid-training on distilled long-CoT data, SFT, "Rollout DPO," then RLVR — beating DeepSeek-R1-Distill-Qwen-7B by 3.2 points on Math-500 despite being smaller.
- [Beyond Scaling Law: A Data-Efficient Distillation Framework for Reasoning](https://huggingface.co/papers/2508.09883) (Aug 2025) continues this thread, targeting distillation efficiency rather than brute-force scaling of distillation data.

---

## 4. Verification and reward modeling

A central design question for RL-trained reasoning is *what to reward*: the final answer only (outcome supervision) or every intermediate step (process supervision)?

- [Let's Verify Step by Step](https://huggingface.co/papers/2305.20050) (May 2023, OpenAI) is the landmark comparison: process supervision significantly outperforms outcome supervision on the MATH dataset, with their process-supervised model solving 78% of a representative test subset. They released PRM800K, 800,000 step-level human labels, which became the standard resource for training process reward models (PRMs).
- [The Lessons of Developing Process Reward Models in Mathematical Reasoning](https://huggingface.co/papers/2501.07301) (Jan 2025) revisits PRM construction at scale and finds that the common Monte Carlo estimation approach for auto-labeling steps is inferior to LLM-as-judge or human annotation, and identifies systematic biases in Best-of-N evaluation of PRMs (policies can produce a correct final answer via a flawed process, inflating apparent PRM quality).
- [Generative Verifiers: Reward Modeling as Next-Token Prediction](https://huggingface.co/papers/2408.15240) (Aug 2024) reframes verification itself as a generation task rather than a scalar classification head, unifying reasoning and verification into the same next-token-prediction interface — letting the verifier "think" before scoring.
- [Beyond Outcome Verification: Verifiable Process Reward Models for Structured Reasoning](https://huggingface.co/papers/2601.17223) (Jan 2026) pushes process supervision toward deterministic, rule-based step verifiers instead of learned neural judges, specifically to avoid the opacity and reward-hacking risk of judge-based PRMs — achieving up to 20% higher F1 in a structured medical-evidence domain where rule-based verification is possible.
- [One Token to Fool LLM-as-a-Judge](https://huggingface.co/papers/2507.08794) (Jul 2025) is a cautionary result showing how brittle LLM-judge-based reward signals can be to superficial, single-token manipulations — relevant to any RLVR pipeline relying on a generative or judge-based reward rather than an exact-match/rule-based one.
- [Reasoning Gym: Reasoning Environments for Reinforcement Learning with Verifiable Rewards](https://huggingface.co/papers/2505.24760) (May 2025) and [RLVE: Scaling Up Reinforcement Learning for Language Models with Adaptive Verifiable Environments](https://huggingface.co/papers/2511.07317) (Nov 2025) address the infrastructure side: procedurally generating large families of programmatically verifiable reasoning tasks, since exact-match rewards are only available for a narrow slice of naturally occurring problems (math, code) and synthetic environments extend RLVR's applicability to more domains.

**Further methods surveyed in the literature**
- [Solving math word problems with process- and outcome-based feedback](https://huggingface.co/papers/2211.14275) - the earlier, smaller-scale DeepMind study comparing process vs. outcome feedback that predates and anticipates OpenAI's "Let's Verify Step by Step" (via System1to2, Long CoT, Stop Overthinking surveys).
- [Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations](https://huggingface.co/papers/2312.08935) - automatically labels step-level correctness by estimating each step's potential to reach the correct final answer, removing the need for human step annotations (via Reinforced Reasoning, Reasoning Economy surveys).
- [Improve Mathematical Reasoning in Language Models by Automated Process Supervision](https://huggingface.co/papers/2406.06592) - OmegaPRM uses Monte Carlo Tree Search to automatically collect process supervision data at scale for training PRMs (via System1to2, Post-Training, Reinforced Reasoning, Long CoT, Reasoning Economy surveys).
- [Process Reinforcement through Implicit Rewards](https://huggingface.co/papers/2502.01456) - PRIME derives dense, token-level rewards implicitly from an outcome reward model, avoiding the cost of separately trained/labeled PRMs (via System1to2, Long CoT, Test-Time Scaling surveys).

---

## 5. Test-time / inference-time scaling

A parallel research axis leaves weights untouched and instead spends more compute *per query* to reason better:

- [s1: Simple Test-Time Scaling](https://huggingface.co/papers/2501.19393) (Jan 2025) is a minimalist, influential result: with only 1,000 curated (question, reasoning trace) pairs (chosen for difficulty, diversity, and quality) and "budget forcing" — forcibly truncating the model's thinking, or extending it by appending "Wait" to make it double-check itself — a fine-tuned Qwen2.5-32B-Instruct beat o1-preview on AIME24/MATH by up to 27%, and further budget-forcing pushed AIME24 from 50% to 57% purely by scaling test-time compute with no additional training.
- [What, How, Where, and How Well? A Survey on Test-Time Scaling in Large Language Models](https://huggingface.co/papers/2503.24235) (Mar 2025) organizes the fragmented TTS literature (sampling/search strategies, verifier-guided search, latent-space scaling, agentic scaling) along four axes: what is scaled, how, where in the pipeline, and how the gains are measured.
- [The Art of Scaling Test-Time Compute for Large Language Models](https://huggingface.co/papers/2512.02008) (Dec 2025) is the largest empirical comparison to date (30B+ tokens, 8 open models from 7B–235B, 4 datasets) and finds **no single TTS strategy universally dominates**; reasoning models split into "short-horizon" and "long-horizon" trace-quality regimes depending on problem difficulty, and for a fixed model, optimal TTS performance scales monotonically with the compute budget — giving a practical recipe for picking a TTS strategy conditioned on model type and budget rather than a single winning method.
- [Sleep-time Compute: Beyond Inference Scaling at Test-time](https://huggingface.co/papers/2504.13171) (Apr 2025) proposes reasoning *offline*, before the user's query arrives, by anticipating likely questions about a given context and pre-computing useful intermediate results — cutting the test-time compute needed for equivalent accuracy by roughly 5x on modified GSM-Symbolic/AIME benchmarks, and amortizing costs 2.5x further when multiple related queries share a context.
- [A Survey on Latent Reasoning](https://huggingface.co/papers/2507.06203) (Jul 2025) and [Implicit Reasoning in Large Language Models: A Comprehensive Survey](https://huggingface.co/papers/2509.02350) (Sep 2025) cover a structurally different bet: instead of verbalizing every reasoning step in natural language (which is slow and bandwidth-limited), perform multi-step inference inside the model's continuous hidden state — via activation-based recurrence, hidden-state propagation, or masked-diffusion-style "infinite-depth" reasoning — trading interpretability for potentially much greater expressive bandwidth and speed.
- [Reasoning with Language Model is Planning with World Model](https://huggingface.co/papers/2305.14992) (May 2023) is an earlier, structurally distinct proposal: treat the LLM itself as a world model for a planning algorithm (e.g., Monte Carlo Tree Search) instead of purely autoregressive token-by-token generation — a conceptual precursor to search-augmented reasoning approaches.

**Further methods surveyed in the literature**
- [Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters](https://huggingface.co/papers/2408.03314) - shows an optimal, difficulty-adaptive allocation of test-time compute (choosing between more search vs. a larger proposal distribution) can outperform simply scaling up model size for a fixed compute budget (via Post-Training, Reinforced Reasoning, Long CoT, Stop Overthinking, Reasoning Economy, Multimodal CoT surveys).
- [Language Agent Tree Search Unifies Reasoning, Acting, and Planning in Language Models](https://huggingface.co/papers/2310.04406) - LATS combines MCTS-style search with ReAct-style environment interaction and self-reflection into a single tree-search framework for agentic tasks (via Reasoning Economy survey).
- [Training Large Language Models to Reason in a Continuous Latent Space](https://huggingface.co/papers/2412.06769) - Coconut feeds the model's own last hidden state back in as the next input embedding instead of decoding a token, letting reasoning unfold in continuous latent space rather than as text (via Long CoT, Test-Time Scaling, Latent Reasoning, Implicit Reasoning, Stop Overthinking, Reasoning Economy surveys).
- [Think before you speak: Training Language Models With Pause Tokens](https://huggingface.co/papers/2310.02226) - inserts learnable "pause" tokens before the answer to give the model extra computation steps without producing extra visible text, an early precursor to latent-reasoning approaches (via Latent Reasoning, Implicit Reasoning surveys).
- [Fast Best-of-N Decoding via Speculative Rejection](https://huggingface.co/papers/2410.20290) - speeds up Best-of-N sampling by early-rejecting low-promise generations using a reward-model proxy, cutting the compute cost of test-time search (via Post-Training, Stop Overthinking, Reasoning Economy surveys).

---

## 6. Efficient reasoning: the "overthinking" problem

Longer chains-of-thought generally help accuracy but come at real latency and cost — this has spawned its own subfield:

- [Stop Overthinking: A Survey on Efficient Reasoning for Large Language Models](https://huggingface.co/papers/2503.16419) (Mar 2025) is the first structured survey of the "overthinking phenomenon" (verbose, redundant CoT), taxonomizing fixes into model-based (train inherently concise reasoners), output-based (dynamically truncate at inference), and input-prompt-based approaches.
- [Harnessing the Reasoning Economy: A Survey of Efficient Reasoning for Large Language Models](https://huggingface.co/papers/2503.24377) (Mar 2025) frames the same territory as a performance/compute trade-off ("reasoning economy"), analyzing root causes of inefficiency and cataloging solutions across both post-training and test-time stages.
- [Token-Budget-Aware LLM Reasoning](https://huggingface.co/papers/2412.18547) (Dec 2024) shows CoT length can simply be compressed by stating a token budget in the prompt, with a framework to dynamically estimate the right budget per problem — trading a small accuracy hit for large token savings.
- [DAST: Difficulty-Adaptive Slow-Thinking for Large Reasoning Models](https://huggingface.co/papers/2503.04472) makes this adaptive rather than uniform: a Token Length Budget metric quantifies difficulty, and budget-aware reward shaping penalizes overlong responses on easy problems while still rewarding extended reasoning on hard ones — cutting token usage over 30% on average without hurting accuracy on genuinely hard problems (the risk with *uniform* length penalties, which the paper notes can degrade performance on exactly the problems that need long reasoning).
- [Your Models Have Thought Enough: Training Large Reasoning Models to Stop Overthinking](https://huggingface.co/papers/2509.23392) (Sep 2025) and [Thinkless: LLM Learns When to Think](https://huggingface.co/papers/2505.13379) (May 2025) push toward models that learn to *decide* whether extended reasoning is needed at all, rather than always defaulting to long CoT — connecting efficient reasoning back to the adaptive-reasoning-format ideas surveyed above.

**Further methods surveyed in the literature**
- [Chain of Draft: Thinking Faster by Writing Less](https://huggingface.co/papers/2502.18600) - prompts the model to write minimal, "draft"-style intermediate steps (a handful of words each) instead of verbose CoT, cutting token usage sharply with little accuracy loss (via Long CoT, Stop Overthinking surveys).
- [TokenSkip: Controllable Chain-of-Thought Compression in LLMs](https://huggingface.co/papers/2502.12067) - learns to identify and skip low-utility tokens within a CoT trace, giving a controllable compression ratio (via Long CoT, Stop Overthinking, Reasoning Economy surveys).
- [CODI: Compressing Chain-of-Thought into Continuous Space via Self-Distillation](https://huggingface.co/papers/2502.21074) - self-distills an explicit-CoT teacher into a student that reasons in continuous latent space, aiming to match explicit-CoT accuracy at a fraction of the decoding cost (via Latent Reasoning, Implicit Reasoning, Stop Overthinking surveys).
- [Do NOT Think That Much for 2+3=? On the Overthinking of o1-Like LLMs](https://huggingface.co/papers/2412.21187) - empirically diagnoses "overthinking" (redundant self-verification and solution-switching on easy problems) in o1-like models and proposes efficiency-focused training strategies to reduce it (via System1to2, Post-Training, Long CoT, Test-Time Scaling, Stop Overthinking, Reasoning Economy surveys).

---

## 7. Self-refinement and reflective agents

A related but distinct idea to RL/verification: let the model critique and revise its own output in a loop, without any parameter updates or external reward model.

- [Self-Refine: Iterative Refinement with Self-Feedback](https://huggingface.co/papers/2303.17651) (Mar 2023) has the same model generate an output, critique it, and refine it iteratively, purely via prompting.
- [Reflexion: Language Agents with Verbal Reinforcement Learning](https://huggingface.co/papers/2303.11366) (Mar 2023) extends this to agentic settings — an agent verbally reflects on task feedback (including from failed environment interactions) and stores that reflection in memory to condition future attempts, functioning as a training-free analog of reinforcement learning via natural-language self-critique rather than gradient updates.

Both remain influential baselines/components inside modern agentic reasoning pipelines (Section 8), though later work has shown self-refinement's benefits are inconsistent and can even degrade performance without external verification signal — a caveat relevant when comparing these training-free approaches to the RL/verifier-based methods above.

---

## 8. Agentic and tool-augmented reasoning

As reasoning models get deployed as agents that call tools, search the web, or execute code, a new axis of research examines how reasoning and *acting* interact:

- [Agentic Reasoning for Large Language Models](https://huggingface.co/papers/2601.12538) (Jan 2026) is a recent, comprehensive survey organizing this space into three layers: foundational single-agent reasoning (planning, tool use, search in stable environments), self-evolving reasoning (refining via feedback/memory/adaptation), and collective multi-agent reasoning (coordination, knowledge sharing) — and separately distinguishes in-context (test-time orchestration) from post-training (RL-optimized) approaches to building these behaviors.
- [SWE-RL: Advancing LLM Reasoning via Reinforcement Learning on Open Software Evolution](https://huggingface.co/papers/2502.18449) (Feb 2025) is a concrete instance applying RLVR-style training to real-world software engineering tasks rather than math/code puzzles, using open-source software evolution data as the reward signal.
- [Reasoning and Tool-use Compete in Agentic RL: From Quantifying Interference to Disentangled Tuning](https://huggingface.co/papers/2602.00994) (Feb 2026) is a notable negative result: jointly training a single model to both reason and use tools via shared parameters is widely assumed to be beneficial, but this paper shows the two objectives often produce *misaligned gradient directions* that interfere with each other during optimization; their proposed fix (DART) explicitly decouples the two via separate low-rank adaptation modules, consistently outperforming joint training.
- [Tool-Augmented Policy Optimization: Synergizing Reasoning and Adaptive Tool Use with Reinforcement Learning](https://huggingface.co/papers/2510.07038) (Oct 2025) is a competing approach to the same interference problem, aiming to make reasoning and adaptive tool invocation cooperate within one RL objective — worth reading alongside the interference paper above as an example of active, unresolved tension in how to train agentic reasoners.

**Further methods surveyed in the literature**
- [ReAct: Synergizing Reasoning and Acting in Language Models](https://huggingface.co/papers/2210.03629) - interleaves CoT reasoning traces with concrete actions and their environment observations, the foundational "reason then act" agent loop that most later tool-use agents build on (via Reinforced Reasoning, Agentic Reasoning surveys).
- [Toolformer: Language Models Can Teach Themselves to Use Tools](https://huggingface.co/papers/2302.04761) - trains a model to decide, in a self-supervised way, when and how to call external tools (calculator, search, calendar) by inserting API calls into its own training text (via Reinforced Reasoning, Agentic Reasoning surveys).
- [ChatCoT: Tool-Augmented Chain-of-Thought Reasoning on Chat-based Large Language Models](https://huggingface.co/papers/2305.14323) - structures reasoning as an explicit "thought → tool call → observation" chat-style loop, letting the model reflect on tool outputs mid-reasoning (via Agentic Reasoning survey).
- [Voyager: An Open-Ended Embodied Agent with Large Language Models](https://huggingface.co/papers/2305.16291) - a Minecraft agent that autonomously writes, tests, and stores reusable code-based skills in a growing library, an early example of self-evolving tool creation (via Test-Time Scaling, Agentic Reasoning surveys).
- [MemGPT: Towards LLMs as Operating Systems](https://huggingface.co/papers/2310.08560) - manages a fixed context window like virtual memory, with the LLM itself deciding what to page in/out of context, an influential design for long-horizon agent memory (via Agentic Reasoning survey).
- [Search-o1: Agentic Search-Enhanced Large Reasoning Models](https://huggingface.co/papers/2501.05366) - equips an o1-style reasoning model with agentic retrieval-augmented search, invoked whenever the model recognizes it lacks needed knowledge mid-chain (via System1to2, Long CoT surveys).

---

## 9. Faithfulness, interpretability, and safety of reasoning traces

A visible chain-of-thought is often treated as a window into "what the model is thinking," which matters enormously for safety monitoring — but the literature is increasingly skeptical this assumption holds:

- [Language Models Don't Always Say What They Think: Unfaithful Explanations in Chain-of-Thought Prompting](https://huggingface.co/papers/2305.04388) (May 2023) is the foundational warning: CoT explanations can be systematically manipulated by biasing model inputs (e.g., always making the correct multiple-choice answer "(A)" in few-shot examples) without the model ever acknowledging this influence in its stated reasoning — dropping accuracy by up to 36% across 13 BIG-Bench Hard tasks while explanations remained fluent and plausible.
- [Measuring Chain-of-Thought Monitorability Through Faithfulness and Verbosity](https://huggingface.co/papers/2510.27378) (Oct 2025) extends the faithfulness question with a "verbosity" axis — whether the CoT actually lists *every* factor needed to solve the task, not just whether stated factors are truthful — combining both into a single monitorability score, since a safety-monitoring scheme that reads the CoT as a proxy for the model's true computation needs both properties to hold.
- [Faithfulness Metrics Don't Measure Faithfulness: A Meta-Evaluation with Ground Truth](https://huggingface.co/papers/2605.25052) (May 2026) is a sharp, very recent result: building a 3,066-example ground-truth benchmark (BonaFide) across 13 tasks and 10 models, the authors find most proposed faithfulness metrics perform "near randomly" against actual ground truth — directly undercutting the evidentiary basis for CoT-monitoring-based safety arguments and suggesting the field needs new, validated metrics before CoT faithfulness claims can be trusted.
- [Deliberative Alignment: Reasoning Enables Safer Language Models](https://huggingface.co/papers/2412.16339) (Dec 2024, OpenAI) takes the opposite, more optimistic tack: rather than treating CoT purely as an interpretability artifact, it trains models to explicitly reason over safety specifications before answering, using the reasoning process itself as an alignment mechanism.
- [The Hidden Risks of Large Reasoning Models: A Safety Assessment of R1](https://huggingface.co/papers/2502.12659) (Feb 2025) and [H-CoT: Hijacking the Chain-of-Thought Safety Reasoning Mechanism to Jailbreak Large Reasoning Models](https://huggingface.co/papers/2502.12893) (Feb 2025) are two concrete adversarial findings specific to the reasoning-model era: R1-style models introduce new safety surface area, and their own visible safety-reasoning steps can themselves be hijacked as an attack vector across o1/o3, R1, and Gemini 2.0 Flash Thinking.

---

## 10. Math and multimodal domain-specific reasoning

Much of the empirical progress above was driven by math and code because they offer cheap, exact verification signals, but the ideas generalize:

- [Gold-medalist Performance in Solving Olympiad Geometry with AlphaGeometry2](https://huggingface.co/papers/2502.03544) (Feb 2025, DeepMind) represents the neuro-symbolic end of the spectrum: pairing language models with formal symbolic search/proof systems to reach gold-medal-level performance on IMO geometry, a domain where pure LLM chain-of-thought historically struggled.
- [DeepMath-103K: A Large-Scale, Challenging, Decontaminated, and Verifiable Mathematical Dataset for Advancing Reasoning](https://huggingface.co/papers/2504.11456) (Apr 2025) addresses the increasingly acute benchmark-contamination problem in math reasoning evaluation by building a decontaminated, high-difficulty dataset explicitly for RLVR-style verifiable training.
- [Multimodal Chain-of-Thought Reasoning: A Comprehensive Survey](https://huggingface.co/papers/2503.12605) (Mar 2025) surveys how CoT-style step-by-step reasoning extends beyond pure text into vision-language settings, building on earlier work like [Multimodal Chain-of-Thought Reasoning in Language Models](https://huggingface.co/papers/2302.00923) (Feb 2023), which first showed that separating rationale generation from answer inference over both text and image inputs improves multimodal reasoning accuracy.

**Further methods surveyed in the literature**
- [LLaVA-CoT: Let Vision Language Models Reason Step-by-Step](https://huggingface.co/papers/2411.10440) - trains a vision-language model to produce four structured stages (summary, caption, reasoning, conclusion) instead of a single free-form response, and applies stage-level Best-of-N search at inference (via System1to2, Long CoT, Implicit Reasoning, Multimodal CoT surveys).
- [DDCoT: Duty-Distinct Chain-of-Thought Prompting for Multimodal Reasoning in Language Models](https://huggingface.co/papers/2310.16436) - assigns distinct "duties" to a language-reasoning sub-chain and a vision-perception sub-chain, then fuses them, explicitly separating what should be reasoned about from what should be perceived (via Multimodal CoT survey).

---

## 11. Synthesis: where the field agrees and disagrees

Reading across these clusters, a few genuine open disputes stand out rather than a tidy consensus narrative:

1. **Does RLVR create new reasoning capacity, or just reweight sampling toward capacity the base model already has?** [2504.13837](https://huggingface.co/papers/2504.13837) and [Spurious Rewards](https://huggingface.co/papers/2506.10947) argue for the latter (and show it's highly model-family-dependent — Qwen-specific effects don't transfer to Llama/OLMo2); [ProRL](https://huggingface.co/papers/2505.24864) argues sufficiently prolonged RL training does expand the reasoning boundary. This is unresolved and depends heavily on training duration, base model family, and reward design.
2. **Is a visible chain-of-thought actually faithful to the model's computation, and is that even measurable yet?** [Unfaithful CoT](https://huggingface.co/papers/2305.04388) (2023) and the very recent [Faithfulness Metrics Don't Measure Faithfulness](https://huggingface.co/papers/2605.25052) (2026) bookend three years of work showing this remains an open, and arguably worsening, measurement problem — which has direct implications for any AI-safety plan that relies on "reading the CoT" as a monitoring mechanism.
3. **Should reasoning be long and verbose, or short and efficient?** The "long CoT" survey ([2503.09567](https://huggingface.co/papers/2503.09567)) documents why longer, more exploratory reasoning helps; the entire "Stop Overthinking" cluster (Section 6) documents the cost and pushes back toward adaptive, difficulty-conditioned reasoning length. The likely resolution emerging from the literature is *adaptive* length (DAST, Thinkless) rather than a fixed answer either way.
4. **Should reasoning happen in natural language at all?** The dominant paradigm (CoT, RLVR, PRMs) assumes verbalized, human-readable reasoning traces. The latent/implicit reasoning survey line ([2507.06203](https://huggingface.co/papers/2507.06203), [2509.02350](https://huggingface.co/papers/2509.02350)) is a structurally different bet — doing reasoning in continuous hidden states — that trades away the interpretability benefits central to point 2, in exchange for potential efficiency and expressiveness gains. This tension between interpretable-but-slow and opaque-but-fast reasoning representations is arguably the deepest unresolved architectural question in the field.

---

## 12. Benchmarks and evaluation

The benchmarks that recur throughout this literature (and that several of the surveys above use to frame progress) are worth collecting on their own:

- [Training Verifiers to Solve Math Word Problems](https://huggingface.co/papers/2110.14168) - introduces GSM8K, 8.5K grade-school math word problems, the most widely used entry-level math-reasoning benchmark (via System1to2, Post-Training, Long CoT, Test-Time Scaling, Implicit Reasoning, Stop Overthinking, Reasoning Economy surveys).
- [Measuring Mathematical Problem Solving With the MATH Dataset](https://huggingface.co/papers/2103.03874) - a harder, competition-level math benchmark spanning multiple difficulty levels and subjects, the standard for evaluating process/outcome reward models above GSM8K difficulty (via Post-Training, Reinforced Reasoning, Long CoT, Test-Time Scaling, Implicit Reasoning, Stop Overthinking surveys).
- [Challenging BIG-Bench Tasks and Whether Chain-of-Thought Can Solve Them](https://huggingface.co/papers/2210.09261) - BIG-Bench Hard (BBH), a 23-task subset of BIG-Bench specifically selected because prior LLMs performed below average human raters, widely used to test whether CoT closes the gap (via System1to2, Post-Training surveys).
- [GPQA: A Graduate-Level Google-Proof Q&A Benchmark](https://huggingface.co/papers/2311.12022) - graduate-level science questions written to resist simple web lookup, used to evaluate reasoning that requires genuine domain expertise rather than retrieval (via System1to2, Long CoT, Test-Time Scaling, Implicit Reasoning, Stop Overthinking surveys).
- [Evaluating Large Language Models Trained on Code](https://huggingface.co/papers/2107.03374) - introduces Codex and the HumanEval benchmark, the origin of functional-correctness (pass@k) evaluation for code reasoning (via Reinforced Reasoning, Test-Time Scaling, Implicit Reasoning, Stop Overthinking surveys).
- [FrontierMath: A Benchmark for Evaluating Advanced Mathematical Reasoning in AI](https://huggingface.co/papers/2411.04872) - research-mathematician-level problems designed to resist near-term saturation and contamination, positioned as a frontier successor to MATH/GSM8K (via System1to2, Long CoT surveys).
- [On the Measure of Intelligence](https://huggingface.co/papers/1911.01547) - Chollet's original formulation of the abstraction-and-reasoning-corpus (ARC) benchmark and its underlying argument that skill on narrow tasks should not be conflated with general intelligence, the conceptual origin of the ARC-AGI benchmark line (via System1to2, Long CoT surveys).

---

## Suggested reading order

For a fast, high-signal on-ramp:

1. [Chain-of-Thought Prompting](https://huggingface.co/papers/2201.11903) and [Self-Consistency](https://huggingface.co/papers/2203.11171) — the prompting-era baseline everything else builds on.
2. [STaR](https://huggingface.co/papers/2203.14465) — the conceptual seed of self-improvement/RLVR.
3. [DeepSeek-R1](https://huggingface.co/papers/2501.12948) — the paper that made large-scale RLVR reasoning open and reproducible.
4. [From System 1 to System 2](https://huggingface.co/papers/2502.17419) and [LLM Post-Training](https://huggingface.co/papers/2502.21321) — broad orienting surveys.
5. [Let's Verify Step by Step](https://huggingface.co/papers/2305.20050) — the outcome-vs-process supervision question that underlies all reward design choices.
6. [Spurious Rewards](https://huggingface.co/papers/2506.10947) and [Does RL Really Incentivize Reasoning Capacity Beyond the Base Model?](https://huggingface.co/papers/2504.13837) — the strongest currently-live controversy in the field.
7. Pick a survey matching your specific interest: [Test-Time Scaling](https://huggingface.co/papers/2503.24235) (inference-time), [Stop Overthinking](https://huggingface.co/papers/2503.16419) (efficiency), [Agentic Reasoning](https://huggingface.co/papers/2601.12538) (agents/tools), or [A Survey on Latent Reasoning](https://huggingface.co/papers/2507.06203) (non-verbal reasoning).
8. Each thematic section's "Further methods surveyed in the literature" block (and the Section 12 benchmarks list) is a good place to go deeper on any of the above once you've picked a direction.

---

## Sources

All papers cited above were fetched via the Hugging Face Papers API (`https://huggingface.co/api/papers/{id}`).

### Taxonomy / overview

- [From System 1 to System 2](https://huggingface.co/papers/2502.17419) (Feb 2025)
- [LLM Post-Training: A Deep Dive](https://huggingface.co/papers/2502.21321) (Feb 2025)
- [Towards Reasoning Era: Long CoT Survey](https://huggingface.co/papers/2503.09567) (Mar 2025)

### Prompting-era foundations

- [Chain-of-Thought Prompting](https://huggingface.co/papers/2201.11903) (Jan 2022)
- [Self-Consistency](https://huggingface.co/papers/2203.11171) (Mar 2022)
- [Least-to-Most Prompting](https://huggingface.co/papers/2205.10625) (May 2022)
- [Decomposed Prompting](https://huggingface.co/papers/2210.02406) (Oct 2022)
- [Program of Thoughts](https://huggingface.co/papers/2211.12588) (Nov 2022)
- [Tree of Thoughts](https://huggingface.co/papers/2305.10601) (May 2023)
- [Emergent Abilities of LLMs](https://huggingface.co/papers/2206.07682) (Jun 2022)
- [Are Emergent Abilities a Mirage?](https://huggingface.co/papers/2304.15004) (Apr 2023)
- [Large Language Models are Zero-Shot Reasoners](https://huggingface.co/papers/2205.11916) (May 2022)
- [Auto-CoT](https://huggingface.co/papers/2210.03493) (Oct 2022)
- [Complexity-Based Prompting](https://huggingface.co/papers/2210.00720) (Oct 2022)
- [Self-Ask (Compositionality Gap)](https://huggingface.co/papers/2210.03350) (Oct 2022)
- [Graph of Thoughts](https://huggingface.co/papers/2308.09687) (Aug 2023)
- [PAL: Program-aided Language Models](https://huggingface.co/papers/2211.10435) (Nov 2022)
- [LLMs as Analogical Reasoners](https://huggingface.co/papers/2310.01714) (Oct 2023)

### Learning to reason (training-time)

- [STaR](https://huggingface.co/papers/2203.14465) (Mar 2022)
- [Quiet-STaR](https://huggingface.co/papers/2403.09629) (Mar 2024)
- [DeepSeek-R1](https://huggingface.co/papers/2501.12948) (Jan 2025)
- [OpenAI o1 System Card](https://huggingface.co/papers/2412.16720) (Dec 2024)
- [Kimi k1.5](https://huggingface.co/papers/2501.12599) (Jan 2025)
- [DAPO](https://huggingface.co/papers/2503.14476) (Mar 2025)
- [LIMO](https://huggingface.co/papers/2502.03387) (Feb 2025)
- [LIMR](https://huggingface.co/papers/2502.11886) (Feb 2025)
- [Towards Large Reasoning Models survey](https://huggingface.co/papers/2501.09686) (Jan 2025)
- [Does RL Really Incentivize Reasoning Capacity Beyond the Base Model?](https://huggingface.co/papers/2504.13837) (Apr 2025)
- [ProRL](https://huggingface.co/papers/2505.24864) (May 2025)
- [Spurious Rewards](https://huggingface.co/papers/2506.10947) (Jun 2025)
- [Reasoning with Sampling](https://huggingface.co/papers/2510.14901) (Oct 2025)
- [Tricks or Traps? Deep Dive into RL for LLM Reasoning](https://huggingface.co/papers/2508.08221) (Aug 2025)
- [ReST](https://huggingface.co/papers/2308.08998) (Aug 2023)
- [Beyond Human Data (ReST-EM)](https://huggingface.co/papers/2312.06585) (Dec 2023)
- [Self-Rewarding Language Models](https://huggingface.co/papers/2401.10020) (Jan 2024)
- [rStar-Math](https://huggingface.co/papers/2501.04519) (Jan 2025)
- [InstructGPT](https://huggingface.co/papers/2203.02155) (Mar 2022)
- [PPO](https://huggingface.co/papers/1707.06347) (Jul 2017)
- [DPO](https://huggingface.co/papers/2305.18290) (May 2023)
- [DeepSeekMath (GRPO)](https://huggingface.co/papers/2402.03300) (Feb 2024)
- [Constitutional AI](https://huggingface.co/papers/2212.08073) (Dec 2022)

### Distillation to small models

- [Small Models Struggle to Learn from Strong Reasoners](https://huggingface.co/papers/2502.12143) (Feb 2025)
- [Phi-4-Mini-Reasoning](https://huggingface.co/papers/2504.21233) (Apr 2025)
- [Beyond Scaling Law: Data-Efficient Distillation](https://huggingface.co/papers/2508.09883) (Aug 2025)

### Verification and reward modeling

- [Let's Verify Step by Step](https://huggingface.co/papers/2305.20050) (May 2023)
- [Lessons of Developing PRMs](https://huggingface.co/papers/2501.07301) (Jan 2025)
- [Generative Verifiers](https://huggingface.co/papers/2408.15240) (Aug 2024)
- [Beyond Outcome Verification: VPRMs](https://huggingface.co/papers/2601.17223) (Jan 2026)
- [One Token to Fool LLM-as-a-Judge](https://huggingface.co/papers/2507.08794) (Jul 2025)
- [Reasoning Gym](https://huggingface.co/papers/2505.24760) (May 2025)
- [RLVE](https://huggingface.co/papers/2511.07317) (Nov 2025)
- [Uesato et al., process- and outcome-based feedback](https://huggingface.co/papers/2211.14275) (Nov 2022)
- [Math-Shepherd](https://huggingface.co/papers/2312.08935) (Dec 2023)
- [OmegaPRM](https://huggingface.co/papers/2406.06592) (Jun 2024)
- [PRIME](https://huggingface.co/papers/2502.01456) (Feb 2025)

### Test-time scaling

- [s1: Simple Test-Time Scaling](https://huggingface.co/papers/2501.19393) (Jan 2025)
- [Survey on Test-Time Scaling](https://huggingface.co/papers/2503.24235) (Mar 2025)
- [The Art of Scaling Test-Time Compute](https://huggingface.co/papers/2512.02008) (Dec 2025)
- [Sleep-time Compute](https://huggingface.co/papers/2504.13171) (Apr 2025)
- [A Survey on Latent Reasoning](https://huggingface.co/papers/2507.06203) (Jul 2025)
- [Implicit Reasoning survey](https://huggingface.co/papers/2509.02350) (Sep 2025)
- [Reasoning with Language Model is Planning with World Model](https://huggingface.co/papers/2305.14992) (May 2023)
- [Scaling LLM Test-Time Compute Optimally](https://huggingface.co/papers/2408.03314) (Aug 2024)
- [LATS](https://huggingface.co/papers/2310.04406) (Oct 2023)
- [Coconut](https://huggingface.co/papers/2412.06769) (Dec 2024)
- [Pause Tokens](https://huggingface.co/papers/2310.02226) (Oct 2023)
- [Fast Best-of-N via Speculative Rejection](https://huggingface.co/papers/2410.20290) (Oct 2024)

### Efficient reasoning

- [Stop Overthinking survey](https://huggingface.co/papers/2503.16419) (Mar 2025)
- [Harnessing the Reasoning Economy survey](https://huggingface.co/papers/2503.24377) (Mar 2025)
- [Token-Budget-Aware LLM Reasoning](https://huggingface.co/papers/2412.18547) (Dec 2024)
- [DAST](https://huggingface.co/papers/2503.04472)
- [Your Models Have Thought Enough](https://huggingface.co/papers/2509.23392) (Sep 2025)
- [Thinkless](https://huggingface.co/papers/2505.13379) (May 2025)
- [Chain of Draft](https://huggingface.co/papers/2502.18600) (Feb 2025)
- [TokenSkip](https://huggingface.co/papers/2502.12067) (Feb 2025)
- [CODI](https://huggingface.co/papers/2502.21074) (Feb 2025)
- [Do NOT Think That Much for 2+3=?](https://huggingface.co/papers/2412.21187) (Dec 2024)

### Self-refinement / reflection

- [Self-Refine](https://huggingface.co/papers/2303.17651) (Mar 2023)
- [Reflexion](https://huggingface.co/papers/2303.11366) (Mar 2023)

### Agentic and tool-augmented reasoning

- [Agentic Reasoning for LLMs survey](https://huggingface.co/papers/2601.12538) (Jan 2026)
- [SWE-RL](https://huggingface.co/papers/2502.18449) (Feb 2025)
- [Reasoning and Tool-use Compete in Agentic RL](https://huggingface.co/papers/2602.00994) (Feb 2026)
- [Tool-Augmented Policy Optimization](https://huggingface.co/papers/2510.07038) (Oct 2025)
- [ReAct](https://huggingface.co/papers/2210.03629) (Oct 2022)
- [Toolformer](https://huggingface.co/papers/2302.04761) (Feb 2023)
- [ChatCoT](https://huggingface.co/papers/2305.14323) (May 2023)
- [Voyager](https://huggingface.co/papers/2305.16291) (May 2023)
- [MemGPT](https://huggingface.co/papers/2310.08560) (Oct 2023)
- [Search-o1](https://huggingface.co/papers/2501.05366) (Jan 2025)

### Faithfulness, interpretability, safety

- [Language Models Don't Always Say What They Think](https://huggingface.co/papers/2305.04388) (May 2023)
- [Measuring CoT Monitorability](https://huggingface.co/papers/2510.27378) (Oct 2025)
- [Faithfulness Metrics Don't Measure Faithfulness](https://huggingface.co/papers/2605.25052) (May 2026)
- [Deliberative Alignment](https://huggingface.co/papers/2412.16339) (Dec 2024)
- [Hidden Risks of Large Reasoning Models](https://huggingface.co/papers/2502.12659) (Feb 2025)
- [H-CoT Jailbreak](https://huggingface.co/papers/2502.12893) (Feb 2025)

### Math and multimodal domain-specific

- [AlphaGeometry2](https://huggingface.co/papers/2502.03544) (Feb 2025)
- [DeepMath-103K](https://huggingface.co/papers/2504.11456) (Apr 2025)
- [Multimodal CoT survey](https://huggingface.co/papers/2503.12605) (Mar 2025)
- [Multimodal CoT Reasoning in Language Models](https://huggingface.co/papers/2302.00923) (Feb 2023)
- [LLaVA-CoT](https://huggingface.co/papers/2411.10440) (Nov 2024)
- [DDCoT](https://huggingface.co/papers/2310.16436) (Oct 2023)

### Benchmarks and evaluation

- [GSM8K](https://huggingface.co/papers/2110.14168) (Oct 2021)
- [MATH dataset](https://huggingface.co/papers/2103.03874) (Mar 2021)
- [BIG-Bench Hard](https://huggingface.co/papers/2210.09261) (Oct 2022)
- [GPQA](https://huggingface.co/papers/2311.12022) (Nov 2023)
- [HumanEval / Codex](https://huggingface.co/papers/2107.03374) (Jul 2021)
- [FrontierMath](https://huggingface.co/papers/2411.04872) (Nov 2024)
- [On the Measure of Intelligence (ARC)](https://huggingface.co/papers/1911.01547) (Nov 2019)

---

## Related

- [Looped Transformers: A Learning Roadmap](looped-transformers-2026-07-21.md) — an architectural rather than training-data-driven route to Section 5's "reason without verbalizing every step" bet: recurrent-depth/looped transformers reason in latent space by iterating a shared block, instead of via chain-of-thought post-training.
- [On-Policy Distillation: A Learning Roadmap](on-policy-distillation-2026-07-21.md) — a deeper dive into Section 3.5's "distilling reasoning into small models" thread, covering the on-policy alternative (student rollouts graded by a teacher) to the off-policy SFT distillation covered there, and sharing the RLVR-cost motivations of Section 3.2.
