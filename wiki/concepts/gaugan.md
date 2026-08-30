# GauGAN

**Type**: concept  
**Tags**: #concept

## Overview

GauGAN (Park et al., 2019; semantic image synthesis with spatially-adaptive normalization) generates photorealistic images from segmentation maps using a [[SPADE]]-based generator and [[Pix2PixHD]] multi-scale discriminators. SPADE injects layout via spatially varying γ/β from the mask instead of feeding the mask into the generator input. Supports multi-modal synthesis via latent noise and optional image encoder (VAE-style). NVIDIA project with public demo.

## Appearances

- [[GANs in Computer Vision: Semantic Image Synthesis and Learning a Generative Model from a Single Image]] — SPADE derivation, generator architecture, pix2pixHD++ baseline, results.
- [[SPADE]] — core normalization module.
- [[Papers Explained 253 - SPADE]] — paper-level coverage.

## Notes

Builds on [[Pix2PixHD]] (multi-scale D) and contrasts [[Adaptive Instance Normalization]] (loses semantics). Segmentation from DeepLab v2 at inference. Fewer parameters than encoder–decoder Pix2PixHD.

## Related

- [[SPADE]]
- [[Pix2PixHD]]
- [[Adaptive Instance Normalization]]
- [[Generative Adversarial Networks]]
