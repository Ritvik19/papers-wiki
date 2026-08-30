# Extrinsic Hallucination

**Type**: concept  
**Tags**: #concept

## Overview

Extrinsic hallucination refers to model-generated content that is fabricated and not grounded by the pre-training data corpus, which is treated as a proxy for world knowledge. It is distinguished from **in-context hallucination** (where the model contradicts the provided context document). To avoid extrinsic hallucination, LLMs must be (1) **factual** — their claims are verifiable against world knowledge — and (2) **calibrated** — they refuse or hedge when the answer lies outside their knowledge boundary.

## Taxonomy

```
Hallucination
├── In-context hallucination   ← model contradicts provided source document
└── Extrinsic hallucination    ← model fabricates content not grounded by world knowledge
    ├── Factual incorrectness  ← claims are verifiably wrong
    └── Overconfidence         ← model asserts answers it should refuse
```

## Root Causes

### 1. Pre-training Data Issues
- Pre-training corpora (dominantly web-crawled text) contain stale, missing, or incorrect information at scale.
- The model may **incorrectly memorize** erroneous content by maximizing log-likelihood over billions of tokens.
- No feasible per-generation mechanism exists to verify claims against the full pre-training corpus.

### 2. Fine-tuning New Knowledge (Gekhman et al. 2024)
Fine-tuning via SFT or RLHF often injects *new* knowledge the base model doesn't already know. Key empirical findings using the EntityQuestions closed-book QA dataset:

- **Knowledge taxonomy**: examples are categorized by `P_Correct(q, a; M, T)` — the likelihood the model generates the correct answer:
  - *HighlyKnown*, *MaybeKnown*, *WeaklyKnown* → Known groups
  - *Unknown* → base model cannot reliably answer

- **Unknown examples are learned much slower** than Known during fine-tuning.
- **Best dev performance** is achieved when the model learns most Known examples but *very few* Unknown ones.
- **Hallucination onset**: the model starts to hallucinate once it begins memorizing most Unknown examples.
- **MaybeKnown > HighlyKnown**: among Known examples, MaybeKnown contribute more to generalization than already-mastered HighlyKnown items.

**Implication**: SFT is a risky mechanism for updating factual knowledge; injecting Unknown-to-the-model facts causes confabulation rather than reliable learning.

## Detection Methods

### Retrieval-Augmented Evaluation
| Method | Key idea | Output |
|--------|----------|--------|
| **FactualityPrompt** (Lee et al. 2022) | Wikipedia-grounded prompt continuation; NE error rate + entailment ratio | Benchmark |
| **FActScore** (Min et al. 2023) | Decompose into atomic facts; retrieve Wikipedia; verify each | Precision score |
| **SAFE** (Wei et al. 2024) | Agentic multi-step Google Search; F1@K metric | F1 score |
| **FacTool** (Chern et al. 2023) | Claim extraction → tool query → agreement verification; supports QA, code, math, lit | Binary factuality labels |

### Sampling-Based Detection
- **SelfCheckGPT** (Manakul et al. 2023): consistency across multiple black-box stochastic samples; no external knowledge needed.

### Calibration / Unknown Knowledge
| Benchmark | Focus |
|-----------|-------|
| **TruthfulQA** (Lin et al. 2021) | 817 adversarially constructed questions; larger models *less* truthful |
| **SelfAware** (Yin et al. 2023) | 1,032 unanswerable + 2,337 answerable questions; tests self-knowledge |
| **CalibratedMath** (Lin et al. 2022) | Math problems at varying difficulty; verbalized confidence + logprob calibration |

**Kadavath et al. (2022)** showed LLMs are well-calibrated on multiple-choice questions, but **RLHF degrades calibration** (human feedback prefers longer, more detailed answers which aren't necessarily more factual); higher sampling temperature partially restores calibration.

### Indirect Query (Agrawal et al. 2023)
Detecting hallucinated references by asking auxiliary questions (e.g., "Who are the authors?") rather than a direct truthfulness query. Multiple samples agreeing on fabricated auxiliary details is less likely than agreeing on the existence of the reference — making indirect queries more discriminative.

## Anti-Hallucination Methods

### RAG + Editing
| Method | Training required | Key mechanism |
|--------|------------------|---------------|
| **RARR** (Gao et al. 2022) | No | Query generation → search → agreement check → minimal edit |
| **FAVA** (Mishra et al. 2024) | Yes (editor) | Retriever + fine-tuned editor on synthetic error-injection data |

### Retrieval + Selection / Adaptive RAG
| Method | Mechanism |
|--------|-----------|
| **RR** (He et al. 2022) | CoT paths × BM25+MPNet retrieval; select most faithful answer |
| **Self-RAG** (Asai et al. 2024) | End-to-end trained; emits retrieval & critique reflection tokens |
| **RECITE** (Sun et al. 2023) | Recite relevant passages from model parametric memory; then answer |

### Inference-Time Intervention
| Method | Mechanism |
|--------|-----------|
| **CoVe** (Dhuliawala et al. 2023) | Plan verification Qs → answer independently → revise draft |
| **Factual Nucleus Sampling** (Lee et al. 2022) | Decay nucleus p as p_t = max(ω, p·λ^(t−1)) within each sentence |
| **ITI** (Li et al. 2023) | Probe attention heads for truthfulness; shift activations at inference |

### Fine-tuning for Factuality / Attribution
| Method | Mechanism |
|--------|-----------|
| **TopicPrefix + sentence loss** (Lee et al. 2022) | Factuality-enhanced training objectives |
| **FLAME / Factuality-aware DPO** (Lin et al. 2024) | SFT + DPO with FActScore as reward signal |
| **FactTune** (Tian & Mitchell et al. 2024) | DPO on pairs annotated by reference-based or reference-free truthfulness |
| **GopherCite** (Menick et al. 2022) | Demonstration generation via few-shot + context stuffing; RL from human preferences |
| **WebGPT** (Nakano et al. 2022) | GPT-3 + web browser environment; behavior cloning + RL; cites web sources |

## Appearances

- [[Extrinsic Hallucinations in LLMs]] — Lilian Weng's comprehensive July 2024 synthesis.
- [[Papers Explained 457 - Hallucination Tax of Reinforcement Finetuning]] — RL fine-tuning (RFT) reduces refusal rates by >80% on unanswerable questions — directly extends Gekhman et al.'s finding.
- [[Reward Hacking in Reinforcement Learning]] — sycophancy, U-Sophistry, and grader gaming overlap with hallucination under RLHF.

## Notes

- The **RLHF calibration degradation** finding (Kadavath et al. 2022) is a fundamental tension: alignment objectives push models toward longer, more detailed answers that satisfy human raters, but this can increase confident confabulation.
- **TruthfulQA's inverse scaling** (larger = less truthful) is unique to adversarially designed benchmarks targeting human misconceptions; standard factual QA benchmarks show normal positive scaling.
- **Factual Nucleus Sampling** rests on the empirical observation that hallucination errors are concentrated in the *later tokens* of a sentence — so decaying the sampling nucleus p over token position is motivated.
- The article explicitly notes that **neuron editing / interpretability approaches** to hallucination reduction exist but are not covered (promised for a future post).

## Related

- [[FActScore]]
- [[SAFE]]
- [[SelfCheckGPT]]
- [[TruthfulQA]]
- [[RARR]]
- [[Self-RAG]]
- [[CoVe]]
- [[ITI]]
- [[Sycophancy]]
- [[Safety and Alignment]]
- [[Evaluation and Benchmarks]]
- [[Reinforcement Learning from Human Feedback]]
- [[Papers Explained 123 - WebGPT]]
