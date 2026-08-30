# Papers Explained: No Position Encoding (NoPE)

**Source**: `raw/draft_Papers-Explained--No-Position-Encoding--NoPE--9a670429a736.md`  
**Paper**: https://arxiv.org/abs/2305.19466  
**Ingested**: 2026-08-23  
**Tags**: #summary

## Summary

**No Position Encoding (NoPE)** investigates whether decoder-only autoregressive Transformers actually require explicit positional encodings (such as sinusoidal, learned absolute, RoPE, or ALiBi). Kazemnejad et al. (2023) show that **causal attention masking alone implicitly injects positional information**, allowing models trained without any explicit positional encodings (NoPE) to learn both absolute and relative positional relationships. Furthermore, NoPE demonstrates superior context length extrapolation compared to traditional absolute positional encodings and matches or exceeds RoPE on length generalization.

![Papers Explained NoPE banner](../assets/papers-explained-nope/fig-1.webp)

### How NoPE Represents Position

Because the lower-triangular causal attention mask restricts each token $i$ to attend only to tokens $j \le i$, the number of available receptive-field tokens directly encodes the absolute position $i$.
1. **Absolute Positional Signal**: The norm and unnormalized query-key product implicitly scale with token index $i$, allowing the model to distinguish prefix positions from later positions.
2. **Relative Positional Signal**: Multi-head self-attention learns to represent relative distances $i - j$ through attention probability decay and token-shifting key transformations.
3. **Length Extrapolation**: Because NoPE has no fixed positional tables or rotary frequencies tuned to specific pretraining sequence bounds, it does not suffer catastrophic out-of-distribution frequency breakdown when evaluating on sequences $2\times\text{--}4\times$ longer than the pretraining window.

![Positional Probing and Extrapolation Analysis](../assets/papers-explained-nope/fig-3.webp)

## Key Claims

- Causal masking inherently provides autoregressive Transformers with sufficient inductive bias to represent both absolute and relative positions.
- NoPE matches explicit positional encodings on standard in-distribution language modeling benchmarks.
- NoPE significantly outperforms learned and sinusoidal absolute positional encodings on length generalization and context extrapolation.

## Figures

| Figure | Caption | Page |
|--------|---------|------|
| ![fig-1](../assets/papers-explained-nope/fig-1.webp) | NoPE overview banner. | Overview |
| ![fig-2](../assets/papers-explained-nope/fig-2.webp) | Causal attention masking and implicit position flow. | Method |
| ![fig-3](../assets/papers-explained-nope/fig-3.webp) | Linear probing of absolute token positions across layers. | Analysis |
| ![fig-4](../assets/papers-explained-nope/fig-4.webp) | Relative position probing and attention distance curves. | Analysis |
| ![fig-5](../assets/papers-explained-nope/fig-5.webp) | Context length extrapolation comparison: NoPE vs RoPE vs ALiBi. | Evaluation |
| ![fig-6](../assets/papers-explained-nope/fig-6.webp) | In-distribution language modeling perplexity across model scales. | Evaluation |
| ![fig-7](../assets/papers-explained-nope/fig-7.webp) | Synthetic tracking tasks (copying, associative recall). | Synthetic |
| ![fig-8](../assets/papers-explained-nope/fig-8.webp) | Attention map visualization showing emergence of relative heads. | Visualization |
| ![fig-9](../assets/papers-explained-nope/fig-9.webp) | Query and Key vector norm scaling with sequence depth. | Dynamics |
| ![fig-10](../assets/papers-explained-nope/fig-10.webp) | Impact of sequence length during pretraining. | Ablations |
| ![fig-11](../assets/papers-explained-nope/fig-11.webp) | Layer-wise emergence of positional representations. | Layer Analysis |
| ![fig-12](../assets/papers-explained-nope/fig-12.webp) | Downstream evaluation on GLUE and SuperGLUE benchmarks. | Downstream |
| ![fig-13](../assets/papers-explained-nope/fig-13.webp) | Comparison across causal vs. non-causal bidirectional attention. | Non-Causal |
| ![fig-14](../assets/papers-explained-nope/fig-14.webp) | Passkey retrieval and needle-in-a-haystack extrapolation. | Retrieval |
| ![fig-15](../assets/papers-explained-nope/fig-15.webp) | Token distance sensitivity heatmaps. | Analysis |
| ![fig-16](../assets/papers-explained-nope/fig-16.webp) | Mathematical proof of implicit causal position encoding. | Theory |
| ![fig-17](../assets/papers-explained-nope/fig-17.webp) | Training throughput and memory comparison. | Efficiency |
| ![fig-18](../assets/papers-explained-nope/fig-18.webp) | Extrapolation curves up to 8k tokens. | Scaling |
| ![fig-19](../assets/papers-explained-nope/fig-19.webp) | Summary of positional encoding paradigms. | Taxonomy |

## Entities

- [[NoPE]] — No Position Encoding paradigm for causal transformers.
- [[Positional Encoding]] — positional representations in transformers.
- [[Long Context]] — sequence length generalization.
- [[Large Language Models]] — causal autoregressive models.

## Questions & Gaps

- Failure of NoPE in bidirectional non-causal models (BERT/T5) where causal masking is absent.
- Performance on exact multi-digit arithmetic and symbolic tasks requiring precise absolute coordinate indexing.

## Related

- [[Papers Explained Review 06 - Position Encodings]] — position encodings survey.
- [[Positional Encoding]] — core concept.
- [[Papers Explained: Attention with Linear Biases (ALiBi)]] — linear bias alternative.
- [[Papers Explained: Rotary Position Embedding (RoPE)]] — rotary alternative.
