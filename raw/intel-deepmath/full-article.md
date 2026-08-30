Source URL: https://huggingface.co/blog/intel-deepmath
Title: DeepMath: A lightweight math reasoning Agent with smolagents

# DeepMath: A lightweight math reasoning Agent with smolagents

Published December 4, 2025

Daniel Fleischer, Moshe Berchansky, Moshe Wasserblat (Intel AI Software Group)

DeepMath is an aligned math reasoning agent built on Qwen3-4B Thinking and fine-tuned with GRPO (Group Relative Policy Optimization). Instead of verbose text, the model emits tiny Python snippets for intermediate steps, runs them in a secure sandbox, and folds the results back into its reasoning, reducing errors and output length. The agent is implemented using the smolagents library.

Evaluated on four math datasets (MATH500, AIME, HMMT, HLE):

- The math agent alone reduces output lengths by up to 66%, while often improving accuracy.
- GRPO training improves agent performance further, in almost all benchmarks.
- Code and evaluation scripts: https://github.com/IntelLabs/DeepMath
- Model: https://huggingface.co/Intel/deepmath-v1

## Why DeepMath?

LLMs have advanced reasoning capabilities, but mathematical problem-solving remains challenging: chain-of-thought traces can be lengthy and prone to arithmetic mistakes. Prior work shows small models can reach strong performance, and other studies investigate tool use for reliability, but they generally don't emphasize reducing trace verbosity or explicitly training models to prefer short, computation-oriented traces executed in a constrained, auditable environment.

Two goals: offload deterministic computation to a safe executor, and train models to prefer concise, computation-oriented traces over verbose text. DeepMath combines a small Python executor with a fine-tuned LLM. The model learns to generate short Python snippets, which are executed in a sandbox and reintegrated into context; GRPO fine-tuning rewards correctness and shorter outputs.

## How it works

- Base model: Qwen3-4B Thinking.
- Executor constraints: sandboxed environment, allow-list of imported modules, per-snippet timeout (no file I/O, no network).
- Inference: a math agent built on smolagents, using vLLM as the inference engine.
- Training: based on the GRPO trainer in TRL, with TRL's vLLM client/server modified to generate GRPO completions using the DeepMath agent.
- During inference the model can output normal tokens or special agent calls containing Python snippets; snippets run in the sandbox and results are inserted back into the trace.

Design goals: concision (short focused snippets instead of multi-line textual calculations), determinism & safety (strict execution limits), and interpretability (readable, auditable snippets).

## Training with GRPO

Reward balances:
- Accuracy reward: +1 for correct answers.
- Using code snippets: +1 for generating code snippets, weighted 10:1 vs. the accuracy reward.
- Length reduction: shorter lengths encouraged by capping GRPO completion candidates at 5k tokens.
- Temperature scheduling: linear T=1.2 → T=0.7 to balance exploration and stability.
- In-context learning: 4 solved examples showing agent calls and executor outputs, so the model learns the syntax and call/response pattern.

Dataset: the Tool-Integrated Reasoning (TIR) subset of OpenMathReasoning. GRPO uses only the `problem` field, not the solution, so problems must genuinely benefit from the external tool.

## Evaluation

Benchmarked against baselines on four datasets, using majority@16 and mean output length as metrics. Configurations compared: baseline Qwen3-4B-Thinking-2507 (no agent), `+Agent` (untrained model run in the agentic framework), `+GRPO` (GRPO-trained but non-agentic inference), and the full DeepMath model (GRPO-trained + agentic). Agentic inference alone reduces output length with mixed accuracy effects; the full DeepMath model (GRPO-trained and run agentically) shows the highest accuracy with the shortest traces. Both GRPO training and agentic inference are needed for best results, and DeepMath reduces output length by up to 66% while improving accuracy on challenging datasets.

## Why it matters

- Accuracy: offloading computation reduces arithmetic errors.
- Efficiency: shorter outputs mean faster inference and easier interpretability.
- Safety: sandbox execution mitigates the risks of running arbitrary code.

## Limitations and future work

Scope is limited to a small model and mathematical reasoning; results are evaluated on contest-style math and may not transfer to open-ended mathematical creativity or formal proofs. Executing generated code is inherently risky; DeepMath uses strict sandboxing and resource limits, but any deployment should carefully manage attack surfaces and enforce rate limits.

## References

1. Luo, Michael, Sijun Tan, Justin Wong, et al. 2025. "DeepScaleR: Surpassing O1-Preview with a 1.5B Model by Scaling RL."
2. Liu, Mingjie, Shizhe Diao, Ximing Lu, et al. 2025. "ProRL: Prolonged Reinforcement Learning Expands Reasoning Boundaries in Large Language Models." arXiv:2505.24864.
3. Moshkov, Ivan, Darragh Hanley, Ivan Sorokin, et al. 2025. "AIMO-2 Winning Solution: Building State-of-the-Art Mathematical Reasoning Models with OpenMathReasoning Dataset." arXiv:2504.16891.
