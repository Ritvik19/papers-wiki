# Agentic Data Curation

**Type**: concept  
**Tags**: #concept

## Overview

**Agentic Data Curation** refers to the systematic methodology and pipeline engineering required to collect, synthesize, filter, and balance training datasets for tool-using, multi-turn language model agents. Established empirically through large-scale ablation studies such as [[Papers Explained 587: OpenThoughts Agent]], agentic data curation focuses on task diversity, trajectory quality, teacher model alignment, and execution verifiability across sandbox environments.

## Key Principles & Mechanisms

1. **Task Sourcing and Top-N Mixing**:
   - Agent capabilities benefit from a heterogeneous mix of synthetic issue-resolution tasks (e.g., `swe-smith`, `issue-tasks`) and authentic human computer-use questions (e.g., StackExchange SuperUser, Tezos).
   - Ingesting a balanced mix of Top 4 to Top 8 validated sources outperforms both single-source training and overly diluted broad mixtures (Top 16).

2. **Task Diversity as the SFT Scaling Bottleneck**:
   - Increasing the number of rollouts per fixed task description yields diminishing returns that plateau rapidly. True scaling requires expanding unique task problem statements.
   - Surface-form instruction rewriting (e.g., expanding ~900 base problems into >21K varied phrasings) successfully bypasses source data scarcity without requiring new underlying problem generation.

3. **LLM-Based Difficulty Filtering**:
   - Filtering task descriptions by the computational effort required by an LLM (such as GPT-5 response token length) isolates high-value, non-trivial agent tasks, delivering consistent downstream gains (~3 percentage points across core agent benchmarks).
   - Conversely, rule-based prompt augmentation (adding synthetic constraints or concatenating tasks) often fails to beat unaugmented baseline descriptions.

4. **Teacher Model Selection Dynamics**:
   - Stronger teacher models do not necessarily yield better student policies. Highly compressed or implicit problem-solving traces from frontier models (e.g., GPT-5.3-Codex) can transfer poorly to smaller open student models compared to teachers with explicit, methodical exploration trajectories (e.g., GLM-4.7).

5. **Trajectory Filtering**:
   - Removing trivial, truncated, or shallow agent rollouts (specifically discarding traces with fewer than 5 turns) significantly boosts downstream performance by forcing the model to learn recovery and sustained multi-turn tool interaction.

6. **RL Post-Training Environment Formulation**:
   - In reinforcement learning with verifiable rewards (RLVR / RLOO), training data composed of concise, single-function Python contracts with auto-generated unit tests (`pymethods2test`) transfers better to complex SWE and terminal benchmarks than noisy, multi-file real-repository bug fixes.
   - The concise contract structure induces a compact **explore $\rightarrow$ patch $\rightarrow$ submit** policy, replacing unproductive verbose thinking loops and exploratory file scanning.

## Appearances

- [[Papers Explained 587: OpenThoughts Agent]] — Comprehensive ablation suite establishing empirical recipes for agentic SFT and RL data curation.
- [[Data for Agents]] — NVIDIA post on open synthetic data mixtures for agent training.
- [[Continually Improving Our Agent Harness]] — Cursor's analysis of data generation and harness-level agent training.

## Related

- [[Agentic AI]]
- [[Agent Harness]]
- [[Synthetic Data]]
- [[RL Environments]]
- [[Reinforcement Learning Topic]]
- [[OpenThoughts]]
