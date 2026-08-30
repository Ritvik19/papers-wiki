# GopherCite

**Type**: concept  
**Tags**: #concept

## Overview

GopherCite (Menick et al. 2022, DeepMind) is a system that trains language models to **produce statements supported by citations** from retrieved web sources. Like [[WebGPT]], it combines search-engine retrieval with RL from human preferences, but differs in how demonstrations are generated: GopherCite uses **few-shot prompting + context stuffing** rather than human behavioral cloning.

## Motivation

Grounded responses that cite sources allow humans to verify factual claims, shifting the burden of trust from the model's parametric memory to inspectable external sources. GopherCite frames factual accuracy as: *can the model produce a response that a human would judge as both supported by its cited evidence and plausible as a direct answer?*

## Method

### Demonstration Generation

```
Unlike WebGPT (which uses human demonstrations for behavior cloning):

GopherCite generates demonstrations via few-shot prompting:
  1. Retrieve relevant documents (context stuffing with top-k results)
  2. Prompt the model to generate a response citing those documents
  3. Use a reward model to score which demonstrations are best
  4. Rerank and select high-scoring demonstrations as training data
```

This avoids the need for human web-browsing demonstrations, making data collection cheaper.

### Training Pipeline

```
1. SFT (Supervised Fine-Tuning):
   Train on high-quality few-shot + reranked demonstrations

2. RL from Human Preference:
   - Collect comparison data: two model-generated responses to the same question,
     each with their own retrieved references
   - Humans judge: (a) Is the response supported by its citations?
                   (b) Is it plausible as a direct answer to the question?
   - Train a reward model (RM) on these judgments
   - Apply RL (PPO) and/or best-of-n rejection sampling
```

### Selective Prediction

An additional mechanism to handle uncertain questions: the model is configured to **decline with "I don't know"** when the global RM score falls below a threshold. This is called *selective prediction* — the model abstains rather than hallucinating a supported-sounding answer.

## Comparison with WebGPT

| Property | GopherCite | WebGPT |
|----------|-----------|--------|
| Demonstrations | Few-shot prompting + context stuffing + RM reranking | Human behavioral cloning (web-browsing demonstrations) |
| Retrieval mechanism | Search engine (pre-retrieved) | Interactive web browser |
| SFT source | RM-reranked generated demos | Human demonstrations |
| RL training | ✅ PPO + best-of-n | ✅ PPO + best-of-n |
| Selective prediction | ✅ ("I don't know" via RM threshold) | ❌ (not emphasized) |
| RL improvement over SFT | Limited / small | Limited / small |

## Key Experimental Finding

Both GopherCite and WebGPT show that **RL only introduces limited improvement** over the SFT/BC baseline — and the benefit is even smaller when rejection sampling is also used. This suggests that the SFT data quality (high-quality demonstrations / diverse context stuffing) is the dominant factor in factuality improvement, not the RL signal itself.

## Appearances

- [[Extrinsic Hallucinations in LLMs]] — presented alongside WebGPT as a factuality fine-tuning with attribution approach.

## Notes

- The **selective prediction** mechanism in GopherCite is directly related to the **SelfAware / TruthfulQA** benchmarks: all three are concerned with whether models know when to say "I don't know" rather than hallucinating a confident answer.
- GopherCite's use of context stuffing (filling the prompt window with retrieved documents) is an early example of long-context grounded generation — a pattern now standard in RAG systems.
- The finding that RL adds limited benefit over SFT is consistent with [[WebGPT]] and somewhat consistent with RLHF research showing that the quality of preference data (and SFT init) matters more than the RL algorithm.

## Related

- [[Extrinsic Hallucination]]
- [[WebGPT]]
- [[Reinforcement Learning from Human Feedback]]
- [[FLAME]]
- [[Safety and Alignment]]
- [[Embedding and Retrieval]]
- [[DeepMind]]
