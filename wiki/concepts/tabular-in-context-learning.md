# Tabular In-Context Learning

**Type**: concept  
**Tags**: #concept

## Overview

**Tabular in-context learning** treats a classification or regression table as a single prompt: training rows and test rows are presented together, and the model predicts labels for the test rows in one forward pass without gradient updates on that dataset. The idea parallels LLM in-context learning but must handle two-dimensional, orderless structure (row and column swaps should not change meaning).

## Appearances

- [[TabFM]] — Google Research foundation model combining TabPFN-style row/column attention with TabICL-style compression (Jun 2026).
- [[Papers Explained 418 - TabArena]] — living benchmark where TabPFN-class models compete against tuned tree ensembles.

## Notes

- Prior models in this line include TabPFN (prior-data fitted network) and TabICL (in-context learning transformer for tabular rows).
- TabFM extends the stack with alternating row/column attention, per-row compression, and an ICL transformer trained on synthetic SCM data at scale.
- Zero-shot ICL removes per-dataset hyperparameter search but ensemble variants (TabFM-Ensemble) reintroduce light tuning for leaderboard gains.

## Related

- [[TabFM]] — Google zero-shot tabular foundation model.
- [[Papers Explained 418 - TabArena]] — evaluation benchmark.
- [[Papers Explained Review 04 - Tabular Deep Learning]] — broader tabular deep learning survey.
- [[Evaluation and Benchmarks]] — topic hub.
