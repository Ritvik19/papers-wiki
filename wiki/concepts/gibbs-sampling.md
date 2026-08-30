# Gibbs Sampling

**Type**: concept  
**Tags**: #concept

## Overview

Gibbs sampling is an MCMC method that samples each variable from its conditional distribution given all others, cycling through coordinates. It is tractable when conditionals are easy to sample.

## Appearances

- [[Deep Learning]] — Section 17.4; Figure 17.1 illustrates mixing behavior; used in training [[Restricted Boltzmann Machine]]s.

## Notes

Slow mixing between separated modes is a practical limitation. Deep learning training rarely uses Gibbs at scale today but it underpins historical energy-based learning.

## Related

- [[Markov Chain Monte Carlo]]
- [[Restricted Boltzmann Machine]]
- [[Deep Learning]]
