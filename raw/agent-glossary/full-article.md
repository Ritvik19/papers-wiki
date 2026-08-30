Source URL: https://huggingface.co/blog/agent-glossary
Title: Harness, Scaffold, and the AI Agent Terms Worth Getting Right

# Harness, Scaffold, and the AI Agent Terms Worth Getting Right

Published May 25, 2026

Sergio Paniego, Aritra Roy Gosthipaty

When a field evolves quickly, its vocabulary often evolves faster than shared understanding. This is happening in AI Agents, where concepts blur, get renamed, or fade after a few months of heavy use. After ICLR 2026, one of the authors posted a question that captured the confusion: "What do you mean by the terms 'harness' and 'scaffold' in the context of agents?" This glossary grounds the terms that keep coming up without clear, consistent explanations, focusing on concepts that are often mixed up rather than being an exhaustive dictionary. Most terms apply whether building an agent, deploying one, or using tools like Claude Code, Codex, or Hermes Agent; the last section covers training-specific concepts.

## Model

The LLM itself: takes text in, produces text out (Claude, Qwen, GPT, Kimi, DeepSeek). On its own it has no memory between calls and no loop; it can express intent to call a tool but needs a harness to execute it. Wrap it in scaffolding and a harness and it becomes an agent.

## Scaffolding

The behavior-defining layer around the model: system prompt, tool descriptions, how responses get parsed, what the model remembers across steps (context management). Products like Claude Code, Codex, and Antigravity CLI call the whole thing a "harness" (Claude Code's own docs: "Claude Code serves as the agentic harness around Claude"). The scaffold/harness distinction matters most when reasoning about them separately, as in a training pipeline. "Scaffold" is also used more broadly for any infrastructure the harness relies on: hooks, runtime configuration, directory structure. Some products (Claude Code, Codex) are tightly coupled to their provider's models; others (Antigravity CLI, Hermes Agent) let you plug in any model.

## Harness

The execution layer inside the agent: calls the model, handles its tool calls, decides when to stop. Harness engineering is the discipline of designing this layer well (when to stop, error handling, guardrails), applying at both training and inference. At evaluation time, the same pattern is an "eval harness": it runs a fixed set of scenarios at a model checkpoint and records metrics rather than updating weights. Some frameworks use "orchestrator" for a higher-level controller coordinating work across multiple agents (each running its own harness), distinct from a harness driving a single model's execution loop.

## Agent

The term originates in reinforcement learning: an agent is a function taking an observation and returning an action, with the environment returning a new observation in a loop. In the LLM world, an agent is a model plus everything around it that lets it act, not just respond. Community shorthand: Agent = Model + Harness. The system prompt, tool descriptions, and output format form the scaffolding; the loop that calls the model, handles tool calls, and decides when to stop is the harness. Products like Claude Code, Codex, or Cursor are a specific harness built on a specific model, designed together; the model, the harness, and the product are three different things.

## Context Engineering

Designing what goes into the agent's context window at each step: system prompt, tool descriptions, conversation history, retrieved knowledge. Applies at both training and inference, but the cost of getting it wrong differs: at training, what the model sees shapes what gets learned (get it wrong and you retrain); at inference, it's just text (change a prompt and redeploy). Short-term memory stays in the context window during a run; long-term memory persists across sessions, stored externally and retrieved/injected on demand.

## Policy

The behavior an agent follows: given any situation, the probability of taking each possible action. Part of it is learned in model weights, but behavior also depends on scaffolding and harness. A policy is not an agent: the policy defines behavior, the agent is the full system acting in an environment.

## Tool Use

How agents reach outside themselves: APIs, code interpreters, databases, web search, file systems. The model expresses intent to use a tool in a structured format; the harness receives the call and routes it to the right function, feeding the result back into context.

## Skills

Reusable, structured packages of knowledge enabling multi-step tasks. A tool is an action ("run this command"); a skill bundles everything needed to accomplish a goal ("investigate this bug, form a hypothesis, write a fix"). Skills are portable across agents and loaded on demand; the line between tool, skill, and sub-agent shifts across frameworks.

## Sub-Agents

An agent called by another agent to handle a specific subtask, with its own model and scaffold, reasoning independently and returning a result. This distinguishes a sub-agent from a tool (a function call) or a skill (packaged knowledge): a sub-agent can itself reason, use tools, and call further sub-agents. The calling agent is sometimes called an orchestrator.

## Training-Specific Terms

**RL Environment**: anything interactable — a stateful object taking an action as input, updating internal state, and returning an observation. In the LLM context, actions are typically tool calls (e.g. a filesystem where `touch foo.txt` updates state and returns an updated file listing).

**Trainer**: runs many agent episodes, scores results, and updates the inner model's weights. TRL's `GRPOTrainer` is a concrete example, handling episode generation, reward scoring, and weight updates in one class.

**Rollout**: one full agent run start to finish (also called a trajectory or trace) — what the agent saw, did, and the reward received at each step; the raw data RL algorithms learn from.

**Reward**: the score telling the training algorithm whether the model is improving. Can be verifiable (tests pass/fail, answer matches) or learned (human preferences, LLM-as-judge); sparse (one score at episode end) or dense (a score per step). Rubrics break a reward into explicit weighted dimensions rather than a single number; frameworks like OpenEnv and Verifiers implement rubrics as combinable objects (`WeightedSum`, `Sequential`, `Gate`).

## Community Discussion

Comments proposed alternative terminology (e.g. "rigging" instead of "scaffolding," to avoid overloading a term already common in software scaffolding/code generation) and additional terms worth defining (Leaderboard, Benchmark, MCP's relationship to the harness/tool-use pipeline). The authors acknowledge many of these terms lack universally accepted definitions and different frameworks use the same word differently; the glossary aims for a practical mental model rather than one enforced vocabulary.
