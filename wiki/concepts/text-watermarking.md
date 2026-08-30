# Text Watermarking

**Type**: concept  
**Tags**: #concept

## Overview

**Text Watermarking** refers to a class of algorithmic techniques that embed imperceptible statistical or cryptographic signals directly into language model token outputs during the generation (sampling) stage. The objective is to enable mathematical verification of AI-generated provenance by authorized detectors while remaining undetectable to human readers and preserving output fluency, accuracy, and perceptual quality.

## Core Paradigms

### 1. Green-List / Red-List Logit Biasing (Kirchenbauer et al., 2023)
- Divides the vocabulary $V$ at step $t$ into a pseudo-random "green list" $G_t \subset V$ and "red list" $R_t \subset V$, partitioned deterministically by hashing the preceding token $x_{t-1}$.
- A constant bias $\delta > 0$ is added to the unnormalized logits of all tokens in $G_t$ before Softmax.
- During detection, a $z$-score hypothesis test evaluates whether the count of green tokens in a text snippet of length $T$ significantly exceeds the random expectation $|G_t| / |V| \approx 0.5$.
- *Limitation*: The constant logit perturbation $\delta$ shifts the output probability distribution, which can increase perplexity and degrade generation quality on nuanced or creative prompts.

### 2. Pseudorandom Transform Sampling (Aaronson & Christiano)
- Employs a secret cryptographic key $K$ and a hash of the preceding $h$-token context window $x_{t-h:t-1}$ to initialize a pseudorandom number generator (PRNG).
- Uses the PRNG output $u_t \sim \text{Uniform}(0, 1)$ to draw from the model's exact Softmax distribution via the Gumbel-max trick or inverse CDF transform:
  $$x_t = \arg\max_{w \in V} \left( \frac{z_w}{T} - \log(-\log(u_w)) \right)$$
- Preserves the model's true token distribution (zero theoretical distribution distortion).
- *Limitation*: Standard pseudorandom detection requires knowing the original logit vector $z$, necessitating an expensive LLM forward pass over the entire text during verification.

### 3. Tournament Sampling & Fast Keyed Scoring (SynthID Text / Claude)
- Developed by Google DeepMind and adopted in Anthropic's [[Claude Models]] deployment.
- Replaces logit biasing and heavy LLM verification with [[Tournament Sampling]] over a bank of binary pseudo-random watermark functions $g_1, \dots, g_n: V \to \{0, 1\}$ derived from key $K$ and prefix history.
- Enables millisecond-level post-hoc verification on arbitrary text snippets using simple string hashing and bit averaging ($S = \frac{1}{T}\sum_t \frac{1}{n}\sum_j g_j$) without executing an LLM forward pass.

## Entropy Selectivity & Quality Preservation

To avoid corrupting factual correctness, modern text watermarking algorithms are **entropy-aware**:
- **High-Entropy Tokens**: When several alternative tokens have high, comparable probabilities (e.g., "overcast" vs "grey" vs "gloomy"), watermarking biases or selects the candidate that matches the keyed hash signature.
- **Low-Entropy / Factual Tokens**: When only one token is plausible (e.g., "The capital of France is [Paris]"), watermarking is suppressed. Forcing watermark selection on low-entropy tokens would produce grammatical errors or factual hallucinations.

## Robustness, Evasion, and the "Worse Text" Dilemma

- **Editing & Cropping**: Watermarking signals accumulate across length $T$. Minor typos, truncations, or individual word replacements reduce detection confidence ($z$-score) but do not fully destroy detection if sufficient watermarked tokens remain.
- **Paraphrasing Attacks**: An adversary can strip watermarks by rewriting the text. In production workflows, users may pass Claude outputs through unwatermarked local models (e.g., Llama, Qwen) for automated paraphrasing.
- **The Quality Paradox**: Because automated paraphrasing disrupts sentence structure and word choice, the process of stripping watermarks often renders the final text noticeably worse and less coherent than the original AI generation.

## Appearances

- [[How Claude Watermarks AI-Generated Text]] — 52-slide explainer by Sebastian Raschka covering Anthropic's Claude watermarking, tournament sampling, and evasion tradeoffs.
- [[Introducing SynthID Text]] — DeepMind / Hugging Face release of the foundational tournament sampling watermarking library.
- [[A Framework for Frontier AI and the Dawning of a New Age]] — Demis Hassabis's governance essay citing cryptographic watermarking and provenance standards.

## Related

- [[Tournament Sampling]]
- [[Introducing SynthID Text]]
- [[Safety and Alignment]]
- [[Responsible Scaling Policy]]
- [[Claude Models]]
- [[Sebastian Raschka]]
- [[Anthropic]]
- [[Google DeepMind]]
