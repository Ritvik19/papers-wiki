# Best Graph Neural Network architectures: GCN, GAT, MPNN and more

Sergios Karagiannakos · 2021-09-23 · 11 mins

**Source URL**: https://theaisummer.com/gnn-architectures/

---

Traditionally, datasets in Deep Learning applications such as computer vision and NLP are typically represented in the euclidean space. Recently though there is an increasing number of non-euclidean data that are represented as graphs.

To this end, Graph Neural Networks (GNNs) are an effort to apply deep learning techniques in graphs. The term GNN is typically referred to a variety of different algorithms and not a single architecture. As we will see, a plethora of different architectures have been developed over the years. To give you an early preview, here is a diagram presenting the most important papers on the field. The diagram has been borrowed from a recent review paper on GNNs by Zhou J. et al.

Before we dive into the different types of architectures, let's start with a few basic principles and some notation.

## Graph basic principles and notation

Graphs consist of a set of nodes and a set of edges. Both nodes and edges can have a set of features. From now on, a node's feature vector will be denoted as \(h_i\), where \(i\) is the node's index. Similarly an edge's feature vector will be denoted as \(e_{ij}\), where \(i, j\) are the nodes that the edge is attached to.

As you might also know, graphs can be directed, undirected, weighted and unweighted. Thus each architecture may be applied only to a type of graph or to all of them.

So can we start developing a Graph Neural Network?

The basic idea behind most GNN architectures is graph convolution. In essence, we try to generalize the idea of convolution into graphs. Graphs can be seen as a generalization of images where every node corresponds to a pixel connected to 8 (or 4) adjacent neighbours. Since CNNs take advantage of convolution with such great success, why not adjust this idea into graphs?

### Graph convolution

Graph convolution predicts the features of the node in the next layer as a function of the neighbours' features. It transforms the node's features \(x_i\) in a latent space \(h_i\) that can be used for a variety of reasons.

Visually this can be represented as follows:

But what can we actually do with these latent node features vectors? Typically all applications fall into one of the following categories:

- **Node classification**
- **Edge classification**
- **Graph classification**

### Node classification

If we apply a shared function \(f\) to each of the latent vectors \(h_i\), we can make predictions for each of the nodes. That way we can classify nodes based on their features: \(Z_i = f(h_i)\).

### Edge classification

Similarly, we can use it to classify edges based on their features. To accomplish this, we generally need both the adjacent node vectors as well as the edge features if they exist. Mathematically we have: \(Z_{ij} = f(h_i, h_j, e_{ij})\).

### Graph classification

Lastly, we can predict some attribute for the entire graph by aggregating all node features and applying an appropriate function \(f\): \(Z_G = f(\sum_i h_i)\). The aggregation usually is a permutation-invariant function such as a sum, mean operation, a pooling operation or even a trainable linear layer.

## Inductive vs Transductive learning

A terminology that can be confusing is the notion of inductive vs transductive, which is used often in the GNNs literature.

In transductive learning, the model has already encountered both the training and the test input data. In our case these are the nodes of a large graph where we want to predict the node labels. If a new node is added to the graph, we need to retrain the model.

In inductive learning, the model sees only the training data. Thus the generated model will be used to predict graph labels for unseen data.

To understand that from the GNNs perspective, imagine the following example. Suppose that we have a graph with 10 nodes. Also consider that the structure of the graph, how nodes are connected, is not important for the following example. We use 6 of them for the training set (with the labels) and 4 for the test set. How do we train this model?

- Use a semi-supervised learning approach and train the whole graph using only the 6 labeled data points. This is called **inductive learning**. Models trained correctly with inductive learning can generalize well but it can be quite hard to capture the complete structure of the data.
- Use a self-supervised approach which will label the unlabeled data points using additional information and train the model on all 10 nodes. This is called **transductive learning** and is quite common in GNNs since we use the whole graph to train the model.

With that out of the way, let's now proceed with the most popular GNN architectures.

## Spectral methods

Spectral methods deal with the representation of a graph in the spectral domain. The idea is quite intuitive.

These methods are based on graph signal processing and define the convolution operator in the spectral domain using the Fourier transform \(F\). The graph signal \(x\) is initially transformed to the spectral domain by the graph Fourier transform \(F\). Then the convolution operation is conducted by doing an element-wise multiplication. After the convolution, the resulting signal is transformed back using the inverse graph Fourier transform \(F^{-1}\).

