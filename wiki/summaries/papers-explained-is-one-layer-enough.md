# Papers Explained: Is One Layer Enough?

**Source**: `raw/draft_Papers-Explained--Is-One-Layer-Enough-36b5241b379b.md`  
**Paper**: https://arxiv.org/abs/2607.01232  
**Ingested**: 2026-08-23  
**Tags**: #summary

## Summary

**Is One Layer Enough?** systematically investigates the per-layer contribution to post-training in deep language models (specifically during Reinforcement Learning with Verifiable Rewards, RLVR, and Supervised Fine-Tuning, SFT). By training only a single transformer block at a time while keeping all other layers frozen, the authors discover that **layer contribution varies dramatically across depth but remains remarkably consistent across datasets, algorithms, and tasks**. In modern architectures like Qwen3 and Llama, middle-to-deep layers account for nearly 80%+ of the total downstream reasoning gains achieved by full-parameter tuning.

![Papers Explained Is One Layer Enough banner](../assets/papers-explained-is-one-layer-enough/fig-1.webp)

### Key Insights & Layer-Adaptive Optimization

1. **Single-Layer Training Power**: Training just *one* carefully chosen middle-to-deep layer can match up to 85–90% of the accuracy gains of full-parameter RLVR on MATH and GSM8K.
2. **Layer Contribution Profile**:
   - Initial layers (embedding and early attention) contribute negligible reasoning improvements.
   - Middle-to-deep layers (e.g. layers 18–28 in a 36-layer model) exhibit peak learning velocity and representational plastic capacity.
   - The final layers before the LM head show moderate, formatting-oriented gains.
3. **Layer-Adaptive Learning Rate (LALR)**: Scaling learning rates proportionally to empirical layer contribution profiles accelerates convergence and improves final full-parameter performance by 2–3 percentage points.
4. **Layer-Selective Training (LST)**: Freezing low-contribution early layers cuts backward-pass memory and compute by 40–50% with zero loss in downstream benchmark accuracy.

![Single Layer Contribution Curves and LALR Performance](../assets/papers-explained-is-one-layer-enough/fig-7.webp)

## Key Claims

- Layer contribution to post-training reasoning is highly heterogeneous across depth but invariant across tasks and datasets.
- A single middle-to-deep layer can recover the vast majority of full-parameter RLVR reasoning performance.
- Layer-Adaptive Learning Rates (LALR) and Layer-Selective Training (LST) dramatically improve training speed and memory efficiency.

## Figures

| Figure | Caption | Page |
|--------|---------|------|
| ![fig-1](../assets/papers-explained-is-one-layer-enough/fig-1.webp) | Overview banner. | Overview |
| ![fig-2](../assets/papers-explained-is-one-layer-enough/fig-2.webp) | Experimental setup across Qwen3 and Llama model families. | Setup |
| ![fig-3](../assets/papers-explained-is-one-layer-enough/fig-3.webp) | Single-layer training contribution across all layers on MATH. | Analysis |
| ![fig-4](../assets/papers-explained-is-one-layer-enough/fig-4.webp) | Layer contribution consistency across GSM8K, Olympiad, and Codeforces. | Analysis |
| ![fig-5](../assets/papers-explained-is-one-layer-enough/fig-5.webp) | Comparison across RLVR (GRPO) and SFT training algorithms. | Comparison |
| ![fig-6](../assets/papers-explained-is-one-layer-enough/fig-6.webp) | Layer-Adaptive Learning Rate (LALR) formulation and schedule. | Method |
| ![fig-7](../assets/papers-explained-is-one-layer-enough/fig-7.webp) | Full-parameter training acceleration with LALR. | Results |
| ![fig-8](../assets/papers-explained-is-one-layer-enough/fig-8.webp) | Layer-Selective Training (LST) compute vs. accuracy Pareto curve. | Efficiency |
| ![fig-9](../assets/papers-explained-is-one-layer-enough/fig-9.webp) | Heuristic layer selection guidelines for arbitrary model depths. | Heuristics |
| ![fig-10](../assets/papers-explained-is-one-layer-enough/fig-10.webp) | Representational drift and weight delta analysis across layers. | Analysis |
| ![fig-11](../assets/papers-explained-is-one-layer-enough/fig-11.webp) | Cross-architecture validation on Gemma and Mistral. | Generalization |
| ![fig-12](../assets/papers-explained-is-one-layer-enough/fig-12.webp) | Memory savings during single-layer and selective-layer backpropagation. | Efficiency |
| ![fig-13](../assets/papers-explained-is-one-layer-enough/fig-13.webp) | Gradient norm distribution across transformer depth. | Dynamics |
| ![fig-14](../assets/papers-explained-is-one-layer-enough/fig-14.webp) | Qualitative reasoning trace changes under middle-layer training. | Qualitative |
| ![fig-15](../assets/papers-explained-is-one-layer-enough/fig-15.webp) | Comparison against LoRA rank scaling across depth. | Comparison |
| ![fig-16](../assets/papers-explained-is-one-layer-enough/fig-16.webp) | Synthesis of layer contribution principles for post-training. | Summary |

## Entities

- [[Layer-Adaptive Learning Rate]] — depth-aware learning rate scheduling.
- [[Layer-Selective Training]] — compute-efficient post-training updating only high-contribution layers.
- [[Reasoning Models]] — mathematical and logical reasoning post-training.
- [[Model Compression and Efficiency]] — training compute optimization.

## Questions & Gaps

- Whether layer contribution profiles shift in multimodal vision-language architectures where early layers process visual tokens.
- Impact of Layer-Selective Training on long-term safety alignment and catastrophic forgetting.

## Related

- [[Model Compression and Efficiency]] — core efficiency topic.
- [[Reinforcement Learning Topic]] — post-training RLVR.
- [[Beyond LoRA: Can You Beat the Most Popular Fine-Tuning Technique?]] — parameter-efficient fine-tuning alternatives.
