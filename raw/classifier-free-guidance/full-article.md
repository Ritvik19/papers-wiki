# An overview of classifier-free guidance for diffusion models

Nikolas Adaloglou, Tim Kaiser on 2024-07-22 · 19 mins

Source: https://theaisummer.com/classifier-free-guidance/

Overview of classifier-free guidance (CFG) and noise-dependent sampling schedule improvements. Follow-up part 2 covers replacing the unconditional model. Appendix recaps cross- and self-attention in U-Net denoisers.

## Classifier guidance (Dhariwal & Nichol)

GAN truncation trick doesn't transfer to diffusion (Gaussian noise constraint). Classifier guidance trains p(c|x_t) on noisy images; guided score = unconditional + w·classifier gradient. w>1 sharpens toward class modes; trades diversity for fidelity. Limitations: weak signal at high noise; requires parallel classifier training.

## Classifier-free guidance (Ho & Salimans)

Derive conditioning term from conditional minus unconditional scores. Train single model with conditioning dropout (10–20%). Guided score = unconditional + w·(conditional − unconditional). w=0 unconditional, w=1 conditional, w>1 extrapolation. Alternative γ=w−1 formulation emphasizes extrapolation. Initially rejected at ICLR 2022.

Limitations: oversaturation, OOD at high w, reduced diversity.

## Static and dynamic thresholding (Imagen)

High w causes denoised x̂₀ outside [-1,1]. Static: clamp to [-1,1]. Dynamic: clip to [-s,s] at percentile p=99.5%, rescale — prevents saturation at high guidance.

## Noise-dependent CFG schedules

- **Dynamic CFG / CADS (Sadat et al.)**: Linear w(σ) from unconditional at high noise to conditional at low noise. CADS anneals condition c with Gaussian corruption instead of w alone.
- **Limited interval CFG (Kynkäänniemi et al.)**: Apply CFG only in intermediate σ interval; disable at start/end. Improves FID and FD_DINOv2; fewer guidance evals.
- **Wang et al.**: Monotonically increasing w schedules for text-to-image.
- **Spatial CFG (Shen et al.)**: Per-region guidance weights W_t from cross/self-attention segmentation maps.

## Appendix: attention in U-Net denoisers

Cross-attention binds text tokens to regions (text-to-image only). Self-attention preserves structure; class-conditional models use self-attention without cross-attention. Condition swap experiments show prompt impact fades in late denoising steps.
