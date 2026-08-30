# FActScore

**Type**: concept  
**Tags**: #concept

## Overview

FActScore (Factual Precision in Atomicity Score; Min et al. 2023) is a factuality evaluation framework that decomposes a long-form language model generation into individual **atomic facts** and validates each one independently against a knowledge base (typically Wikipedia). The final score is the **average precision** — the fraction of atomic facts supported by the knowledge source — averaged across a prompt set.

## Motivation

Long-form generation factuality is hard to measure holistically because:
- A single response may mix accurate and inaccurate statements.
- Sentence-level scores conflate factual density with factual accuracy.
- Existing NLI-based entailment scores require a known reference text.

FActScore decomposes the problem: if every atomic fact is verified independently, precision becomes a tractable, granular metric that does not require a pre-existing reference response.

## Method

```
Long-form generation
    ↓ decompose
[atomic fact 1], [atomic fact 2], ..., [atomic fact N]
    ↓ for each fact
retrieve k passages from knowledge base (Wikipedia)
    ↓ verify
is the fact supported by the passage?  (True / False)
    ↓ aggregate
FActScore = |supported facts| / |all facts|   (averaged over prompts)
```

### Validation Strategies (tested in paper)

| Strategy | Description | Performance |
|----------|-------------|-------------|
| **Non-context LLM** | Prompt LLM with "True or False?" directly, no context | Weakest |
| **Retrieval→LLM** | Retrieve k related passages; prompt LLM with them as context | Strong |
| **NP (Nonparametric)** | Average log-likelihood of atomic fact tokens under a masked LM | Varies by model |
| **Retrieval→LLM + NP** | Ensemble of the two above | Best overall |

**Finding**: retrieval-augmented validation consistently outperforms non-context LLM. The best exact estimator among retrieval methods depends on the model.

## Key Empirical Observations

Tested on the task of **biography generation** (writing biographical entries about people):

- **Rarer entities → higher error rates**: the model hallucinates more about lesser-known people.
- **Later-in-generation → higher error rates**: the further into a response, the more factual drift occurs.
- **Retrieval grounding substantially helps**: retrieval-augmented methods dramatically reduce error rates vs. no retrieval.

## Evaluation Benchmark: LongFact

FActScore motivated the **LongFact** benchmark (Wei et al. 2024):
- 2,280 fact-seeking prompts across 38 manually curated topics.
- Designed for long-form factuality evaluation using the SAFE evaluator and F1@K metric.
- Reveals meaningful separation between frontier models on factuality under length pressure.

## Limitations

- Atomic decomposition quality matters: poorly decomposed facts lead to misleading scores.
- Precision-only: does not reward **comprehensive** responses (how many relevant facts were included). This motivated the F1@K metric in [[SAFE]].
- Knowledge base coverage: facts about niche or very recent topics may not appear in Wikipedia.

## Appearances

- [[Extrinsic Hallucinations in LLMs]] — introduced as the core detection framework alongside SAFE, FacTool, and SelfCheckGPT.
- [[Extrinsic Hallucination]] — cited as the primary atomic-fact precision metric.

## Notes

SAFE (Wei et al. 2024) directly extends FActScore in two ways: (1) it replaces static Wikipedia retrieval with an agentic multi-step Google Search loop, and (2) it adds an F1@K metric that rewards both precision (factual) and recall (length). FLAME (Lin et al. 2024) uses FActScore as the reward signal in a DPO alignment pipeline, demonstrating its utility beyond evaluation.

## Related

- [[SAFE]]
- [[FacTool]]
- [[SelfCheckGPT]]
- [[Extrinsic Hallucination]]
- [[Evaluation and Benchmarks]]
- [[Papers Explained 123 - WebGPT]]
