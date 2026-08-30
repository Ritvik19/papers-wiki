# Introducing SynthID Text

**Source**: `raw/synthid-text/full-article.md`, `raw/synthid-text/full-article.md`
**Ingested**: 2026-07-10
**Tags**: #summary

## Summary

A joint Google DeepMind / Hugging Face post announcing SynthID Text's integration into `transformers` v4.46.0: a text watermarking system that lets a model owner mark AI-generated text as such, imperceptibly to human readers but detectably to a trained classifier. The technique modifies the sampling step of generation using a pseudo-random "g-function" via tournament sampling, biasing token choices in a way invisible to a casual reader but statistically detectable in aggregate, without altering the underlying model's weights or materially degrading generation quality. It ships as a `SynthIDTextWatermarkingConfig` dataclass passed to `model.generate()` via a `watermarking_config=` argument, working with any causal LM through the standard `generate()` API with no model-specific changes.

Two configuration parameters govern the tradeoff between detectability and robustness: `keys` (20-30 recommended random integers used to compute g-function scores across the vocabulary; must be kept private, since a leaked key set lets others reproduce or strip the watermark) and `ngram_len` (default 5, minimum 2; larger values are more detectable but more brittle to text edits). Detection requires training a dedicated classifier per watermarking configuration (the post recommends ~10k+ labeled watermarked/non-watermarked examples); `transformers` ships a Bayesian detector class and an end-to-end training example, and models sharing a tokenizer and watermarking config can share one detector, uploadable to a private Hub repo for org-wide reuse.

The watermark is described as robust to some transformations (text cropping, minor word edits, mild paraphrasing) but has real limitations: it is less effective on factual, low-entropy responses (fewer tokens where sampling can be biased without hurting correctness), and detector confidence drops sharply under heavy rewriting or translation. The authors are explicit that SynthID Text is not designed to stop a motivated adversary outright: it raises the cost of passing off AI text as human-written and is meant to be combined with other provenance/detection approaches, not relied on alone.

## Key Claims

- SynthID Text watermarks generated text via a pseudo-random g-function applied during sampling (tournament sampling), imperceptible to humans but detectable by a trained classifier, without modifying the base model.
- Integrated into `transformers` v4.46.0 as `SynthIDTextWatermarkingConfig`, passed to any model's `model.generate()` via `watermarking_config=`; compatible with any causal LM without model-specific modification.
- Two required config parameters: `keys` (20-30 random integers recommended, must be kept private per model) and `ngram_len` (default 5, min 2; trades detectability against robustness to text changes).
- Detection needs a dedicated classifier per watermarking config, trained on ~10k+ watermarked/non-watermarked examples; `transformers` provides a Bayesian detector implementation and training walkthrough; detectors are shareable across models using the same tokenizer/config.
- Limitations: reduced watermark strength on factual/low-entropy text; detector confidence degrades significantly under heavy rewriting or cross-language translation; not designed to stop a determined adversary, intended as one layer in a broader AI-content-provenance toolkit.

## Figures

No figures were extracted for this ingest, per this batch's no-figure-download policy; the article is primarily prose and a code sample.

## Entities

- [[Hugging Face]] — ships the SynthID Text integration in `transformers` v4.46.0 and co-authors the post.
- [[DeepMind]] — Google DeepMind develops the underlying SynthID Text watermarking algorithm (published in Nature) and its Responsible GenAI Toolkit guidance.

## Questions & Gaps

- The post does not quantify the generation-quality cost of watermarking (e.g. perplexity or downstream-task delta) beyond stating the effect is designed to be minimal.
- No benchmark numbers are given for detector accuracy/AUC at the recommended ~10k-example training-set size; the post treats dataset size as a rule of thumb rather than a validated minimum.

## Related

- [[Text Watermarking]] — Core concept page on statistical, cryptographic, and sampling-based LLM watermarks.
- [[Tournament Sampling]] — Detailed algorithmic breakdown of the tournament selection and lightweight scoring scheme used in SynthID Text.
- [[How Claude Watermarks AI-Generated Text]] — Explains Anthropic's adoption of tournament sampling for production Claude watermarking.
- [[Nano Banana Pro]] — separately covers Google's SynthID watermarking applied to Gemini image generation, for comparison across modalities.
- [[Gemini 3.1 Flash TTS]], [[Gemini 3.1 Flash Live]] — also apply SynthID watermarking to audio/voice outputs.
