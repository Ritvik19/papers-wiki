# Mixed Precision Training

**Type**: concept  
**Tags**: #concept

## Overview

Mixed Precision Training is an optimization technique that utilizes half-precision floating point (FP16 or BF16) numbers for the majority of tensor operations during model training, while maintaining specific variables in single-precision (FP32) to preserve model convergence and accuracy. By replacing standard FP32 operations with FP16, mixed precision reduces GPU memory usage by 2x, increases memory bandwidth throughput, and accelerates tensor execution (leveraging specialized cores like Tensor Cores) with negligible accuracy loss.

## Appearances

- [[How to Train Really Large Models on Many GPUs?]] — *How to Train Really Large Models on Many GPUs?* (Sep 25, 2021): Compiles mixed precision workflows, numerical stability techniques (loss scaling, master copies), and gradient histograms.

## Notes

*   **FP16 Numerical Limitations & Challenges**:
    Standard FP32 uses 32 bits (1 sign, 8 exponent, 23 mantissa) representing a vast range. In contrast, FP16 uses only 16 bits (1 sign, 5 exponent, 10 mantissa), representing a narrow dynamic range $[5.96 \times 10^{-8}, 65504]$. 
    This creates two primary hazards during deep learning training:
    -   **Gradient Underflow**: A significant fraction of gradient updates are extremely small ($< 2^{-24}$). Under FP16's minimum representable value of $2^{-14}$ (about $6 \times 10^{-5}$), these tiny gradients underflow and are truncated to absolute zero, causing the model to stop learning.
    -   **Update Swamping**: When small gradient updates are added directly to large weight parameters, the floating-point mantissa bits cannot represent the small difference, causing the gradient update to be discarded (swamped).
*   **Three Core Stabilization Techniques**:
    Narang & Micikevicius (2018) formulated three crucial techniques to stabilize training and prevent accuracy loss:
    
    ### 1. Full-Precision (FP32) Master Copy of Weights
    The optimizer maintains a master copy of the model parameters in full FP32 precision. 
    1.  During each forward pass, the FP32 master weights are rounded down to FP16.
    2.  The forward and backward passes are executed entirely using fast FP16 arithmetic.
    3.  The resulting gradients are converted to FP32 and passed to the optimizer.
    4.  The optimizer applies the gradient update directly to the FP32 master copy, ensuring that tiny updates are preserved and accumulated correctly without swamping.
    
    ### 2. Loss Scaling
    To prevent gradient underflow, the loss value is multiplied by a scale factor $S$ (e.g. 8, 16, or dynamically adjusted) right after the forward pass, before backpropagation begins.
    By applying the chain rule, this multiplies all backward gradients by $S$, effectively shifting the gradient exponent histogram to the right, safely into the representable range of FP16. 
    $$\text{Scaled Gradients} = \nabla_{\theta} (S \cdot \mathcal{L})$$
    Before the optimizer updates the FP32 master weights, the gradients are divided by $S$ (unscaled) to restore their original mathematical magnitudes, ensuring that the actual learning rate is unaltered.
    
    ### 3. High-Precision Accumulation (Arithmetic Precision)
    Certain sensitive arithmetic operations—such as vector dot-products, batch normalization reductions, and softmax operations—are executed by accumulating intermediate sums in FP32 precision, before casting the final block output back down to FP16 to be saved in memory.
*   **BFloat16 (Brain Floating Point)**:
    While FP16 requires careful loss scaling due to its narrow 5-bit exponent, newer hardware supports **BFloat16 (BF16)**. BF16 allocates 8 bits to the exponent (matching FP32) and 7 bits to the mantissa. Because its dynamic range matches FP32, BF16 eliminates the need for dynamic loss scaling altogether, greatly simplifying implementation and improving training stability.

*   **FP16 vs. BF16 Comparison**:

    | Property | FP32 | FP16 | BF16 |
    |---|---|---|---|
    | Total bits | 32 | 16 | 16 |
    | Exponent bits | 8 | 5 | 8 |
    | Mantissa bits | 23 | 10 | 7 |
    | Max value | ~3.4 × 10³⁸ | 65,504 | ~3.4 × 10³⁸ |
    | Requires loss scaling | No | Yes | No |
    | Precision | High | Medium | Low |
    | Supported hardware | All | V100+ | A100+, TPU |

*   **Dynamic Loss Scaling**:
    Static loss scaling (multiplying by a fixed constant) can cause overflows if the constant is too large, or underflow if too small. **Dynamic Loss Scaling** (Micikevicius et al. 2018) automates this:
    1. Start with a large scale factor $S$ (e.g. $S = 2^{15}$).
    2. After each backward pass, check gradients for `Inf` or `NaN`.
    3. If overflow is detected: discard the update, halve $S$, and retry.
    4. If no overflow for $T$ consecutive steps (e.g. $T = 2000$): double $S$.
    This adaptive feedback loop keeps $S$ in the optimal range throughout training without any manual tuning.

*   **Tensor Core Acceleration**:
    NVIDIA GPUs from Volta (V100) onwards include **Tensor Cores** — specialized GEMM compute units that natively execute mixed-precision matrix multiplications. In each Tensor Core cycle:
    - Inputs are loaded as FP16 (or BF16 on Ampere+).
    - The matrix product is accumulated internally in FP32.
    - The result is written back as FP16 or FP32.
    This matches precisely the Mixed Precision Training recipe: fast FP16/BF16 compute with FP32 accumulation. Tensor Cores provide 4–8× more FLOPS than standard FP32 CUDA cores on the same hardware.

*   **Memory Savings Accounting**:
    For a model with $\Psi$ parameters under full mixed precision:
    - FP16 parameters: $2\Psi$ bytes (vs. $4\Psi$ for FP32-only)
    - FP16 gradients: $2\Psi$ bytes
    - FP32 master copy: $4\Psi$ bytes
    - FP32 Adam states: $8\Psi$ bytes
    - Total: $16\Psi$ bytes (same as FP32 with Adam, but compute is faster)
    The memory reduction benefit is primarily in **activation tensors** (halved from $4\Psi$ to $2\Psi$ bytes) and **communication buffers** (gradient `AllReduce` volume halved).

    See [[How to Train Really Large Models on Many GPUs?]] fig-16 for the mixed precision training workflow, and fig-17 for the FP32 gradient exponent histogram showing underflow values.

## Related

- [[ZeRO]]
- [[Activation Recomputation]]
- [[Data Parallelism]]
- [[How to Train Really Large Models on Many GPUs?]]
