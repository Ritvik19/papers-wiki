# Backpropagation Through Time

**Type**: concept  
**Tags**: #concept

## Overview

Backpropagation through time (BPTT) trains [[Recurrent Neural Networks]] by unrolling the network across timesteps into a deep feedforward graph with shared weights, then applying standard [[Back-Propagation]] and summing gradients from all timesteps into the same parameters.

## Appearances

- [[Recurrent Neural Networks: Building a Custom LSTM Cell]] — primary intuitive treatment: unrolled layers, per-timestep losses, gradient accumulation analogy to micro-batch training.
- [[Deep Learning]] — Chapter 10 discusses unfolding RNNs and the long-term dependency problem that motivates gated cells.

## Notes

For a sequence of length \(N\), BPTT creates \(N\) virtual layers with identical weights. Time and space complexity scale linearly with \(N\), limiting training on very long sequences. Truncated BPTT (not covered in the AI Summer tutorial) backprops only through a window of recent timesteps to reduce cost. Gradient accumulation across micro-batches is analogous: forward on batch 1, retain graph; forward on batch 2, average losses; then one backward pass.

## Related

- [[Recurrent Neural Networks]]
- [[LSTM]]
- [[Vanishing Gradients]]
- [[Back-Propagation]]
- [[Deep Learning]]
