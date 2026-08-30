# Differential Transformer V2

**Source**: `raw/diff-attn-v2/full-article.html`, `raw/diff-attn-v2/full-article.md`
**Ingested**: 2026-07-10
**Tags**: #summary

## Summary

A Microsoft Research post introducing Differential Transformer V2 (DIFF V2), a revision of Differential Attention (DIFF V1) aimed at closing two practical gaps that limited DIFF V1's production adoption: decoding speed and training stability at scale. DIFF computes attention as a difference of two softmax attention maps, `attn1 - λ·attn2`. This cancels out noise/outlier attention mass and, per the DIFF V1 paper, improves long-context retrieval and reduces hallucination. DIFF V1 doubled both query and value head dimensions to construct the two attention maps, which meant slower decoding (the KV cache's value component must be loaded twice) and required custom attention kernels incompatible with off-the-shelf FlashAttention.

DIFF V2 fixes this by doubling only the query heads while keeping key/value heads fixed at baseline count, borrowing the extra query parameters from elsewhere in the model rather than inflating the KV cache. Because head dimensions now match a standard GQA layout, DIFF V2 runs directly on stock FlashAttention with no custom kernel, matching baseline Transformer decoding speed (decoding is memory-bound, and only the KV cache size, which is unchanged, determines that bound). The design also crucially requires that the two subtracted attention heads share the same GQA group (same K/V), confirmed via ablation to be necessary for the differential construction to actually improve loss and stability; subtracting cross-group heads instead produces markedly worse training stability.

The second major change removes DIFF V1's per-head RMSNorm on the context vector, identified as a stability hazard: for a uniform attention distribution over `n=8192` tokens, RMSNorm needs to rescale by √n ≈ 90.5x, producing large gradient spikes at scale. DIFF V2 instead uses a token- and head-wise projected λ (via `sigmoid`, replacing DIFF V1's globally shared, exponentially-reparameterized λ) that bounds the context RMS in `(0, √2)` without needing RMSNorm's rescaling, and can push the RMS lower bound to exactly zero, a property the authors tie to eliminating attention sinks. In production-scale pretraining (dense models and a 30A3 MoE, trillions of tokens, aggressive learning rates of 6e-4 to 1e-3), DIFF V2 shows notably lower LM loss than a matched Transformer baseline (a 0.02-0.03 gap at 1T tokens), fewer/smaller loss and gradient spikes, and reduced activation-outlier magnitude, with training still ongoing at time of writing and downstream long-context/post-training evaluations pending.

## Key Claims

- DIFF V2 doubles query heads only (not KV heads), so it decodes at baseline Transformer speed and runs on stock FlashAttention with no custom kernel, unlike DIFF V1 which doubled value-head dimension and needed custom kernels.
- DIFF V2 removes DIFF V1's per-head RMSNorm; at `n=8192` tokens, RMSNorm's implicit √n ≈ 90.5x rescaling of a uniform-attention context vector is identified as the source of DIFF V1's large-scale training instability.
- The replacement mechanism is a token-/head-wise projected λ passed through `sigmoid`, bounding context RMS in `(0, √2)` and allowing the lower bound to reach zero, which the post ties to eliminating attention sinks (comparing to similar softmax-denominator tricks in "Attention Is Off By One," gpt-oss's learned per-head scalar, and Gated Attention).
- Ablations confirm the two subtracted attention heads must share a GQA group (same K/V): cross-group subtraction produces markedly worse instability; omitting the λ scaling factor gives too-small initial context RMS; skipping the `sigmoid` leaves RMS unbounded above.
- Pretraining on production-scale dense and 30A3-MoE models over trillions of tokens at 6e-4-1e-3 learning rates shows DIFF V2 with 0.02-0.03 lower LM loss than baseline Transformer at 1T tokens, fewer/smaller gradient spikes, and reduced activation outliers; results are preliminary and experiments were still running at publication.
- Constructing the differential operation explicitly (rather than letting a standard Transformer learn `W_O^{2i} = -W_O^{2i+1}` implicitly) saves roughly 25% of attention-module parameters under GQA, since attention parameters are dominated by `W_Q` and `W_O`.
- DIFF V2 is compatible with sparse attention frameworks, though block-selection strategy needs to account for pairs of differential heads within a GQA group rather than treating all heads uniformly.

## Figures

No figures were extracted for this ingest, per this batch's no-figure-download policy; the article is primarily text, math, and code rather than charts.

## Entities

- [[Microsoft]] — Microsoft Research authors the Differential Transformer line of work (DIFF V1 and V2).
- [[Hugging Face]] — hosts the post on its Enterprise blog.

## Questions & Gaps

- The post explicitly defers evaluation of mid-/post-training learning efficiency and downstream long-context benchmark performance ("context rot" alleviation) to a future, more formal report.
- No comparison is given yet against other softmax-denominator-relaxation approaches (Gated Attention, gpt-oss's learned scalar) on the same production-scale pretraining setup, only a qualitative discussion of how they relate mathematically.

## Related

- [[Papers Explained 428 - gpt-oss]] — its learned per-head softmax-denominator scalar is cited as a related mechanism for bounding context RMS.
- [[Gated Attention]]
- [[Grouped-Query Attention]]
