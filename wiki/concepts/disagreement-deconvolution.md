# Disagreement Deconvolution

**Type**: concept  
**Tags**: #concept

## Overview

Disagreement Deconvolution (Gordon et al., 2021) is a descriptive label aggregation technique designed to separate valid, stable human disagreement from stochastic rater noise. When annotators label subjective or culturally sensitive items (e.g., safety, toxicity, hate speech), they often exhibit **stochastic inconsistency**—meaning a rater might assign different labels to the exact same prompt at different times due to inattention, cognitive fatigue, or interface issues. Disagreement Deconvolution models these observed annotations as a convolution of a clean, stable belief distribution with a random "label flipping" noise process, and applies deconvolution to reconstruct the clean demographic belief distribution.

## Appearances

- [[2024-02-05-human-data-quality]] — Described as a pioneering framework within the descriptive paradigm that handles individual stochastic inconsistency while preserving collective demographic perspectives.

## The Mathematical Framework

Let $x$ be a sample instance, $y \in \{1, \dots, C\}$ be an annotator's latent **stable belief** about that instance, and $\hat{y} \in \{1, \dots, C\}$ be the **observed label** produced by the annotator at a given moment.

The observed label distribution $p_{\text{obs}}(\hat{y} \mid x)$ is a mixture of the latent stable belief distribution $p^*(y \mid x)$ and the probability of random rater lapse represented by the conditional transition probability $p_{\text{flip}}(\hat{y} \mid y)$:

$$p_{\text{obs}}(\hat{y} \mid x) = \sum_{y=1}^{C} p_{\text{flip}}(\hat{y} \mid y) p^*(y \mid x)$$

In vector-matrix form, this can be written as:

$$\mathbf{p}_{\text{obs}}(x) = \mathbf{P}_{\text{flip}} \, \mathbf{p}^*(x)$$

where:
* $\mathbf{p}_{\text{obs}}(x) \in \mathbb{R}^C$ is the observed label distribution.
* $\mathbf{p}^*(x) \in \mathbb{R}^C$ is the clean, stable belief distribution we want to recover.
* $\mathbf{P}_{\text{flip}} \in \mathbb{R}^{C \times C}$ is the label transition matrix where the element at $(r, c)$ represents $P(\text{observed label } r \mid \text{stable belief } c)$.

### Deconvolution (Inversion)

If the label transition matrix $\mathbf{P}_{\text{flip}}$ is known or can be estimated, we can recover the clean belief distribution by solving the inverse problem:

$$\mathbf{p}^*(x) = \mathbf{P}_{\text{flip}}^{-1} \, \mathbf{p}_{\text{obs}}(x)$$

To ensure the deconvolved distribution is a valid probability vector (non-negative elements summing to 1), optimization methods like constrained least squares or maximum likelihood estimation under a simplex constraint are typically used instead of direct matrix inversion.

## Estimating the Flip Matrix ($P_{\text{flip}}$)

The transition matrix $\mathbf{P}_{\text{flip}}$ is estimated using a **test-retest methodology**:
1. A subset of instances is randomly selected.
2. The same annotators are presented with these identical instances at two separate time steps, separated by a time delay to prevent memory recall.
3. The frequency with which annotators switch their answers between the first and second presentations is tracked.
4. Under the assumption that the annotator's stable belief $y$ is constant over the experiment, the rate of self-disagreement directly parameterizes the noise transition probabilities in $\mathbf{P}_{\text{flip}}$.

## Preserving Diverse Perspectives

Unlike prescriptive methods (such as [[Majority Voting]] and [[MACE]]) which treat *all* disagreement as error to be removed, Disagreement Deconvolution separates:
* **Stochastic Inconsistency (Noise)**: The random error of an individual rater.
* **Stable Disagreement (Signal)**: The persistent difference in beliefs between groups of raters due to varying demographic backgrounds, values, or cultural standards.

By filtering out only the stochastic noise, the model is trained on a clean, soft probability distribution that faithfully represents real-world demographic diversity.

## Related

- [[Majority Voting]]
- [[MACE]]
- [[Jury Learning]]
- [[2024-02-05-human-data-quality]]
