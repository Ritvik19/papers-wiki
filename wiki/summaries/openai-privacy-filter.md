# OpenAI Privacy Filter

**Source**: `raw/introducing-openai-privacy-filter/full-article.md`
**Ingested**: 2026-07-10
**Tags**: #summary

## Summary

OpenAI Privacy Filter is an open-weight model released April 22, 2026 that masks personally identifiable information (PII) in text before it reaches a language model. It targets a gap in traditional PII detection, which relies on deterministic rules for structured formats like phone numbers and emails and consequently misses subtler, context-dependent personal information. Privacy Filter combines language understanding with a dedicated privacy-labeling scheme to catch a wider range of PII in unstructured text and to better tell public information apart from information that should be masked. It can run locally, so PII never has to leave a user's machine, and OpenAI says it uses a fine-tuned internal version in its own privacy-preserving workflows.

Architecturally, Privacy Filter is a bidirectional token-classification model with span decoding. It starts from an autoregressive pretrained checkpoint, which is then adapted into a token classifier over a fixed taxonomy of eight privacy labels: `private_person`, `private_address`, `private_email`, `private_phone`, `private_url`, `private_date`, `account_number`, and `secret` (the last two covering banking details and credentials such as passwords or API keys). It labels an entire input sequence in a single forward pass, then decodes coherent spans using a constrained Viterbi procedure and BIOES tagging, supports inputs up to 128,000 tokens, and exposes a tunable recall/precision tradeoff. The released model has 1.5B total parameters with 50M active parameters. Training combined public and synthetic data, using model-assisted annotation and review where public labels were incomplete, and generating synthetic examples for format, context, and subtype diversity.

On the PII-Masking-300k benchmark, Privacy Filter reaches an F1 score of 96% (94.04% precision, 98.04% recall); on a version of the benchmark corrected for identified annotation issues, F1 rises to 97.43% (96.79% precision, 98.08% recall), which OpenAI describes as state of the art. Fine-tuning on a small amount of domain-specific data improves results quickly: F1 on the domain-adaptation benchmark evaluated goes from 54% to 96% and nearly saturates. OpenAI also evaluated secret detection in codebases and stress-tested the model across multilingual, adversarial, and context-dependent examples, with more detail in the accompanying model card.

OpenAI states that Privacy Filter is not an anonymization tool, a compliance certification, or a substitute for policy review in high-stakes settings, but one component in a broader privacy-by-design system. Behavior follows the trained label taxonomy and decision boundaries, so different organizations may need in-domain evaluation or further fine-tuning for their own policies, and performance can vary across languages, scripts, and naming conventions, or when a private reference is ambiguous or uncommon. The model is released under the Apache 2.0 license on Hugging Face and GitHub, along with documentation covering architecture, label taxonomy, decoding controls, intended use, evaluation setup, and known limitations.

## Key Claims

- Released April 22, 2026, open-weight, Apache 2.0 licensed, on Hugging Face and GitHub.
- 1.5B total parameters, 50M active parameters; bidirectional token-classification model with Viterbi span decoding.
- Detects eight PII categories: private_person, private_address, private_email, private_phone, private_url, private_date, account_number, secret.
- Supports inputs up to 128,000 tokens in a single forward pass; can run entirely locally.
- F1 of 96% on PII-Masking-300k (94.04% precision, 98.04% recall); 97.43% F1 on a corrected version of the benchmark.
- Fine-tuning on domain-specific data raises F1 from 54% to 96% on the domain-adaptation benchmark tested.
- Not intended as a full anonymization or compliance tool; explicitly one layer in a larger privacy-by-design approach.

## Figures

No article figures extracted; openai.com blocks direct HTML download so figures could not be downloaded, and WebFetch markdown does not preserve chart images.

## Entities

- [[OpenAI]]: developer of Privacy Filter.

## Questions & Gaps

- The article does not name the specific pretrained base model Privacy Filter's checkpoint derives from.
- No latency or throughput numbers are given to support the "high-throughput" claim.

## Related

- [[OpenAI]]
- [[Safety and Alignment]]
- [[Papers Explained - OpenAI Privacy Filter]]
