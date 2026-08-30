# Test-Time Compute

**Type**: concept  
**Tags**: #concept

## Overview

**Test-Time Compute** (also termed inference compute or inference scaling) refers to the computational resources—measured in generated tokens, parallel rollouts, search steps, dollar cost, or wall-clock latency—allocated dynamically during inference to solve a problem, in contrast to the static compute invested during pre-training and fine-tuning. While traditional autoregressive generation uses a fixed token count per query, test-time compute methods enable models to "think," explore multiple solution paths, self-correct, backtrack, or coordinate multi-agent scaffolds before emitting a final answer.

## Mechanisms and Scaling Regimes

Test-time compute can be scaled through several complementary mechanisms:
1. **Extended Chain-of-Thought (Sequential Scaling)**: Generating longer internal reasoning traces (e.g. [[Think Tokens]], reasoning effort) where the model works through intermediate lemmas, code trials, and error detection.
2. **Parallel Sampling and Verification (Best-of-N / Majority Voting)**: Generating multiple independent candidate rollouts and selecting the top candidate using a verifier (e.g. code compiler, execution sandbox, or [[Process Reward Models]]).
3. **Tree Search and Heuristic Exploration (MCTS / Lookahead)**: Guiding search trees via policy priors and value/verifier estimates (e.g. AlphaGo-style search or Monte Carlo Tree Search in reasoning tasks).
4. **Agent Scaffolding and Environment Interaction**: Multi-step agent loops that execute tools, observe outputs, run experiments, and refine solutions over thousands of steps.

## Empirical Properties

- **Third Scaling Law**: Empirical research (OpenAI o1, o3, [[Gemini 3 Deep Think]], [[GPT-5.5]], [[Noam Brown]]) shows that test-time compute acts as an independent scaling axis orthogonal to parameter count and pre-training data. Smaller models with abundant test-time compute frequently outperform larger models operating with standard decoding.
- **Distant Performance Plateaus**: Unlike early assumptions that test-time scaling rapidly hits diminishing returns, empirical benchmarks on complex long-horizon tasks (such as Andrej Karpathy's autoresearch experiments and the [[AI Security Institute]]'s cyber evaluations) show capability curves continuing to climb past hundreds of iterations and over 100M cumulative tokens.
- **Evaluation Requirements**: Because performance is a dynamic function of compute, single-number benchmark scores fail to capture model capability. Rigorous evaluation requires 2D performance-vs-compute curves (tokens, dollars, or latency on the x-axis) or strictly defined resource budgets (as implemented in [[ARC-AGI-2]] cost-scaled leaderboards).

## Appearances

- [[Implications of Large-Scale Test-Time Compute]] — [[Noam Brown]]'s synthesis on why LLM benchmark performance is a function of test-time compute and how safety frameworks must adapt.
- [[Controlling Reasoning Effort in LLMs]] — Sebastian Raschka's reference on training recipes for effort-conditioned test-time compute.
- [[Gemini 3 Deep Think]] — Google DeepMind's parallel reasoning mode leveraging heavy test-time exploration.
- [[GPT-5.5]] — demonstrates that efficiency in test-time compute allows smaller token footprints to achieve frontier step-changes.

## Notes

- Tokens, dollar cost, and wall-clock time represent distinct trade-offs: token counts vary by tokenizer and model efficiency; dollar costs reflect hardware batching; wall-clock latency can be minimized via massive parallelization.
- The shift to heavy test-time compute creates new challenges for safety evaluation, as well-funded adversaries can apply $10M+ in compute to extract capabilities unobserved during low-budget safety tests.

## Related

- [[Reasoning Models]] — architectures trained to utilize test-time compute.
- [[Reasoning Effort]] — user- and system-level controls for allocating test-time compute.
- [[Inference-Budget Safety Evaluation]] — safety testing methodology accounting for high-compute adversaries.
- [[Evaluation and Benchmarks]] — benchmark methodology incorporating compute axes.
- [[Noam Brown]] — key researcher in test-time search and reasoning scaling.
