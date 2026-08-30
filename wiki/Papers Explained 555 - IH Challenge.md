# Papers Explained 555 - IH Challenge

The dataset is available at [HuggingFace](https://huggingface.co/datasets/openai/ih-challenge).

This page ingests the source article into the wiki and connects it to [[Papers Explained Corpus]], [[Synthetic Data]], [[Reinforcement Learning Topic]], [[Evaluation and Benchmarks]], [[Code Models]], [[Reinforcement Learning]].

Official source: [[Instruction Hierarchy Challenge]].

## Source Metadata

- Source file: `raw/2026-04-03_Papers-Explained-555--IH-Challenge-cf2433051b7e.html`
- Source title: Papers Explained 555: IH Challenge
- Published: 2026-04-03
- Canonical: [https://medium.com/@ritvik19/papers-explained-555-ih-challenge-cf2433051b7e](https://medium.com/@ritvik19/papers-explained-555-ih-challenge-cf2433051b7e)

## Key Ideas

- Given a conversation consisting of messages from multiple roles, a priority order is imposed:
- That is, lower-priority instructions are honored only when compatible with higher-priority constraints; otherwise, the conflicting lower-priority instructions are ignored.
- To train models to robustly follow Instructions Following (IH) under such conflicts, the IH-Challenge aims to be adversarially hard while remaining programmatically gradable.
- Offline task skeletons consist of one or more high-priority instructions, a placeholder for the low-priority (conflicting, potentially adversarial) message, and a Python grader.
- IF-simple (under attacks): Tasks should be simple enough for a good IH model to reliably succeed, even when faced with adversarial low-priority instructions. The goal is to reward good IH handling rather than puzzle-solving.

## Notes

IH-Challenge is a reinforcement learning training dataset designed to improve instruction hierarchy (IH) robustness in frontier LLMs by teaching them how to prioritize conflicting system, developer, user, and tool instructions in a trust-ordered way. Built around three principles: keeping underlying tasks instruction-following simple (IF-simple), making every datapoint programmatically gradable via Python graders, and avoiding shortcut strategies like overrefusal through diverse task families, it is used to fine-tune GPT-5-Mini (yielding GPT-5-Mini-R), which achieves a +10.0% average IH robustness gain across 16 benchmarks.

The dataset is available at [HuggingFace](https://huggingface.co/datasets/openai/ih-challenge).

## Constructing IH-Challenge

Given a conversation consisting of messages from multiple roles, a priority order is imposed:

> system ≻ developer ≻ user ≻ tool

That is, lower-priority instructions are honored only when compatible with higher-priority constraints; otherwise, the conflicting lower-priority instructions are ignored.

To train models to robustly follow Instructions Following (IH) under such conflicts, the IH-Challenge aims to be adversarially hard while remaining programmatically gradable. However, adversarially generating the IH-conflict conversation and the grader code together makes it difficult to ensure the grader is valid, so data construction is split into two stages.

*Figure: Illustration of the task design and training data pipeline.*

### Offline Task Skeleton Construction

Offline task skeletons consist of one or more high-priority instructions, a placeholder for the low-priority (conflicting, potentially adversarial) message, and a Python grader.

Design Principles:

- IF-simple (under attacks): Tasks should be simple enough for a good IH model to reliably succeed, even when faced with adversarial low-priority instructions. The goal is to reward good IH handling rather than puzzle-solving.

- Programmatically gradeable (under attacks): Tasks must be clearly defined and gradable by a program, even with adversarial conflicts. This is achieved by keeping conflicting instructions low-priority and ensuring the grading criterion can be determined solely from the high-priority instructions. Ambiguous tasks are excluded.

- Avoiding shortcut learning: Tasks should be diverse to prevent models from relying on simple heuristics (shortcuts). This encourages the development of robust IH capabilities rather than brittle solutions.

Construction Process:

1. LLM synthesis: An LLM is prompted to generate a structured task object, including:

- A conversation with high-priority instructions from different roles and a placeholder for low-priority conflicting instructions.

- Python grader code to evaluate the model’s response based on IH.

- Example responses for passing and failing the task.

- Diversity is introduced by varying factors like logical constraints and output format.

2. Filtering and validation:

- Static checks are applied to the grader code to ensure correctness.

- Response formatting is normalized to reduce grading noise.

- Each grader is unit-tested against the provided examples.

- Tasks with inconsistent descriptions and graders are removed.

- A final manual review is conducted to ensure the graders are accurate.

*Figure: Summary of IH-Challenge task skeletons.*

### Online Adversarial Conflict Synthesis

Adversarial low-priority conflicting messages are synthesized using language model programming to fill each task skeleton’s low-priority placeholder online during (defender) model training. The attacker is a frozen model without safety guardrails that interacts with a defender evaluation tool.

The Attacker uses a “budgeted propose-evaluate-revise” loop to synthesize these messages:

- Propose: Generates a candidate conflicting message.

- Evaluate: Tests the candidate message against the current defender model using an evaluation tool. The tool measures the defender’s performance on the modified task.

- Revise: Refines the candidate message based on the evaluation feedback.

The attacker is guided by a structured prompt that encourages exploration of diverse attack strategies.

The Defender is trained using reinforcement learning (RL).

- It is trained on conflict prompts generated by the attacker.

- For each conflict prompt, the defender generates multiple responses, which are scored by a Python grader.

- The RL policy gradient update is based on these scores.

- To prevent capability regression, the training data includes both conflict prompts and capability-focused tasks.

## Evaluation

A static evaluation set is created by running the synthesis procedure on held-out data.This allows for measuring the defender’s generalization ability on unseen conflict prompts.

GPT-5-Mini is trained with RL on IH-Challenge to create GPT-5-Mini-R

*Figure: Training and test robustness of GPT-5-Mini-R on IH-Challenge tasks.*

RL on IH-Challenge improves in-distribution IH robustness and generalizes to unseen attacks.

- Training reward increases and saturates on simpler splits, indicating successful optimization.

- GPT-5-Mini-R shows significant robustness gains against:

- Impersonation attacks (fake system messages)

- Automated LLM-generated IH-violating prompts

- Human red-teaming attacks

- These gains hold on held-out attacks from the same distribution, indicating generalization to unseen but similar attacks.

*Figure: Overrefusal and capability.*

Overrefusal is controlled and core capabilities are largely preserved, with targeted gains on IH-related overrefusal.

- On overrefusal datasets where higher-tier instructions no longer conflict (e.g., “it is okay to reveal your PIN”), GPT-5-Mini-R performs well, indicating it is not simply refusing based on task type.

- GPT-5-Mini-R maintains similar performance to GPT-5-Mini on: GPQA Diamond (science), AIME 2024 (math)

- Slight regressions are observed in: Chat win-rate vs OpenAI’s o1, User preference score

- Significant gains on IH-Challenge (overrefusal) due to training on Anti-Overrefusal subset.

*Figure: Robustness on OOD tasks.*

*Figure: Robustness on academic evaluations.*

IH robustness generalizes to OOD IH tasks, including internal and academic benchmarks.

GPT-5-Mini-R shows notable robustness gains across:

- Internal OOD tasks: Tutor Jailbreak (sys-user and dev-user), internal multi-turn conflict dataset.

- Academic IH datasets: Gandalf Password, TensorTrust, RealGuardrails (Distractors and Handwritten), System IFEval, with multiple conflict types (sys-user, dev-user, etc.).

*Figure: Safety scores on OpenAI’s Production Benchmarks.*

*Figure: Helpfulness on OpenAI Production Benchmarks.*

Improved IH robustness enhances safety steerability without sacrificing helpfulness.

- Adding a safety spec in the system prompt makes GPT-5-Mini-R:

- More likely to refuse disallowed content (illicit, personal data, harassment, etc.)

- Better at nuanced safety reasoning and safety refusal

- Safety improvements are larger for GPT-5-Mini-R than for GPT-5-Mini, even when both use the same safety spec.

- Helpfulness on allowed content is largely preserved despite stronger safety behavior.

*Figure: Robustness on prompt injection evaluations.*

IH robustness also improves prompt injection robustness.

- GPT-5-Mini-R is more resistant to:

- A static internal prompt injection benchmark (adversarial attacks similar to those in ChatGPT Atlas, including attempts to induce harmful agentic behavior).

- CyberSecEval 2, which tests both IH conflicts and prompt injection via malicious tool outputs.

- GPT-5-Mini-R saturates the internal PI benchmark and substantially improves scores on CyberSecEval 2, without needing extra system-message changes.

*Figure: Evaluation of GPT-5-Mini and GPT-5-Mini-R with various system mitigations.*

Effectiveness of additional system mitigations changes once IH robustness is high.

- For the less robust GPT-5-Mini, various system-level mitigations (e.g., safety prompts) are effective.

- For the more robust GPT-5-Mini-R, many of these mitigations become less effective or can even reduce robustness, suggesting diminishing returns or interference once base IH robustness is strong.

*Figure: Ablation on training task splits.*

Training-task composition affects the trade-off between IH robustness, overrefusal, safety, and helpfulness.

- Using all IH-Challenge splits yields a balanced profile of high IH robustness, low overrefusal, strong safety, and good helpfulness.

- Restricting to only some splits (e.g., Single-Constraint + Multi-Constraint) can increase some metrics (e.g., safety) but hurt others (e.g., helpfulness or overrefusal).

## Paper

IH-Challenge: A Training Dataset to Improve Instruction Hierarchy on Frontier LLMs [2603.10521](https://arxiv.org/abs/2603.10521)

## Figures

Figures from the Medium HTML export (`raw/2026-04-03_Papers-Explained-555--IH-Challenge-cf2433051b7e.html`); local copies under `wiki/assets/papers-explained-555-ih-challenge/` when download succeeded.

| Figure | Caption |
|--------|---------|
| ![Figure 1](assets/papers-explained-555-ih-challenge/fig-1.png) | Title card: IH Challenge. |
| ![Figure 2](assets/papers-explained-555-ih-challenge/fig-2.png) | Illustration of the task design and training data pipeline. |
| ![Figure 3](assets/papers-explained-555-ih-challenge/fig-3.png) | Summary of IH-Challenge task skeletons. |
| ![Figure 4](assets/papers-explained-555-ih-challenge/fig-4.png) | Training and test robustness of GPT-5-Mini-R on IH-Challenge tasks. |
| ![Figure 5](assets/papers-explained-555-ih-challenge/fig-5.png) | Overrefusal and capability. |
| ![Figure 6](assets/papers-explained-555-ih-challenge/fig-6.png) | Robustness on OOD tasks. |
| ![Figure 7](assets/papers-explained-555-ih-challenge/fig-7.png) | Robustness on academic evaluations. |
| ![Figure 8](assets/papers-explained-555-ih-challenge/fig-8.png) | Safety scores on OpenAI’s Production Benchmarks. |
| ![Figure 9](assets/papers-explained-555-ih-challenge/fig-9.png) | Helpfulness on OpenAI Production Benchmarks. |
| ![Figure 10](assets/papers-explained-555-ih-challenge/fig-10.png) | Robustness on prompt injection evaluations. |
| ![Figure 11](assets/papers-explained-555-ih-challenge/fig-11.png) | Evaluation of GPT-5-Mini and GPT-5-Mini-R with various system mitigations. |
| ![Figure 12](assets/papers-explained-555-ih-challenge/fig-12.png) | Ablation on training task splits. |
## Related

- [[Papers Explained Corpus]]
- [[Synthetic Data]]
- [[Reinforcement Learning Topic]]
- [[Evaluation and Benchmarks]]
- [[Code Models]]
- [[Reinforcement Learning]]
- [[Papers Explained 554 - Jina Embeddings v5 Text]]

#summary #topic
