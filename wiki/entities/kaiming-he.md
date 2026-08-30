# Kaiming He

**Type**: person  
**Tags**: #entity

## Overview

Kaiming He is a researcher known for **ResNet** (deep residual learning), **RoIAlign**, and co-authorship of **Faster R-CNN** and **Mask R-CNN**—architectures and alignment fixes that define modern instance-level vision pipelines.

## Appearances

- [[Object Detection for Dummies Part 2]] — ResNet residual blocks (152-layer example).
- [[Object Detection for Dummies Part 3]] — Mask R-CNN, RoIAlign, COCO mask results.

## Technical highlights in Weng series

- **Residual block**: \(y = F(x) + x\) passes gradients and identity—enables very deep CNNs used as detection backbones.
- **RoIAlign**: bilinear sampling without quantizing RoI corners—mask AP gains over RoI Pooling.
- **Mask R-CNN**: decoupled mask branch per RoI, per-class masks without inter-class softmax competition.

## Related

- [[Mask R-CNN]], [[Faster R-CNN]], [[RoIAlign]], [[Convolutional Neural Networks]]
- [[Papers Explained 16 - Faster RCNN]], [[Papers Explained 17 - Mask RCNN]]
