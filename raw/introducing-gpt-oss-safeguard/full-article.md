---
Source URL: https://openai.com/index/introducing-gpt-oss-safeguard/
Fetched via: WebFetch (curl returns 403 on openai.com/index/*)
Date: October 29, 2025
---

# Introducing gpt-oss-safeguard

New open safety reasoning models (120b and 20b) that support custom safety policies.

A research preview of gpt-oss-safeguard, open-weight reasoning models for safety classification, in two sizes: `gpt-oss-safeguard-120b` and `gpt-oss-safeguard-20b`. Fine-tuned from the gpt-oss open models, released under the same Apache 2.0 license, downloadable from Hugging Face.

The models use reasoning to directly interpret a developer-provided policy at inference time, classifying user messages, completions, and full chats according to the developer's needs. The developer decides the policy; the model exposes its chain-of-thought so the developer can review how it reached its decision. Because the policy is supplied at inference time rather than trained in, developers can iteratively revise policies without retraining. This is more flexible than the traditional approach of training a classifier to indirectly infer a decision boundary from labeled examples.

The model takes two inputs simultaneously (a policy and content to classify under it) and outputs a conclusion plus reasoning. This reasoning-based approach performs especially well when: the potential harm is emerging or evolving and policies need to adapt quickly; the domain is nuanced and hard for smaller classifiers; there aren't enough samples to train a high-quality classifier per risk; or latency matters less than explainable, high-quality labels.

Developed over months with ROOST to identify developer needs, test the model, and produce documentation. ROOST is launching a model community (RMC) the same day to explore open AI models for protecting online spaces. A companion technical report details safety performance.

## System-level safety: the role of safety classifiers

OpenAI's defense-in-depth approach trains models to respond safely and adds additional layers to detect and address unsafe inputs/outputs. Traditional safety classifiers (e.g. via the Moderation API) are trained on manually curated examples under a policy the classifier never directly sees; it infers the policy from patterns in labeled data. This can have low latency and cost but requires time-consuming, costly data collection, and updating the policy requires retraining.

gpt-oss-safeguard's reasoning lets developers apply any policy, including self-written ones, and generalize to newly written policies without retraining. It can also label content for non-safety purposes relevant to specific products.

## How OpenAI uses safety reasoning internally

OpenAI's primary reasoning models learn safety policies directly and reason about what's safe, an approach called **deliberative alignment**, which improves on earlier safety training and makes reasoning models safer on several axes even as capability increases. gpt-oss-safeguard is an open-weight implementation of an internal tool called **Safety Reasoner**, developed via reinforcement fine-tuning on policy-labeling tasks that reward the model for mirroring correct judgments from human experts.

Safety Reasoner lets OpenAI dynamically update safety policies in production faster than retraining a classifier would take. New model launches often start with stricter policies and heavier compute for Safety Reasoner, then relax as understanding of production risk improves; in some recent launches, the fraction of total compute devoted to safety reasoning has been as high as 16%. Safety Reasoner performs dynamic, step-wise evaluation of image generation and Sora 2 outputs to block unsafe generations in real time; in domains like biology and self-harm, fast high-recall classifiers first determine relevant content, then Safety Reasoner reviews it against a detailed taxonomy, forming part of the layered safeguards across GPT‑5 and ChatGPT Agent.

## Performance

In an internal multi-policy evaluation (correctly classifying text under all included policies simultaneously), gpt-oss-safeguard models and the internal Safety Reasoner outperform gpt-5-thinking and the gpt-oss open models, despite gpt-oss-safeguard's small size. On the 2022 moderation dataset (adapted for policy changes), gpt-oss-safeguard slightly outperformed all other tested models including Safety Reasoner and gpt-5-thinking (not statistically significant versus Safety Reasoner). On ToxicChat (a public benchmark from an open-source chatbot), Safety Reasoner outperformed gpt-5-thinking, while gpt-5-thinking and Safety Reasoner both marginally outperformed the gpt-oss-safeguard models.

## Limitations

Classifiers trained on tens of thousands of labeled samples can still outperform gpt-oss-safeguard reasoning directly from policy; dedicated classifiers may be preferred for complex risks needing higher performance. gpt-oss-safeguard can be time- and compute-intensive, challenging to scale across all platform content; internally mitigated by using smaller/faster pre-filter classifiers and, in some cases, running Safety Reasoner asynchronously.

## Availability

Iterated with trust and safety specialists at SafetyKit, ROOST, Tomoro, and Discord during early testing. Downloadable from Hugging Face.
