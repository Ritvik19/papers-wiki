# Papers Explained 493: gpt oss safeguard

Papers Explained 493: gpt oss safeguard

Papers Explained 493: gpt oss safeguard

gpt-oss-safeguard-120b and gpt-oss-safeguard-20b are two open-weight reasoning models post-trained from the gpt-oss models. These models…

Papers Explained 493: gpt oss safeguard

gpt-oss-safeguard-120b and gpt-oss-safeguard-20b are two open-weight reasoning models post-trained from the gpt-oss models. These models are trained to reason from a provided policy in order to label content under that policy. They are fine-tunes of their gpt-oss counterparts, and were trained without any additional biological or cybersecurity data.

The models are available on HuggingFace. User Guide is available here.

gpt-oss-safeguard enables developers to draw the policy lines that best fit their use case. The model takes two inputs at once: a policy and the content to classify under that policy. The model outputs a conclusion about where the content falls, along with its reasoning. Developers decide how, if at all, to use those conclusions in their own safety pipelines.

This reasoning-based approach performs especially well in situations where:

The potential harm is emerging or evolving, and policies need to adapt quickly.
The domain is highly nuanced and difficult for smaller classifiers to handle.
Developers don’t have enough samples to train a high-quality classifier for each risk on their platform.
Latency is less important than producing high-quality, explainable labels.

System-Level Safety

The core philosophy for safety is “defense in depth,” which involves training models to respond safely and implementing additional layers of protection to detect and address potentially unsafe inputs and outputs according to predefined policies. Safety classifiers are a primary layer of defense, distinguishing safe from unsafe content in specific risk areas.

These classifiers are built by manually curating thousands of examples of safe and unsafe content, based on pre-defined safety policies. The classifier then learns to differentiate safe from unsafe outputs by inferring the underlying policy from these labeled examples, identifying similarities in unsafe content and differences between safe and unsafe content.

Pros: They can achieve high performance with low latency and operating costs.
Cons: Gathering sufficient training examples is time-consuming and costly. Any update or change to the safety policy necessitates re-training the entire classifier, which is inefficient.

gpt-oss-safeguard represents a significant departure from traditional classifiers due to its reasoning capabilities.

Direct Policy Application: Developers can apply any policy, including custom-written ones or those from external sources, directly to the model.
Generalization: Its reasoning abilities help the model generalize effectively over newly written policies.
Broader Utility: Beyond safety policies, gpt-oss-safeguard can be used to label content in other ways relevant to specific products and platforms.

The principles behind gpt-oss-safeguard were developed internally in a tool called Safety Reasoner.

Development of Safety Reasoner began with reinforcement fine-tuning on policy labeling tasks.

The model was rewarded for accurately mirroring judgments made by human experts, which taught it to reason about how a policy leads to a specific judgment.

Deliberative Alignment is the internal approach where primary reasoning models directly learn safety policies and use their reasoning capabilities to determine what is safe. This method significantly improves upon earlier safety training, making reasoning models safer across multiple dimensions, even as their overall capabilities grow.

Safety Classification Performance

Internal Evaluation: Models were tested on multi-policy accuracy by simultaneously providing multiple policies at inference time. Accuracy required an exact match to golden set labels for all included policies.
Internal moderation evaluation (multi-policy accuracy).
gpt-oss-safeguard models and internal-safety-reasoner outperformed gpt-5-thinking and gpt-oss open models on multi-policy accuracy. internal-safety-reasoner achieved the highest score (52.2%). The gpt-oss-safeguard models outperforming gpt-5-thinking was noted as surprising given their smaller size.

External Evaluation: Models were evaluated on a 2022 moderation dataset (using adapted internal safety policies) and on ToxicChat, a public benchmark (using a hand-written prompt adapted from internal policies).
OpenAI Moderation API and ToxicChat evaulations.
OpenAI Moderation API (2022) Evaluation: gpt-oss-safeguard models slightly outperformed all other tested models, including internal-safety-reasoner and gpt-5-thinking, though the difference with Safety Reasoner was not statistically significant.
ToxicChat Evaluation: internal-safety-reasoner outperformed gpt-5-thinking, and both marginally outperformed gpt-oss-safeguard models.

