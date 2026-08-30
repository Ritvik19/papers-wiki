# SAFE

**Type**: concept  
**Tags**: #concept

## Overview

SAFE (Search-Augmented Factuality Evaluator; Wei et al. 2024) extends [[FActScore]] by replacing static Wikipedia retrieval with an **LLM agent** that iteratively issues Google Search queries in a multi-step reasoning loop to verify each atomic fact. SAFE simultaneously introduces the **F1@K** metric, which evaluates long-form factuality along both a precision axis (factual) and a recall axis (comprehensive).

## Motivation

FActScore measures only *precision* — what fraction of stated facts are supported. But a high-quality long-form response should also be *long* and *comprehensive*, not just accurate. A model that states one correct fact and stops would score 100% on precision but provide almost no value. F1@K resolves this by incorporating a recall component capped at K relevant facts.

## Agentic Verification Loop

```
For each atomic fact in the model response:
    Step 1: Generate a Google Search query based on the fact
            (conditioned on the fact + prior search results)
    Step 2: Execute search; collect results
    Repeat Steps 1-2 for several iterations
    Final Step: Reason over accumulated search results
                → label fact as Supported or Not Supported
```

**Key difference from FActScore**: SAFE uses real-time web search rather than a static knowledge base, enabling evaluation of recent facts and niche topics not covered by Wikipedia snapshots.

## F1@K Metric

Given model response y:

| Symbol | Meaning |
|--------|---------|
| S(y) | Number of supported atomic facts |
| N(y) | Number of not-supported atomic facts |
| Prec(y) | S(y) / (S(y) + N(y)) — factual precision |
| R_K(y) | min(S(y)/K, 1) — recall capped at K |
| F1@K | 2·Prec·R_K / (Prec + R_K), or 0 if S(y) = 0 |

**K** is a fixed target for how many supported facts an ideal response should contain. Setting K higher rewards longer, more comprehensive responses.

**Intuition**: 
- A short but perfectly accurate response → high Prec, low R_K → moderate F1@K
- A long but inaccurate response → low Prec → low F1@K regardless of R_K
- Only a long *and* accurate response achieves high F1@K

## Performance vs. Human Annotators

| Metric | Value |
|--------|-------|
| Agreement with human annotations | **72%** |
| Win rate when human & SAFE disagree | **76%** (SAFE wins) |
| Cost vs. human annotation | **20× cheaper** |

SAFE outperforms human annotators on factuality verification while being dramatically cheaper.

## Benchmark: LongFact

SAFE is evaluated on the **LongFact** benchmark (Wei et al. 2024):
- 2,280 fact-seeking prompts across 38 manually curated topics.
- Prompts designed to elicit long-form factual responses.
- Results using F1@K reveal meaningful ranking among frontier models.

## Appearances

- [[Extrinsic Hallucinations in LLMs]] — presented as the state-of-the-art factuality evaluation method, advancing beyond FActScore with its agentic loop and F1@K metric.

## Notes

- The F1@K recall cap K is a hyperparameter; its value encodes a judgment about what "comprehensive" means for a given task. This requires domain-specific tuning.
- The agentic search loop means SAFE is not fully reproducible over time (search results change), unlike static-knowledge-base methods.
- FLAME (Lin et al. 2024) uses FActScore (not SAFE) as a reward signal in DPO, suggesting FActScore remains the more tractable tool for training-time use despite SAFE's superior evaluation performance.

## Related

- [[FActScore]]
- [[Extrinsic Hallucination]]
- [[Evaluation and Benchmarks]]
- [[Agentic AI]]
- [[SelfCheckGPT]]
