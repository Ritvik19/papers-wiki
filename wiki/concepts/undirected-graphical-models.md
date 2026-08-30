# Undirected Graphical Models

**Type**: concept  
**Tags**: #concept

## Overview

Undirected graphical models (Markov random fields) define joint distributions via an energy function over cliques; probabilities are proportional to exp(−energy). [[Restricted Boltzmann Machine]]s and [[Deep Boltzmann Machine]]s are key examples.

## Appearances

- [[Deep Learning]] — Chapter 16 and 20 treat undirected models, partition functions, and learning difficulties.

## Notes

Learning requires handling the [[Partition Function]], often via MCMC or contrastive divergence. Unlike directed models, conditional sampling can be complex.

## Related

- [[Directed Graphical Models]]
- [[Restricted Boltzmann Machine]]
- [[Partition Function]]
- [[Deep Learning]]
