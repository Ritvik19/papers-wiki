# ServiceNow

**Type**: org
**Tags**: #entity

## Overview

ServiceNow, primarily known as an enterprise workflow-automation platform, runs an AI research group (SLAM Lab) that builds open-source reinforcement learning infrastructure and efficient reasoning models. Its work spans RL training systems (PipelineRL) and model efficiency (Apriel-H1's attention-to-Mamba distillation), both built on Fast-LLM, its own Apache-2.0 training framework.

## Appearances

- [[PipelineRL]] — open-sourced RL implementation using inflight weight updates to keep inference throughput high while minimizing policy staleness during RL training.
- [[Apriel-H1: The Surprising Key to Distilling Efficient Reasoning Models]] — converts a 15B reasoning model into a Mamba hybrid via staged distillation, reaching 2.1x throughput with minimal quality loss.
- [[AprielGuard: A Guardrail for Safety and Adversarial Robustness in Modern LLM Systems]] — 8B safety/security guardrail model covering 16 risk categories and adversarial attacks across prompts, conversations, and agentic workflows.

## Notes

- Fast-LLM, ServiceNow's training framework, treats attention and Mamba as interchangeable "mixer" implementations of the same interface, configurable per decoder block.
- Both projects are attributed to ServiceNow's SLAM Lab / ServiceNow-AI research group.

## Related

- [[GRPO]]
- [[Reasoning Models]]
- [[Reinforcement Learning Topic]]
