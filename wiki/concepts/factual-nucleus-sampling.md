# Factual Nucleus Sampling

**Type**: concept  
**Tags**: #concept

## Overview

Factual Nucleus Sampling (Lee et al. 2022) is a **decoding-time** hallucination mitigation technique that dynamically adapts the nucleus sampling probability p *within each sentence* as generation progresses. It is based on the empirical observation that **sampling randomness does more harm to factuality in the later tokens of a sentence** than in the earlier tokens.

## Background: Nucleus Sampling vs. Greedy Decoding

Standard **nucleus sampling** (top-p sampling) samples tokens from the smallest vocabulary subset whose cumulative probability mass ≥ p:
- **Advantage**: better diversity and less repetition than greedy decoding.
- **Disadvantage**: on the FactualityPrompt benchmark, nucleus sampling performs *worse* than greedy on factuality — the extra randomness in later token positions introduces hallucination.

This creates a trade-off: greedy is more factual but less diverse; nucleus is more diverse but more hallucination-prone. Factual Nucleus Sampling resolves this.

## Method

**Hypothesis**: Sampling randomness is beneficial at the *beginning* of a sentence (creativity, diversity) but harmful at the *end* (where specific factual details — names, dates, numbers — must be filled in).

**Formula**: For the t-th token within a sentence, set the sampling probability to:

```
p_t = max(ω, p · λ^(t−1))
```

| Parameter | Role |
|-----------|------|
| p | Initial nucleus probability (standard top-p) |
| λ ∈ (0, 1) | Decay factor — controls how fast p shrinks |
| t | Token position within the current sentence (1-indexed) |
| ω | Minimum floor value — prevents full collapse to greedy (preserves some diversity) |

As t increases, p_t → ω. Early tokens in the sentence sample more broadly (high p_t); late tokens converge toward greedy (low p_t, approaching ω).

## Evaluation

Tested on the **FactualityPrompt** benchmark using two metrics:
- **Hallucination NE (Named Entity) error**: fraction of named entities not grounded in the reference Wikipedia document.
- **Diversity and repetition** metrics.

**Key result**: Factual Nucleus Sampling achieves:
- **Better diversity and less repetition** than standard nucleus sampling.
- **Lower NE hallucination error** than standard nucleus sampling.
- A favorable balance between factuality and fluency compared to greedy decoding.

## Why This Works

Named entities, dates, and specific factual content tend to appear **later** in a sentence (e.g., "The president of France is [NAME]"). By decaying the sampling probability over token position, the method ensures that these high-stakes positions are sampled more deterministically, reducing the chance that a wrong but plausible-sounding token is sampled.

## Appearances

- [[Extrinsic Hallucinations in LLMs]] — presented alongside ITI as an inference-time, no-retrieval anti-hallucination method.

## Notes

- This method is **hyper-parameter sensitive**: λ controls the decay rate and ω sets the minimum. Both need tuning per task/model.
- It operates at the **decoding level** — entirely orthogonal to retrieval, fine-tuning, or activation steering. Can be combined with any of those approaches.
- The same group (Lee et al. 2022) also proposed **FactualityPrompt** as a benchmark, **TopicPrefix** and **sentence completion loss** as factuality-enhanced training objectives — making this paper a comprehensive factuality contribution at both training and decoding levels.

## Related

- [[Extrinsic Hallucination]]
- [[ITI]]
- [[CoVe]]
- [[Evaluation and Benchmarks]]
