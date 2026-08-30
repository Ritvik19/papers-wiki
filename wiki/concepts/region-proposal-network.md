# Region Proposal Network

**Type**: concept  
**Tags**: #concept

## Overview

The **Region Proposal Network (RPN)** in [[Faster R-CNN]] is a fully convolutional head that predicts **objectness** and **box deltas** for **anchors** at each feature-map location, replacing external [[Selective Search]] with proposals learned end-to-end from the same features as the detector.

## Appearances

- [[Object Detection for Dummies Part 3]] — anchor grid, loss, alternating training.

## Anchors

At each sliding position (e.g. center of 3×3 conv window):

- **k** combinations of **scale** × **aspect ratio** (e.g. 3×3 = 9 anchors).
- Each anchor: reference box on the image (via stride and receptive field).

Labels by [[Intersection over Union|IoU]] with GT:

| Label | IoU (Weng) |
|-------|------------|
| Positive | > 0.7 |
| Negative | < 0.3 |
| Ignore | between (optional in implementations) |

## Outputs per anchor

- **\(p_i\)**: objectness probability (binary cls in practice).
- **\(t_i\)**: 4 parameterized offsets vs anchor (same family as [[Bounding Box Regression]]).

## Loss

See [[Faster R-CNN]]: balanced cls + \(\lambda\)-weighted [[Smooth L1 Loss]] on positives.

## Shared features

RPN and Fast R-CNN heads sit on **one conv trunk**—proposals adapt to dataset statistics (object sizes, aspect ratios) without hand-tuned selective search configs.

## Related

- [[Faster R-CNN]], [[Region Proposal]], [[Bounding Box Regression]]
- [[Shaoqing Ren]], [[Papers Explained 16 - Faster RCNN]]
- [[Object Detection for Dummies Part 3]]
