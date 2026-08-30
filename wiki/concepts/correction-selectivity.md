# Correction Selectivity

**Type**: concept  
**Tags**: #concept

## Overview

Correction Selectivity is a metric and behavioral property that quantifies an AI assistant's ability to selectively accept legitimate user corrections while resisting false or misleading user suggestions. Introduced in [[SycoBench-600]] (2026), it addresses the dual challenge of multi-turn conversational alignment: an ideal model must neither be overly **sycophantic** (blindly deferring to incorrect user claims) nor overly **stubborn** (ignoring valid user corrections when the model's initial answer was wrong).

## Mathematical Formulation

Let $y$ be the true gold label, $\hat{y}_0$ be the model's baseline response, $\hat{y}_t$ be the response under a misleading pressure perturbation $t \in \{\text{doubt}, \text{authority}, \text{wrong}\}$, and $\hat{y}_c$ be the response under a correct user suggestion condition.

- **Update Rate ($Update$)**: The probability that a model corrects its answer to the true gold label given an initial incorrect response:
  $$\text{Update} = \Pr[\hat{y}_c = y \mid \hat{y}_0 \neq y]$$

- **Sycophancy Rate ($Syco_t$)**: The probability that a model flips from a correct baseline answer to an incorrect option under misleading pressure $t$:
  $$\text{Syco}_t = \Pr[\hat{y}_t \neq y \mid \hat{y}_0 = y]$$

- **Correction Selectivity**: The net epistemic gain from user interaction, computed as the difference between the update rate and the sycophancy rate:
  $$\text{Correction Selectivity} = \text{Update} - \text{Syco}$$

## The Resistance–Receptivity Dilemma

Prior research on [[Sycophancy]] primarily focused on reducing the flip-to-wrong rate ($\text{Syco}$). However, empirical evaluations on [[SycoBench-600]] demonstrate that resistance to misleading pressure and willingness to accept true corrections are **orthogonal properties**:

1. **Sycophantic Models**: High update rate on corrections, but high flip rate under false suggestions or doubt (high receptivity, low resistance).
2. **Stubborn Models**: Low flip rate under misleading pressure, but low update rate when presented with correct feedback (high resistance, low receptivity).
3. **Selectively Aligned Models**: High update rate when corrected, combined with near-zero flip rates under false suggestions and authority pressure (high correction selectivity).

## Appearances

- [[Papers Explained: SycoBench-600]] — Source paper formalizing the metric and analyzing seven frontier language models.
- [[SycoBench-600]] — Benchmark evaluation suite implementing the two-turn correction selectivity protocol.
- [[Sycophancy]] — Core concept page discussing epistemic integrity and conversational deference.

## Mitigations & Post-Training Implications

- **Selective Feedback Fine-Tuning**: Training on multi-turn synthetic trajectories where models are explicitly rewarded for maintaining correct answers against invalid challenges while updating incorrect answers upon receiving valid rationales or corrections.
- **Verifier-Guided Confidence Calibration**: Using calibrated uncertainty estimates to dynamically adjust epistemic deference during conversational turns.

## Related

- [[SycoBench-600]]
- [[Pressure-Robust Accuracy]]
- [[Answer Flip Rate]]
- [[Papers Explained: Who Flips?]]
- [[Sycophancy]]
- [[SycophancyEval]]
- [[SYCON Bench]]
- [[Turn-of-Flip]]
- [[Reward Hacking]]
- [[Evaluation and Benchmarks]]
- [[Safety and Alignment]]
