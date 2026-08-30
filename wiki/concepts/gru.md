# GRU

**Type**: concept  
**Tags**: #concept

## Overview

Gated Recurrent Units (GRUs) simplify LSTMs by combining forget and input gates into an update gate and merging cell and hidden state. They often match LSTM performance with fewer parameters.

## Appearances

- [[Deep Learning]] — Section 10.10 covers GRU alongside [[LSTM]] as a solution to long-term dependencies.
- [[Recurrent Neural Networks: Building GRU Cells VS LSTM Cells in PyTorch]] — gate-by-gate equation walkthrough and LSTM-vs-GRU empirical tradeoffs (Chung et al. 2014, Greff et al. 2016).

## Notes

Widely used in speech and NLP before self-attention. Still appears in efficient on-device sequence models.

GRU equations (PyTorch-style): reset \(r_t = \sigma(W_{ir}x_t + b_{ir} + W_{hr}h_{t-1} + b_{hr})\); update \(z_t = \sigma(W_{iz}x_t + b_{iz} + W_{hz}h_{t-1} + b_{hz})\); candidate \(n_t = \tanh(W_{in}x_t + b_{in} + r_t \odot (W_{hn}h_{t-1} + b_{hn}))\); hidden \(h_t = (1-z_t)\odot n_t + z_t \odot h_{t-1}\). Merges LSTM input and output gates into update gate \(z\); no separate cell state. Fewer parameters than LSTM; often comparable accuracy, especially with limited data. LSTM may win on very long dependencies and large datasets.

## Related

- [[LSTM]]
- [[Recurrent Neural Networks]]
- [[Backpropagation Through Time]]
- [[Vanishing Gradients]]
- [[Deep Learning]]
