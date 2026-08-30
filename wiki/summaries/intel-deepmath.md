# DeepMath: A Lightweight Math Reasoning Agent With Smolagents

**Source**: `raw/intel-deepmath/full-article.html` (216 KB), `raw/intel-deepmath/full-article.md`
**Ingested**: 2026-07-10
**Tags**: #summary

## Summary

Intel AI Software Group's DeepMath is a math reasoning agent built on Qwen3-4B Thinking and fine-tuned with GRPO, designed to offload deterministic computation to a sandboxed Python executor instead of doing arithmetic in verbose chain-of-thought text. Rather than writing out long calculations, the model emits short Python snippets mid-reasoning; the smolagents library runs them in a secure, allow-listed sandbox (no file I/O, no network, per-snippet timeout) and folds the results back into the trace. The motivation is twofold: reduce arithmetic errors that accumulate over long textual chains of thought, and shorten output length/latency by replacing multi-line textual calculation with concise, auditable code calls.

Training uses TRL's GRPO trainer, with the vLLM client/server modified so rollouts are generated using the full DeepMath agent loop (not plain text completion), on the Tool-Integrated Reasoning (TIR) subset of OpenMathReasoning; critically, GRPO only sees the `problem` field, not the reference solution, so the model must genuinely benefit from tool use rather than pattern-match a provided answer. Reward combines an accuracy term (+1 for correct final answers), a code-usage term (weighted 10:1 against accuracy to strongly encourage generating snippets), a completion-length cap (5k tokens) to discourage verbosity, and a temperature schedule (1.2 to 0.7) balancing exploration against stability, plus 4 in-context examples showing the agent-call syntax.

Evaluated on MATH500, AIME, HMMT, and HLE using majority@16 and mean output length, four configurations were compared: the untrained base model with no agent, the untrained model run agentically, the GRPO-trained model run non-agentically, and the full DeepMath model (GRPO-trained + agentic). Agentic inference alone shortens outputs with mixed accuracy effects; GRPO training alone improves accuracy without shortening outputs; only the combination (GRPO-trained and run agentically) delivers both the highest accuracy and the shortest traces, reducing output length by up to 66% while improving accuracy on the harder benchmarks.

## Key Claims

- Base model: Qwen3-4B Thinking; inference framework: smolagents + vLLM; training: TRL's GRPO trainer with a modified vLLM client/server for agentic rollout generation.
- The full DeepMath model (GRPO-trained + agentic) achieves the highest accuracy and shortest traces of all four tested configurations; agentic inference or GRPO training alone are each necessary but not individually sufficient.
- Output length is reduced by up to 66% versus the non-agentic baseline, with accuracy improvements concentrated on the harder benchmarks (HMMT, HLE).
- Reward design weights code-snippet usage 10:1 against the accuracy reward, and caps GRPO completion length at 5k tokens to push toward concision.
- Training uses only the `problem` field from OpenMathReasoning's TIR subset (not the reference solution), so gains reflect genuine tool-use benefit rather than answer leakage.
- Code, evaluation scripts, and the released model (`Intel/deepmath-v1`) are open-sourced.

## Figures

No figures were extracted for this ingest; the per-benchmark accuracy/length comparison charts across the four configurations are described inline but not downloaded, per this batch's no-figure-download policy.

## Entities

- [[Intel]] — Intel AI Software Group builds and releases DeepMath.
- [[Hugging Face]] — hosts the blog post; smolagents (the agent framework used) is a Hugging Face library.

## Questions & Gaps

- The post scopes results to a small (4B) model and contest-style math; it explicitly flags that findings may not transfer to open-ended mathematical creativity or formal proofs.
- Executing generated code is inherently risky even in a sandbox; the post notes this but doesn't detail a security review of the sandbox's allow-list boundaries.

## Related

- [[GRPO]]
- [[Reasoning Models]]
- [[Agentic AI]]
