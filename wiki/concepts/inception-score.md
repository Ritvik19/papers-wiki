# Inception Score

**Type**: concept  
**Tags**: #concept

## Overview

Inception Score (IS) is an automated metric for GAN-generated image quality introduced in Salimans et al. (2016) "Improved Techniques for Training GANs." A pretrained Inception classifier assigns class probabilities to generated images; IS rewards both high confidence in a single class (sharp, recognizable images) and high entropy across the batch (diversity). Replaces purely visual inspection for model comparison.

## Appearances

- [[GANs in Computer Vision: Introduction to Generative Learning]] — introduced as part of Improved GAN evaluation toolkit alongside training stabilization tricks.

## Notes

Widely used historically but criticized for sensitivity to the classifier, insensitivity to intra-class diversity, and poor correlation with human judgment on some datasets. FID largely superseded IS for image GAN evaluation.

## Related

- [[Generative Adversarial Networks]]
- [[Feature Matching]]
- [[Evaluation and Benchmarks]]
