# Tournament Sampling

**Type**: concept  
**Tags**: #concept

## Overview

**Tournament Sampling** is a modified decoding algorithm for autoregressive language models that embeds a statistical watermark into generated text while enabling fast, lightweight post-hoc detection without running a large language model during verification. Originally developed by Google DeepMind for **SynthID Text** and adopted in Anthropic's **Claude** production text watermarking, tournament sampling structures token selection as a multi-round tournament governed by pseudorandom binary hash functions.

## Algorithm and Mechanics

```
                 [ Candidate Vocabulary Tokens & Probabilities ]
                                     │
                 [ Compute m-bit Signatures: (g_1, g_2, ..., g_m) ]
                                     │
           ┌─────────────────────────┴─────────────────────────┐
      Round 1 (g_1)                                       Round 1 (g_1)
   [Token A] vs [Token B]                              [Token C] vs [Token D]
           │ (g_1 match / prob weight)                         │ (g_1 match / prob weight)
       [Winner 1]                                          [Winner 2]
           └─────────────────────────┬─────────────────────────┘
                               Round 2 (g_2)
                          [Winner 1] vs [Winner 2]
                                     │ (g_2 match / prob weight)
                              [ Sampled Token ]
```

### 1. Hash Function Instantiation
At token generation step $t$, the generator uses a secret key $K$ and the preceding $h$-token context window $x_{t-h:t-1}$ to initialize a pseudorandom generator, defining $m$ binary hash functions:
$$g_1, g_2, \dots, g_m : V \to \{0, 1\}$$

Each token $w$ in the vocabulary $V$ has a deterministic $m$-bit signature $\mathbf{b}(w) = (g_1(w), g_2(w), \dots, g_m(w))$.

### 2. Bracket Execution
1. Candidate tokens are paired up into tournament brackets.
2. In round 1, candidate pairs $(u, v)$ compete based on function $g_1$:
   - If $g_1(u) = 1$ and $g_1(v) = 0$, token $u$ advances.
   - If $g_1(u) = g_1(v)$, the winner is selected with probability proportional to their respective model probabilities:
     $$P(u \text{ wins}) = \frac{P(u)}{P(u) + P(v)}$$
3. In round 2, surviving winners compete based on $g_2$.
4. The process repeats across $m$ rounds until a final winning token $x_t$ is selected.

This structure biases generation toward tokens whose bit signatures match 1s under the keyed hash functions, while closely respecting the underlying probability distribution.

## Lightweight Verification (No LLM Required)

The principal operational advantage of tournament sampling over earlier watermarking schemes (such as exponential min-hash or Gumbel sampling) is **post-hoc computational efficiency**:

| Dimension | Standard PRNG Sampling | Tournament Sampling |
|-----------|-------------------------|---------------------|
| **Inference Overhead** | Minimal | Minimal (bracket sorting on top-k candidates) |
| **Detection Cost** | Requires full LLM forward pass to recompute logits $P(w \mid x_{<t})$ | **Zero LLM cost**: requires only string hashing using secret key $K$ |
| **Detection Speed** | Slow / expensive (GPU required) | Ultra-fast / cheap (CPU string lookup, <1 ms) |
| **Detector Sharing** | Requires distributing model weights or hosting heavy inference endpoints | Shareable via lightweight API or encrypted key container |

### Scoring Formula
Given a text sequence of length $T$, the detector evaluates the average watermark bit score across all token positions:
$$S = \frac{1}{T} \sum_{t=1}^T \frac{1}{m} \sum_{j=1}^m g_j(x_t)$$

- **Unwatermarked / Human Text**: For text not generated with key $K$, the watermark functions evaluate as unbiased Bernoulli random variables, giving:
  $$\mathbb{E}[S] = 0.5$$
- **Watermarked Text**: Tournament-sampled text contains a statistically elevated ratio of 1s:
  $$\mathbb{E}[S] \gg 0.5 \quad (\text{e.g., } 0.70 - 0.85+)$$
- A decision threshold $\tau$ (calibrated against sample length $T$) yields high-confidence attribution with near-zero false-positive rates.

## Appearances

- [[How Claude Watermarks AI-Generated Text]] — Explains step-by-step tournament brackets, token bit signatures, and scoring mechanics.
- [[Introducing SynthID Text]] — Foundational integration of tournament sampling in Hugging Face `transformers` and Google DeepMind systems.

## Related

- [[Text Watermarking]]
- [[Claude Models]]
- [[Introducing SynthID Text]]
- [[Anthropic]]
- [[Google DeepMind]]
- [[Sebastian Raschka]]
- [[Safety and Alignment]]
