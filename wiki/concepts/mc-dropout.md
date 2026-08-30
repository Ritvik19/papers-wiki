# MC Dropout

**Type**: concept  
**Tags**: #concept

## Overview

Monte Carlo dropout (Gal & Ghahramani, ICML 2016) estimates **epistemic uncertainty** by running multiple forward passes with dropout enabled at test time, treating the set of outputs as samples from an approximate Bayesian posterior. Dropout before every weight layer is shown equivalent to approximate deep Gaussian-process inference.

## Appearances

- [[Learning with not Enough Data Part 2: Active Learning]] — DBAL uses MC dropout for acquisition; compared to naive ensembles and Beluch et al. cheap proxies.

## Procedure

1. Enable dropout at inference (all layers)
2. Run $T$ forward passes on input $\mathbf{x}$
3. Aggregate mean/variance of predictions or vote distribution
4. Use variance / entropy of MC samples as uncertainty score

## vs Ensembles

| Approach | Cost | Calibration |
|----------|------|---------------|
| Naive ensemble | $C\times$ train | Best in Beluch et al. 2018 |
| MC dropout | $T\times$ forward | Good, economical |
| Snapshot / DEE | Intermediate | Worse than naive |

## Related

- [[Active Learning]]
- [[BALD]]
- [[Dropout]]
- [[DBAL]]