Multilingual Performance

The evaluation was conducted using the MMMLU eval, which is a professionally human-translated version of MMLU available in 14 languages.
MMMLU evaluation.
The gpt-oss-safeguard models perform at parity with gpt-oss models across all reasoning levels (low, medium, high) in multilingual contexts.

Observed safety challenges and mitigations

Disallowed Content Evaluation

Evaluated using “Standard Disallowed Content Evaluations” (an older, saturated benchmark) and “Production Benchmarks” (a new, more challenging, multi-turn evaluation set representative of production data). LLM-based grading models were used to evaluate completions, with the metric not_unsafe checking for unsafe output according to OpenAI policy.
Standard Disallowed Content Evaluation.Production Benchmarks.
Standard Disallowed Content Evaluations are saturated and no longer provide useful signal for incremental safety progress, leading to the development of the more challenging Production Benchmarks.
gpt-oss-safeguard-120b and gpt-oss-safeguard-20b generally perform on par with their gpt-oss counterparts on both standard and production benchmarks.
Minor degradations were observed in certain categories of the Production Benchmarks for safeguard models, but they also outperformed gpt-oss models in other categories.

Jailbreak Evaluation

The StrongReject approach was used, which inserts known jailbreaks into safety refusal examples.

Evaluations were conducted across several harm categories using the same policy graders as disallowed content checks, measuring not_unsafe.
Jailbreak evaluations.
Robustness to jailbreaks is considered less critical for gpt-oss-safeguard models due to their recommended internal-only use cases.
gpt-oss-safeguard-120b outperforms gpt-oss-120b, while gpt-oss-safeguard-20b underperforms gpt-oss-20b by 1–5 points.

Instruction Hierarchy Evaluation

Models were post-trained with a harmony prompt format incorporating system, developer, and user messages. Evaluations involved scenarios with conflicting messages (e.g., System prompt extraction, Prompt injection hijacking) and tests for phrase/password protection against user message attempts.
Instruction Hierarchy Evaluation — System User message conflict.Instruction Hierarchy Evaluation — Phrase and Password Protection.
Adherence to an Instruction Hierarchy is less important for gpt-oss-safeguard models given their intended internal use.
The gpt-oss-safeguard models tend to underperform their gpt-oss counterparts in instruction hierarchy evaluations, and further research is needed to understand this discrepancy.

Hallucination Evaluation

Evaluations were performed without giving models internet browsing ability. Used “SimpleQA” (a diverse dataset of fact-seeking questions) and “PersonQA” (a dataset of questions about publicly available facts about people). Metrics included accuracy (higher is better) and hallucination rate (lower is better).
Hallucination evaluations.
gpt-oss-safeguard models generally perform on par with their gpt-oss counterparts on SimpleQA and PersonQA evaluations.
gpt-oss-safeguard-120b is slightly more prone to hallucinating than gpt-oss-120b on both evaluations.
gpt-oss-safeguard-20b is more prone to hallucinating on PersonQA but less so on SimpleQA compared to gpt-oss-20b.

Fairness and Bias Evaluation

Models were evaluated using the BBQ evaluation.
BBQ evaluation.
Both gpt-oss-safeguard models outperform their gpt-oss counterparts across all metrics in the BBQ evaluation.

Paper

Technical Report: Performance and baseline evaluations of gpt-oss-safeguard-120b and gpt-oss-safeguard-20b

Hungry for more insights?

Don’t miss out on exploring other fascinating threads in this series. Simply click here and uncover the state-of-the-art research!

Do Subscribe for weekly updates!!

By Ritvik Rastogi on November 17, 2025.

Canonical link

Exported from Medium on May 4, 2026.
