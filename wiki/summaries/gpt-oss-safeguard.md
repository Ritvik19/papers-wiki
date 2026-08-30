# gpt-oss-safeguard

**Source**: `raw/introducing-gpt-oss-safeguard/full-article.md`, `raw/gpt-oss-safeguard-technical-report/full-article.md`
**Ingested**: 2026-07-10
**Tags**: #summary

## Summary

gpt-oss-safeguard is a research preview of two open-weight safety-reasoning models, released October 29, 2025 in 120b and 20b sizes and fine-tuned from the gpt-oss open models under the same Apache 2.0 license. Unlike a conventional safety classifier, which learns a decision boundary by training on thousands of manually labeled examples and never sees the policy behind those labels directly, gpt-oss-safeguard takes two inputs at once: a developer-written policy and the content to classify against it. It outputs a classification plus its chain of thought, so a developer can see how it reached that conclusion, and because the policy is supplied at inference time rather than baked in through training, developers can revise a policy without retraining the model. OpenAI positions this as most useful when harms are new or evolving and policies need to change quickly, when a risk area is too nuanced for a small trained classifier, when there are not enough labeled examples to train a dedicated classifier, or when latency matters less than getting an explainable, high-quality label.

gpt-oss-safeguard is an open-weight version of an internal OpenAI tool called Safety Reasoner, which was built through reinforcement fine-tuning that rewards a model for matching the judgments of human experts on policy-labeling tasks. Internally, OpenAI's primary reasoning models are trained through deliberative alignment, where the model learns safety policies directly and reasons about what is and is not safe, rather than only learning to imitate labeled outputs. In production, Safety Reasoner lets OpenAI update safety policy faster than retraining a classifier would allow, and OpenAI says the share of total compute devoted to safety reasoning has reached as high as 16% for some recent launches. It also runs step by step against image generation and Sora 2 outputs to block unsafe content as it is generated, working alongside faster, high-recall pre-filter classifiers in domains like biology and self-harm.

The technical report benchmarks the two model sizes against their gpt-oss base models and against the internal Safety Reasoner. On an internal multi-policy evaluation, where a model has to classify text correctly against every included policy at once, gpt-oss-safeguard and the internal Safety Reasoner beat gpt-5-thinking and the base gpt-oss models despite their smaller size. On a 2022 moderation dataset adapted for policy changes, gpt-oss-safeguard slightly outperformed every other tested model, including Safety Reasoner, though not by a statistically significant margin; on the public ToxicChat benchmark, Safety Reasoner beat gpt-5-thinking, and both of those marginally beat gpt-oss-safeguard. Because the models are open, someone could run them conversationally rather than as a policy classifier, so the report also confirms they meet OpenAI's chat-safety bar and reports an initial multi-language chat evaluation, separate from their intended policy-classification use.

Both sizes were fine-tuned from gpt-oss without additional biological or cybersecurity training data, so OpenAI treats the worst-case risk estimates already established for the base gpt-oss release as applying to gpt-oss-safeguard as well. OpenAI recommends developers use these models to classify content against a supplied policy rather than as a general-purpose conversational model, since the base gpt-oss models are better suited to that role. The models are text-only, work with the Responses API, support low/medium/high reasoning effort, support Structured Outputs, and were developed with input from ROOST, which separately launched a model community the same day to explore open models for protecting online spaces. Early testing partners included SafetyKit, ROOST, Tomoro, and Discord.

## Key Claims

- Released October 29, 2025, in two sizes: gpt-oss-safeguard-120b and gpt-oss-safeguard-20b, fine-tuned from gpt-oss, Apache 2.0 licensed, on Hugging Face.
- Classifies content against a developer-supplied policy at inference time, rather than a policy learned implicitly from labeled training examples.
- Exposes full chain-of-thought reasoning alongside its classification decision.
- Beats gpt-5-thinking and base gpt-oss models on an internal multi-policy accuracy evaluation despite smaller size.
- Slightly outperforms all tested models, including internal Safety Reasoner, on a 2022 moderation dataset adapted for policy changes (not a statistically significant gap versus Safety Reasoner).
- Underperforms gpt-5-thinking and Safety Reasoner, marginally, on the public ToxicChat benchmark.
- Trained without additional biological or cybersecurity data, so existing gpt-oss worst-case risk estimates are treated as applying to both sizes.
- In some recent OpenAI launches, safety reasoning has consumed as much as 16% of total compute.
- Developed with ROOST; early access partners included SafetyKit, Tomoro, and Discord.

## Figures

No article figures extracted; openai.com blocks direct HTML download so figures could not be downloaded, and WebFetch markdown does not preserve chart images.

## Entities

- [[OpenAI]]: developer of gpt-oss-safeguard.

## Questions & Gaps

- Neither raw source gives exact score numbers for the multi-policy accuracy, ToxicChat, or 2022-moderation-dataset comparisons, only relative rankings.
- The technical report's multilingual chat evaluation is mentioned but not quantified in the fetched source.
- The sources do not say how "research preview" status is expected to change before any full release.

## Related

- [[OpenAI]]
- [[Safety and Alignment]]
- [[Reasoning Models]]
- [[Papers Explained 493 - gpt oss safeguard]]
