---
Source URL: https://openai.com/index/introducing-openai-privacy-filter/
Fetched via: WebFetch (curl returns 403 on openai.com/index/*)
Date: April 22, 2026
---

# Introducing OpenAI Privacy Filter

OpenAI's state-of-the-art model for masking personally identifiable information (PII) in text, released open-weight. Part of a broader effort to support a more resilient software ecosystem with practical infrastructure for building with AI safely.

Privacy Filter is a small model with frontier personal-data detection capability, designed for high-throughput privacy workflows with context-aware detection of PII in unstructured text. It can run locally so PII never has to leave the user's machine, and processes long inputs in a single efficient pass. OpenAI uses a fine-tuned version internally in its own privacy-preserving workflows. The released version achieves state-of-the-art performance on the PII-Masking-300k benchmark, when corrected for annotation issues identified during evaluation.

## A small model with frontier personal data detection capability

Traditional PII detection relies on deterministic rules for formats like phone numbers and emails, working well for narrow cases but missing subtler personal information and struggling with context. Privacy Filter combines strong language understanding with a privacy-specific labeling system to detect a wider range of PII in unstructured text, including context-dependent cases, and to better distinguish public information from information that should be masked.

## Model overview

Privacy Filter is a bidirectional token-classification model with span decoding: starts from an autoregressive pretrained checkpoint, adapted into a token classifier over a fixed taxonomy of privacy labels. It labels an input sequence in one forward pass, then decodes coherent spans with a constrained Viterbi procedure. Properties: fast (single forward pass), context-aware, long-context (supports up to 128,000 tokens), and configurable (tunable recall/precision tradeoff). The released model has 1.5B total parameters with 50M active parameters.

Predicts spans across eight categories: `private_person`, `private_address`, `private_email`, `private_phone`, `private_url`, `private_date`, `account_number`, `secret`. `account_number` covers banking info (credit card, bank account numbers); `secret` covers passwords and API keys. Labels decoded with BIOES span tags for cleaner masking boundaries.

## How it was built

1. Built a privacy taxonomy defining span types (personal identifiers, contact details, addresses, private dates, account numbers, secrets).
2. Converted a pretrained language model into a bidirectional token classifier by replacing the language-modeling head with a token-classification head, post-trained with a supervised classification objective.
3. Trained on a mixture of public and synthetic data; used model-assisted annotation/review where public labels were incomplete, and generated synthetic examples for format/context/subtype diversity.

At inference time, token-level predictions are decoded into coherent spans via constrained sequence decoding.

## Performance

On PII-Masking-300k, Privacy Filter achieves an F1 score of 96% (94.04% precision, 98.04% recall). On a corrected version of the benchmark accounting for identified dataset annotation issues, F1 is 97.43% (96.79% precision, 98.08% recall). Fine-tuning on even a small amount of domain-specific data quickly improves accuracy, increasing F1 from 54% to 96% and approaching saturation on the domain-adaptation benchmark evaluated. Also evaluated on secret detection in codebases and stress-tested across multilingual, adversarial, and context-dependent examples (model card).

## Limitations

Not an anonymization tool, compliance certification, or substitute for policy review in high-stakes settings; one component in a broader privacy-by-design system. Behavior reflects its trained label taxonomy and decision boundaries; different organizations may need different policies requiring in-domain evaluation or further fine-tuning. Performance may vary across languages, scripts, naming conventions, and out-of-distribution domains. Can miss uncommon identifiers or ambiguous private references, and over- or under-redact when context is limited, especially in short sequences; human review remains important in legal, medical, and financial workflows.

## Availability

Released under the Apache 2.0 license on Hugging Face and GitHub, intended for experimentation, customization, and commercial deployment, fine-tunable for different data distributions and privacy policies. Released alongside documentation covering architecture, label taxonomy, decoding controls, intended use cases, evaluation setup, and known limitations.
