# Majority Voting

**Type**: concept  
**Tags**: #concept

## Overview

Majority voting is the most common consensus-based aggregation method in crowdsourcing, where the final ground truth label for an instance is determined by the class that receives the highest frequency of votes from the annotator pool. While simple to implement and theoretically robust under the assumption of independent, identically distributed annotator errors, it treats all raters as equally competent, failing to filter spammers, handle subjective disagreement, or preserve valid dissenting perspectives.

## Appearances

- [[2024-02-05-human-data-quality]] — The baseline prescriptive paradigm aggregation method compared against modern probabilistic and demographic modeling frameworks.

## Mathematical Formulation

Let $y_i^j \in \{1, \dots, C\}$ represent the label assigned by annotator $j$ to sample $i$. For an instance $i$ annotated by a pool of $M$ raters, the majority voting consensus label $\hat{y}_i$ is defined as:

$$\hat{y}_i = \arg\max_{c \in \{1, \dots, C\}} \sum_{j=1}^{M} \mathbb{I}(y_i^j = c)$$

where $\mathbb{I}(\cdot)$ is the indicator function:

$$\mathbb{I}(y_i^j = c) = \begin{cases} 1 & \text{if } y_i^j = c \\ 0 & \text{otherwise} \end{cases}$$

In the event of a tie, the label is either resolved randomly, marked as ambiguous, or audited by an expert reviewer.

## Structural Limitations

* **Expertise Ignorance**: It assigns identical weight to a highly trained domain expert and a fast, low-effort spammer.
* **Prescriptive Bias**: It assumes there is a single absolute ground truth. On subjective or culturally loaded tasks (like toxicity or humor), minority opinions reflect valid demographic consensus rather than random label noise.
* **Information Loss**: Discarding the vote distribution washes out the model's capacity to learn soft labels or express uncertainty.

## Related

- [[MACE]]
- [[Disagreement Deconvolution]]
- [[Jury Learning]]
- [[2024-02-05-human-data-quality]]
