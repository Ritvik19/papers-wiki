# Mode Collapse

**Type**: concept  
**Tags**: #concept

## Overview

Mode collapse is a GAN training failure where the generator maps many latent inputs to a small set of outputs (or a single point), losing diversity over the data distribution. The discriminator then easily rejects the repeated fakes, generator gradients become unstable, and training can oscillate without recovery.

## Appearances

- [[GANs in Computer Vision: Introduction to Generative Learning]] — introductory definition; DCGAN single-class CIFAR-10 demo shows collapse into repeating square patterns; framed as a 2-player game where one side gains an irreversible advantage.
- [[GANs in Computer Vision: Conditional Image Synthesis and 3D Object Generation]] — [[PacGAN]] packed-sample discriminator; CycleGAN domain mapping also encounters collapse.
- [[GANs in Computer Vision: Improved Training with Wasserstein Distance, Game Theory Control, and Progressively Growing Schemes]] — [[Wasserstein GAN]] reduces saturation-induced collapse; Progressive GAN still exhibits competition-driven collapse at high resolution.
- [[Grokking Self-Supervised (Representation) Learning: How It Works in Computer Vision and Why]] — two SSL collapse modes (DINO): uniform outputs across feature dims, or one dominant dimension with zero entropy; mitigated by EMA teachers, predictor heads ([[BYOL]]), and BN implicit contrast.

## Notes

Can arise from generator collapse (G always emits the same sample) or from a weak discriminator stuck in a local minimum. In self-supervised representation learning, collapse means the encoder ignores input and emits constant or low-entropy features — addressed by explicit negatives (SimCLR), implicit contrast via batch statistics (BYOL), or clustering objectives (DINO). Mitigations in GAN literature include minibatch discrimination, feature matching, Wasserstein objectives, and unrolled GAN training—not covered in the part-1 survey.

## Related

- [[Generative Adversarial Networks]]
- [[DCGAN]]
- [[Wasserstein GAN]]
- [[PacGAN]]
- [[Feature Matching]]
