# Jury Learning

**Type**: concept  
**Tags**: #concept

## Overview

Jury Learning (Gordon et al., 2022) is a descriptive machine learning framework that models diverse human perspectives by predicting labels through simulated "juror" panels. Rather than aggregating conflicting opinions into a single majority label prior to training, Jury Learning trains a model to predict how *individual* annotators will label an input based on their demographic and background characteristics (e.g., age, gender, race, education, political views). At inference time, instead of outputting a generic consensus prediction, the framework allows system designers to specify a custom "jury composition" (e.g., reflecting local community demographics or safety auditor standards) and aggregates the predicted votes of those simulated jurors to produce the final model response.

## Appearances

- [[2024-02-05-human-data-quality]] — Focuses on the Deep & Cross Network (DCN) structure of Jury Learning as a primary method for preserving annotator demographic voice and diversity.

## The Model Architecture

Jury Learning decomposes the labeling task into a joint prediction problem over content features and annotator profiles. 

### 1. Inputs
* **Content Embedding ($\mathbf{v}_x$)**: The text or image content $x$ is encoded using a pre-trained model (e.g., BERT for text) to produce a feature vector:
  $$\mathbf{v}_x = \text{Encoder}(x)$$
* **Annotator Profile Embedding ($\mathbf{u}_a$)**: For an annotator $a$, categorical demographic features (e.g., age bracket, gender identity, ethnicity, geographic region) are mapped to low-dimensional learnable embedding vectors and concatenated:
  $$\mathbf{u}_a = \left[ \mathbf{e}_{\text{age}}, \mathbf{e}_{\text{gender}}, \mathbf{e}_{\text{race}}, \dots \right]$$

### 2. Deep & Cross Network (DCN)
To capture complex, non-linear interactions between demographic groups and content nuances, Jury Learning feeds these embeddings into a Deep & Cross Network (DCN). The input vector is:

$$\mathbf{x}_0 = \left[ \mathbf{v}_x \ ; \ \mathbf{u}_a \right]$$

The architecture splits into two parallel pathways:
* **The Cross Network**: Explicitly models degree-$d$ feature crossings. The update rule for layer $l+1$ is:
  $$\mathbf{x}_{l+1} = \mathbf{x}_0 \mathbf{x}_l^T \mathbf{w}_l + \mathbf{b}_l + \mathbf{x}_l$$
  where $\mathbf{w}_l$ and $\mathbf{b}_l$ are learnable weight vectors and bias vectors.
* **The Deep Network**: A standard Multi-Layer Perceptron (MLP) that extracts implicit deep hierarchical combinations:
  $$\mathbf{h}_{j+1} = \text{ReLU}(\mathbf{W}_j \mathbf{h}_j + \mathbf{b}_j)$$

The final hidden layers of both networks are concatenated and passed through a softmax classifier head to yield the predicted annotator label probability:

$$\hat{y}(x, a) = P(Y = 1 \mid x, a) = f(\mathbf{x}_L, \mathbf{h}_J)$$

## Inference & Jury Composition

At inference time, a system designer defines a **jury composition** $J$, which is a set of simulated juror profiles $\{a_1, a_2, \dots, a_K\}$. The jury composition can be selected to:
* Match the census demographics of a target population.
* Heavily represent a marginalized or vulnerable group for safety-critical tasks.
* Emulate a balanced political spectrum to evaluate toxicity or bias.

For a given content $x$ and jury $J$, the model computes predictions for each juror individually, and then aggregates their outputs (typically using majority vote or mean probability thresholding) to generate the final jury verdict $\hat{y}_J(x)$:

$$\hat{y}_J(x) = \frac{1}{K} \sum_{k=1}^{K} f(x, a_k)$$

## Key Advantages

* **Dynamic Adaptability**: The same underlying network can simulate an infinite variety of juror panels at inference time without requiring retraining.
* **Calibrated Uncertainty**: Because the model aggregates votes over a large, diverse panel, the variance in votes provides a direct, highly calibrated measure of semantic ambiguity and community disagreement.
* **Demographic Representation**: Ensures minority populations have a structured, mathematical voice in model decisions, preventing their beliefs from being drowned out by a dominant majority.

## Related

- [[Majority Voting]]
- [[MACE]]
- [[Disagreement Deconvolution]]
- [[2024-02-05-human-data-quality]]
