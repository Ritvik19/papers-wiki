# Time-Contrastive Networks

**Type**: concept  
**Tags**: #concept

## Overview

Time-Contrastive Networks (TCN), introduced by Sermanet et al. (2018), represent a powerful self-supervised metric representation learning framework designed to extract viewpoint-invariant, time-cohesive, and state-centric representations from video sequences. By leveraging synchronized multi-angle video recordings of the same workspace, TCN trains a visual encoder to map identical physical states captured from different perspectives to identical latent coordinates, while pushing states from different timesteps apart. TCN is highly effective for robotic control and third-person imitation learning, where a robot must learn to perform a task by watching a human demonstrate it from an arbitrary camera angle.

```
                    TCN Synchronized Triplet Sampling
                    
  Timeline (Time t)                 Timeline (Time t + \delta)
  
  Camera A (Anchor)                 Camera A (Negative)
  +---------------+                 +---------------+
  |  Robot Arm    | <=============> |  Robot Arm    | 
  |  Grasping (t) |   (Push Apart)  |  Lifting (t+\delta)
  +---------------+                 +---------------+
         ||                                
         || (Pull Close)                   
         \/                                
  Camera B (Positive)
  +---------------+
  |  Different    |
  |  Viewpoint (t)|
  +---------------+
```

---

## Mathematical Formulation & Triplet Loss

TCN constructs a highly structured metric space using a **triplet loss** objective. For any given training step, the dataset is sampled to form a triplet of images:

1. **Anchor Image ($\mathbf{x}_t^a$)**: A video frame captured by Camera $A$ at time $t$.
2. **Positive Image ($\mathbf{x}_t^p$)**: A video frame captured by Camera $B$ at the **exact same timestep $t$**, representing the identical physical state from a different viewpoint.
3. **Negative Image ($\mathbf{x}_{t+\delta}^n$)**: A video frame captured by Camera $A$ (or any other camera) at a different timestep $t + \delta$, where the temporal difference exceeds a safety margin:
   $$ |\delta| > K_{\text{window}} $$

The visual encoder $\phi_\theta$ maps these frames into a low-dimensional metric space. The parameters $\theta$ are optimized by minimizing the **Multi-View Triplet Loss**:
$$ \mathcal{L}_{\text{triplet}}(t) = \max\left(0, \|\phi_\theta(\mathbf{x}_t^a) - \phi_\theta(\mathbf{x}_t^p)\|_2^2 - \|\phi_\theta(\mathbf{x}_t^a) - \phi_\theta(\mathbf{x}_{t+\delta}^n)\|_2^2 + M\right) $$
where $M > 0$ is a scalar margin that defines the minimum desired separation between positive and negative distances.

### Viewpoint Invariance vs. Temporal Cohesion
The loss objective enforces two critical structural constraints:
- **Viewpoint Invariance**: Minimizing $\|\phi_\theta(\mathbf{x}_t^a) - \phi_\theta(\mathbf{x}_t^p)\|_2^2$ forces the encoder to discard viewpoint-specific features like background elements, camera focal lengths, and illumination profiles, focusing entirely on features that are shared across perspectives (e.g., joint angles, object coordinates).
- **Temporal Cohesion**: Maximizing the negative distance term forces the encoder to capture the dynamic change in state over time, building a continuous manifold of the physical process.

---

## Multi-Frame Extension (mfTCN)

To capture dynamic state quantities like velocity, acceleration, and movement direction, Dwibedi et al. (2019) extended the architecture to **Multi-Frame TCN (mfTCN)**.

Instead of encoding a single frame $\mathbf{x}_t$, the input to the network is a temporal sliding stack of $S$ frames sampled at stride $d$:
$$ X_t = \left[ \mathbf{x}_t, \mathbf{x}_{t-d}, \mathbf{x}_{t-2d}, \dots, \mathbf{x}_{t-(S-1)d} \right] \in \mathbb{R}^{H \times W \times 3 \cdot S} $$

This sliding window volume is processed using:
- **3D Convolutional Neural Networks** (spatio-temporal convolutions)
- Or **2D Spatial CNNs** followed by **1D Temporal Convolutions** over the channel dimension.

The resulting dynamic embedding:
$$ z_t = \phi_{\text{dynamic}}(X_t) $$
stores velocity vectors directly inside the latent coordinate system, enabling highly stable, smooth control feedback.

---

## Third-Person Imitation Learning

A premier application of TCN is **Third-Person Imitation Learning**:
1. A human performs a task (e.g., pouring water) captured on video.
2. The human demonstration is mapped to a sequence of latent trajectories using the TCN encoder:
   $$ \mathcal{T}_{\text{human}} = \{ \phi(\mathbf{x}_1^{\text{human}}), \phi(\mathbf{x}_2^{\text{human}}), \dots \} $$
3. The robotic agent is placed in the workspace and learns a control policy $\pi$ to perform the same task by minimizing the Euclidean distance between its own latent state $\phi(\mathbf{x}_t^{\text{robot}})$ and the corresponding human state in the demonstration:
   $$ R(s_t) = - \| \phi(\mathbf{x}_t^{\text{robot}}) - \phi(\mathbf{x}_t^{\text{human}}) \|_2 $$

Because TCN representations are viewpoint and morphology invariant, the robot can directly map the human's physical state trajectories to its own control coordinates, successfully completing imitation learning without explicit translation mappings.

---

## Appearances

- [[Self-Supervised Representation Learning]] — Covers TCN and its multi-frame extension (mfTCN) as key robotic state-representation learning architectures that optimize viewpoint invariance.

## Related

- [[Representation Learning]]
- [[Self-Supervised Representation Learning]]
- [[Triplet Loss]]
- [[Contrastive Learning]]
