# Gemma 4 Technical Report

**Source URL**: https://arxiv.org/abs/2607.02770

Google DeepMind technical report for Gemma 4. See `raw/gemma-4-technical-report/full-article.html` for full content.

Section 2.6 Multi-Token Prediction Drafter: 4-layer cross-attending block (3 local + 1 global), dims 256 (E2B/E4B) or 1024 (26B-A4B/31B), fed last-layer activations + token embeddings, cross-attends main model KV cache. E2B/E4B clustered LM head reduces matmul from d×262000 to d×4096.

Drafter params: E2B 76M, E4B 77M, 12B 400M, 26B-A4B 430M, 31B 500M.
