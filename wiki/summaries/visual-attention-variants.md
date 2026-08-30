# A Visual Guide to Attention Variants in Modern LLMs

**Source**: `raw/visual-attention-variants/full-article.html` (595 KB), `raw/visual-attention-variants/full-article.md` (markdown view)  
**URL**: https://magazine.sebastianraschka.com/p/visual-attention-variants  
**Ingested**: 2026-06-07  
**Tags**: #summary

## Summary

Sebastian Raschka's March 2026 *Ahead of AI* article is a visual reference tour of attention mechanisms used in prominent **open-weight** LLMs—from classic [[Multi-Head Attention]] through [[KV Cache]]-oriented efficiency variants (GQA, MLA), sparse/local patterns (SWA, DeepSeek Sparse Attention), stability tweaks (gated attention), and [[Linear Attention Hybrids]]. It accompanies Raschka's public [LLM architecture gallery](https://sebastianraschka.com/llm-architecture-gallery/) (45+ model cards at publication) and poster release.

The article opens with a compressed [[Self-Attention]] refresher: causal masked \(T \times T\) weight matrices, Q/K/V projections, and parallel heads—then walks seven deployed families with example architectures and memory/compute intuition. **Grouped-query attention (GQA)** shares key-value heads across query heads, cutting cache traffic with minimal recipe change; Raschka frames it as the pragmatic 2023–2026 default when MLA's implementation cost is unwelcome. **Multi-head latent attention (MLA)** compresses cached state into a latent representation (DeepSeek-V2 lineage); ablations suggest better quality-per-byte than GQA at large scale, at the cost of serving complexity—Sarvam's 30B (GQA) vs 105B (MLA) pair is cited as a deliberate side-by-side choice.

**Sliding window attention (SWA)** limits each position to a local prefix (often interleaved with periodic global layers); Gemma 3's more aggressive 5:1 local:global ratio and 1024-token window barely moved perplexity in reported ablations. **DeepSeek Sparse Attention (DSA)** also attends to a subset of past tokens but learns which positions via a lightning indexer and top-\(k\) selector—paired with MLA in DeepSeek V3.2 and GLM-5. **Gated attention** adds output gating, zero-centered QK-norm, and partial RoPE to retained full-attention layers in hybrids (Qwen3-Next/3.5) and conventional stacks (Trinity). **Hybrid attention** replaces most layers with linear-time mixers ([[Gated DeltaNet]], Kimi Delta Attention, Lightning Attention, Mamba-2) while keeping periodic heavy layers for retrieval—typically 3:1—with Qwen3.5 promoting the former Qwen3-Next recipe into the flagship line.

Raschka closes pragmatically: no public apples-to-apples architecture bake-off exists; hybrids trade long-context efficiency for less mature inference stacks; he runs classic GQA models (e.g., GPT-OSS) faster locally today, but expects hybrid stacks to matter for agentic long contexts.

## Key Claims

- Raschka's LLM architecture gallery documents 45+ open models with visual cards; a print poster is available but smallest sizes sacrifice readable micro-text.
- MHA gives each head its own K/V projections—modeling-friendly but expensive for [[KV Cache]] at long context.
- GQA (Ainslie et al., 2023) shares K/V across query-head groups; it became the "new standard" dense replacement for MHA because it cuts cache memory and traffic with modest implementation change.
- GQA savings grow with context length; reducing to one shared K/V group approaches multi-query attention (cheaper, more quality risk).
- MLA (DeepSeek-V2) compresses cached K/V into a latent representation rather than sharing heads; DeepSeek-V2 ablations show GQA below MHA on quality while MLA stays competitive or better when tuned.
- Colleagues report MLA works best at large scale (~100B+); below that GQA is easier to tune (Sarvam 30B GQA vs 105B MLA as reference).
- SWA restricts attention to a fixed local window; hybrid local:global ratios (e.g., Gemma 3 5:1, OLMo 3 / Arcee Trinity 3:1) tune how aggressively global context is preserved.
- Gemma 3 ablations: smaller window + more local layers had little perplexity impact vs Gemma 2's milder hybrid.
- DSA (DeepSeek V3.2) learns sparse attention patterns via indexer + top-\(k\) selector instead of a fixed sliding window; combined with MLA for cache representation + sparse revisit pattern.
- Gated attention modifies full-attention blocks (output gate, zero-centered QK-norm, partial RoPE) for stability inside hybrid stacks—not a separate attention family.
- Qwen3-Next/3.5 use 3:1 Gated DeltaNet : gated full attention; Kimi Linear swaps in Kimi Delta Attention + gated MLA; Ling 2.5 uses Lightning Attention + MLA.
- Nemotron 3 Nano/Super push further toward Mamba-2-heavy hybrids with sparse MoE and only occasional self-attention layers.
- Hybrids aim at long-context efficiency; Raschka notes inference stacks are less optimized than classic GQA and may suit agent contexts; local tok/s can still favor classic architectures today.

## Figures

| Figure | Caption | Page |
|--------|---------|------|
| ![fig-1](../assets/visual-attention-variants/fig-1.png) | LLM architecture gallery overview with visual model cards | — |
| ![fig-2](../assets/visual-attention-variants/fig-2.jpg) | Printed poster version with scale objects | — |
| ![fig-3](../assets/visual-attention-variants/fig-3.png) | OLMo 2 as an MHA example architecture | — |
| ![fig-4](../assets/visual-attention-variants/fig-4.webp) | Word-by-word translation failure illustrating sentence-level structure needs | — |
| ![fig-5](../assets/visual-attention-variants/fig-5.webp) | Attention lets decoders revisit full input instead of one compressed state | — |
| ![fig-6](../assets/visual-attention-variants/fig-6.webp) | Causal masked attention matrix (\(T \times T\)) | — |
| ![fig-7](../assets/visual-attention-variants/fig-7.png) | Self-attention pipeline: \(X \to Q,K,V \to A \to Z\) | — |
| ![fig-8](../assets/visual-attention-variants/fig-8.png) | Single-head scaled dot-product attention (compact view) | — |
| ![fig-9](../assets/visual-attention-variants/fig-9.png) | Multi-head attention: parallel heads with separate projections | — |
| ![fig-10](../assets/visual-attention-variants/fig-10.png) | GQA: multiple query heads share key-value projections | — |
| ![fig-11](../assets/visual-attention-variants/fig-11.png) | KV-cache memory savings: lower is better as context grows | — |
| ![fig-12](../assets/visual-attention-variants/fig-12.webp) | Total KV cache: Sarvam 105B MLA vs 30B GQA vs plain MHA | — |
| ![fig-13](../assets/visual-attention-variants/fig-13.webp) | MLA caches latent representation instead of grouping K/V heads | — |
| ![fig-14](../assets/visual-attention-variants/fig-14.png) | MLA latent-cache savings vs full K/V tensors at long context | — |
| ![fig-15](../assets/visual-attention-variants/fig-15.png) | DeepSeek-V2 ablation: GQA below MHA; MLA competitive or better | — |
| ![fig-16](../assets/visual-attention-variants/fig-16.webp) | GQA vs MLA: simplicity vs modeling performance at scale | — |
| ![fig-17](../assets/visual-attention-variants/fig-17.png) | SWA: global attention vs local sliding-window layers | — |
| ![fig-18](../assets/visual-attention-variants/fig-18.webp) | Gemma 3 SWA ablation: aggressive local:global ratio barely hurts perplexity | — |
| ![fig-19](../assets/visual-attention-variants/fig-19.webp) | Long-context savings from interleaving local SWA layers | — |
| ![fig-20](../assets/visual-attention-variants/fig-20.webp) | DSA: learned sparse subset vs fixed SWA window | — |
| ![fig-21](../assets/visual-attention-variants/fig-21.webp) | DeepSeek V3.2 combines MLA cache compression with DSA sparse pattern | — |
| ![fig-22](../assets/visual-attention-variants/fig-22.png) | DSA lightning indexer + token selector mechanism | — |
| ![fig-23](../assets/visual-attention-variants/fig-23.webp) | Gated attention in Trinity (output gate before projection) | — |
| ![fig-24](../assets/visual-attention-variants/fig-24.webp) | Qwen3-Next/3.5: gated full attention among Gated DeltaNet blocks | — |
| ![fig-25](../assets/visual-attention-variants/fig-25.webp) | Hybrid 3:1 pattern: cheap mixers + periodic full attention | — |
| ![fig-26](../assets/visual-attention-variants/fig-26.png) | Memory curve: Gated DeltaNet hybrid vs full attention | — |
| ![fig-27](../assets/visual-attention-variants/fig-27.png) | Qwen3.5 promotes Qwen3-Next hybrid into flagship line | — |
| ![fig-28](../assets/visual-attention-variants/fig-28.webp) | Kimi Linear: Kimi Delta Attention + gated MLA in 3:1 hybrid | — |
| ![fig-29](../assets/visual-attention-variants/fig-29.png) | Ling 2.5: Lightning Attention + MLA hybrid | — |
| ![fig-30](../assets/visual-attention-variants/fig-30.png) | Ling 2.5 reported 32k-token throughput vs Kimi K2 | — |
| ![fig-31](../assets/visual-attention-variants/fig-31.webp) | Nemotron 3 Nano: Mamba-2-heavy hybrid with sparse MoE | — |
| ![fig-32](../assets/visual-attention-variants/fig-32.png) | Nemotron 3 Super: Mamba-2 hybrid + latent MoE + shared-weight MTP | — |

Gallery and attention-variant landscape:

![LLM architecture gallery](../assets/visual-attention-variants/fig-1.png)

MHA vs GQA vs MLA on KV cache size (Sarvam comparison):

![KV cache: MLA vs GQA vs MHA](../assets/visual-attention-variants/fig-12.webp)

Hybrid 3:1 stacking pattern:

![Hybrid attention pattern](../assets/visual-attention-variants/fig-25.webp)

## Entities

- [[Sebastian Raschka]] — author; gallery curator and pedagogical explainer of open LLM architectures.
- [[Multi-Head Attention]] — baseline mechanism; OLMo 2/3, GPT-2 cited as MHA examples.
- [[Grouped-Query Attention]] — shared K/V heads for cache-efficient dense models (Llama 3, Qwen3, Gemma 3, Mistral, Sarvam 30B).
- [[Multi-Head Latent Attention]] — DeepSeek-V2 latent cache compression; Sarvam 105B, Kimi K2, GLM-5, Ling 2.5.
- [[Sliding Window Attention]] — local attention windows with periodic global layers (Gemma 3, OLMo 3, Mistral).
- [[DeepSeek Sparse Attention]] — learned sparse indexer/selector in DeepSeek V3.2 and GLM-5.
- [[Gated Attention]] — stability-oriented full-attention block tweaks in Qwen3-Next/3.5 and Trinity.
- [[Gated DeltaNet]] — linear-time mixer in Qwen3 hybrid stacks.
- [[Linear Attention Hybrids]] — 3:1 cheap-mixer + full-attention pattern across Qwen, Kimi, Ling, Nemotron families.
- [[KV Cache]] — central bottleneck motivating GQA, MLA, SWA, and hybrids.
- [[Self-Attention]] — foundational mechanism recap in Section 1.

## Questions & Gaps

- No controlled training-data-matched comparison across attention families; conclusions rely on per-paper ablations and architecture choices.
- MLA quality advantage may be scale-dependent (<100B GQA may remain preferable in practice).
- DSA and hybrid stacks lack mature, universally fast inference implementations vs classic GQA.
- Article defers DeepSeek V4 coverage; future releases may shift the taxonomy again.
- Mamba-3 integration and "attention residuals" flagged as forward-looking but not yet standardized.

## Related

- [[Beyond Standard LLMs]] — companion survey of linear hybrids, diffusion LLMs, and other non-standard decoder designs.
- [[Understanding and Coding the KV Cache in LLMs from Scratch]] — from-scratch KV cache implementation motivating GQA/MLA discussions.
- [[Self-Attention]] — longer conceptual treatment of masked multi-head attention.
- [[Model Compression and Efficiency]] — topic hub for GQA, SWA, MLA, and hybrid efficiency patterns.
- [[Long Context]] — long-window motivation for SWA, DSA, and linear hybrids.
- [[Inference Engineering]] — production serving context for cache layout, paging, and kernel maturity.
