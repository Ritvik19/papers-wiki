# Activation Functions

**Type**: concept  
**Tags**: #concept

## Overview

Activation functions introduce nonlinearity between affine layers so neural networks can approximate complex functions. Common choices include ReLU, sigmoid, tanh, softmax (output), and gated activations in RNNs.

## Appearances

- [[Deep Learning]] — Section 6.3 surveys hidden-unit nonlinearities and their gradient properties (vanishing vs exploding).

## Notes

ReLU mitigates vanishing gradients compared to sigmoid/tanh but can cause dead neurons. Modern architectures mix activations (GELU, Swish) not all covered in the 2016 edition.

## Related

- [[Vanishing Gradients]]
- [[Feedforward Neural Networks]]
- [[Weight Initialization]]
- [[Deep Learning]]
