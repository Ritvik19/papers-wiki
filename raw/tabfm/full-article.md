# Introducing TabFM: A zero-shot foundation model for tabular data

Source: https://research.google/blog/introducing-tabfm-a-zero-shot-foundation-model-for-tabular-data/

TabFM frames tabular classification and regression as in-context learning. The full dataset (training rows plus test rows) is passed as a single prompt; predictions come from one forward pass with no per-dataset training or hyperparameter tuning.

Architecture: alternating row/column attention (TabPFN-style), row compression into dense vectors, then a TabICL-style transformer over compressed rows.

Pre-training uses hundreds of millions of synthetic datasets from structural causal models. Benchmarked on TabArena (38 classification + 13 regression datasets, 700-150,000 samples). TabFM and TabFM-Ensemble lead Elo ratings. BigQuery AI.PREDICT integration planned.
