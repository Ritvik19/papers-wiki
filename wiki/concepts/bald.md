# BALD

**Type**: concept  
**Tags**: #concept

## Overview

Bayesian Active Learning by Disagreement (BALD; Houlsby et al., 2011) acquires samples maximizing **information gain about model parameters** $\boldsymbol{\theta}$. Equivalently: maximize decrease in expected posterior entropy. Intuition — pick $\mathbf{x}$ where the model is marginally uncertain but individual posterior weight draws are confident (committee disagreement).

## Appearances

- [[Learning with not Enough Data Part 2: Active Learning]] — Original formulation; BatchBALD (Kirsch et al. 2019) for batch mode; compared to MAL on ImageNet.

## Information gain form

$$I[\boldsymbol{\theta}, y | x, \mathcal{D}] = H(y|x,\mathcal{D}) - \mathbb{E}_{\boldsymbol{\theta} \sim p(\boldsymbol{\theta}|\mathcal{D})}[H(y|x,\boldsymbol{\theta})]$$

High $H(y|x,\mathcal{D})$ and low per-draw $H(y|x,\boldsymbol{\theta})$ → high BALD score.

## Worked example: binary committee (toy)

Unlabeled point $\mathbf{x}$; binary labels $\{0,1\}$; committee of $C=3$ models (e.g. MC dropout draws or ensemble members).

| Model $c$ | $P_{\theta_c}(y{=}0|\mathbf{x})$ | $P_{\theta_c}(y{=}1|\mathbf{x})$ | Hard vote |
|-----------|----------------------------------|----------------------------------|-----------|
| 1 | 0.90 | 0.10 | 0 |
| 2 | 0.15 | 0.85 | 1 |
| 3 | 0.88 | 0.12 | 0 |

**Marginal** (committee average): $\bar{p}_0 = (0.90+0.15+0.88)/3 = 0.643$, $\bar{p}_1 = 0.357$.

$$H(y|\mathbf{x},\mathcal{D}) = -0.643\log 0.643 - 0.357\log 0.357 \approx 0.63 \text{ nats}$$

**Per-draw entropies** (each model confident):

| Model | $H(y|\mathbf{x},\theta_c)$ |
|-------|---------------------------|
| 1 | $\approx 0.33$ |
| 2 | $\approx 0.33$ |
| 3 | $\approx 0.33$ |

$$\mathbb{E}_{\theta}[H(y|\mathbf{x},\theta)] \approx 0.33$$

**BALD** $\approx 0.63 - 0.33 = 0.30$ — **high** (acquire this point).

**Contrast — unanimous committee**:

| Model | $P(y{=}0)$ | Vote |
|-------|------------|------|
| 1,2,3 | 0.92, 0.88, 0.95 | all 0 |

$\bar{p}_0 \approx 0.92$ → $H(y|\mathbf{x},\mathcal{D}) \approx 0.28$; per-draw $\approx 0.28$ each → BALD $\approx 0$ — **low** (skip; everyone agrees and is confident).

**Interpretation**: BALD peaks when the *pool* is unsure (marginal entropy high) but *individual* hypotheses are sharp (committee members disagree confidently) — classic "borderline" acquisition target.

Approximation with [[MC Dropout]]: replace the 3 rows with $T=10$ dropout forward passes; compute voter entropy or BALD from sample mean vs per-pass entropies.

## Related

- [[Active Learning]]
- [[MC Dropout]]
- [[BADGE]]
- [[Bayesian Statistics]]
