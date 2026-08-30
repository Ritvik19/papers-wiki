# Intersection over Union

**Type**: concept  
**Tags**: #concept

## Overview

**Intersection over union (IoU)**, also **Jaccard index** for boxes, measures overlap between two axis-aligned rectangles: area of intersection divided by area of union. It gates true positives in [[Mean Average Precision|mAP]], training labels for anchors, and [[Non-Maximum Suppression]].

## Appearances

- [[Object Detection for Dummies Part 2]] — mAP@0.5 matching.
- [[Object Detection for Dummies Part 3]] — R-CNN SVM positives IoU ≥ **0.3**; bbox regressor pairs ≥ **0.6**; NMS suppresses IoU > **0.5**; Faster R-CNN RPN positives > **0.7**, negatives < **0.3**.
- [[Object Detection Part 4]] — YOLO confidence × IoU; SSD matching; YOLOv2 k-means with \(1 - \text{IoU}\) distance.

## Definition

\[
IoU(B_1, B_2) = \frac{|B_1 \cap B_2|}{|B_1 \cup B_2|} \in [0, 1]
\]

0 = no overlap; 1 = identical boxes.

## Threshold usage in the Weng series

| Stage | Typical threshold | Source note |
|-------|-------------------|-------------|
| R-CNN SVM positive | ≥ 0.3 | Weng blog (paper may use 0.5 in places) |
| R-CNN bbox regression train | ≥ 0.6 | Needs nearby GT for meaningful offsets |
| NMS duplicate removal | > 0.5 overlap with kept box | Suppress lower-score boxes |
| Faster R-CNN RPN positive | > 0.7 | High-quality anchors |
| Faster R-CNN RPN negative | < 0.3 | Clear background |
| mAP TP | > 0.5 (mAP@0.5) | Evaluation |

When comparing to [[Papers Explained 14 - RCNN]], check which IoU cutoffs the implementation uses.

## YOLO confidence

YOLO objectness: \(\text{Pr(object)} \times IoU(\text{pred}, \text{truth})\) for responsible cell/box.

## Related

- [[Mean Average Precision]]
- [[Bounding Box Regression]]
- [[Non-Maximum Suppression]]
- [[Region Proposal Network]]
- [[Object Detection for Dummies Part 2]]
- [[Object Detection for Dummies Part 3]]
