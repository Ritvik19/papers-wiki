# Asynchronous Advantage Actor-Critic

**Type**: concept  
**Tags**: #concept

## Overview

Asynchronous Advantage Actor-Critic (A3C) is a DeepMind (2016) parallel RL algorithm: multiple independent agent networks explore copies of the environment and **asynchronously** push gradient updates to a shared global network, periodically resetting local weights from the global model. It extends advantage actor-critic with parallel exploration for faster wall-clock learning on standard RL benchmarks.

## Appearances

- [[The Idea behind Actor-Critics and How A2C and A3C Improve Them]] — AI Summer: parallel workers, global network, asynchronous vs synchronous A2C tradeoffs.

## Notes

At release, A3C was influential for combining deep networks with stable policy-gradient training; synchronous [[Advantage Actor-Critic]] with vectorized environments is often preferred in modern implementations.

## Related

- [[Advantage Actor-Critic]]
- [[Actor-Critic Methods]]
- [[DeepMind]]
- [[Policy Gradient]]
