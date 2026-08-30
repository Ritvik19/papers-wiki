# YOLO

**Type**: concept  
**Tags**: #concept

## Overview

**YOLO** (You Only Look Once; Redmon et al., CVPR 2016) treats detection as **single-network regression**: divide the image into an \(S \times S\) grid; each cell predicts bounding boxes, **objectness**, and class probabilities in **one forward pass**—optimized for real-time speed.

## Appearances

- [[Object Detection Part 4]] — v1–v3, YOLO9000, loss and improvements.

## YOLO v1

![YOLO workflow](../assets/2018-12-27-object-recognition-part-4/fig-1.png) ![YOLO network](../assets/2018-12-27-object-recognition-part-4/fig-2.png)

| Concept | Definition |
|---------|------------|
| Responsibility | Cell whose center falls in object owns detection |
| Box params | \((x,y,w,h)\) normalized to image, offsets from cell |
| Confidence | \(\Pr(\text{object}) \times IoU(\text{pred}, \text{truth})\) |
| Classes | One \(K\)-dim conditional distribution **per cell** (shared across \(B\) boxes) |
| Output tensor | \(S \times S \times (5B + K)\) |

**Responsible predictor** (per cell): among \(B\) boxes, the one with highest IoU to GT gets box loss.

![Responsible predictor](../assets/2018-12-27-object-recognition-part-4/fig-3.png)

### Loss (v1)

\[
\mathcal{L} = \mathcal{L}_{loc} + \mathcal{L}_{cls}
\]

- \(\mathcal{L}_{loc}\): weighted SSE on coordinates (uses \(\sqrt{w},\sqrt{h}\) for size); \(\lambda_{coord}=5\).
- \(\mathcal{L}_{cls}\): SSE on confidence + class probs; \(\lambda_{noobj}=0.5\) down-weights empty-cell confidence errors.
- Indicators \(\mathbb{1}_{ij}^{obj}\), \(\mathbb{1}_i^{obj}\) gate which terms apply.

### Limits

Poor on **crowded small objects** (one cell, few boxes); fixed grid resolution.

## YOLOv2 (Redmon & Farhadi, 2017)

| Change | Detail |
|--------|--------|
| BatchNorm | All conv layers |
| Anchors | k-means on training boxes; distance \(1 - IoU(x, c_i)\) |
| Location | \(b_x=\sigma(t_x)+c_x\), \(b_w=p_w e^{t_w}\) (see figure) |
| Passthrough | Route early fine features to output (ResNet-like) |
| Multi-scale | Random input dims every 10 batches (multiple of 32) |
| Backbone | **Darknet-19** (19 conv + 5 pool) |

![YOLOv2 boxes](../assets/2018-12-27-object-recognition-part-4/fig-7.png)

## YOLO9000

Joint COCO detection + ImageNet **9000** classes; **WordTree** hierarchy—conditional probabilities along tree paths; avoids mutually exclusive softmax across unrelated fine labels.

![WordTree](../assets/2018-12-27-object-recognition-part-4/fig-8.png)

## YOLOv3

Multi-scale predictions; compared to SSD/RetinaNet on speed–mAP plot in Weng post.

## Related

- [[Joseph Redmon]], [[One-Stage Object Detector]], [[Intersection over Union]]
- [[SSD Object Detection]], [[RetinaNet]]
- [[Object Detection Part 4]]
