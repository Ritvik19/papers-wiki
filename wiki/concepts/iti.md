# ITI

**Type**: concept  
**Tags**: #concept

## Overview

Inference-Time Intervention (ITI; Li et al. 2023) reduces LLM hallucination by identifying a sparse set of **attention heads** that encode a "truthfulness" direction in their activation space, then **shifting those activations** along that direction at inference time. It requires no fine-tuning or retrieval — only a linear probe trained on a small factuality dataset and a one-time identification of the most informative heads.

## Motivation

LLMs contain structured internal representations. If truthfulness is encoded in particular attention heads as a linear direction, then pushing activations in that direction at inference time should increase the probability of truthful outputs without modifying weights.

This was verified empirically: for many heads, linear probes trained on truthful/false activations do no better than random; but a sparse subset shows **strong linear separability** between truthful and false activations.

## Method

### Step 1: Probe Training

```
Dataset: A balanced set of truthful / not-truthful statements
         (e.g., from TruthfulQA)

For each attention head h in each layer l:
  Collect activations a_{l,h} for each statement in the dataset
  Train a linear probe: a_{l,h} → {truthful, false}
  Record probe accuracy acc_{l,h}
```

### Step 2: Head Selection

```
Rank all attention heads by probe accuracy acc_{l,h}
Select top-K heads with highest linear probing accuracy for truthfulness

Finding: Most heads ≈ random; a sparse set has strong probe accuracy
```

### Step 3: Inference-Time Intervention

```
At generation time, for each selected head h in layer l:
  h_{l} ← h_{l} + α × d_{l,h}
  
  where:
    d_{l,h} = the linear probe direction (unit vector toward "truthful" activations)
    α       = intervention strength hyperparameter
```

This shifts the internal representation toward the truthfulness direction **without changing model weights**.

## Key Properties

| Property | Value |
|----------|-------|
| Fine-tuning required? | ❌ No |
| Retrieval required? | ❌ No |
| External knowledge base? | ❌ No |
| Probe training data size | Small (TruthfulQA-scale) |
| Applies to | Any transformer with attention heads |
| Interpretability basis | Linear probe on attention activations |

## Experimental Findings (on TruthfulQA)

- Significant improvement over baseline on **TruthfulQA** truthfulness scores.
- The intervention is robust: shifting too aggressively (high α) can hurt fluency; a moderate α gives the best truthfulness/fluency trade-off.
- Only a **sparse subset** of heads are informative for truthfulness — most heads carry no useful linear signal, confirming that truthfulness is not diffuse but localized in the model.

## Relationship to Mechanistic Interpretability

ITI is an applied instance of the **linear representation hypothesis**: the idea that high-level concepts (here: truthfulness) are encoded as linear directions in activation space. This connects to a broader body of mechanistic interpretability work (activation patching, causal tracing, probing classifiers) that tries to localize and steer model behavior via internal activations.

## Limitations

- **Probe dataset dependency**: the "truthfulness" direction is defined relative to the probe training data (TruthfulQA). It may not generalize to all hallucination types — especially fabrications about niche topics not covered in the probe set.
- **Doesn't address systematic confabulation**: if the model's parametric knowledge is wrong, shifting activations toward a "truthful" direction doesn't fix the underlying incorrect belief.
- **Hyperparameter sensitivity**: α must be tuned — too aggressive shifts can produce incoherent or repetitive outputs.
- **Static intervention**: the same shift is applied uniformly; there is no per-token or per-claim adaptivity (unlike Self-RAG reflection tokens).

## Comparison with Related Methods

| Method | Level of intervention | Knowledge source | Training? |
|--------|----------------------|-----------------|-----------|
| **ITI** | Attention head activations | Internal parametric | ❌ (probe only) |
| **CoVe** | Generation-level prompting | Internal parametric | ❌ |
| **Self-RAG** | Token-level reflection | External retrieval | ✅ |
| **RARR** | Post-generation editing | External search | ❌ |
| **Factual Nucleus Sampling** | Decoding distribution | Internal parametric | ❌ |

## Appearances

- [[Extrinsic Hallucinations in LLMs]] — presented as a mechanistic, interpretability-grounded inference-time anti-hallucination method.

## Notes

- Related activation-direction intervention: [[Abliteration]] subtracts a [[Refusal Direction]] at inference or via [[Weight Orthogonalization]]—distinct goal (remove refusal) from ITI's truthfulness steering.

- The article groups ITI with "sampling methods" even though it operates at the activation level, not on the logit distribution — reflecting the broader category of inference-time techniques that don't require retrieval.
- ITI is a **lightweight baseline** for practitioners who cannot afford fine-tuning or retrieval infrastructure — it only requires one probe training pass.

## Related

- [[Extrinsic Hallucination]]
- [[TruthfulQA]]
- [[CoVe]]
- [[Self-RAG]]
- [[Safety and Alignment]]
- [[Representation Learning]]
- [[Abliteration]]
- [[Refusal Direction]]
- [[Weight Orthogonalization]]
