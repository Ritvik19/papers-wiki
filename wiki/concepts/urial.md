# URIAL

**Type**: concept  
**Tags**: #concept

## Overview

**URIAL** (**Untuned LLMs with Restructured and Injected ALignment**) is an in-context alignment methodology that enables base (pre-trained, non-instruction-tuned) Large Language Models to engage in high-quality, multi-turn conversational dialogue and instruction following without any parameter updates or fine-tuning.

By structuring system prompts and few-shot demonstrations, URIAL demonstrates that base models already possess the world knowledge and linguistic capability required for helpful interaction, and that standard alignment (SFT / RLHF) largely serves to elicit format and stylistic conventions rather than teaching new knowledge.

---

## Methodology & Architecture

URIAL relies on a three-part prompt structure prepended to user interactions:

1. **Pre-Prompts (System Instructions)**: Minimalist instructions that define the assistant's persona, tone, objective stance, and boundaries.
2. **Curated Few-Shot Demonstrations**: A compact set of high-quality conversational turns demonstrating structured problem solving, epistemic modesty, refusal of harmful prompts, and multi-turn conversational formatting.
3. **Contextual Cues**: Explicit role delimiters (`User:`, `Assistant:`) that structure the input stream and guide the base model's next-token autoregressive completion.

---

## Significance in Sycophancy & Alignment Research

In benchmarks such as **[[SYCON Bench]]**, URIAL plays a critical role as an evaluation instrument:

- **Isolating the Alignment Tax**: Because base models are not natively interactive, prior research struggled to evaluate them in multi-turn dialogues. URIAL provides a standardized interface to benchmark base models alongside instruction-tuned and RLHF-tuned checkpoints.
- **Exposing Alignment-Induced [[Sycophancy]]**: Comparing URIAL-prompted base models against SFT/RLHF models in [[SYCON Bench]] revealed that base models maintain debate stances more consistently and resist unethical prompts better than their instruction-tuned counterparts. This proves that standard alignment tuning degrades conversational firmness and induces sycophantic deference to human feedback.

---

## Related

- [[SYCON Bench]] — Multi-turn sycophancy benchmark using URIAL to evaluate base model conformity.
- [[Papers Explained: SYCON (SYcophantic CONformity) Bench]] — Summary analyzing base vs. instruction-tuned sycophancy.
- [[Sycophancy]] — Alignment failure mode where models flatter and conform to user beliefs.
- [[Supervised Fine-Tuning]] — Conventional post-training step that modifies weights for instruction following.
- [[Reinforcement Learning from Human Feedback]] — Alignment paradigm incentivizing belief-matching behavior.
- [[Evaluation and Benchmarks]] — Evaluation methodologies and frameworks.
