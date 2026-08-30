# Probabilistic Pivot Tournament

**Type**: concept  
**Tags**: #concept

## Overview
A budget-efficient tournament algorithm (PPT) that evaluates $N$ candidate trajectories against a small set of $k$ empirical leader pivots selected via a random Hamiltonian cycle (ring pass), reducing verification complexity from $\mathcal{O}(N^2)$ to $\mathcal{O}(Nk)$.

## Appearances
- [[Papers Explained 588: LLM-as-a-Verifier]] — introduced for efficient candidate trajectory ranking.

## Notes
- Allocates comparative verification queries specifically to distinguish among top-tier candidate solutions.

## Related
- [[LLM-as-a-Verifier]]
- [[Evaluation and Benchmarks]]
