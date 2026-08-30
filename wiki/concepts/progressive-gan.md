# Progressive GAN

**Type**: concept  
**Tags**: #concept

## Overview

Progressive Growing of GANs (Karras et al. 2017) trains generator and discriminator incrementally from low to high resolution. New layers learn high-frequency details while existing layers retain coarse structure. Smooth transitions blend old and new resolution paths via \(\alpha\)-weighted residual skips (0→1). First method to generate realistic **1024×1024** images; 2–6× training speedup from spending most iterations at low resolution.

## Appearances

- [[GANs in Computer Vision: Improved Training with Wasserstein Distance, Game Theory Control, and Progressively Growing Schemes]] — architecture diagram, transition mechanics, toRGB/fromRGB blocks, weight normalization and feature normalization stabilizers.
- [[GANs in Computer Vision: 2K Image and Video Synthesis, and Large-Scale Class-Conditional Image Generation]] — Pix2PixHD G1/G2 coarse-to-fine design compared to progressive growing.
- [[GANs in Computer Vision: Semantic Image Synthesis and Learning a Generative Model from a Single Image]] — [[SinGAN]] coarse-to-fine multi-scale training analogy.
- [[Papers Explained Review 05 - Generative Adversarial Networks]] — paper survey context.

## Notes

Precursor to [[StyleGAN]] lineage (same authors; Karras et al.). Mode collapse can still occur from escalating G/D error magnitudes at high resolution. Transition timing underspecified in original paper. Official TensorFlow implementation.

## Related

- [[Wasserstein GAN]]
- [[DCGAN]]
- [[Generative Adversarial Networks]]
- [[Mode Collapse]]
