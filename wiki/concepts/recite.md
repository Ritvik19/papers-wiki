# RECITE

**Type**: concept  
**Tags**: #concept

## Overview

RECITE ("Recitation-Augmented Generation"; Sun et al. 2023) is an inference-time hallucination reduction method that treats the **Transformer's parametric memory as an information retrieval mechanism**. Rather than retrieving from an external index, RECITE prompts the model to first *recite* relevant passages from its own memory, then generate the answer conditioned on the recited content.

## Motivation

Standard RAG requires a retrieval index (e.g., a Wikipedia BM25 index). RECITE asks: *can the model's own weights serve as a retrieval corpus?* If a model has memorized enough relevant content, asking it to explicitly surface that content before answering reduces hallucination — because the answer is now grounded in a stated, checkable intermediate step rather than implicit weight activations.

This is distinct from [[Self-RAG]] and [[RARR]], which retrieve from external sources. RECITE is fully parametric — no external knowledge base is needed.

## Recite-and-Answer Scheme

```
Standard generation:
  prompt Q → answer A

RECITE scheme:
  prompt Q → recitation R (relevant passages from parametric memory)
           → answer A conditioned on (Q, R)
```

Both steps use **few-shot in-context prompting** to teach the model the recite-then-answer format. Example few-shot demonstrations include (question, recitation, answer) triples.

## Self-Consistency Extension

RECITE can be combined with **self-consistency ensemble**:
- Generate multiple (recitation, answer) pairs at temperature > 0.
- Majority-vote or select the most consistent answer across samples.
- This extends to **multi-hop QA** by chaining recitation steps for each reasoning hop.

## Empirical Findings

| Finding | Detail |
|---------|--------|
| Recitation vs. BM25 retrieval | Generated recitation is *comparable* in quality to BM25-retrieved passages |
| Gap with gold passage | Both recitation and BM25 have a performance gap vs. using the actual ground-truth passage |
| Correct recitation but wrong answer | ~7–10% of questions |
| Wrong recitation but correct answer | ~12% of questions |

The **~12% correct-despite-wrong-recitation** result is informative: the model sometimes "knows" the answer through parametric routes even when the recitation step fails to surface the right context.

## Comparison with External Retrieval

| Property | RECITE | RAG (external) | Self-RAG |
|----------|--------|----------------|---------|
| Knowledge source | Parametric memory | External index | External index |
| External retriever required? | ❌ | ✅ | ✅ |
| Knowledge up-to-date? | Limited to training data | Can be current | Can be current |
| Verifiable intermediate step? | ✅ (recitation is readable) | ✅ (retrieved passage) | ✅ (retrieved + reflection tokens) |

## Appearances

- [[Extrinsic Hallucinations in LLMs]] — presented as a retrieval-from-memory approach alongside [[Self-RAG]] and Rethinking with Retrieval (RR).

## Notes

- RECITE is most effective for **well-memorized topics** — it degrades for niche or recent information not well-represented in the model's pre-training corpus.
- The readable recitation acts as a natural **chain-of-thought** that users and auditors can inspect, unlike implicit parametric retrieval.
- The comparison with BM25 (comparable performance) is striking — it suggests that for sufficiently well-trained models, parametric memory can approximate a structured retrieval system on common topics.

## Related

- [[Extrinsic Hallucination]]
- [[Self-RAG]]
- [[RARR]]
- [[CoVe]]
- [[Embedding and Retrieval]]
