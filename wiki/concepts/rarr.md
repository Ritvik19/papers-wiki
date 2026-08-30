# RARR

**Type**: concept  
**Tags**: #concept

## Overview

RARR ("Retrofit Attribution using Research and Revision"; Gao et al. 2022, ACL 2023) is a **training-free, post-hoc attribution** framework that retroactively enables any LLM to support its outputs with evidence from external sources. Given an arbitrary model-generated text x, RARR outputs a **revised text y** (with unsupported claims corrected) and an **attribution report A** (linking claims to their evidence sources).

## Motivation

RAG (Retrieval-Augmented Generation) typically grounds generation *before* or *during* production. RARR retrofits attribution *after the fact*: any existing model output can be revised to support attribution without retraining the model. This is useful when the underlying model cannot be modified or accessed.

## Two-Stage Pipeline

### Stage 1: Research (Find Evidence)

```
Input: model-generated text x

1. Query generation model (few-shot prompted):
   x → {q₁, q₂, ..., qₙ}
   One query per verifiable aspect of each sentence

2. Google Search:
   Run K=5 results per query qᵢ

3. Relevance filtering:
   Pretrained query-document relevance model →
   Retain the J=1 most relevant document eᵢⱼ per query qᵢ
```

### Stage 2: Revision (Edit the Output)

```
Initialize: revised text y = x

For each (qᵢ, eᵢⱼ):
  1. Agreement model (few-shot + CoT):
     (y, q, e) → {0, 1}
     Does evidence eᵢ disagree with current y?
  
  2. [Only if disagreement detected]:
     Edit model (few-shot + CoT):
     (y, q, e) → new y
     Revise y to agree with eᵢⱼ while minimally altering text

3. Attribution report A:
   Collect at most M=5 evidence documents
```

## Evaluation Metrics

| Metric | What it measures | How computed |
|--------|-----------------|--------------|
| **Attribution (AIS)** | How much of revised text y can be attributed to report A | AIS (Attributable to Identified Sources) score — human or NLI-approximated |
| **Preservation (intent)** | Whether original meaning of x is preserved | Human annotation (Prev_intent) |
| **Preservation (Lev)** | How close y is to original x in wording | Character-level Levenshtein distance (Prev_Lev) |
| **Overall Preservation** | Combined | Prev_intent × Prev_Lev |

**Key result**: RARR achieves better preservation–attribution balance than retrieve-and-regenerate baselines, especially on the preservation side.

## Comparison with FAVA

| Property | RARR | FAVA (Mishra et al. 2024) |
|----------|------|--------------------------|
| Training required? | ❌ No | ✅ Yes (editor model fine-tuned) |
| Retrieval | Google Search | Retriever M_ret |
| Editor | Few-shot prompted LLM | Fine-tuned M_edit |
| Training data | N/A | Synthetic error-injection triplets (c, y, y*) |
| Hallucination taxonomy | Binary | Fine-grained (multiple error types) |

FAVA extends RARR by training a dedicated editor on synthetic error-injection data (gold Wikipedia context c, LM output with errors y, corrected output y*) annotated with a richer taxonomy of hallucination error types.

## Appearances

- [[Extrinsic Hallucinations in LLMs]] — primary RAG+editing anti-hallucination method.

## Notes

- **No retraining required**: RARR uses entirely few-shot prompted LLMs for both agreement checking and editing — applicable to any LLM.
- The **minimal alteration** constraint is critical: aggressive editing could change the meaning of correct statements. RARR explicitly optimizes preservation alongside attribution.
- **Limitation**: the quality of the output depends on the quality of the query generation model. If queries fail to capture the verifiable aspects of a claim, evidence will be missed.
- The **M=5 evidence cap** keeps the attribution report concise and manageable for users.

## Related

- [[Self-RAG]]
- [[Extrinsic Hallucination]]
- [[Embedding and Retrieval]]
- [[Safety and Alignment]]
- [[FActScore]]
