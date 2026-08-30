# An overview of classifier-free diffusion guidance: impaired model guidance with a bad version of itself (part 2)

Nikolas Adaloglou, Tim Kaiser on 2024-09-26 · 11 mins

Source: https://theaisummer.com/classifier-free-guidance-part-2/

CFG alternatives when models lack conditioning dropout or for unconditional generation. Generalizes CFG to positive/negative models: D_out = D_neg + (1+γ)(D_pos − D_neg).

## Self-Attention Guidance (SAG, Hong et al.)

Negative term = same model with high self-attention patches Gaussian-blurred. Training-free; works conditional or unconditional. ~10% FID improvement; OOD sensitivity at aggressive perturbation.

## Perturbed Attention Guidance (PAG, Ahn et al.)

Replace selected self-attention maps with identity → D̃_θ. Training-free; breaks semantic structure as negative signal. Architecture/layer selection remains manual.

## Autoguidance (Karras et al.)

Negative = inferior version of positive model: fewer parameters (30–50%) and/or earlier checkpoint (τ ∈ [T/3.5, T/16]). Both conditional — avoids task discrepancy of vanilla CFG. EMA hyperparameters tuned at sampling. SOTA on ImageNet-512/64; requires training smaller model or multiple checkpoints.

## Independent Condition Guidance (ICG, Sadat et al.)

Training-free for models without dropout: use random condition as negative instead of unconditional. Similar metrics to CFG on Stable Diffusion and DiT-XL.

## Other approaches

- **SIMS**: Retrain auxiliary model on synthetic data from main model.
- **SEG**: Gaussian-blur attention weights (smoothed energy guidance); tune σ only.

Conclusion: no single drop-in CFG replacement; tradeoffs between training cost, hyperparameter search, and architecture dependence.
