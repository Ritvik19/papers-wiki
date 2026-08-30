# Gradient Flow on Convex Functions

**Type**: concept  
**Tags**: #concept

## Overview

Gradient flow on a convex function is the continuous-time dynamical system defined by the differential equation $\dot{x}(t) = -\nabla f(x(t))$ (or $\dot{x}(t) \in -\partial f(x(t))$ for non-smooth convex functions), where $f: \mathbb{R}^n \to \mathbb{R}$ is a convex potential. It represents the continuous-time analogue of gradient descent and serves as a fundamental foundation for continuous optimization theory, differential inclusions, and Wasserstein metric spaces.

## Key Theoretical Properties

### Monotonicity and Self-Contraction
Because $f$ is convex, the subdifferential operator is monotone: $\langle \nabla f(x) - \nabla f(y), x - y \rangle \ge 0$. As a consequence, solution trajectories $x(t)$ are [[Self-Contracted Curves]]: the Euclidean distance $\|x(s) - x(t)\|$ is monotonically non-increasing for $s \le t$.

### Path Length and Rectifiability
While the convergence rate of gradient descent in function value ($f(x(t)) - f^* = O(1/t)$) is dimension-free, the *arc length* of the continuous trajectory under a spatial constraint (remaining within the unit Euclidean ball $\mathcal{B}_n$) exhibits strong dimensional dependence:
- Manselli & Pucci (1991) proved all such flows have finite arc length (rectifiable), bounded above by $n^{O(n)}$.
- [[Sebastien Bubeck]] and collaborators proved the true supremum arc length is exponential in dimension ($2^n \le L(n) \le 2.29\dots^n$).
- In July 2026, [[GPT-5.6]]-pro established a $2.31\dots^n$ upper bound and the $2^n$ lower bound autonomously via long-horizon test-time compute.

### Contrast with Accelerated Dynamics
Unlike standard gradient flow, second-order or momentum-accelerated dynamics (such as continuous limits of Nesterov's accelerated gradient descent, $\ddot{x}(t) + \frac{3}{t}\dot{x}(t) + \nabla f(x(t)) = 0$) do not generate self-contracted curves. Such trajectories can oscillate with increasing frequency, leading to infinite path length (non-rectifiable curves) even on smooth convex potentials within the unit ball (Ryu, 2026).

## Appearances

- [[A Single Question to Track Progress from o3 to GPT-5.6 and Beyond]] — Primary context exploring trajectory arc lengths of convex gradient flows in unit balls.
- [[Self-Contracted Curves]] — Geometric characterization of convex gradient flow solution paths.

## Related

- [[Self-Contracted Curves]]
- [[Sebastien Bubeck]]
- [[GPT-5.6]]
- [[Gradient Descent]]
- [[Reasoning Models]]
