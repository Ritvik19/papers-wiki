# Graph Neural Networks - An overview

Sergios Karagiannakos · 2020-02-01 · 3 mins

**Source URL**: https://theaisummer.com/Graph_Neural_Networks/

---

Over the past decade, we've seen that Neural Networks can perform tremendously well in structured data like images and text. Most of the popular models like convolutional networks, recurrent, autoencoders work very well on data that have a tabular format like a matrix or a vector. But what about unstructured data? What about Graph data?

## Graph Neural Networks

Graph Neural Networks were introduced back in 2005 but they started to gain popularity in the last 5 years. The GNNs are able to model the relationship between the nodes in a graph and produce a numeric representation of it. The importance of GNNs is quite significant because there are so many real-world data that can be represented as a graph. Social networks, chemical compounds, maps, transportation systems to name a few.

**Problem**: Map a given graph to a single label (numeric value, class, etc.):

\[ F(\text{Graph}) = \text{embedding} \]

Example: each graph is a chemical compound; the label is likelihood of drug usefulness — predict which molecules are viable drug candidates.

## RNNs as graphs

Recurrent neural networks can operate on a special type of graph — a **chained graph** (a line). Time series are chained graphs where each timestamp is a node followed by the next timestamp.

We can build a network where each graph node is a recurrent unit (LSTM or similar) and node information is an embedding transferred through the chain like a message. Recurrent units preserve information as embeddings travel through the graph — the same mechanism as NLP sequence models.

## Extending to general graphs

Each node becomes a recurrent unit; envelopes represent node embeddings traveling through the graph; each edge is replaced by a neural network to capture edge weight information (Microsoft Research GNN talk slide).

**Learning procedure** (per time step):

1. Each node pulls embeddings from all neighbors, sums them.
2. Passes the sum along with its own embedding to the recurrent unit → new embedding (node + neighbors).
3. Next time step: embedding also contains second-order neighbor information.
4. Process continues until every node embedding contains information from all other nodes.
5. **Readout**: sum all node embeddings → single graph-level embedding for downstream classification, prediction, or clustering.

## Libraries

- DeepMind `graph_nets` (TensorFlow)
- `rusty1s/pytorch_geometric` (PyTorch Geometric) — recommended for documentation
