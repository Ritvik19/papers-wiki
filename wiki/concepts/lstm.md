# LSTM

**Type**: concept  
**Tags**: #concept

## Overview

Long Short-Term Memory (LSTM) networks use gated memory cells to store information over long sequences, mitigating vanishing gradients in vanilla RNNs. Gates control what to forget, input, and output at each time step.

## Appearances

- [[Deep Learning]] — Section 10.10.2 is the canonical textbook treatment of LSTM and gated RNNs.
- [[Recurrent Neural Networks: Building a Custom LSTM Cell]] — gate-by-gate equation walkthrough, PyTorch-aligned notation (no peephole connections), and custom `LSTM_cell_AI_SUMMER` implementation validated on sine-wave prediction.
- [[Recurrent Neural Networks: Building GRU Cells VS LSTM Cells in PyTorch]] — side-by-side LSTM vs GRU tradeoffs: LSTM has more gates and a cell state; may excel on large data and long-range dependencies; GRU is faster and more compact.

## Notes

LSTMs dominated sequence modeling before transformers. Encoder–decoder LSTMs powered early neural machine translation. [[GRU]] is a lighter gated alternative.

Standard LSTM equations (PyTorch-style, no peephole): input gate \(i_t = \sigma(W_{xi}x_t + W_{hi}h_{t-1} + b_i)\); forget gate \(f_t = \sigma(W_{xf}x_t + W_{hf}h_{t-1} + b_f)\); cell \(c_t = f_t \odot c_{t-1} + i_t \odot \tanh(W_{xc}x_t + W_{hc}h_{t-1} + b_c)\); output gate \(o_t = \sigma(W_{xo}x_t + W_{h0}h_{t-1} + W_{co}c_t + b_o)\); hidden \(h_t = o_t \odot \tanh(c_t)\). Greff et al. (2016) found LSTM variants do not significantly outperform the standard architecture at scale.

## Related

- [[GRU]]
- [[Recurrent Neural Networks]]
- [[Backpropagation Through Time]]
- [[Vanishing Gradients]]
- [[Bidirectional RNN]]
- [[Encoder-Decoder Architecture]]
- [[Deep Learning]]
