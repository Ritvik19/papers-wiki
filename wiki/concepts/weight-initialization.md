# Weight Initialization

**Type**: concept  
**Tags**: #concept

## Overview

Weight initialization sets starting parameters before training. Poor initialization can cause vanishing or exploding activations and gradients; good schemes preserve variance of activations and gradients across layers (Xavier/Glorot, He initialization).

## Appearances

- [[Deep Learning]] — Chapter 8.4 covers initialization strategies and their interaction with activation functions and depth.

## Notes

Initialization is especially critical for deep networks without normalization. The book links initialization choices to activation function (ReLU vs sigmoid/tanh) and fan-in/fan-out.

## Related

- [[Vanishing Gradients]]
- [[Feedforward Neural Networks]]
- [[Deep Learning]]
