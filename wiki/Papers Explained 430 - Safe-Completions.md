# Papers Explained 430 - Safe-Completions

Large Language Models used in ChatGPT have traditionally been trained to learn a refusal boundary: depending on the user’s intent, the model is taught to either fully comply or outright refuse.

This page ingests the source article into the wiki and connects it to [[Papers Explained Corpus]], [[Safety and Alignment]], [[Large Language Models]], [[Reinforcement Learning Topic]], [[Supervised Fine-Tuning]], [[Reinforcement Learning]].

## Source Metadata

- Source file: `raw/2025-08-13_Papers-Explained-430--Safe-Completions-a8e8176bcc9b.html`
- Source title: Papers Explained 430: Safe-Completions
- Published: 2025-08-13
- Canonical: [https://medium.com/@ritvik19/papers-explained-430-safe-completions-a8e8176bcc9b](https://medium.com/@ritvik19/papers-explained-430-safe-completions-a8e8176bcc9b)

## Key Ideas

- As an alternative, safe-completions are proposed: a safety-training approach that centers on the safety of the assistant’s output, rather than a binary classification of the user’s intent.
- This approach was incorporated into GPT-5 and finds that across both production comparisons and internally controlled experiments, safe-completion training improves safety (especially on dual-use prompts), reduces the severity of residual safety failures, and...
- Safe-completion training builds on top of Deliberative Alignment (DA), a safety-training method used to teach models to reason over content policies when replying to unsafe prompts (used for OpenAI o1 and o3).
- However, whereas the augmented prompt in DA instructs the model to decide whether to comply or refuse and then answer accordingly, the model is instead trained to select one of three response modes:
- Direct answer: fully address the user’s query when it is purely harmless and poses no material risk;

## Notes

Large Language Models used in ChatGPT have traditionally been trained to learn a refusal boundary: depending on the user’s intent, the model is taught to either fully comply or outright refuse. While this is a strong mitigation for explicitly malicious prompts, focusing safety training on refusals can lead to brittleness for prompts with obscured user intent.

As an alternative, safe-completions are proposed: a safety-training approach that centers on the safety of the assistant’s output, rather than a binary classification of the user’s intent.

This approach was incorporated into GPT-5 and finds that across both production comparisons and internally controlled experiments, safe-completion training improves safety (especially on dual-use prompts), reduces the severity of residual safety failures, and substantially increases model helpfulness.

## Method

*Figure: Left: Overall structure of the safe-completion training stack. Right: Details of the safecompletion reward design.*

Safe-completion training builds on top of Deliberative Alignment (DA), a safety-training method used to teach models to reason over content policies when replying to unsafe prompts (used for OpenAI o1 and o3). As in DA, the mitigation proceeds over two main post-training stages: a Supervised Fine-Tuning (SFT) stage which instills the correct initial behavior, and a Reinforcement Learning (RL) stage.

### SFT Stage

The SFT stage supervises ideal (CoT, answer) pairs for a safety-related prompt. Following DA, the prompt is first augmented with the policy spec and an instruction to consult the spec before answering. This augmented input is then passed to a base reasoning model and the resulting spec-aware CoT and answer are recorded. The final SFT training example uses the original (unaugmented) prompt as input and the collected (CoT, answer) as the supervised target. Since the CoT references the spec, the SFT stage teaches the model to reason over the spec itself before answering. As in DA, SFT examples with unsafe answers are filtered using a “judge” reasoning model with access to the spec.

However, whereas the augmented prompt in DA instructs the model to decide whether to comply or refuse and then answer accordingly, the model is instead trained to select one of three response modes:

- Direct answer: fully address the user’s query when it is purely harmless and poses no material risk;

- Safe-completion: provide high-level, non-operational, and within-safety-constraint guidance when the content is restricted but not outright disallowed;

- Refuse with redirection: courteously decline when the request cannot be safely fulfilled even in part, while offering a brief rationale and constructive alternatives.

### RL Stage

In the RL stage of safe-completions, the model is rewarded for being helpful as long as its output is within safety constraints. For each safety-related prompt and sampled response, two reward models (RMs) are queried, each outputting scores normalized to [0,1]:

- Safety (si ∈[0, 1]): This score reflects the degree to which the output adheres to the content policy specification. Perfectly compliant responses receive si = 1, severe or definitive violations receive si = 0, and intermediate values reflect borderline, low-severity violations.

- Helpfulness (hi ∈[0, 1]): This score measures the response’s helpfulness to the user, considering both direct and indirect helpfulness. The helpfulness RM outputs a single score that accounts for both types.

- Direct helpfulness: The degree to which the response directly fulfills the user’s stated task.

- Indirect helpfulness: How well the response supports the user’s underlying well-being and goals by offering clear, constructive, and relevant alternatives, as well as transparent, well-reasoned refusals.

Both RMs assign rewards based on the prompt and the assistant’s final response. The final reward is computed as ri = hi·si.

## Experiments

To evaluate and compare both the safety training paradigms: refusal training and safe-completion training:

- Controlled Experiments (CE): Compared CE-Refusal (refusal-oriented objectives) with CE-SafeComplete (safe-completion stack), keeping architecture, pretraining, and post-training recipe constant.

- Production Models: Compared o3 (refusal training) with GPT-5 Thinking (gpt5-r, safe-completion training), acknowledging differences in architecture, data, and capability.

*Figure: Evaluation rubrics.*

*Figure: Safety and helpfulness given safe outputs broken down by user intent.*

- Controlled Experiments: CE-SafeComplete improved safety on dual-use prompts and maintained similar safety levels on benign and malicious prompts compared to CE-Refusal. It also yielded small but significant helpfulness gains for benign and dual-use cases, and a major improvement (over 1.0 point on the 1–4 scale) on malicious prompts, by offering safety cautions, alternatives, and relevant information instead of hard refusals.

- Production Models: gpt5-r improved safety across all intents compared to o3, with particularly large gains on dual-use (9 percentage points) and malicious (10 percentage points) prompts. Helpfulness also increased across all intents without sacrificing safety.

- Stronger Models: The safe-completion pipeline appears especially well-suited to stronger models like GPT-5, which effectively learn how to safe-complete.

- Harm Categories: Safe-completion models (CE-SafeComplete and gpt5-r) generally improved or maintained safety across various harm categories (Illicit, Erotic, Hate, Sensitive Information) and intents, with pronounced helpfulness lifts on malicious prompts.

*Figure: Harmfulness distribution among unsafe responses, by user intent.*

- When failures (unsafe responses) did occur, the safe-completion stack (CE-SafeComplete, gpt5-r) shifted the distribution of harmfulness away from Moderate/High severity towards Low/Negligible severity compared to refusal-oriented baselines.

- This reduction in high severity was most visible on Malicious prompts, while Benign and Dual-use prompts saw a shift from Moderate to Low/Negligible.

- Conclusion: Safe-completion models tend to fail “softer,” producing less actionable, lower-severity content, which complements binary safety gains by attenuating residual risk when unsafe outputs occur.

## Paper

[From Hard Refusals to Safe-Completions: Toward Output-Centric Safety Training](https://cdn.openai.com/pdf/be60c07b-6bc2-4f54-bcee-4141e1d6c69a/gpt-5-safe_completions.pdf)

## Figures

Figures from the Medium HTML export (`raw/2025-08-13_Papers-Explained-430--Safe-Completions-a8e8176bcc9b.html`); local copies under `wiki/assets/papers-explained-430-safe-completions/` when download succeeded.

| Figure | Caption |
|--------|---------|
| ![Figure 1](assets/papers-explained-430-safe-completions/fig-1.png) | Title card: Safe-Completions. |
| ![Figure 2](assets/papers-explained-430-safe-completions/fig-2.png) | Left: Overall structure of the safe-completion training stack. Right: Details of the safecompletion reward design. |
| ![Figure 3](assets/papers-explained-430-safe-completions/fig-3.png) | Evaluation rubrics. |
| ![Figure 4](assets/papers-explained-430-safe-completions/fig-4.png) | Safety and helpfulness given safe outputs broken down by user intent. |
| ![Figure 5](assets/papers-explained-430-safe-completions/fig-5.png) | Harmfulness distribution among unsafe responses, by user intent. |
## Related

- [[Papers Explained Corpus]]
- [[Safety and Alignment]]
- [[Large Language Models]]
- [[Reinforcement Learning Topic]]
- [[Supervised Fine-Tuning]]
- [[Reinforcement Learning]]
- [[Papers Explained 429 - GPT-5]]
- [[Papers Explained 431 - Anatomy of a Machine Learning Ecosystem]]

#summary #topic
