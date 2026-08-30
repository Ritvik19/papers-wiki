# Video-to-Video Synthesis

**Type**: concept  
**Tags**: #concept

## Overview

Video-to-video synthesis (vid2vid, Wang et al., 2018) generates temporally coherent high-resolution video from segmentation sequences. Generator \(F\) conditions on two past frames and segmentations (Markov assumption), blending FlowNet2 optical-flow-warped pixels with hallucinated occluded regions via Mask R-CNN soft masks. Dual discriminators: image PatchGAN \(D_I\) and flow-conditioned video PatchGAN \(D_V\) on \(k\)-frame patches. Uses Pix2PixHD-style architecture, multi-scale feature matching, and VGG perceptual loss.

## Appearances

- [[GANs in Computer Vision: 2K Image and Video Synthesis, and Large-Scale Class-Conditional Image Generation]] — generator decomposition, foreground/background prior, instance feature embeddings for multimodal synthesis.

## Notes

Per-frame [[Pix2PixHD]] lacks temporal consistency; vid2vid explicitly models spatio-temporal structure. Official NVIDIA repository. Builds on instance embedding scheme from Pix2PixHD.

## Related

- [[Pix2PixHD]]
- [[Pix2Pix]]
- [[Generative Adversarial Networks]]
- [[Computer Vision]]
