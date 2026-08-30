# Automatic Domain Randomization

**Type**: concept  
**Tags**: #concept

## Overview

**Automatic Domain Randomization** (ADR; OpenAI et al., 2019) is an advanced curriculum learning algorithm designed to solve the **Sim-to-Real transfer** problem in robotics. Rather than hand-crafting a sequence of environments or manually tuning physics parameter ranges, ADR automatically adjusts the complexity of a simulated training distribution based on the empirical performance of the RL agent.

ADR was the core technical breakthrough that enabled OpenAI to train a physical 24-degree-of-freedom shadow robot hand to manipulate and solve a Rubik's cube. The policy was trained entirely in simulation, and because ADR forced the policy to generalize across an extremely wide and dynamically adjusting distribution of physics parameters, the resulting model transferred to the physical robot without any fine-tuning.

---

## Background: Domain Randomization vs. ADR

Traditional **Domain Randomization (DR)** trains an agent in an environment where physical properties (such as friction, gravity, mass, or visual lighting) are randomized according to a fixed distribution:

$$\theta \sim P_\phi(\theta)$$

Where $\theta$ represents physical parameters and $\phi$ defines the range (boundaries) of the uniform or Gaussian distribution. If the ranges $\phi$ are chosen too narrow, the policy will overfit to the simulation and fail on a real robot. If the ranges $\phi$ are chosen too wide, the task becomes impossible to learn from scratch, and the policy will fail to converge.

**ADR solves this by turning $\phi$ into a dynamic curriculum.** It starts with a tiny, nearly deterministic range $\phi_0$ (easy task). As the policy masters this simple environment, ADR automatically widens the range of physical parameter variations, gradually pushing the boundaries toward highly chaotic regimes. If the policy's performance degrades due to the increased difficulty, ADR shrinks the boundaries until the policy recovers.

---

## The ADR Algorithm and Mathematical Formulation

