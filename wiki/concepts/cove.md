# CoVe

**Type**: concept  
**Tags**: #concept

## Overview

Chain-of-Verification (CoVe; Dhuliawala et al. 2023) is an **inference-time hallucination mitigation** method that prompts a model to (1) draft a response, (2) plan a set of targeted verification questions, (3) answer those questions **independently** (without the draft in context), and (4) revise the draft based on the verification answers. The independence of step 3 is the key design choice — it avoids the model anchoring on its own hallucinated draft when checking facts.

## Motivation

Standard self-revision approaches (ask the model to check its own response) fail because the model attends to the original hallucinated response when re-reading it, tending to confirm rather than correct errors. CoVe breaks this loop by separating *what to verify* (planned from the draft) from *how to verify* (executed without the draft).

Separately, Weng (2024) notes that **instruction-tuning and standard CoT do not reduce hallucinations** — a direct motivation for the CoVe approach.

## Four Core Steps

```
Step 1 – Baseline Response
  Model generates an initial draft response (the "baseline").

Step 2 – Plan Verification
  Conditioned on the baseline, the model generates
  a set of non-templated verification questions
  for fact-checking each claim.
  (Few-shot prompted with (response, verification Qs) examples)

Step 3 – Execute Verifications (independently)
  The model answers each verification question.
  Key: the original draft is NOT in context during execution.
  → Prevents the model from anchoring on its own hallucination.

Step 4 – Final Output
  The model generates the final refined response,
  conditioned on the draft AND the verification Q&A pairs.
  Inconsistencies detected in Step 3 are corrected here.
```

## Variants of Step 3 (Verification Execution)

| Variant | Description | Issue |
|---------|-------------|-------|
| **(1) Joint** | Verification planning and execution in one prompt; original response is in context | Model may repeat hallucinations from the draft |
| **(2) 2-step** | Planning and execution are separated; original response absent during execution | Better; removes draft anchoring |
| **(3) Factored** | Each verification question answered independently in a separate call | Best single-question accuracy |
| **(4) Factor+Revise** | Factored + explicit cross-checking step comparing answers to the baseline | Adds inconsistency detection; best overall |

## Key Experimental Findings

- **Instruction-tuning and CoT do not reduce hallucinations** — this establishes why a structured verification loop is necessary.
- **Factored and 2-step CoVe outperform Joint** — confirming that draft independence in verification execution is critical.
- **Factor+Revise further improves** — explicit inconsistency detection at the end helps.
- **Short-form verification questions are more accurately answered** than long-form queries.
- **Free-form LLM-generated verification questions outperform heuristics** (e.g., templated "Does X answer the question?").
- **Open-ended generation questions beat yes/no questions** for verification.

## When CoVe Helps Most

- Long-form generation with multiple distinct claims (biographical entries, summaries).
- Factual questions where the model has partial knowledge (knows the entity but confabulates details).
- Tasks where the model is likely to propagate an initial error across multiple sentences.

## Comparison with Related Methods

| Method | When to check | Draft in verification context? | Requires external knowledge? |
|--------|--------------|-------------------------------|------------------------------|
| **CoVe** | After draft; planned questions | ❌ (Factored/2-step variants) | ❌ |
| **ITI** | At inference, continuously | N/A (activation-level) | ❌ |
| **RARR** | Post-generation | N/A (external grounding) | ✅ (Google Search) |
| **Self-RAG** | During generation | ❌ (reflection tokens) | ✅ (retrieval) |

## Appearances

- [[Extrinsic Hallucinations in LLMs]] — presented as a chain-of-thought inspired inference-time hallucination reduction method requiring no retrieval.

## Notes

- CoVe is a **zero-retrieval** approach — it relies entirely on the model's parametric knowledge to answer verification questions. This means it cannot detect hallucinations about facts the model doesn't know at all (systematic confabulation), unlike retrieval-backed methods.
- The Factor+Revise variant most closely mirrors a human fact-checker's workflow: check each claim individually, then reconcile inconsistencies against the full response.
- Weng specifically notes that CoVe-style short-form, open-ended verification questions work better than yes/no questions — an important implementation detail for practitioners.

## Related

- [[Extrinsic Hallucination]]
- [[Self-RAG]]
- [[RARR]]
- [[ITI]]
- [[Safety and Alignment]]
