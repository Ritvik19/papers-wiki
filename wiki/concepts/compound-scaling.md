# Compound Scaling

**Type**: concept  
**Tags**: #concept

## Overview

Compound scaling (Tan & Le, 2019) jointly scales CNN **depth** (d), **width** (w), and input **resolution** (r) with a single coefficient φ: d=α^φ, w=β^φ, r=γ^φ, subject to α·β²·γ² ≈ 2. Squaring β and γ accounts for FLOPs growing quadratically with width and resolution but linearly with depth.

## Appearances

- [[Best Deep CNN Architectures and Their Principles: from AlexNet to EfficientNet]] — motivation from individual scaling saturation; grid search for α,β,γ on EfficientNet-B0; hardware-limited φ for B1–B7.

## Notes

Fix φ=1 and search α,β,γ with 2× resource budget; then fix coefficients and scale φ for larger models. Underpins the EfficientNet family. Distinct from naive "make everything bigger" scaling used in earlier eras (VGG depth-only, Inception width-only).

## Related

- [[EfficientNet]]
- [[Convolutional Neural Networks]]
