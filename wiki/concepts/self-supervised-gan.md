# Self-Supervised GAN

**Type**: concept  
**Tags**: #concept

## Overview

Self-supervised GAN (Chen et al., 2019) adds an auxiliary rotation-prediction head \(Q_D\) on the discriminator alongside the real/fake head \(P_D\). D learns rotation classification on real images only; generator is trained to produce images whose D features remain rotation-discriminative. Mitigates **forgetting** in unconditional GAN training where shifting \(P_G\) causes D to lose class-discriminative representations. Collaborative training: \(\alpha\) (G rotation loss) annealed to 0, \(\beta=1\) for D.

## Appearances

- [[GANs in Computer Vision: Self-Supervised Adversarial Training and High-Resolution Image Synthesis with Style Incorporation]] — forgetting experiment, collaborative adversarial training, ImageNet 128×128 results vs conditional GAN.

## Notes

Bridges self-supervised learning (Gidaris rotation pretext) with GANs. Closes unconditional–conditional quality gap on ImageNet without labels. Uses ResNet G/D, hinge loss, batch 2048 on TPU.

## Related

- [[Generative Adversarial Networks]]
- [[BigGAN]]
- [[Unsupervised Learning]]
- [[Mode Collapse]]
