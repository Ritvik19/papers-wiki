# Mean Average Precision

**Type**: concept  
**Tags**: #concept

## Overview

**Mean average precision (mAP)** is the standard object-detection metric: for each class, compute **average precision (AP)** as the area under the precision–recall curve, then average AP across classes. Reported on a 0–100 scale in PASCAL VOC tradition; higher is better.

## Appearances

- [[Object Detection for Dummies Part 2]] — PR curve construction, mAP@0.5.
- [[Object Detection Part 4]] — speed vs mAP comparisons (YOLO, SSD, RetinaNet).

## Computation pipeline

1. Run detector on all test images; collect scored bounding boxes per class.
2. Match predictions to ground truth by [[Intersection over Union|IoU]] threshold (e.g. **0.5** → **mAP@0.5**).
3. Sort predictions by confidence; sweep threshold to trace **precision–recall**.
4. **AP** = area under PR curve for that class (or interpolated AP per VOC protocol).
5. **mAP** = mean of AP over all object classes.

## True positive rule

A detection is a TP if IoU with some unmatched ground-truth box of the same class exceeds the threshold. Multiple detections on one object: typically only highest-scoring match counts; others are false positives unless suppressed by [[Non-Maximum Suppression]].

## Why mAP not accuracy

Detection outputs variable numbers of boxes per image; class imbalance and IoU matching require ranking-based metrics, not single-threshold accuracy.

## COCO extensions

Modern benchmarks often report mAP@[0.5:0.95] (average over IoU 0.5 to 0.95 step 0.05) for stricter localization—Weng's 2017 post focuses on single-threshold mAP@0.5.

## Related

- [[Intersection over Union]]
- [[Non-Maximum Suppression]]
- [[Object Detection for Dummies Part 2]]
- [[Evaluation and Benchmarks]]
