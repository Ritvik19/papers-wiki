# Smooth L1 Loss

**Type**: concept  
**Tags**: #concept

## Overview

**Smooth L1 loss** (Huber-style) is used for [[Bounding Box Regression]] in Fast/Faster R-CNN: quadratic near zero, linear for large errors—less sensitive to outliers than pure L2.

## Appearances

- [[Object Detection for Dummies Part 3]] — Fast R-CNN \(\mathcal{L}_{box}\); RPN box term.

## Definition

\[
L_1^{smooth}(x) = \begin{cases} 0.5 x^2 & |x| < 1 \\ |x| - 0.5 & \text{otherwise} \end{cases}
\]

![Smooth L1 curve](../assets/2017-12-31-object-recognition-part-3/fig-6.webp)

## Behavior

| \(|x|\) region | Effect |
|---------------|--------|
| Small errors | L2-like, smooth gradients |
| Large errors | L1-like, capped influence of outliers |

Mis-matched proposals or noisy box annotations produce large \(t^u - v\); smooth L1 prevents single examples from dominating.

## In multi-task loss

Fast R-CNN: \(\mathcal{L}_{box} = \sum_{i \in \{x,y,w,h\}} L_1^{smooth}(t^u_i - v_i)\) only when \(u \geq 1\) (not background).

Faster R-CNN RPN: \(\sum_i p_i^* L_1^{smooth}(t_i - t_i^*)\) on positive anchors, normalized by \(N_{box}\).

## Related

- [[Bounding Box Regression]], [[Fast R-CNN]], [[Faster R-CNN]]
- [[Object Detection for Dummies Part 3]]
