# One-Stage Object Detector

**Type**: concept  
**Tags**: #concept

## Overview

**One-stage detectors** predict classes and boxes on a **dense** sampling of locations (grid cells or anchors) in a **single network evaluation**, skipping a separate proposal stage. Faster inference; historically challenged by **foreground/background imbalance** until focal loss and better pyramids.

## Appearances

- [[Object Detection Part 4]] — YOLO, SSD, RetinaNet; all models in that post are one-stage.

## vs two-stage

| | One-stage | [[Two-Stage Object Detector]] |
|---|-----------|-------------------------------|
| Proposals | Implicit (dense) | Explicit sparse set |
| Pipelines | Single loss, one forward | Propose then classify |
| Speed | Often real-time (YOLO) | Faster R-CNN ~5 FPS era |
| Accuracy (2017–18) | Gap vs best two-stage | RetinaNet narrowed gap |

## Representative models (Weng series)

| Model | Mechanism | Key idea |
|-------|-----------|----------|
| [[YOLO]] | \(S\times S\) grid | Extreme speed; few boxes per cell |
| [[SSD Object Detection]] | Multi-scale anchors | VGG pyramid + default boxes |
| [[RetinaNet]] | FPN + focal loss | Handle class imbalance |

![Speed mAP tradeoff](../assets/2018-12-27-object-recognition-part-4/fig-13.png)

## Class imbalance problem

Dense sampling yields **vastly more background** than objects. Mitigations:

- [[Hard Negative Mining]] (SSD, R-CNN training)
- **Focal loss** (RetinaNet)—reweight CE by \((1-p_t)^\gamma\)
- Careful anchor matching and loss normalization

## Related

- [[YOLO]], [[SSD Object Detection]], [[RetinaNet]]
- [[Two-Stage Object Detector]], [[Mean Average Precision]]
- [[Object Detection Part 4]], [[Object Detection for Dummies Part 3]]
