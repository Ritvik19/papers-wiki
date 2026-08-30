# Hard Negative Mining

**Type**: concept  
**Tags**: #concept

## Overview

**Hard negative mining** augments training with **difficult background** regions—patches that look like objects but are not (texture, partial objects, clutter)—so classifiers learn sharper decision boundaries. Easy negatives (blank sky) contribute little gradient.

## Appearances

- [[Object Detection for Dummies Part 3]] — R-CNN training loops; false positives re-injected.
- [[Object Detection Part 4]] — SSD keeps top false positives; neg:pos ≤ 3:1.

## Easy vs hard negatives

| Type | Example | Gradient signal |
|------|---------|-----------------|
| Easy negative | Uniform background | Weak |
| Hard negative | Tree bark, car interior through window | Strong; often misclassified |

## R-CNN procedure (conceptual)

1. Train initial classifier on positives + random negatives.
2. Run detector on training images; collect **false positives** (high-score background RoIs).
3. Add hardest FPs to negative set; retrain.
4. Repeat.

Related to [[Hard Negative Mining]] in SVM literature; complements [[Non-Maximum Suppression]] at test time (NMS removes duplicates, mining improves training).

## Modern analogue

[[RetinaNet]] **focal loss** down-weights easy negatives automatically—reduces need for explicit mining in many pipelines. SSD still uses explicit hard negative mining per Weng.

## Related

- [[R-CNN]], [[Fast R-CNN]], [[SSD Object Detection]]
- [[Papers Explained 22 - Focal Loss for Dense Object Detection (RetinaNet)]]
- [[Object Detection for Dummies Part 3]], [[Object Detection Part 4]]
