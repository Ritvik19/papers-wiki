# Chain of Thought Controllability

**Source**: `raw/reasoning-models-chain-of-thought-controllability/full-article.md`
**Ingested**: 2026-07-10
**Tags**: #summary

## Summary

OpenAI studied how well reasoning models can deliberately control the content of their own chain of thought (CoT), and found that current frontier models are bad at it, which the paper frames as a good outcome for AI safety rather than a limitation to fix. OpenAI's defense-in-depth safety approach layers several complementary methods: safety training, behavioral testing, agentic code review, and CoT monitoring, where an agent's reasoning steps are analyzed to help catch unsafe or misaligned behavior during training and deployment. Current model reasoning is generally interpretable and easy to monitor, but that could change. This work looks at one specific way monitorability could break down: whether a model that can deliberately reshape or obscure its own reasoning, once it knows it is being monitored, could make evaluations overestimate how aligned or safe it actually is.

The paper defines CoT controllability as a reasoning model's ability to control properties of its own chain of thought in ways that reduce monitorability. As a practical, measurable proxy for a model trying to evade a monitor under realistic incentives, the researchers test whether a model can follow user instructions about its own CoT, such as using only lowercase letters, avoiding a specific keyword, or appending a specific phrase, rather than just changing its final visible answer. To measure this at scale, OpenAI built CoT-Control, an open-source evaluation suite of more than 13,000 tasks drawn from GPQA, MMLU-Pro, HLE, BFCL, and SWE-bench Verified, each task pairing a benchmark problem with one instruction about the CoT that produces its answer. A model's CoT-Control score is the fraction of these paired tasks where it both solves the underlying problem and successfully follows the CoT instruction, so the score functions as a percentage of instructed-CoT tasks in which the model's reasoning was successfully controlled to the given specification.

Across 13 reasoning models evaluated, all of them struggled to reliably control their CoTs: controllability scores ranged as low as 0.1% and did not exceed 15.4% for any current frontier model tested. Models often noticed within their own CoT that they were failing to comply with an instruction, and then kept failing anyway; one example given is GPT-5.2 Thinking, told not to use the word "XOR" in its reasoning, using the word repeatedly while explicitly noticing and reacting to the violation as it happened. This low overall performance is what makes the result reassuring for monitorability: if models cannot reliably steer their own reasoning even when explicitly told what to avoid, they likely also lack the ability to deliberately obfuscate their reasoning well enough to fool a monitor. Controllability increases with model scale within open-weight model families, tapering off at larger sizes, but decreases as models reason for longer and as they undergo more reinforcement learning post-training. For one model, OLMo-3-7B-RL-Zero-Math, controllability dropped by more than a factor of ten over the course of RL training. Telling a model outright that it is being monitored or evaluated only slightly increases its controllability, and automated prompt optimization can raise controllability against a training set of instructions but transfers poorly to new instruction types it was not optimized against.

The authors note that CoT-Control tasks are practical proxies, not a direct test of whether a model that is naturally pursuing a misaligned goal could control its CoT well enough to evade a real monitor, and the suite covers only a narrow set of controllability types, so it may over- or underestimate true controllability. Even so, the paper argues that low CoT controllability is a feature rather than a bug: it makes CoT monitoring a more trustworthy safeguard, though it is not sufficient on its own to guarantee monitorability, since monitorability could still degrade through other mechanisms, such as directly optimizing training against the visible CoT. OpenAI frames CoT controllability evaluations as a canary eval, an early warning sign for whether models are getting better at shaping or hiding their reasoning over time, and plans to report CoT controllability alongside CoT monitorability in system cards for future frontier models, starting with GPT-5.4 Thinking, consistent with its stated commitment not to apply optimization pressure directly to frontier reasoning models' CoTs. The paper is authored by Tomek Korbak, Micah Carroll, Bowen Baker, and Ian Kivlichan.

## Key Claims

- CoT controllability is defined as a reasoning model's ability to control properties of its own chain of thought in ways that would reduce how monitorable that reasoning is.
- CoT-Control, OpenAI's open-source evaluation suite for this, has over 13,000 tasks built from GPQA, MMLU-Pro, HLE, BFCL, and SWE-bench Verified, each pairing a benchmark problem with one CoT instruction; a model's score is the percentage of such tasks where it both solves the problem and follows the CoT instruction.
- Across 13 reasoning models tested, controllability scores ranged from 0.1% to at most 15.4%, meaning no current frontier model reliably controls its own CoT even when explicitly instructed to.
- Models frequently recognize mid-reasoning that they are violating an instruction and continue to violate it anyway (documented for GPT-5.2 Thinking and the word "XOR").
- Controllability rises with scale within open-weight model families but falls with longer reasoning and more RL post-training; one model, OLMo-3-7B-RL-Zero-Math, lost more than 10x controllability over RL training.
- Telling a model it is being monitored only slightly raises its controllability, and prompt-optimized controllability gains transfer poorly to new instruction types.
- OpenAI treats low controllability as reassuring for CoT monitorability, and plans to report CoT controllability scores alongside CoT monitorability scores in system cards starting with GPT-5.4 Thinking.

## Figures

No article figures extracted; openai.com blocks direct HTML download so figures could not be downloaded, and WebFetch markdown does not preserve chart images.

## Entities

- [[OpenAI]]: built the CoT-Control suite and ran the evaluation across 13 reasoning models, including its own.

## Questions & Gaps

- The source does not list all 13 reasoning models evaluated beyond the two named examples (GPT-5.2 Thinking and OLMo-3-7B-RL-Zero-Math).
- It does not specify whether or how controllability scores are broken down by CoT length (for example, by token count) in the reported ranges; later system cards that cite CoT-Control results by token-length bucket appear to build on this methodology without that detail being given here.
- The paper's own limitations section notes that CoT-Control measures only a narrow set of controllability types, so it is unclear how well the 0.1% to 15.4% range would generalize to instruction types outside the suite.

## Related

- [[OpenAI]]
- [[Reasoning Models]]
- [[Safety and Alignment]]
- [[Evaluation and Benchmarks]]
- [[Chain of Thought Monitorability]]: a related but distinct concept. This page covers whether a model can deliberately steer its CoT, while chain-of-thought monitorability concerns whether a model's CoT remains legible and useful for outside observers to monitor in the first place.
