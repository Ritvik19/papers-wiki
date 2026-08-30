# Region Proposal

**Type**: concept  
**Tags**: #concept

## Overview

A **region proposal** (region of interest, RoI) is a candidate image window that might contain an object, generated **before** final classification. Proposals shrink the search space from dense sliding windows to hundreds–thousands of high-recall boxes per image.

## Appearances

- [[Object Detection for Dummies Part 1]] — [[Selective Search]] hierarchical regions.
- [[Object Detection for Dummies Part 3]] — ~2k Selective Search boxes; [[Region Proposal Network]] anchors.

## Historical progression

| Era | Method | Proposals/image | Notes |
|-----|--------|-----------------|-------|
| Classical | Sliding window + pyramid | Very many | HOG + linear SVM |
| R-CNN | [[Selective Search]] | ~2000 | CNN feature per warped RoI |
| Fast R-CNN | Selective Search | ~2000 | Shared CNN + [[RoI Pooling]] |
| Faster R-CNN | [[Region Proposal Network]] | ~300–2400 anchors | End-to-end learnable |
| One-stage | — | Dense grid/anchors | [[YOLO]], [[SSD Object Detection]] skip separate stage |

## What makes a good proposal set

- **High recall**: most objects hit by at least one box with decent [[Intersection over Union|IoU]].
- **Manageable count**: few enough for downstream classifiers.
- **Category-independent**: same proposals for all classes (R-CNN family).

## RoI in CNN detectors

After proposals exist, **region of interest** also names the feature-map patch corresponding to a box—pooled via [[RoI Pooling]] or [[RoIAlign]] into fixed-length vectors for classification and regression.

## Related

- [[Selective Search]]
- [[Region Proposal Network]]
- [[Two-Stage Object Detector]]
- [[One-Stage Object Detector]]
- [[RoI Pooling]]
- [[Object Detection for Dummies Part 1]]
- [[Object Detection for Dummies Part 3]]
