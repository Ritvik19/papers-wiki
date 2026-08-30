# MACE

**Type**: concept  
**Tags**: #concept

## Overview

MACE (Multi-Annotator Competence Estimation) is a generative probabilistic graphical model proposed by Hovy et al. (2013) to address the challenges of crowdsourcing quality control. Unlike standard majority voting, which treats all annotators equally, MACE models each annotator's latent competence and private spamming behavior. By using the Expectation-Maximization (EM) or Variational Bayes (VB) algorithm, MACE simultaneously predicts the true latent labels of training instances and identifies which raters are untrustworthy spammers, downweighting their future influence.

## Appearances

- [[2024-02-05-human-data-quality]] — Highlighted as a sophisticated prescriptive paradigm model that leverages graphical models to filter out low-effort spam.

## The Generative Process

MACE models label generation as a generative trial. For each instance $i \in \{1, \dots, N\}$ with a latent true label $T_i$ drawn from a class prior $\pi$, and for each annotator $j \in \{1, \dots, M\}$ who labels instance $i$:

1. **Spamming Decision**: The annotator decides whether to act competently or to spam. This is modeled by a latent binary variable $S_{ij} \sim \text{Bernoulli}(\theta_j)$, where $\theta_j \in [0, 1]$ represents the competence/trustworthiness of annotator $j$.
2. **Label Generation**:
   * **If $S_{ij} = 1$ (Competent)**: The annotator observes the true label and outputs it correctly:
     $$y_i^j = T_i$$
   * **If $S_{ij} = 0$ (Spamming)**: The annotator ignores the true instance context and randomly draws a label from their private spamming multinomial distribution:
     $$y_i^j \sim \text{Multinomial}(\vec{\omega}_j)$$
     where $\vec{\omega}_j = \{\omega_{j1}, \dots, \omega_{jC}\}$ is the spam label preference vector of annotator $j$, summing to 1.

The joint probability of the latent variables and observed labels under this generative structure is:

$$P(T_i = c, S_{i1}, \dots, S_{iM}, y_i^1, \dots, y_i^M) = \pi_c \prod_{j=1}^{M} \left[ \theta_j \mathbb{I}(y_i^j = c) \right]^{S_{ij}} \left[ (1 - \theta_j) \omega_{j, y_i^j} \right]^{1 - S_{ij}}$$

## Expectation-Maximization (EM) Optimization

Because the true labels $T_i$ and the spamming indicators $S_{ij}$ are latent variables, MACE optimizes its parameters $\Theta = \{\theta_1, \dots, \theta_M\}$ and $\Omega = \{\vec{\omega}_1, \dots, \vec{\omega}_M\}$ using the Expectation-Maximization algorithm to maximize the marginal log-likelihood of the observed annotations $Y$:

### E-step (Expectation)
Compute the posterior distributions of the latent variables given the current parameter estimates $\Theta^{(t)}$ and $\Omega^{(t)}$:

$$q_i(c) = P(T_i = c \mid Y_i; \Theta^{(t)}, \Omega^{(t)}) \propto \pi_c \prod_{j=1}^{M} \left[ \theta_j^{(t)} \mathbb{I}(y_i^j = c) + (1 - \theta_j^{(t)}) \omega_{j, y_i^j}^{(t)} \right]$$

### M-step (Maximization)
Update the competence parameter $\theta_j$ and spamming preference $\omega_{jc}$ to maximize the expected complete log-likelihood:

$$\theta_j^{(t+1)} = \frac{\sum_{i=1}^{N} \sum_{c=1}^{C} q_i(c) P(S_{ij} = 1 \mid T_i = c, y_i^j; \Theta^{(t)}, \Omega^{(t)})}{N}$$

$$\omega_{jc}^{(t+1)} \propto \sum_{i=1}^{N} \mathbb{I}(y_i^j = c) \sum_{c'=1}^C q_i(c') P(S_{ij} = 0 \mid T_i = c', y_i^j; \Theta^{(t)}, \Omega^{(t)})$$

## Strengths & Weaknesses

* **Pros**: Exceptionally effective at identifying "uniform spammers" (who click rapidly to maximize monetary payout) and "biased spammers" (who always select a specific choice like class 1).
* **Cons**: Assumes spamming behavior is independent across raters and items. It cannot detect complex, coordinated click-farms or systematic bias where multiple annotators share the same incorrect beliefs.

## Related

- [[Majority Voting]]
- [[Disagreement Deconvolution]]
- [[Jury Learning]]
- [[2024-02-05-human-data-quality]]