\(F(x) = U^T x\), \(F^{-1}(x) = U x\)

\(U\) is a matrix defined by the eigenvectors of \(L\), where \(L = U \Lambda U^T\). \(\Lambda\) is a diagonal matrix with the eigenvalues of the graph.

The convolution operation is defined as: \(g * x = F^{-1}(F(g) \cdot F(x)) = U (U^T g \cdot U^T x)\)

\(L\) is the normalized graph Laplacian: \(L = I - D^{-1/2} A D^{-1/2}\)

### Spectral Networks

Spectral networks reduced the filter in the spectral domain to be a diagonal matrix \(g_w\) where \(w\) are the learnable parameters. Drawbacks: filter applied on entire graph (no locality); computationally inefficient for big graphs.

### ChebNets

ChebNets propose that feature representation should be affected only by k-hop neighborhood. Using Chebyshev expansion of order K, we define K-localized convolution without computing Laplacian eigenvectors.

### Graph Convolutional Networks (GCN)

GCN (Kipf & Welling) simplifies ChebNets to K=1 with: (1) self-connections \( \tilde{A} = A + I \); (2) symmetric Laplacian normalization; (3) renormalization trick \(\tilde{D}^{-1/2}\tilde{A}\tilde{D}^{-1/2}\).

Update rule: \(H^{(l+1)} = \sigma (\tilde{D}^{-\frac{1}{2}}\tilde{A}\tilde{D}^{-\frac{1}{2}} H^{(l)}W^{(l)})\)

Node-wise: \(h^{(l)}_i = \sigma( \sum_{j \in N_i} c_{ij} W h_j)\) where \(c_{ij} = \frac{1}{\sqrt{|N_i| |N_j|}}\).

Limitations: no direct edge features; no explicit messages along edges.

## Spatial methods

Spatial approaches define convolutions directly on the graph based on topology: transform node features, aggregate with permutation-invariant function, update each node from current values and aggregated neighborhood.

### Message Passing Neural Networks (MPNN)

MPNNs send messages \(m_{ij} = f_e(h_i, h_j, e_{ij})\) across edges via message function \(f_e\) (typically a small MLP). Messages are aggregated (e.g. summation) and combined with node features via update function \(f_v\): \(h_i = f_v (h_{i}, \sum_{j \in N_i} m_{ji})\). Powerful and generic but stores edge messages — scalability issues on large graphs.

### Graph Attention Networks (GAT)

GAT replaces GCN's fixed coefficient \(c_{ij} = 1/\sqrt{|N_i||N_j|}\) with learnable attention \(a_{ij} = \text{attention}(h_i, h_j)\), softmax-normalized over neighbors. Update: \(h^{(l)}_i = \sigma( \sum_{j \in N_i} a_{ij} W h_j)\). Multi-head attention concatenates K heads. Attention depends on node representations, not graph structure alone. Scalable and can incorporate edge features.

## Sampling methods

Sampling modules use a subset of neighborhood instead of full neighborhood for propagation.

### GraphSAGE

GraphSAGE: (1) sample uniform neighborhood subset; (2) aggregate sampled neighbor features; (3) classify nodes or graphs. Each layer extends K-hop receptive field. Key: trains learnable aggregation (mean, LSTM, max-pooling) alongside weight matrices. Supports unsupervised (nearby nodes similar) or supervised training. Inductive on large graphs.

### PinSAGE

PinSAGE extends GraphSAGE to Pinterest's 3B-node / 18B-edge graph. Neighborhood from random walks (importance scores); importance-sampling aggregation; supervised training on user engagement. Production web-scale recommender.

## Dynamic Graphs

Dynamic graphs change structure over time (social networks, transactions). Represented as time-stamped event streams.

### Temporal Graph Networks (TGN)

TGN predicts node embeddings at timestamp \(t\) from temporal neighborhoods (graph snapshots). Twitter architecture: GAT encoder on temporal neighborhood features + per-node memory (RNN-updated from MPNN-style messages). Self-supervised edge/interaction prediction on tweet graph.

## Conclusion

GNNs are an active field with many real-world graph-structured datasets. Follow-up articles plan PyTorch Geometric tutorials. Recommended: Petar Veličković lecture on theoretical foundations; Aleksa Gordić AI Epiphany video series.
