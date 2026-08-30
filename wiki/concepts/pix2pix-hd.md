# Pix2PixHD

**Type**: concept  
**Tags**: #concept

## Overview

Pix2PixHD (Wang et al., 2017) extends [[Pix2Pix]] to 2048×1024 semantic image synthesis. A global generator G1 produces coarse 1024×512 structure; a local enhancer G2 at full resolution refines high-frequency details by fusing G1 features. Three scale-specific PatchGAN discriminators on an image pyramid enforce global and local realism. Multi-scale [[Feature Matching]] loss stabilizes training. Instance boundary maps and learned instance feature embeddings add object-level diversity.

## Appearances

- [[GANs in Computer Vision: 2K Image and Video Synthesis, and Large-Scale Class-Conditional Image Generation]] — full architecture, segmentation types, boundary maps, K-means instance embeddings.
- [[GANs in Computer Vision: Semantic Image Synthesis and Learning a Generative Model from a Single Image]] — multi-scale D reused by [[GauGAN]]; pix2pixHD++ baseline vs SPADE generator.
- [[Pix2Pix]] — lower-resolution paired-translation predecessor.

## Notes

NVIDIA work building on [[Progressive GAN]]-style coarse-to-fine ideas but asymmetric (generator-only two-stage). Official code and pretrained models on project page.

## Related

- [[Pix2Pix]]
- [[Video-to-Video Synthesis]]
- [[Feature Matching]]
- [[Progressive GAN]]