Consider a simulated environment with $D$ independent physical parameters (e.g., mass of the Rubik's cube, friction coefficient of the fingertips, joint limits of the robot fingers). 

ADR models each parameter $d \in \{1, \dots, D\}$ as a uniform distribution bounded by two dynamic limits:

$$\theta_d \sim \mathcal{U}(L_d, U_d)$$

Where $L_d$ is the lower boundary and $U_d$ is the upper boundary. The total parameter space is represented by the vector:

$$\phi = [L_1, U_1, L_2, U_2, \dots, L_D, U_D]$$

### The Evaluation and Boundary Update Loop

To decide whether to expand or contract the boundaries, ADR evaluates the policy at the extreme edges of the current randomized distribution. For a chosen parameter $d$:

1. **Sample Boundary Cases**: To test parameter $d$ at its limits, ADR sets $\theta_d = L_d$ (the lower limit) or $\theta_d = U_d$ (the upper limit), while all other $j \ne d$ parameters are sampled normally: $\theta_j \sim \mathcal{U}(L_j, U_j)$.
2. **Collect Performance Metrics**: The RL agent is evaluated on these boundary environments, producing a performance metric $D_{eval}$ (e.g., success rate or episodic length).
3. **Update Boundaries**: ADR compares $D_{eval}$ to two pre-defined performance thresholds, $C_{thr}^{high}$ and $C_{thr}^{low}$ (for example, success rates of $80\%$ and $50\%$):

- **If $D_{eval} \ge C_{thr}^{high}$ (Expansion)**: The agent has mastered this limit. Expand the boundary to make it harder:
  - If evaluating the lower bound $L_d$: $L_d \leftarrow L_d - \delta$
  - If evaluating the upper bound $U_d$: $U_d \leftarrow U_d + \delta$
- **If $D_{eval} \le C_{thr}^{low}$ (Contraction)**: The agent is struggling. Contract the boundary to make it easier:
  - If evaluating the lower bound $L_d$: $L_d \leftarrow L_d + \delta$
  - If evaluating the upper bound $U_d$: $U_d \leftarrow U_d - \delta$

Where $\delta$ is a small step-size hyperparameter.

```
          Contract                     Expand
  [---------|----------------------------|---------]  <-- Parameter Space
            L_d                          U_d
     Performance < 50%            Performance > 80%
```

---

## Detailed Algorithm Pseudocode

```python
import numpy as np

class ADRScheduler:
    def __init__(self, num_params, init_centers, init_half_widths, 
                 delta=0.05, c_low=0.5, c_high=0.8):
        self.D = num_params
        self.delta = delta
        self.c_low = c_low
        self.c_high = c_high
        
        # Initialize L and U using centers and half-widths
        self.L = np.array(init_centers) - np.array(init_half_widths)
        self.U = np.array(init_centers) + np.array(init_half_widths)
        
        # Track evaluation queues for each boundary
        self.queues = {d: {"L": [], "U": []} for d in range(self.D)}

    def sample_parameters(self):
        """Standard environment rollouts sample from the current distribution."""
        theta = np.zeros(self.D)
        for d in range(self.D):
            theta[d] = np.random.uniform(self.L[d], self.U[d])
        return theta

    def sample_boundary_env(self, boundary_d, boundary_type):
        """Evaluations are targeted at the edges to test limits."""
        theta = np.zeros(self.D)
        for d in range(self.D):
            if d == boundary_d:
                theta[d] = self.L[d] if boundary_type == "L" else self.U[d]
            else:
                theta[d] = np.random.uniform(self.L[d], self.U[d])
        return theta

    def update_boundary(self, d, boundary_type, performance):
        """Update boundaries based on targeted performance evaluation."""
        q = self.queues[d][boundary_type]
        q.append(performance)
        
        # Compute rolling average performance (e.g. over last 10 episodes)
        if len(q) >= 10:
            avg_perf = np.mean(q[-10:])
            q.clear() # Reset queue after update
            
            if avg_perf >= self.c_high:
                # Expansion
                if boundary_type == "L":
                    self.L[d] -= self.delta
                else:
                    self.U[d] += self.delta
            elif avg_perf <= self.c_low:
                # Contraction (preventing bounds from crossing)
                if boundary_type == "L":
                    self.L[d] = min(self.L[d] + self.delta, self.U[d] - 1e-4)
                else:
                    self.U[d] = max(self.U[d] - self.delta, self.L[d] + 1e-4)
```

---

## Applied Case Study: OpenAI's Rubik's Cube Hand

In the Rubik's cube setup, the policy faced extreme physical variance. ADR randomized:
- **Physics Parameters**: Gravity vector, mass of the hand joints, mass of the cube, friction coefficients of the shadow hand skin, motor dynamics, joint limits, action delays.
- **Visual Parameters**: Light sources, camera positions, image resolutions, color noise.

ADR scaled these parameters to extreme, unphysical bounds. At its peak training frontier, the policy learned to successfully manipulate the cube under:
- Simulating gravity at angles tilted up to $45^\circ$.
- Friction coefficients scaled up to $5\times$ standard levels.
- Large physical cubes (simulating massive objects) vs. tiny cubes.

Because the policy learned to coordinate hand movements under these impossible physical parameters, the standard physical world was simply a "mild, normal case" within the massive distribution it had mastered. 

---

## Comparison: Parameter-Scaling Curriculum Methods

| | ADR | ALP-GMM |
|---|---|---|
| **Distribution Shape** | Independent, uniform multidimensional hyperbox | Fully coupled, multimodal Gaussian mixtures |
| **Expansion Logic** | Edge-performance threshold evaluations | Absolute Learning Progress density estimation |
| **Exploration Mode** | Deterministic boundary expansion ($\pm \delta$) | Weighted GMM sampling + $\epsilon$-greedy |
| **Parameter Correlation**| Assumes uncorrelated dimensions | Captures correlated dimensions via covariance |
| **Best Used For** | Sim-to-Real transfer / physical parameter robustification | Path finding in continuous parameter spaces |

## Appearances

- [[Curriculum for Reinforcement Learning]] — Covered in the Task-Specific Curriculum section as a prime example of automation via environment scaling.

## Related

- [[Curriculum Learning]] — Foundational parent concept.
- [[Curriculum for Reinforcement Learning]] — Main survey page.
- [[ALP-GMM]] — Continuous task-space alternative.
- [[OpenAI]] — Developer of the ADR framework.
- [[Reinforcement Learning Topic]] — Parent topic.
