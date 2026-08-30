# CycleGAN

**Type**: concept  
**Tags**: #concept

## Overview

CycleGAN (Zhu et al. 2017) performs **unpaired** image-to-image translation between domains X and Y using two generators \(G: X \to Y\) and \(F: Y \to X\) plus two discriminators. Cycle-consistency loss enforces \(F(G(x)) \approx x\) and \(G(F(y)) \approx y\), constraining mappings without paired supervision. Optional identity loss preserves color when domains share structure.

## Appearances

- [[GANs in Computer Vision: Conditional Image Synthesis and 3D Object Generation]] — cycle consistency derivation, training pseudocode, results vs Pix2Pix, failure modes (geometric changes, global vs local structure).
- [[Papers Explained Review 05 - Generative Adversarial Networks]] — paper survey entry.

## Notes

Four networks trained jointly (2 G + 2 D). Generally blurrier than paired Pix2Pix but enables translation from unpaired collections (e.g. horses↔zebras, photos↔paintings). Struggles when large geometric deformations are required.

## Related

- [[Pix2Pix]]
- [[Generative Adversarial Networks]]
- [[Mode Collapse]]
