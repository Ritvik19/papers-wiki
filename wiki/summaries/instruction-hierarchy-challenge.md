# Instruction Hierarchy Challenge

**Source**: `raw/instruction-hierarchy-challenge/full-article.md`
**Ingested**: 2026-07-10
**Tags**: #summary

## Summary

Instruction Hierarchy Challenge (IH-Challenge) is a reinforcement-learning training dataset and public red-teaming release, announced March 10, 2026, aimed at strengthening how frontier language models resolve conflicting instructions. OpenAI's models are trained to follow a strict priority order, system > developer > user > tool (see [[Instruction Hierarchy]]), where a lower-priority instruction is followed only when it does not conflict with a higher-priority one. OpenAI frames a large share of safety and reliability failures, disallowed-content requests, private-information extraction, and prompt-injection attacks embedded in tool output, as the same underlying failure: the model follows the wrong instruction when two sources disagree.

Training a model to hold this hierarchy under adversarial pressure at scale runs into three specific pitfalls. First, a model can fail to resolve a conflict simply because the instructions themselves are too complicated, which looks like an instruction-hierarchy failure but is really an instruction-following failure. Second, many instruction conflicts are genuinely nuanced or subjective, so using a separate LLM as a judge to assign reward risks inheriting that judge's own mistakes. Third, a model under RL pressure can learn shortcuts that raise the reward score without being useful, such as refusing benign requests just to look safer. IH-Challenge is built to sidestep these problems: each task pairs a high-priority instruction (for example, "only answer Yes or No") with a lower-priority instruction that tries to violate it, and the response is graded with a simple Python script rather than a judge model, so tasks stay simple enough to isolate hierarchy-following from general instruction-following, are objectively checkable, and have no shortcut that guarantees a high score across every task.

Training an internal model, GPT-5 Mini-R, on IH-Challenge produced consistent gains on instruction-hierarchy benchmarks without a drop in general usefulness. On academic benchmarks, TensorTrust (dev-user) improved from 0.76 to 0.91 and RealGuardrails (Distractors) from 0.88 to 0.95; on internal benchmarks, System-versus-User conflict handling improved from 0.84 to 0.95 and Developer-versus-User conflict handling from 0.83 to 0.95. Overrefusal on IH-Challenge itself rose from 0.79 to 1.00, while capability evals such as GPQA Diamond (0.83) and AIME 2024 (0.93 to 0.94) held roughly steady; chat win rate against o1 slipped slightly, from 0.71 to 0.66. Beyond the benchmark gains, adding category-specific safety guidance to the system prompt raised refusal and safe-completion rates on disallowed-content categories without hurting helpfulness, and the same training improved robustness on CyberSecEval 2 and an internal prompt-injection benchmark modeled partly on an attack previously demonstrated against an older version of ChatGPT Atlas.

OpenAI released the IH-Challenge dataset publicly, framing consistent prioritization of trusted over untrusted instructions as a safety property that matters more as models take on agentic work such as calling tools and reading untrusted documents.

## Key Claims

- Announced March 10, 2026; releases both a training methodology and a public dataset on Hugging Face.
- Enforces the priority order system > developer > user > tool.
- Training data pairs a high-priority instruction with an adversarial low-priority instruction and grades responses with a Python script instead of an LLM judge.
- Produced an internal model, GPT-5 Mini-R, by applying reinforcement learning with this dataset to GPT-5-Mini.
- TensorTrust (dev-user) improved from 0.76 to 0.91; System <> User Conflict improved from 0.84 to 0.95; Developer <> User Conflict improved from 0.83 to 0.95.
- IH-Challenge (overrefusal) improved from 0.79 to 1.00 with no measurable loss on GPQA Diamond or AIME 2024.
- Chat win rate versus o1 dropped slightly, from 0.71 to 0.66, one of the few measured regressions.
- Improves robustness on CyberSecEval 2 and an internal static prompt-injection benchmark related to a ChatGPT Atlas attack.

## Benchmarks

Robustness on academic benchmarks (GPT-5-Mini vs. GPT-5 Mini-R):

| Eval | GPT-5-Mini | GPT-5 Mini-R |
| --- | --- | --- |
| Gandalf Password (sys-user) | 0.99 | 0.99 |
| Gandalf Password (dev-user) | 0.98 | 1.00 |
| TensorTrust (sys-user) | 0.86 | 0.94 |
| TensorTrust (dev-user) | 0.76 | 0.91 |
| RealGuardrails (Distractors) | 0.88 | 0.95 |
| RealGuardrails (Handwritten) | 0.82 | 0.89 |
| System IFEval | 0.92 | 0.96 |

Robustness on internal benchmarks:

| Eval | GPT-5-Mini | GPT-5 Mini-R |
| --- | --- | --- |
| TutorJailbreak (sys-user) | 0.96 | 0.99 |
| Tutor Jailbreak (dev-user) | 0.97 | 0.99 |
| System <> User Conflict | 0.84 | 0.95 |
| System <> Developer Conflict | 0.86 | 0.86 |
| Developer <> User Conflict | 0.83 | 0.95 |

Capability and overrefusal:

| Eval | GPT-5-Mini | GPT-5 Mini-R |
| --- | --- | --- |
| IH-Challenge (overrefusal) | 0.79 | 1.00 |
| TensorTrust (overrefusal) | 0.91 | 0.90 |
| GPQA Diamond | 0.83 | 0.83 |
| AIME 2024 | 0.93 | 0.94 |
| Chat WinRate vs. o1 | 0.71 | 0.66 |
| Preference Score | 0.46 | 0.40 |

## Figures

No article figures extracted; openai.com blocks direct HTML download so figures could not be downloaded, and WebFetch markdown does not preserve chart images.

## Entities

- [[OpenAI]]: developer of IH-Challenge and GPT-5 Mini-R.

## Questions & Gaps

- The raw source does not clarify whether GPT-5 Mini-R shipped as a production model or remained an internal research artifact.
- The full IH-Challenge dataset schema is not described beyond the "high-priority instruction plus adversarial low-priority instruction plus Python grader" outline.

## Related

- [[OpenAI]]
- [[Safety and Alignment]]
- [[Instruction Hierarchy]]
- [[Evaluation and Benchmarks]]
- [[Papers Explained 555 - IH Challenge]]
