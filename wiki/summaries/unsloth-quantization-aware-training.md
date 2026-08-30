# Unsloth Quantization-Aware Training

**Ingested**: 2026-07-22  
**Tags**: #summary #topic

## Summary

Unsloth documents **Quantization-Aware Training (QAT)** workflows: simulate quantization during fine-tuning ("fake quant") so deployed INT4/FP8 weights retain quality. Covers general QAT concepts (TorchAO, ExecuTorch) and **Gemma 4 QAT** specifics—Q4_0 lattice fixes, mobile formats, and integration with Google's QAT checkpoints. Cross-links [[Gemma 4 QAT]] (Google blog) without duplicating Google's release details.

## Key Claims

- **Fake quant** forward pass: round-trip weights through target quantizer during training (quantization-aware-training-qat).
- **TorchAO / ExecuTorch** export paths for edge deployment.
- **Q4_0 lattice fixes**: Unsloth corrects asymmetric rounding bugs vs naive PTQ.
- **Gemma 4 QAT** doc (gemma-4-qat): how to fine-tune on top of Google's QAT checkpoints; preserves MTP speedups when applicable.
- QAT preferred over PTQ when **<2% quality loss** target at 4-bit.

## Figures

| Figure | Caption |
|--------|---------|
| — | Fake-quant flow described in source docs |

## Entities

- [[Quantization-Aware Training]] — concept.
- [[Gemma 4]] — primary QAT model family.
- [[Google Research]] — official Gemma 4 QAT checkpoints.
- [[Model Compression and Efficiency]] — QAT vs PTQ.
- [[Unsloth]] — training integration.

## Questions & Gaps

- QAT recipe generalization beyond Gemma 4 (Qwen, Llama) undocumented.
- Interaction between QAT and Unsloth dynamic quant export pipeline.

## Related

- [[Unsloth Dynamic Quantization]]
- [[Gemma 4 QAT]]
- [[Unsloth Model Support 2026]]

## Sources

- `raw/quantization-aware-training-qat/full-article.html`
- `raw/gemma-4-qat/full-article.html`
