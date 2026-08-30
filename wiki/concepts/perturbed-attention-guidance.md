# Perturbed Attention Guidance

**Type**: concept  
**Tags**: #concept

## Overview

Perturbed Attention Guidance (PAG; Ahn et al., 2024) is a **training-free** diffusion sampling technique that replaces the CFG unconditional negative term with a **perturbed forward pass** of the same denoiser. Selected self-attention maps in the U-Net encoder are replaced with identity matrices, breaking semantic structure while preserving appearance via values \(V_t\).

## Appearances

- [[An Overview of Classifier-Free Diffusion Guidance: Impaired Model Guidance with a Bad Version of Itself (Part 2)]] — Full treatment alongside SAG and autoguidance; ablation of perturbation strategies.

## Notes

Guidance update:

$$\hat{D}_\theta(x_t) = D_\theta(x_t) + \gamma\left(D_\theta(x_t) - \widetilde{D}_\theta(x_t)\right)$$

where \(\widetilde{D}_\theta\) uses perturbed self-attention:

$$\text{PerturbedSelfAttn}(Q_t, K_t, V_t) = I \cdot V_t = V_t$$

Rationale: self-attention matrix \(A_t = \text{softmax}(QK^\top / \sqrt{d})\) encodes **structure**; values \(V_t\) encode **appearance**. Identity attention removes structural mixing.

Works on conditional and unconditional models without conditioning dropout. Limitations: manual layer/head selection; architecture-dependent; can produce OOD samples under aggressive perturbation (similar to SAG).

Related training-free alternative: **Self-Attention Guidance (SAG)** blurs high-attention input patches instead of perturbing internal attention.

## Related

- [[Autoguidance]]
- [[Classifier-Free Guidance]]
- [[Self-Attention]]
- [[An Overview of Classifier-Free Diffusion Guidance: Impaired Model Guidance with a Bad Version of Itself (Part 2)]]
