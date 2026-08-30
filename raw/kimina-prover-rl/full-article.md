Source URL: https://huggingface.co/blog/AI-MO/kimina-prover-rl
Title: Kimina-Prover-RL

# Kimina-Prover-RL

Team Article. Published August 14, 2025

Thibaut Barroyer, Jonas Bayer, Marina Vinyes, Mert Unsal, Haiming Wang, Xiaohan Lin, Mantas Baksys, Junqi Liu, Marco Dos Santos, Flood Sung, and others (AI-MO)

A slimmed-down training pipeline from Kimina Prover, with core features and full compatibility with verl.

kimina-prover-rl is an open-source training pipeline for formal theorem proving in Lean 4, based on a structured reasoning-then-generation paradigm inspired by DeepSeek-R1. It is a simplified version of the system used to train Kimina Prover, preserving the key components while offering full compatibility with the open-source Verl framework. It's released as part of a fork of Verl containing the complete training recipe in `recipe/kimina-prover-rl`.

Two released models:
- `AI-MO/Kimina-Prover-RL-1.7B`: 76.63% Pass@32 on MiniF2F, new SOTA for open-source models in this size category.
- `AI-MO/Kimina-Prover-RL-0.6B`: 71.30% Pass@32 on MiniF2F, also SOTA for its size category.

## Introduction

kimina-prover-rl teaches LLMs to solve formal proof goals in Lean 4 using a two-stage output structure: a natural-language reasoning trace followed by corresponding Lean code. This paradigm, inspired by DeepSeek-R1, separates planning from execution, promoting explainability, error recovery, and stronger generalization.

Training uses GRPO, implemented via the Verl RL library. During rollout, the model generates N outputs per prompt; a reward of 1 is assigned to any output whose Lean code is successfully verified using the `kimina-lean-server`. Two additional features: a format-checking reward that teaches the model to structure its outputs, and an error-correction turn that encourages learning from failure signals.

## Kimina-Client

Verifying a large number of Lean 4 proof candidates simultaneously during training requires a high-throughput verification system. Numina and Kimi developed `kimina-lean-server`, an open-source server supporting parallel proof checking at scale using Lean 4, plus `kimina-client`, a lightweight Python package (on PyPI) for interacting with the server's API.

## Dataset

Training uses `Kimina-Prover-Promptset`, a curated subset of the `NuminaMath-LEAN` dataset (referred to as NuminaMath-LEAN-RL), filtered and preprocessed by:
- Removing easy problems (historical win rate above 0.5) to keep only challenging statements.
- Generating variants of existing problems with Gemini to increase diversity.
- Duplicating hard problems to weight them more heavily during training.

Example input format includes a natural-language problem statement followed by a Lean 4 formal statement stub for the model to complete.

## Format reward

Output is structured into a reasoning block (`<think>...</think>`) followed by a Lean 4 code block. Each rollout is verified to respect this format; malformed outputs (missing `<think>` block, misplaced code) receive zero reward regardless of proof validity. Additional checks beyond block presence:
- Exactly one `<think>` block and one Lean code block per output.
- Rejecting outputs with repetitive reasoning lines (often indicating hallucinated/degenerate generations).
- Checking that tactic blocks in the thinking section contain enough non-comment lines.
- Thresholds on comment density in both reasoning and Lean code to penalize verbose/boilerplate outputs.
- Comparing semantic alignment between tactics described in the reasoning block and the final Lean code (e.g. via IoU or subcode coverage matching).
- Penalizing unnecessarily long responses to encourage token efficiency.

Only generations passing all checks are considered well-formatted and eligible for reward, improving training stability and encouraging clean reasoning.

## Error correction

An error-correction mechanism gives the model a chance to fix its own failed proofs: when a rollout fails (Lean error or incorrect proof), the full prompt, response, and Lean feedback are stored, and a new training sample is created where the model is explicitly prompted to revise its previous reasoning/code. This enables multi-turn interaction chains where Lean feedback is injected into the prompt and the model is rewarded for successfully debugging its own output. Only one error-fix turn is allowed, and the error message is capped at a set token length.

## Training setup

Prior work ("Understanding R1-Zero-Like Training: A Critical Perspective") identified an optimization bias in GRPO that leads to artificially longer responses, especially for incorrect outputs; the same behavior was observed here, so DrGRPO was used instead, which aggregates token-level losses by normalizing with a global constant to eliminate length bias.

The provided configuration targets an 8-GPU setup. The finetuned model is `AI-MO/Kimina-Prover-Distill-1.7B`, itself a finetuned version of `Qwen/Qwen3-1.7B` using cold-start data generated from `AI-MO/Kimina-Prover-72B`. At every step, 256 samples are drawn from the training dataset (one in two is an error-correction sample), with 8 rollouts per sample (2048 generations total; can scale to 16-32 rollouts on more nodes). The model is evaluated every 5 training steps using best@8 (via verl), before and after the error-correction turn.

## Results

Over 48 hours of training on 8 H100 GPUs, by step 85 the pipeline improved accuracy by 4 points, reaching 70% best@8 and 74% after the error-correction turn. Format errors steadily decreased over training, and average output token length increased, consistent with the model learning to reason in longer, more structured traces.

Post-training pass@32 results on MiniF2F:

| Model | Pass@32 | Pass@32 with error fixing |
| --- | --- | --- |
| AI-MO/Kimina-Prover-Distill-1.7B | 72.95% | 75.41% |
| AI-MO/Kimina-Prover-RL-1.7B | 76.23% | 77.87% |

| Model | Pass@32 |
| --- | --- |
| AI-MO/Kimina-Prover-Distill-0.6B | 68.85% |
| AI-MO/Kimina-Prover-RL-0.6B | 71.30% |

## Conclusion

Kimina-Prover-RL provides a lightweight yet powerful RL pipeline for training Lean 4 theorem provers. Combining structured reasoning, format rewards, and error correction achieves state-of-the-art results for open-source models in the 0.6B-1.7B range. The fork of Verl with the full training recipe (`recipe/kimina-prover-rl`) is released so the community can reproduce results or adapt the pipeline to their own datasets and models.
