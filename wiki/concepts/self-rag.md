# Self-RAG

**Type**: concept  
**Tags**: #concept

## Overview

Self-RAG ("Self-Reflective Retrieval-Augmented Generation"; Asai et al. 2024, ICLR 2024) trains a language model **end-to-end** to adaptively retrieve external documents and critique its own generation by emitting special **reflection tokens** interleaved with normal text. Unlike always-retrieve RAG (which can dilute responses with irrelevant documents) or never-retrieve LLMs (which hallucinate), Self-RAG learns *when* retrieval helps and *how well* its generation is grounded.

## Motivation

Standard RAG always retrieves, regardless of whether the question needs external knowledge. For simple factual prompts this adds noise; for complex multi-hop questions a single retrieval pass may be insufficient. Self-RAG makes retrieval a learnable, conditional decision integrated directly into generation.

## Reflection Token Vocabulary

| Token Type | Function | Values |
|-----------|----------|--------|
| **Retrieve** | Should the model retrieve at this step? | `Retrieve` / `No Retrieve` |
| **ISREL** | Is the retrieved document relevant to the input? | `Relevant` / `Irrelevant` |
| **ISSUP** | Does the generated segment follow from / is supported by the document? | `Fully Supported` / `Partially Supported` / `No Support` |
| **ISUSE** | Is the overall response useful to the user? | Likert scale (1–5) |

These tokens are emitted by the **same model** that generates the answer — not a separate critic — making Self-RAG a single unified model.

## Training Pipeline

```
Step 1: Critic model training
  - Prompt GPT-4 to annotate (input, output, passage) triplets
    with reflection token labels
  - Distill into an in-house critic model C

Step 2: Generator model training
  - Use C to annotate training corpus with reflection tokens
  - Train generator G on augmented sequences (text + reflection tokens)
  - G learns to retrieve, generate, and self-critique jointly

Result: A single model G that produces text + reflection tokens
        with no test-time modification required
```

## Inference Procedure

```
Given input prompt x:
1. Model generates tokens normally
2. When a [Retrieve] token fires:
   → Retrieve top-k documents in parallel
3. For each retrieved document d:
   → Generate candidate continuation conditioned on (x, d)
   → Emit ISREL, ISSUP, ISUSE tokens for this continuation
4. Select best continuation using reflection scores as ranking signal
5. Continue generation; repeat retrieval when [Retrieve] fires again
```

## Key Experimental Findings

- **Outperforms always-retrieve RAG** on knowledge-intensive tasks (PopQA, PubHealth, ARC-C) and long-form generation (ASQA, FactScore).
- **No test-time modifications needed**: the reflection tokens handle all decisions at inference.
- **Better calibrated** than standard RAG: retrieval tokens fire only when needed.
- The **ISSUP token** is particularly important — it teaches the model to flag when it is generating text not supported by the retrieved passage.

## Comparison with Related Methods

| Method | Retrieval decision | Self-critique | Training required |
|--------|-------------------|---------------|------------------|
| **RAG** | Always | ❌ | Optional (retriever) |
| **RARR** | Post-hoc | ❌ | ❌ |
| **RR (Rethinking with Retrieval)** | Always (CoT-decomposed) | ❌ | ❌ |
| **Self-RAG** | Adaptive (learned) | ✅ | ✅ (full end-to-end) |

## Appearances

- [[Extrinsic Hallucinations in LLMs]] — presented as a training-based approach to adaptive retrieval with self-critique.

## Notes

- The distillation from GPT-4 for reflection token annotation means the quality of the critic is bounded by GPT-4's ability to assess factuality — a form of knowledge distillation for epistemic self-awareness.
- ISSUP partial support is an important nuance: many real retrieved passages partially support a claim, and treating this as binary (full support / no support) would lose information.
- Self-RAG's adaptive retrieval is conceptually related to the **Retrieve** token in tool-use / agentic systems, but here it is learned from demonstration rather than hand-coded.

## Related

- [[RARR]]
- [[Extrinsic Hallucination]]
- [[Embedding and Retrieval]]
- [[Agentic AI]]
- [[Safety and Alignment]]
- [[FActScore]]
