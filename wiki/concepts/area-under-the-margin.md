# Area Under the Margin

**Type**: concept  
**Tags**: #concept

## Overview

Area Under the Margin (AUM) is a highly scalable, robust diagnostic method proposed by Pleiss et al. (NeurIPS 2020) to identify and prune mislabeled data in deep neural network training sets. AUM leverages the fundamental gradient tension in Stochastic Gradient Descent (SGD) between global model generalization (clean data regularizing the network) and local label memorization (fitting noisy data). By tracking the margin between the logit of the annotated class and the largest logit among all other classes across epochs, AUM separates clean samples from noisy annotations. AUM is particularly notable for having virtually zero computational overhead during standard training, making it highly suitable for large-scale industrial datasets.

## Appearances

- [[2024-02-05-human-data-quality]] — Highlighted as a state-of-the-art training dynamic metric that separates flipped annotations from clean data using logit margins and fake threshold samples.

## Mathematical Formulation

Let $z_i = (x_i, y_i^*)$ be a training instance where $y_i^*$ is the annotated class label. Let $f_c(x_i; \theta^{(e)}) \in \mathbb{R}$ denote the model's logit output (before the softmax activation) for class $c \in \{1, \dots, C\}$ at the end of epoch $e \in \{1, \dots, E\}$.

### 1. The Logit Margin
The margin $M^{(e)}(x_i, y_i^*)$ at epoch $e$ is defined as the difference between the logit of the annotated class $y_i^*$ and the largest logit among all other classes:

$$M^{(e)}(x_i, y_i^*) = f_{y_i^*}(x_i; \theta^{(e)}) - \max_{c \neq y_i^*} f_c(x_i; \theta^{(e)})$$

* **Correctly Labeled Sample**: The model easily predicts the annotated label, so $f_{y_i^*}(x_i)$ is large and positive, while other class logits are small or negative. This results in a large **positive** margin.
* **Mislabeled Sample**: Generalization from surrounding clean data causes the model to predict the true, unannotated class. Thus, the logit of the unannotated true class becomes much larger than the logit of the annotated noisy class $y_i^*$. This results in a highly **negative** margin.

### 2. Area Under the Margin (AUM)
The AUM for a training sample is the average logit margin calculated across all training epochs:

$$\text{AUM}(x_i, y_i^*) = \frac{1}{E} \sum_{e=1}^{E} M^{(e)}(x_i, y_i^*)$$

Samples are then ranked in ascending order of their AUM. Points with lowest AUM are flagged as the most likely mislabeled candidates.

## Fake Threshold Samples (Thresholding)

To determine the exact boundary for pruning without throwing away clean but highly difficult edge cases, Pleiss et al. introduce a calibration technique using **threshold samples**:

1. **Injection**: Before training begins, a small fraction (e.g., 1%) of the training dataset is selected, and their labels are deliberately flipped to a random incorrect class. These act as known, guaranteed noisy reference points.
2. **Dynamic Tracking**: The AUM of these known flipped "threshold samples" is tracked throughout standard training along with the rest of the data.
3. **Threshold Calculation**: After training, a pruning threshold $\tau$ is set based on the AUM distribution of the threshold samples (for example, the 99th percentile of their AUM values):
   $$\tau = \text{Percentile}\left(\{ \text{AUM}(z_{\text{threshold}}) \}, 99\right)$$
4. **Pruning**: Any regular training instance with an AUM below the threshold $\tau$ is classified as mislabeled and pruned from the dataset:
   $$\text{Prune } z_i \iff \text{AUM}(x_i, y_i^*) < \tau$$

## Scalability and Benefits

* **No Overhead**: Unlike [[Influence Functions in DL]] which require complex inverse Hessian estimations ($\mathcal{H}^{-1}$), AUM is calculated simply by caching the output logit vectors of size $C$ for each training sample at the end of each epoch. This has $O(1)$ extra compute.
* **Generalization Preservation**: By using calibrated threshold samples, AUM prevents the accidental pruning of highly difficult but clean boundary examples, which are highly valuable for the model's final capacity.

## Related

- [[Influence Functions in DL]]
- [[Data Maps]]
- [[2024-02-05-human-data-quality]]
