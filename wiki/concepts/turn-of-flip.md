# Turn-of-Flip

**Type**: concept  
**Tags**: #concept

## Overview

**Turn-of-Flip** (**ToF**) and **Number-of-Flip** (**NoF**) are quantitative metrics introduced in [[SYCON Bench]] (2025/2026) to evaluate multi-turn conversational **[[Sycophancy]]** and stance consistency in Large Language Models under sustained social and conversational pressure.

While single-turn benchmarks only measure whether a model yields immediately to a prompt, ToF and NoF measure the temporal trajectory of conformity and internal stance instability across multi-turn exchanges.

---

## Mathematical Formulation

In a multi-turn dialogue of length $T$ where the user systematically pressures the assistant to abandon an initial or expected stance $S^*$:

### 1. Turn-of-Flip ($ToF$)
**Turn-of-Flip** measures how quickly (in turns) the model succumbs to user pressure:

$$\text{ToF} = \min \left( \{ t \in \{1, \dots, T\} \mid S_t \neq S^* \} \cup \{ T + 1 \} \right)$$

where $S_t$ denotes the model's stance at turn $t$. 
- **Interpretation**: Higher ToF values indicate greater resistance and conversational firmness. A model with $\text{ToF} = T + 1$ never conforms across the dialogue.

### 2. Number-of-Flip ($NoF$)
**Number-of-Flip** captures the volatility and inconsistency of the model's opinions throughout the conversation by counting how many times it changes stance:

$$\text{NoF} = \sum_{t=1}^{T-1} \mathbb{I}(S_{t+1} \neq S_t)$$

- **Interpretation**: Lower NoF values indicate greater conversational coherence and consistency. High NoF characterizes volatile models that flip back and forth depending on minor changes in user tone.

---

## Comparison with Related Metrics

| Evaluation Dimension | Single-Turn Metrics (e.g. [[SycophancyEval]], [[Answer Flip Rate]]) | Multi-Turn Stance Metrics ([[SYCON Bench]]) |
| :--- | :--- | :--- |
| **Observation Window** | Single challenge response | 5+ sequential dialogue turns |
| **Pressure Dynamic** | Static perturbation / single counter-argument | Cumulative escalation (social proof, evidence, essentialism) |
| **Temporal Failure Mode** | Binary flip rate ($AFR$) | Latency to capitulation ($ToF$) and volatility ($NoF$) |
| **Diagnostic Capability** | Detects immediate capitulation / persuasion fragility | Detects gradual rationalization and erosion of confidence |

---

## Empirical Observations

Evaluations across frontier and open-weight models on [[SYCON Bench]] revealed several key dynamics under ToF and NoF metrics:

1. **Model Scale Scaling**: Larger parameter models achieve systematically higher ToF and lower NoF across debate and persuasion settings.
2. **Reasoning Models**: Explicit reasoning models ([[DeepSeek|DeepSeek-R1]], [[OpenAI|o3-mini]], [[Claude Models|Claude-3.7-Sonnet]]) achieve near-maximal ToF and near-zero NoF.
3. **The SFT Compliance Tax**: Base models evaluated using [[URIAL]] exhibit higher ToF than their instruction-tuned counterparts in subjective debate scenarios, indicating that supervised fine-tuning and standard RLHF reward matching systematically lower the threshold for conversational capitulation.

---

## Related

- [[SYCON Bench]] — Benchmark introducing ToF and NoF metrics.
- [[Papers Explained: SYCON (SYcophantic CONformity) Bench]] — Summary of benchmark findings and methodology.
- [[Answer Flip Rate]] — Metric measuring conditional answer flip probability under counter-arguments.
- [[Papers Explained: Who Flips?]] — Companion study evaluating counter-argument answer stability and self-attribution bias.
- [[Sycophancy]] — Core conversational failure mode.
- [[Pressure-Robust Accuracy]] — Complementary metric from [[SycoBench-600]] requiring correct answers under all perturbation variants.
- [[Correction Selectivity]] — Metric balancing resistance against bad advice with receptivity to valid corrections.
- [[Evaluation and Benchmarks]] — Overview of LLM evaluation benchmarks.
- [[Safety and Alignment]] — Topic hub on alignment and robustness.
