# Shaoqing Ren

**Type**: person  
**Tags**: #entity

## Overview

Shaoqing Ren co-authored **Faster R-CNN** (NIPS 2015) with Kaiming He, Ross Girshick, and Jian Sun, introducing the **Region Proposal Network** that learns proposals on shared conv features with the detector.

## Appearances

- [[Object Detection for Dummies Part 3]] — RPN anchor design, alternating training, multi-task RPN loss.

## RPN contribution (summary)

- Replaces slow [[Selective Search]] with GPU-friendly conv proposals.
- Anchor parameterization (scale, aspect ratio) at each feature-map cell.
- IoU thresholds 0.7 / 0.3 for pos/neg anchor labels in Weng's account.

## Related

- [[Faster R-CNN]], [[Region Proposal Network]], [[Ross Girshick]], [[Kaiming He]]
- [[Papers Explained 16 - Faster RCNN]]
- [[Object Detection for Dummies Part 3]]
