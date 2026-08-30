# SEAL Framework

**Type**: concept  
**Tags**: #concept

## Overview

The SEAL Framework ("Systematic Error Analysis for Value ALignment") is a quantitative diagnostic evaluation methodology introduced by Revel et al. (2024) to analyze how training datasets influence the behavioral alignment of Large Language Models (LLMs). By performing a systematic error analysis on human preference datasets (such as Anthropics' **HHH-RLHF**), SEAL measures how specific text features affect reward model optimization and identifies gameable vulnerabilities known as **spoiler features**.

---

## Predefined Feature Taxonomy

SEAL uses an LLM to label preference dataset samples with binary flags according to a predefined feature taxonomy. These features are categorized into two groups:
1.  **Target Features**: Core values that the model is explicitly intended to learn (e.g., `is harmless`, `is helpful`, `is refusal`, `is creative`).
2.  **Spoiler Features**: Unintended stylistic or structural shortcuts that are inadvertently learned during training (e.g., `eloquence`, `positive sentiment`, `high coherence`). Spoiler features serve as the LLM equivalent of **spurious correlations** in OOD computer vision tasks (Geirhos et al. 2020).

---

## Three Core Metrics

SEAL defines three statistics to evaluate value alignment and data effectiveness:

### 1. Feature Imprint ($\beta_\tau$)
The **Feature Imprint** estimates the expected change in predicted reward associated with the presence of a specific feature $\tau$, holding all other factors constant. It is computed via a fixed-effects linear regression of predicted rewards $r(t_i)$ against the feature matrix:
$$
r(t_i) = \alpha + \sum_{\tau} \beta_\tau \cdot x_{i,\tau} + \epsilon_i
$$
Where $x_{i,\tau} \in \{0, 1\}$ indicates the presence of feature $\tau$ in sample $i$, and $\beta_\tau$ is the estimated feature imprint.

#### Key Empirical Findings (HHH-RLHF):
*   **Harmlessness vs. Helpfulness Dynamics**: Harmlessness imprints on the reward model (RM) symmetrically through both chosen and rejected entries (both `"is harmless (chosen)"` and `"is harmless (rejected)"` have significant regression coefficients). In contrast, helpfulness imprints almost entirely through rejected entries (`"is helpful (rejected)"`), showing that RMs learn helpfulness by penalizing unhelpful outputs rather than rewarding helpful ones.
*   **Reward Shift ($\theta_i$)**: The framework also computes imprints on the reward shift angle $\theta_i$, defined as the vector angle between reward coefficients before and after alignment training, to trace how optimization refines the model's sensitivity to target values.

### 2. Alignment Resistance
**Alignment Resistance** measures the percentage of preference pairs in the dataset where the trained Reward Model (RM) fails to match the actual human annotator choice. 
*   **HHH-RLHF Baseline**: Revel et al. (2024) discovered that standard reward models exhibit an alignment resistance **exceeding $25\%$ ($1/4$)** on the HHH-RLHF dataset, highlighting a substantial structural mismatch between proxy reward models and true human values.

### 3. Alignment Robustness ($\pi^{c/r}_{+/-} (\tau)$)
**Alignment Robustness** measures the odds ratio of human preference choices flipping when inputs are synthetically perturbed or rewritten to inject or remove spoiler features $\tau$.

#### Mathematical Interpretations:
*   **Chosen-to-Rejected Flipping ($\pi^c_-(\tau)$)**: A chosen entry (denoted by $c$) that is rewritten to contain a stronger spoiler feature $\tau$ (such as becoming highly `"eloquent"` or `"sentiment positive"`) has $\exp(\pi^c_-(\tau))$ times higher odds of being rejected compared to the baseline without the feature flip.
*   **Rejected-to-Chosen Flipping ($\pi^r_+(\tau)$)**: A rejected entry (denoted by $r$) that is rewritten to obtain a weaker spoiler feature $\tau$ has $\exp(\pi^r_+(\tau))$ times higher odds of being selected as chosen compared to the baseline without the flip.

#### Significance:
According to the empirical analysis of HHH-RLHF rewrites, only robustness scores based on **sentiment spoiler features** ($\pi^c_+(\text{sentiment})$ and $\pi^r_-(\text{sentiment})$) are statistically significant, proving that reward models are highly sensitive to superficial politeness and positive phrasing, which generator models learn to exploit during reward hacking.

---

## Mitigations & Applications

*   **Targeted Pruning**: Identify and prune preference pairs with high alignment resistance to prevent the reward model from learning contradictory objectives.
*   **Spoiler Feature Neutralization**: Use synthetically rewritten data pairs to force the reward model to ignore stylistic features like sentiment and eloquence, ensuring that the reward is based strictly on target features.

## Related

*   [[Reward Hacking]]
*   [[Sycophancy]]
*   [[Evaluation and Benchmarks]]
