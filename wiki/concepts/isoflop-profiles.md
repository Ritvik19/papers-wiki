# IsoFLOP Profiles

**Type**: concept  
**Tags**: #concept

## Overview

IsoFLOP profiles are Chinchilla's Method 2 for estimating compute-optimal model size. Fix a FLOPs budget $C$, train models at several parameter counts $N$, and plot final loss against $N$. Each iso-FLOP curve is roughly parabolic in log-space; its minimum is the optimal $N$ for that budget. Repeating across budgets traces the compute-optimal frontier.

Hoffmann et al. (2022) used this alongside fixed-$N$ token sweeps (Method 1) and direct parametric fitting (Method 3). All three agreed on $N_\text{opt} \propto C^{0.5}$, contradicting Kaplan et al.'s $C^{0.73}$ recommendation.

## Appearances

- [[Scaling Laws, Carefully]] — diagram and explanation of Method 2 within the Kaplan/Chinchilla reconciliation narrative.
- [[Papers Explained 49 - Chinchilla]] — primary source for the three-method protocol.

## Notes

- Method 3 parametric fit was slightly off the other two methods; Besiroglu et al. (2024) traced this to optimizer and rounding issues in the original implementation.
- IsoFLOP assumes unique tokens and fixed training recipe; data repetition breaks the infinite-data assumption.

## Related

- [[Scaling Laws]]
- [[Data-Constrained Scaling Laws]]
- [[Papers Explained 49 - Chinchilla]]
