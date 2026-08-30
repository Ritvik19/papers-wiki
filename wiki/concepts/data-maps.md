# Data Maps

**Type**: concept  
**Tags**: #concept

## Overview

Data Maps (Swayamdipta et al., EMNLP 2020) is a dataset cartography framework that evaluates dataset quality by analyzing the learning dynamics of individual training samples across epochs. By tracking a model's predicted probability for the gold standard label of each sample throughout training, the framework maps the dataset along two primary axes: **Confidence** and **Variability**. This mapping reveals three distinct categories of data—**easy-to-learn**, **ambiguous**, and **hard-to-learn**—providing system engineers with a highly interpretable diagnostic tool to find and prune mislabeled instances, locate edge cases, and select the most informative data points for training.

## Appearances

- [[2024-02-05-human-data-quality]] — Described as a major diagnostic paradigm that maps dataset cartography along Confidence and Variability axes to identify label errors and high-value edge cases.

## Mathematical Formulation

Let $D = \{(x_1, y_1^*), \dots, (x_N, y_N^*)\}$ be the training dataset where $y_i^*$ is the annotated gold-standard label. Let $\theta^{(e)}$ represent the model parameters at the end of epoch $e \in \{1, \dots, E\}$. For each training instance $i$, let $p_{\theta^{(e)}}(y_i^* \mid x_i)$ be the model's soft prediction probability for the annotated label at epoch $e$.

We compute two diagnostic metrics for each training sample:

### 1. Confidence ($\mu_i$)
The mean probability assigned by the model to the annotated label $y_i^*$ across all $E$ training epochs:

$$\hat{\mu}_i = \frac{1}{E} \sum_{e=1}^{E} p_{\theta^{(e)}}(y_i^* \mid x_i)$$

### 2. Variability ($\sigma_i$)
The standard deviation of the model's predicted probability for the annotated label $y_i^*$ across all $E$ training epochs:

$$\hat{\sigma}_i = \sqrt{\frac{1}{E} \sum_{e=1}^{E} \left( p_{\theta^{(e)}}(y_i^* \mid x_i) - \hat{\mu}_i \right)^2}$$

*(Note: Sometimes a third metric, **Correctness**, is tracked, which represents the fraction of epochs in which the model predicts the gold label correctly.)*

## Dataset Segmentation (The Cartography)

Plotting confidence on the y-axis and variability on the x-axis segments the dataset into three distinct regions:

```
▲ Confidence (High)
│
│   ┌────────────────────────────────┐
│   │                                │
│   │         Easy-to-learn          │
│   │      (Low Var, High Conf)      │
│   │                                │
│   ├────────────────────────────────┤
│   │                                │
│   │           Ambiguous            │
│   │      (High Var, Med Conf)      │
│   │                                │
│   ├────────────────────────────────┤
│   │                                │
│   │         Hard-to-learn          │
│   │       (Low Var, Low Conf)      │
│   │                                │
│   └────────────────────────────────┘
└───────────────────────────────────────► Variability (High)
```

### 1. Easy-to-learn (High Confidence, Low Variability)
* **Characteristics**: The model learns these samples very early in training and remains highly confident in their correct labels throughout.
* **Interpretation**: These are clean, prototypical, and representative training points. While necessary for basic calibration, training exclusively on them yields poor generalization because they offer little gradient signal.

### 2. Ambiguous (Moderate Confidence, High Variability)
* **Characteristics**: The model's predictions fluctuate wildly. It learns them, forgets them, and relearns them repeatedly.
* **Interpretation**: These lie directly on the decision boundary. They represent highly informative edge cases. Training on ambiguous samples is critical for driving out-of-distribution generalization and maximizing parameter optimization.

### 3. Hard-to-learn (Low Confidence, Low Variability)
* **Characteristics**: The model is consistently unable to predict the annotated label, maintaining low probability across all epochs.
* **Interpretation**: These samples typically consist of two groups:
  1. **Extreme outliers**: Physically valid but exceptionally rare edge cases.
  2. **Mislabeled samples**: Noisy annotations where the human label contradicts the surrounding data manifold. Because other clean samples act as general regularizers, the model resists memorizing these incorrect labels, resulting in consistently low confidence.

## Applications to Data Quality

Data Maps are highly effective for **noisy label pruning**. When human crowd workers make errors or spam, those instances inevitably land in the *hard-to-learn* segment. Filtering out low-confidence, low-variability samples yields immediate gains in model test performance, often outperforming models trained on the complete, unfiltered dataset.

## Related

- [[Influence Functions in DL]]
- [[Area Under the Margin]]
- [[2024-02-05-human-data-quality]]
