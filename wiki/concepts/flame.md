# FLAME

**Type**: concept  
**Tags**: #concept

## Overview

FLAME ("Factuality-Aware Alignment"; Lin et al. 2024) is an alignment training pipeline that integrates factuality signals into both the **SFT** and **DPO/RLHF** stages of LLM fine-tuning. The key motivation is that standard RLHF makes models *less* factual — human raters prefer longer, more detailed responses, which are not necessarily more accurate. FLAME counteracts this by explicitly using FActScore as a factuality reward signal.

## Motivation: RLHF Degrades Factuality

A crucial empirical finding motivating FLAME:

> *"RLHF makes factuality worse, because human feedback often prefers longer, more detailed answers, which are not necessarily more factual."*

This creates a tension: RLHF aligns models with human preferences (helpfulness, detail), but factuality is not directly rewarded by human raters, who cannot easily verify every claim in a long response.

## Two-Stage Pipeline

### Stage 1: Factuality-Aware SFT

**Goal**: Generate SFT training data that is *more factual* than the model's own (unaided) generation.

```
1. Sample model responses with retrieval (RAG)
2. Compute FActScore for each response
3. Use high-FActScore responses as SFT training targets
→ Model learns to generate text closer to RAG-grounded outputs
```

**Risk**: This can inadvertently distill new knowledge the model doesn't already have (Unknown knowledge in the Gekhman et al. sense), which can *increase* hallucination — a known tension.

**Mitigation**: Use the model's *own* generated responses (not RAG responses) to form the SFT dataset where possible, to avoid distilling unknown knowledge.

### Stage 2: Factuality-Aware DPO

Two approaches were tested:

| Approach | Method | Result |
|----------|--------|--------|
| **(1) RAG-as-positive DPO** | Use RAG-grounded response as preferred, original model generation as rejected | ❌ **Works poorly** — likely distills unknown knowledge, causing hallucination |
| **(2) FActScore-as-reward DPO** | Use FActScore as the preference signal; higher-FActScore response is preferred | ✅ **Works** — directly optimizes for factuality without introducing unknown facts |

The failure of approach (1) directly echoes Gekhman et al. 2024's finding: trying to distill new factual knowledge via SFT/DPO causes the model to hallucinate.

## Key Results

- Factuality-Aware DPO with FActScore reward improves FActScore on biography generation tasks.
- Helpfulness (measured as win rate on Alpaca Eval vs. baseline SFT+DPO) is preserved.
- Using model-generated responses (not RAG) for training data avoids the Unknown-knowledge problem.

## Comparison with FactTune (Tian & Mitchell et al. 2024)

**FactTune** is a related approach using DPO with two types of preference annotation (no human needed):

| Method | Truthfulness estimation | Best variant |
|--------|------------------------|-------------|
| **Reference-based (FactTune-FS)** | Atomic claim extraction → Wikipedia lookup → NLI check; same as FActScore | Best performer |
| **Reference-free (FactTune-EC)** | Model confidence proxy: rephrase claim as question → sample answers → aggregate consistency | Weaker |

**FactTune-FS** (using FActScore as annotation signal) achieves the best improvement on factuality, validating that FActScore-graded DPO is an effective training strategy.

## Process: FactTune

```
1. Sample pairs of model completions for each prompt
   (e.g. "Write a bio of Yo-Yo Ma")
2. Annotate each with truthfulness:
   Reference-based: extract atomic claims → find Wikipedia passage → NLI check
   Reference-free:  rephrase claim as Q → sample multiple model answers → check consistency
3. Assign preference: higher-truthfulness completion = preferred
4. Fine-tune with DPO on these annotated preference pairs
```

## Appearances

- [[Extrinsic Hallucinations in LLMs]] — presented as the canonical factuality fine-tuning approach combining SFT + DPO with explicit FActScore reward.

## Notes

- FLAME and FactTune independently converge on the same insight: **FActScore is a tractable automatic reward signal for factuality alignment**, avoiding costly human annotation.
- The RLHF calibration degradation finding (Kadavath et al.) and FLAME's results are consistent: human raters prefer detailed, confident-sounding responses even when they hallucinate.
- TopicPrefix and sentence completion loss (Lee et al. 2022) are simpler training-level factuality techniques that work at the **pre-training / continued pre-training** level, while FLAME operates at the **alignment fine-tuning** level.

## Related

- [[Extrinsic Hallucination]]
- [[FActScore]]
- [[Reinforcement Learning from Human Feedback]]
- [[Supervised Fine-Tuning]]
- [[Safety and Alignment]]
- [[GopherCite]]
