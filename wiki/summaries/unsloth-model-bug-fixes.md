# Unsloth Model Bug Fixes

**Ingested**: 2026-07-22  
**Tags**: #summary #topic

## Summary

Unsloth repeatedly ships **day-zero model support** by patching upstream Hugging Face implementations before official fixes land. The gemma-bugs post is the canonical case study; the same patterns recur across Gemma, Llama, Mistral, and DeepSeek launches: tokenizer/chat-template errors, RoPE precision, activation approximations, and softcapping mismatches.

## Key Claims

**Gemma-specific (gemma-bugs):**
- Missing **`<bos>`** token in training data → add explicitly.
- **Untrained tokens** (e.g. `<start_of_turn>`) → initialize embeddings to mean of trained tokens.
- **Chat template / EOS / PAD** misconfiguration breaks SFT loss masking.
- **RoPE** must run in float32 for stability at long context.
- **GELU** should use `approximate="tanh"` to match Google checkpoints.
- **Softcapping** logits must match Gemma reference implementation.

**Cross-cutting fixes (synthesized across 2024–2026 launches):**
- Attention **sliding-window** + KV cache alignment for Mistral/Llama variants.
- **Vision tower** dtype and pixel-normalization parity for multimodal models.
- **MoE** router dtype and expert load-balancing loss toggles.
- **Tokenizer** `add_eos_token` vs `add_bos_token` defaults per model family.

## Figures

| Figure | Caption |
|--------|---------|
| — | Debugging workflow described in prose |

## Entities

- [[Google Research]] — Gemma reference implementations.
- [[Hugging Face]] — Transformers configs Unsloth patches.
- [[Unsloth]] — ships fixes in `unsloth` package before upstream merge.

## Questions & Gaps

- Upstream merge lag: which fixes remain Unsloth-only vs merged to Transformers?
- Automated regression tests for per-model chat templates.

## Related

- [[Unsloth Model Support 2024]]
- [[Unsloth Model Support 2025]]
- [[Gemma 4]]
- [[KV Cache]]

## Sources

- `raw/gemma-bugs/full-article.md`
