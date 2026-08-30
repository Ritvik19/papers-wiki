# Self-Contracted Curves

**Type**: concept  
**Tags**: #concept

## Overview

A self-contracted curve is a continuous curve $\gamma: [0, T) \to \mathbb{R}^n$ (or more generally in a metric space) such that the distance between any earlier point $\gamma(s)$ and a future point $\gamma(t)$ is non-increasing as $s$ advances toward $t$: for all $s_1 \le s_2 \le t$, $\mathrm{dist}(\gamma(s_2), \gamma(t)) \le \mathrm{dist}(\gamma(s_1), \gamma(t))$. Self-contracted curves arise naturally as the solution trajectories of continuous-time [[Gradient Flow on Convex Functions]] $\dot{x}(t) = -\nabla f(x(t))$.

## Mathematical Properties & Bounds

### Rectifiability
A central question in differential geometry and continuous optimization is whether self-contracted curves staying within a compact set (specifically the unit Euclidean ball $\mathcal{B}_n \subset \mathbb{R}^n$) have finite arc length (rectifiability), and how the maximum arc length $L(n)$ scales with dimension $n$.

- **Manselli & Pucci (1991)**: Proved that all continuous self-contracted curves in $\mathbb{R}^n$ staying within a bounded domain are rectifiable, providing an upper bound of $L(n) \le n^{O(n)}$.
- **Ill-Conditioned Quadratic Lower Bound**: Rescaling trajectories of gradient descent on anisotropic quadratics $\sum_{i=1}^n c_i x_i^2$ (with $c_{i+1} \gg c_i$) inside the unit hypercube yields an initial lower bound of $L(n) \ge \sqrt{n}$.
- **Exponential Bounds (Human Research)**: Research by [[Sebastien Bubeck]], Omer Angel, Tomas Merchan Rodriguez, and Fedja Nazarov established that $L(n)$ is exponential in dimension $n$:
  - Initial bounds: $\sqrt{2}^n \le L(n) \le 4^n$.
  - Refined bounds (Merchan Rodriguez & Nazarov): $2^n \le L(n) \le 2.29\dots^n$, where $2.29\dots^n$ is bounded by minimal volume intersections of self-dual cones with the sphere.
- **AI-Discovered Proofs ([[GPT-5.6]]-pro)**: In July 2026, GPT-5.6-pro one-shot proved:
  - The $2^n$ lower bound in 80 minutes of test-time compute.
  - A $2.31\dots^n$ upper bound in 88 minutes of test-time compute.
- **Conjectured Optimum**: The supremum length of self-contracted curves in the unit ball in dimension $n$ is conjectured to be exactly $2^n$.

## Appearances

- [[A Single Question to Track Progress from o3 to GPT-5.6 and Beyond]] — Serves as the central open mathematical benchmark used by [[Sebastien Bubeck]] to track frontier model reasoning capabilities from o3 to GPT-5.6.
- [[Gradient Flow on Convex Functions]] — Theoretical setting generating self-contracted trajectories.

## Notes

- The non-increasing distance property implies that the curve cannot spiral back out or oscillate wildly, which enables rectifiability proofs.
- Accelerated gradient flows (e.g. continuous limits of Nesterov accelerated gradient descent) violate the self-contraction property and can produce non-rectifiable curves of infinite length within the unit ball (Ryu, 2026).

## Related

- [[Gradient Flow on Convex Functions]]
- [[Sebastien Bubeck]]
- [[GPT-5.6]]
- [[Reasoning Models]]
- [[Ten Advances in Mathematics and Theoretical Computer Science]]
