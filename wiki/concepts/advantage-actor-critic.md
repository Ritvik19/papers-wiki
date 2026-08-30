# Advantage Actor-Critic

**Type**: concept  
**Tags**: #concept

## Overview

Advantage Actor-Critic (A2C) is an [[Actor-Critic Methods|actor-critic]] variant where the critic learns the **advantage function** A(s,a) = Q(s,a) − V(s) rather than raw Q-values. Advantages measure how much better an action is than the state baseline, reducing policy-gradient variance. Synchronous A2C runs parallel environment copies with a rollout (step) network and training network that sync after each batch of experience.

## Appearances

- [[The Idea behind Actor-Critics and How A2C and A3C Improve Them]] — AI Summer: advantage decomposition, variance reduction, parallel-env step/train model pattern.

## Notes

Often contrasted with [[Asynchronous Advantage Actor-Critic]] (A3C), which updates a global network asynchronously from independent workers.

## Related

- [[Actor-Critic Methods]]
- [[Asynchronous Advantage Actor-Critic]]
- [[Policy Gradient]]
- [[Temporal-Difference Learning]]
