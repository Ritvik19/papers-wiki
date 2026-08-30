# DCGAN

**Type**: concept  
**Tags**: #concept

## Overview

Deep Convolutional Generative Adversarial Networks (DCGAN, Radford et al. 2015) are a topologically constrained convolutional GAN. Design guidelines: strided convolutions instead of pooling in the discriminator, transpose convolutions in the generator, batch normalization in both, no fully connected hidden layers, ReLU in G (tanh output in \([-1,1]\)), and LeakyReLU in D. Became the standard convolutional GAN baseline for image synthesis.

## Appearances

- [[GANs in Computer Vision: Introduction to Generative Learning]] — architecture diagram, MNIST quality improvement, CIFAR-10 results, and mode-collapse demonstration on single-class training.
- [[Papers Explained Review 05 - Generative Adversarial Networks]] — paper survey entry.

## Notes

Generator typically has more parameters than discriminator in the original work, but relative capacity is task-dependent. Still struggles with unconditional high-resolution generation without later architectural advances.

## Related

- [[Generative Adversarial Networks]]
- [[Mode Collapse]]
- [[Convolutional Neural Networks]]
