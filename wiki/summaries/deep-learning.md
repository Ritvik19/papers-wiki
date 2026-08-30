# Deep Learning

**Source**: `raw/deep-learning-book/Deep Learning.pdf`  
**Authors**: Ian Goodfellow, Yoshua Bengio, Aaron Courville  
**Publisher**: MIT Press (2016); companion site [deeplearningbook.org](https://www.deeplearningbook.org)  
**Ingested**: 2026-05-20  
**Tags**: #summary

## Summary

*Deep Learning* (Goodfellow, Bengio & Courville, 2016) is the standard graduate-level textbook for modern neural networks. Across 801 pages and 20 chapters it moves from mathematical foundations to practice to research frontiers. Part I (**Applied Math and Machine Learning Basics**, Chapters 2–5) covers linear algebra, probability and information theory, numerical computation, and classical ML concepts—capacity, regularization, MLE, SGD, and the curse of dimensionality that motivates depth.

Part II (**Deep Networks: Modern Practices**, Chapters 6–12) is the core applied material: [[Feedforward Neural Networks]] and [[Back-Propagation]]; regularization (weight decay, early stopping, dropout, adversarial training); optimization (momentum, Adam, initialization, batch norm era precursors); [[Convolutional Neural Networks]]; [[Recurrent Neural Networks]] (bidirectional, encoder–decoder, LSTM/GRU, attention precursors); practical methodology; and applications in vision, speech, and NLP. Part III (**Deep Learning Research**, Chapters 13–20) treats [[Representation Learning]], structured probabilistic models, Monte Carlo and variational inference, partition-function tricks, and deep generative models (RBMs, DBNs, DBMs, directed nets, GSNs).

For readers of this wiki's LLM- and RL-focused material, the book supplies foundational vocabulary—computational graphs, vanishing gradients, distributed representations, sequence models, and generative modeling—that later work on transformers, scaling laws, and post-training builds on. It predates the transformer era (no attention chapter) but remains the canonical reference for CNNs, RNNs, autoencoders, and probabilistic deep learning.

## Key Claims

- **Deep learning** is representation learning: multiple learned layers of abstraction convert raw inputs into features suitable for the task, avoiding hand-engineered features that break when the data distribution shifts.
- Neural networks are **differentiable programs**; training is end-to-end gradient-based optimization over a computational graph, with [[Back-Propagation]] as the efficient reverse-mode automatic differentiation algorithm.
- **Depth** can provide exponential representational efficiency for some function classes; deeper models tend to generalize better when regularized appropriately, though optimization becomes harder.
- **Convolution** encodes translation equivariance and local connectivity; **pooling** adds translation invariance and downsampling—together they define the inductive bias of CNNs for grid data.
- **Recurrent networks** unfold over time; long-term dependency problems motivate gated architectures (LSTM, GRU) and later attention-based models.
- **Regularization** (L2, dropout, early stopping, data augmentation, noise) combats overfitting in high-capacity models; dropout approximates an ensemble of thinned networks.
- **Optimization** for deep nets differs from convex optimization: saddle points, ill-conditioning, and learning-rate schedules matter; adaptive methods (AdaGrad, RMSProp, Adam) address per-parameter scaling.
- **Unsupervised and generative** objectives (autoencoders, RBMs, graphical models) learn structure in data and support pretraining, density estimation, and sample generation—precursors to modern foundation-model pretraining.
- **Structured probabilistic models** (directed/undirected graphs, MCMC, variational inference) formalize uncertainty and dependencies; the partition function makes exact learning intractable for many undirected models.
- Historical trends (dataset scale, compute, algorithmic ideas) explain why neural nets succeeded after decades of skepticism—the book documents the transition from shallow to deep architectures around ImageNet-era breakthroughs.

## Figures

169 image assets in `wiki/assets/deep-learning-book/`: **168 textbook figures** (`fig-{chapter}-{number}.png`) plus **cover** (`fig-1.png`). Landmark aliases `fig-2`–`fig-27` mirror selected chapter figures for inline use elsewhere. Crops use caption-band splitting, chapter-header exclusion, 200 dpi render, and whitespace trim (`scripts/extract-dl-book-figures.py`).


### Cover

| Figure | Caption | Page |
|--------|---------|------|
| ![Cover](../assets/deep-learning-book/fig-1.png) | Book cover | 1 |

### Chapter 1: Introduction

| Figure | Caption | Page |
|--------|---------|------|
| ![Figure 1.1](../assets/deep-learning-book/fig-1-1.png) | **Figure 1.1**: Example of diﬀerent representations: suppose we want to separate twocategories of data by drawing a line between them... | 20 |
| ![Figure 1.2](../assets/deep-learning-book/fig-1-2.png) | **Figure 1.2**: Illustration of a deep learning model. It is diﬃcult for a computer to understandthe meaning of raw sensory input dat... | 22 |
| ![Figure 1.3](../assets/deep-learning-book/fig-1-3.png) | **Figure 1.3**: Illustration of computational graphs mapping an input to an output whereeach node performs an operation. Depth is the... | 23 |
| ![Figure 1.4](../assets/deep-learning-book/fig-1-4.png) | **Figure 1.4**: A Venn diagram showing how deep learning is a kind of representation learning,which is in turn a kind of machine lear... | 25 |
| ![Figure 1.5](../assets/deep-learning-book/fig-1-5.png) | **Figure 1.5**: Flowcharts showing how the diﬀerent parts of an AI system relate to eachother within diﬀerent AI disciplines. Shaded ... | 26 |
| ![Figure 1.6](../assets/deep-learning-book/fig-1-6.png) | **Figure 1.6**: The high-level organization of the book. An arrow from one chapter to anotherindicates that the former chapter is pre... | 28 |
| ![Figure 1.7](../assets/deep-learning-book/fig-1-7.png) | **Figure 1.7**: The ﬁgure shows two of the three historical waves of artiﬁcial neural netsresearch, as measured by the frequency of t... | 30 |
| ![Figure 1.8](../assets/deep-learning-book/fig-1-8.png) | **Figure 1.8**: Dataset sizes have increased greatly over time. In the early 1900s, statisticiansstudied datasets using hundreds or t... | 37 |
| ![Figure 1.9](../assets/deep-learning-book/fig-1-9.png) | **Figure 1.9**: Example inputs from the MNIST dataset. The “NIST” stands for NationalInstitute of Standards and Technology, the agenc... | 38 |
| ![Figure 1.10](../assets/deep-learning-book/fig-1-10.png) | **Figure 1.10**: Initially, the number of connections between neurons in artiﬁcial neuralnetworks was limited by hardware capabilities... | 40 |
| ![Figure 1.11](../assets/deep-learning-book/fig-1-11.png) | **Figure 1.11**: Since the introduction of hidden units, artiﬁcial neural networks have doubledin size roughly every 2.4 years. Biolog... | 43 |
| ![Figure 1.12](../assets/deep-learning-book/fig-1-12.png) | **Figure 1.12**: Since deep networks reached the scale necessary to compete in the ImageNetLarge Scale Visual Recognition Challenge, t... | 44 |

### Chapter 2: Linear Algebra

| Figure | Caption | Page |
|--------|---------|------|
| ![Figure 2.1](../assets/deep-learning-book/fig-2-1.png) | **Figure 2.1**: The transpose of the matrix can be thought of as a mirror image across themain diagonal. | 49 |
| ![Figure 2.2](../assets/deep-learning-book/fig-2-2.png) | **Figure 2.2**: Example identity matrix: This is I3. | 52 |
| ![Figure 2.3](../assets/deep-learning-book/fig-2-3.png) | **Figure 2.3**: An example of the eﬀect of eigenvectors and eigenvalues. Here, we havea matrix A with two orthonormal eigenvectors, v... | 59 |

### Chapter 3: Probability and Information Theory

| Figure | Caption | Page |
|--------|---------|------|
| ![Figure 3.1](../assets/deep-learning-book/fig-3-1.png) | **Figure 3.1**: The normal distribution: The normal distribution N (x; µ, σ2) exhibitsa classic “bell curve” shape, with the x coordi... | 80 |
| ![Figure 3.2](../assets/deep-learning-book/fig-3-2.png) | **Figure 3.2**: Samples from a Gaussian mixture model. In this example, there are threecomponents. From left to right, the ﬁrst compo... | 84 |
| ![Figure 3.3](../assets/deep-learning-book/fig-3-3.png) | **Figure 3.3**: The logistic sigmoid function. | 85 |
| ![Figure 3.4](../assets/deep-learning-book/fig-3-4.png) | **Figure 3.4**: The softplus function. | 85 |
| ![Figure 3.5](../assets/deep-learning-book/fig-3-5.png) | **Figure 3.5**: This plot shows how distributions that are closer to deterministic have lowShannon entropy while distributions that a... | 91 |
| ![Figure 3.6](../assets/deep-learning-book/fig-3-6.png) | **Figure 3.6**: The KL divergence is asymmetric. Suppose we have a distributionp(x) andwish to approximate it with another distributi... | 92 |
| ![Figure 3.7](../assets/deep-learning-book/fig-3-7.png) | **Figure 3.7**: A directed graphical model over random variables a, b, c, d and e. This graphcorresponds to probability distributions... | 94 |
| ![Figure 3.8](../assets/deep-learning-book/fig-3-8.png) | **Figure 3.8**: An undirected graphical model over random variablesa, b, c, d and e. Thisgraph corresponds to probability distributio... | 95 |

### Chapter 4: Numerical Computation

| Figure | Caption | Page |
|--------|---------|------|
| ![Figure 4.1](../assets/deep-learning-book/fig-4-1.png) | **Figure 4.1**: An illustration of how the gradient descent algorithm uses the derivatives of afunction can be used to follow the fun... | 99 |
| ![Figure 4.2](../assets/deep-learning-book/fig-4-2.png) | **Figure 4.2**: Examples of each of the three types of critical points in 1-D. A critical point isa point with zero slope. Such a poi... | 100 |
| ![Figure 4.3](../assets/deep-learning-book/fig-4-3.png) | **Figure 4.3**: Optimization algorithms may fail to ﬁnd a global minimum when there aremultiple local minima or plateaus present. In ... | 101 |
| ![Figure 4.4](../assets/deep-learning-book/fig-4-4.png) | **Figure 4.4**: The second derivative determines the curvature of a function. Here we showquadratic functions with various curvature.... | 103 |
| ![Figure 4.5](../assets/deep-learning-book/fig-4-5.png) | **Figure 4.5**: A saddle point containing both positive and negative curvature. The functionin this example is f (x) = x2 | 106 |
| ![Figure 4.6](../assets/deep-learning-book/fig-4-6.png) | **Figure 4.6**: Gradient descent fails to exploit the curvature information contained in theHessian matrix. Here we use gradient desc... | 107 |

### Chapter 5: Machine Learning Basics

| Figure | Caption | Page |
|--------|---------|------|
| ![Figure 5.1](../assets/deep-learning-book/fig-5-1.png) | **Figure 5.1**: A linear regression problem, with a training set consisting of ten data points,each containing one feature. Because t... | 125 |
| ![Figure 5.2](../assets/deep-learning-book/fig-5-2.png) | **Figure 5.2**: We ﬁt three models to this example training set. The training data wasgenerated synthetically, by randomly sampling x... | 129 |
| ![Figure 5.3](../assets/deep-learning-book/fig-5-3.png) | **Figure 5.3**: Typical relationship between capacity and error. Training and test errorbehave diﬀerently. At the left end of the gra... | 131 |
| ![Figure 5.4](../assets/deep-learning-book/fig-5-4.png) | **Figure 5.4**: The eﬀect of the training dataset size on the train and test error, as well ason the optimal model capacity. We const... | 133 |
| ![Figure 5.5](../assets/deep-learning-book/fig-5-5.png) | **Figure 5.5**: We ﬁt a high-degree polynomial regression model to our example training setfrom ﬁgure. The true function is quadratic... | 135 |
| ![Figure 5.6](../assets/deep-learning-book/fig-5-6.png) | **Figure 5.6**: As capacity increases (x-axis), bias (dotted) tends to decrease and variance(dashed) tends to increase, yielding anot... | 146 |
| ![Figure 5.7](../assets/deep-learning-book/fig-5-7.png) | **Figure 5.7**: Diagrams describing how a decision tree works. (Top)Each node of the treechooses to send the input example to the chi... | 161 |
| ![Figure 5.8](../assets/deep-learning-book/fig-5-8.png) | **Figure 5.8**: PCA learns a linear projection that aligns the direction of greatest variancewith the axes of the new space. (Left)Th... | 164 |
| ![Figure 5.9](../assets/deep-learning-book/fig-5-9.png) | **Figure 5.9**: As the number of relevant dimensions of the data increases (from left toright), the number of conﬁgurations of intere... | 172 |
| ![Figure 5.10](../assets/deep-learning-book/fig-5-10.png) | **Figure 5.10**: Illustration of how the nearest neighbor algorithm breaks up the input spaceinto regions. An example (represented her... | 175 |
| ![Figure 5.11](../assets/deep-learning-book/fig-5-11.png) | **Figure 5.11**: Data sampled from a distribution in a two-dimensional space that is actuallyconcentrated near a one-dimensional manif... | 177 |
| ![Figure 5.12](../assets/deep-learning-book/fig-5-12.png) | **Figure 5.12**: Sampling images uniformly at random (by randomly picking each pixelaccording to a uniform distribution) gives rise to... | 179 |
| ![Figure 5.13](../assets/deep-learning-book/fig-5-13.png) | **Figure 5.13**: Training examples from the QMUL Multiview Face Dataset (,)Gong et al. 2000for which the subjects were asked to move i... | 181 |

### Chapter 6: Deep Feedforward Networks

| Figure | Caption | Page |
|--------|---------|------|
| ![Figure 6.1](../assets/deep-learning-book/fig-6-1.png) | **Figure 6.1**: Solving the XOR problem by learning a representation. The bold numbersprinted on the plot indicate the value that the... | 189 |
| ![Figure 6.2](../assets/deep-learning-book/fig-6-2.png) | **Figure 6.2**: An example of a feedforward network, drawn in two diﬀerent styles. Speciﬁcally,this is the feedforward network we use... | 190 |
| ![Figure 6.3](../assets/deep-learning-book/fig-6-3.png) | **Figure 6.3**: The rectiﬁed linear activation function. This activation function is the defaultactivation function recommended for u... | 191 |
| ![Figure 6.4](../assets/deep-learning-book/fig-6-4.png) | **Figure 6.4**: Samples drawn from a neural network with a mixture density output layer.The input x is sampled from a uniform distrib... | 207 |
| ![Figure 6.5](../assets/deep-learning-book/fig-6-5.png) | **Figure 6.5**: An intuitive, geometric explanation of the exponential advantage of deeperrectiﬁer networks formally by().Montufar et... | 216 |
| ![Figure 6.6](../assets/deep-learning-book/fig-6-6.png) | **Figure 6.6**: Empirical results showing that deeper networks generalize better when usedto transcribe multi-digit numbers from phot... | 218 |
| ![Figure 6.7](../assets/deep-learning-book/fig-6-7.png) | **Figure 6.7**: Deeper models tend to perform better. This is not merely because the model islarger. This experiment from Goodfellow2... | 219 |
| ![Figure 6.8](../assets/deep-learning-book/fig-6-8.png) | **Figure 6.8**: Examples of computational graphs.The graph using the(a)× operation tocompute z = xy.The graph for the logistic regres... | 222 |
| ![Figure 6.9](../assets/deep-learning-book/fig-6-9.png) | **Figure 6.9**: A computational graph that results in repeated subexpressions when computingthe gradient. Let w ∈R be the input to th... | 227 |
| ![Figure 6.10](../assets/deep-learning-book/fig-6-10.png) | **Figure 6.10**: An example of the symbol-to-symbol approach to computing derivatives. Inthis approach, the back-propagation algorithm... | 230 |
| ![Figure 6.11](../assets/deep-learning-book/fig-6-11.png) | **Figure 6.11**: The computational graph used to compute the cost used to train our exampleof a single-layer MLP using the cross-entro... | 236 |

### Chapter 7: Regularization for Deep Learning

| Figure | Caption | Page |
|--------|---------|------|
| ![Figure 7.1](../assets/deep-learning-book/fig-7-1.png) | **Figure 7.1**: An illustration of the eﬀect ofL2 (or weight decay) regularization on the valueof the optimal w. The solid ellipses r... | 249 |
| ![Figure 7.2](../assets/deep-learning-book/fig-7-2.png) | **Figure 7.2**: Multi-task learning can be cast in several ways in deep learning frameworksand this ﬁgure illustrates the common situ... | 261 |
| ![Figure 7.3](../assets/deep-learning-book/fig-7-3.png) | **Figure 7.3**: Learning curves showing how the negative log-likelihood loss changes overtime (indicated as number of training iterat... | 262 |
| ![Figure 7.4](../assets/deep-learning-book/fig-7-4.png) | **Figure 7.4**: An illustration of the eﬀect of early stopping. (Left)The solid contour linesindicate the contours of the negative lo... | 267 |
| ![Figure 7.5](../assets/deep-learning-book/fig-7-5.png) | **Figure 7.5**: A cartoon depiction of how bagging works. Suppose we train an 8 detector onthe dataset depicted above, containing an ... | 273 |
| ![Figure 7.6](../assets/deep-learning-book/fig-7-6.png) | **Figure 7.6**: Dropout trains an ensemble consisting of all sub-networks that can beconstructed by removing non-output units from an... | 276 |
| ![Figure 7.7](../assets/deep-learning-book/fig-7-7.png) | **Figure 7.7**: An example of forward propagation through a feedforward network usingdropout. (Top)In this example, we use a feedforw... | 277 |
| ![Figure 7.8](../assets/deep-learning-book/fig-7-8.png) | **Figure 7.8**: A demonstration of adversarial example generation applied to GoogLeNet(,) on ImageNet. By adding an imperceptibly sma... | 285 |
| ![Figure 7.9](../assets/deep-learning-book/fig-7-9.png) | **Figure 7.9**: Illustration of the main idea of the tangent prop algorithm (,Simard et al.1992Rifai2011c) and manifold tangent class... | 288 |

### Chapter 8: Optimization for Training Deep Models

| Figure | Caption | Page |
|--------|---------|------|
| ![Figure 8.1](../assets/deep-learning-book/fig-8-1.png) | **Figure 8.1**: Gradient descent often does not arrive at a critical point of any kind. In thisexample, the gradient norm increases t... | 299 |
| ![Figure 8.2](../assets/deep-learning-book/fig-8-2.png) | **Figure 8.2**: A visualization of the cost function of a neural network. Image adaptedwith permission from Goodfellow2015et al. (). ... | 303 |
| ![Figure 8.3](../assets/deep-learning-book/fig-8-3.png) | **Figure 8.3**: The objective function for highly nonlinear deep neural networks or forrecurrent neural networks often contains sharp... | 305 |
| ![Figure 8.4](../assets/deep-learning-book/fig-8-4.png) | **Figure 8.4**: Optimization based on local downhill moves can fail if the local surface doesnot point toward the global solution. He... | 308 |
| ![Figure 8.5](../assets/deep-learning-book/fig-8-5.png) | **Figure 8.5**: Momentum aims primarily to solve two problems: poor conditioning of theHessian matrix and variance in the stochastic ... | 313 |
| ![Figure 8.6](../assets/deep-learning-book/fig-8-6.png) | **Figure 8.6**: The method of steepest descent applied to a quadratic cost surface. Themethod of steepest descent involves jumping to... | 330 |
| ![Figure 8.7](../assets/deep-learning-book/fig-8-7.png) | **Figure 8.7**: Illustration of one form of greedy supervised pretraining (,).Bengio et al. 2007(a)We start by training a suﬃciently ... | 340 |

### Chapter 9: Convolutional Networks

| Figure | Caption | Page |
|--------|---------|------|
| ![Figure 9.1](../assets/deep-learning-book/fig-9-1.png) | **Figure 9.1**: An example of 2-D convolution without kernel-ﬂipping. In this case we restrictthe output to only positions where the ... | 350 |
| ![Figure 9.2](../assets/deep-learning-book/fig-9-2.png) | **Figure 9.2**: Sparse connectivity, viewed from below: We highlight one input unit, x3,and also highlight the output units in s that... | 352 |
| ![Figure 9.3](../assets/deep-learning-book/fig-9-3.png) | **Figure 9.3**: Sparse connectivity, viewed from above: We highlight one output unit,s3,and also highlight the input units in x that ... | 353 |
| ![Figure 9.4](../assets/deep-learning-book/fig-9-4.png) | **Figure 9.4**: The receptive ﬁeld of the units in the deeper layers of a convolutional networkis larger than the receptive ﬁeld of t... | 353 |
| ![Figure 9.5](../assets/deep-learning-book/fig-9-5.png) | **Figure 9.5**: Parameter sharing: Black arrows indicate the connections that use a particularparameter in two diﬀerent models. (Top)... | 354 |
| ![Figure 9.6](../assets/deep-learning-book/fig-9-6.png) | **Figure 9.6**: Eﬃciency of edge detection. The image on the right was formed by takingeach pixel in the original image and subtracti... | 356 |
| ![Figure 9.7](../assets/deep-learning-book/fig-9-7.png) | **Figure 9.7**: The components of a typical convolutional neural network layer. There are twocommonly used sets of terminology for de... | 357 |
| ![Figure 9.8](../assets/deep-learning-book/fig-9-8.png) | **Figure 9.8**: Max pooling introduces invariance. (Top)A view of the middle of the outputof a convolutional layer. The bottom row sh... | 359 |
| ![Figure 9.9](../assets/deep-learning-book/fig-9-9.png) | **Figure 9.9**: Example of learned invariances: A pooling unit that pools over multiple featuresthat are learned with separate parame... | 360 |
| ![Figure 9.10](../assets/deep-learning-book/fig-9-10.png) | **Figure 9.10**: Pooling with downsampling. Here we use max-pooling with a pool width ofthree and a stride between pools of two. This ... | 360 |
| ![Figure 9.11](../assets/deep-learning-book/fig-9-11.png) | **Figure 9.11**: Examples of architectures for classiﬁcation with convolutional networks. Thespeciﬁc strides and depths used in this ﬁ... | 362 |
| ![Figure 9.12](../assets/deep-learning-book/fig-9-12.png) | **Figure 9.12**: Convolution with a stride.In this example, we use a stride of two.(Top)Convolution with a stride length of two implem... | 366 |
| ![Figure 9.13](../assets/deep-learning-book/fig-9-13.png) | **Figure 9.13**: The eﬀect of zero padding on network size: Consider a convolutional networkwith a kernel of width six at every layer.... | 367 |
| ![Figure 9.14](../assets/deep-learning-book/fig-9-14.png) | **Figure 9.14**: Comparison of local connections, convolution, and full connections.(Top)A locally connected layer with a patch size o... | 369 |
| ![Figure 9.15](../assets/deep-learning-book/fig-9-15.png) | **Figure 9.15**: A convolutional network with the ﬁrst two output channels connected toonly the ﬁrst two input channels, and the secon... | 370 |
| ![Figure 9.16](../assets/deep-learning-book/fig-9-16.png) | **Figure 9.16**: A comparison of locally connected layers, tiled convolution, and standardconvolution. All three have the same sets of... | 371 |
| ![Figure 9.17](../assets/deep-learning-book/fig-9-17.png) | **Figure 9.17**: An example of a recurrent convolutional network for pixel labeling. Theinput is an image tensor, with axes correspond... | 375 |
| ![Figure 9.18](../assets/deep-learning-book/fig-9-18.png) | **Figure 9.18**: Gabor functions with a variety of parameter settings. White indicateslarge positive weight, black indicates large neg... | 386 |
| ![Figure 9.19](../assets/deep-learning-book/fig-9-19.png) | **Figure 9.19**: Some of the most striking correspondences between neuroscience and machinelearning come from visually comparing the f... | 386 |

### Chapter 10: Sequence Modeling: Recurrent and Recursive Nets

| Figure | Caption | Page |
|--------|---------|------|
| ![Figure 10.1](../assets/deep-learning-book/fig-10-1.png) | **Figure 10.1**: The classical dynamical system described by equation, illustrated as an10.1unfolded computational graph. Each node re... | 391 |
| ![Figure 10.2](../assets/deep-learning-book/fig-10-2.png) | **Figure 10.2**: A recurrent network with no outputs. This recurrent network just processesinformation from the input x by incorporati... | 392 |
| ![Figure 10.3](../assets/deep-learning-book/fig-10-3.png) | **Figure 10.3**: The computational graph to compute the training loss of a recurrent networkthat maps an input sequence of x values to... | 394 |
| ![Figure 10.4](../assets/deep-learning-book/fig-10-4.png) | **Figure 10.4**: An RNN whose only recurrence is the feedback connection from the outputto the hidden layer. At each time step t, the ... | 396 |
| ![Figure 10.5](../assets/deep-learning-book/fig-10-5.png) | **Figure 10.5**: Time-unfolded recurrent neural network with a single output at the endof the sequence. Such a network can be used to ... | 398 |
| ![Figure 10.6](../assets/deep-learning-book/fig-10-6.png) | **Figure 10.6**: Illustration of teacher forcing. Teacher forcing is a training technique that isapplicable to RNNs that have connecti... | 399 |
| ![Figure 10.7](../assets/deep-learning-book/fig-10-7.png) | **Figure 10.7**: Fully connected graphical model for a sequencey(1),y (2),. .. , y( )t ,. ..: everypast observation y( )i may inﬂuence... | 404 |
| ![Figure 10.8](../assets/deep-learning-book/fig-10-8.png) | **Figure 10.8**: Introducing the state variable in the graphical model of the RNN, eventhough it is a deterministic function of its in... | 404 |
| ![Figure 10.9](../assets/deep-learning-book/fig-10-9.png) | **Figure 10.9**: An RNN that maps a ﬁxed-length vectorx into a distribution over sequencesY. This RNN is appropriate for tasks such as... | 408 |
| ![Figure 10.10](../assets/deep-learning-book/fig-10-10.png) | **Figure 10.10**: A conditional recurrent neural network mapping a variable-length sequenceof x values into a distribution over sequenc... | 409 |
| ![Figure 10.11](../assets/deep-learning-book/fig-10-11.png) | **Figure 10.11**: Computation of a typical bidirectional recurrent neural network, meantto learn to map input sequences x to target seq... | 410 |
| ![Figure 10.12](../assets/deep-learning-book/fig-10-12.png) | **Figure 10.12**: Example of an encoder-decoder or sequence-to-sequence RNN architecture,for learning to generate an output sequence (y... | 412 |
| ![Figure 10.13](../assets/deep-learning-book/fig-10-13.png) | **Figure 10.13**: A recurrent neural network can be made deep in many ways (Pascanuet al.,).The hidden recurrent state can be broken do... | 415 |
| ![Figure 10.14](../assets/deep-learning-book/fig-10-14.png) | **Figure 10.14**: A recursive network has a computational graph that generalizes that of therecurrent network from a chain to a tree. A... | 416 |
| ![Figure 10.15](../assets/deep-learning-book/fig-10-15.png) | **Figure 10.15**: When composing many nonlinear functions (like the linear-tanh layer shownhere), the result is highly nonlinear, typic... | 418 |
| ![Figure 10.16](../assets/deep-learning-book/fig-10-16.png) | **Figure 10.16**: Block diagram of the LSTM recurrent network “cell.” Cells are connectedrecurrently to each other, replacing the usual... | 425 |
| ![Figure 10.17](../assets/deep-learning-book/fig-10-17.png) | **Figure 10.17**: Example of the eﬀect of gradient clipping in a recurrent network withtwo parameters w and b. Gradient clipping can ma... | 430 |
| ![Figure 10.18](../assets/deep-learning-book/fig-10-18.png) | **Figure 10.18**: A schematic of an example of a network with an explicit memory, capturingsome of the key design elements of the neura... | 433 |

### Chapter 11: Practical Methodology

| Figure | Caption | Page |
|--------|---------|------|
| ![Figure 11.1](../assets/deep-learning-book/fig-11-1.png) | **Figure 11.1**: Typical relationship between the learning rate and the training error. Noticethe sharp rise in error when the learnin... | 446 |
| ![Figure 11.2](../assets/deep-learning-book/fig-11-2.png) | **Figure 11.2**: Comparison of grid search and random search. For illustration purposes wedisplay two hyperparameters but we are typic... | 449 |

### Chapter 12: Applications

| Figure | Caption | Page |
|--------|---------|------|
| ![Figure 12.1](../assets/deep-learning-book/fig-12-1.png) | **Figure 12.1**: GCN maps examples onto a sphere. (Left)Raw input data may have any norm.(Center)GCN with λ = 0 maps all non-zero exam... | 472 |
| ![Figure 12.2](../assets/deep-learning-book/fig-12-2.png) | **Figure 12.2**: A comparison of global and local contrast normalization. Visually, the eﬀectsof global contrast normalization are sub... | 473 |
| ![Figure 12.3](../assets/deep-learning-book/fig-12-3.png) | **Figure 12.3**: Two-dimensional visualizations of word embeddings obtained from a neuralmachine translation model (,), zooming in on ... | 481 |
| ![Figure 12.4](../assets/deep-learning-book/fig-12-4.png) | **Figure 12.4**: Illustration of a simple hierarchy of word categories, with 8 wordsw0, . . . , w7organized into a three level hierarc... | 484 |
| ![Figure 12.5](../assets/deep-learning-book/fig-12-5.png) | **Figure 12.5**: The encoder-decoder architecture to map back and forth between a surfacerepresentation (such as a sequence of words o... | 490 |
| ![Figure 12.6](../assets/deep-learning-book/fig-12-6.png) | **Figure 12.6**: A modern attention mechanism, as introduced by(), isBahdanau et al. 2015essentially a weighted average. A context vec... | 491 |

### Chapter 13: Linear Factor Models

| Figure | Caption | Page |
|--------|---------|------|
| ![Figure 13.1](../assets/deep-learning-book/fig-13-1.png) | **Figure 13.1**: The directed graphical model describing the linear factor model family, inwhich we assume that an observed data vecto... | 506 |
| ![Figure 13.2](../assets/deep-learning-book/fig-13-2.png) | **Figure 13.2**: Example samples and weights from a spike and slab sparse coding modeltrained on the MNIST dataset. (Left)The samples ... | 515 |
| ![Figure 13.3](../assets/deep-learning-book/fig-13-3.png) | **Figure 13.3**: Flat Gaussian capturing probability concentration near a low-dimensionalmanifold. The ﬁgure shows the upper half of t... | 516 |

### Chapter 14: Autoencoders

| Figure | Caption | Page |
|--------|---------|------|
| ![Figure 14.1](../assets/deep-learning-book/fig-14-1.png) | **Figure 14.1**: The general structure of an autoencoder, mapping an inputto an outputx(called reconstruction) r through an internal r... | 519 |
| ![Figure 14.2](../assets/deep-learning-book/fig-14-2.png) | **Figure 14.2**: The structure of a stochastic autoencoder, in which both the encoder and thedecoder are not simple functions but inst... | 526 |
| ![Figure 14.3](../assets/deep-learning-book/fig-14-3.png) | **Figure 14.3**: The computational graph of the cost function for a denoising autoencoder,which is trained to reconstruct the clean da... | 527 |
| ![Figure 14.4](../assets/deep-learning-book/fig-14-4.png) | **Figure 14.4**: A denoising autoencoder is trained to map a corrupted data point˜x back tothe original data point x. We illustrate tr... | 528 |
| ![Figure 14.5](../assets/deep-learning-book/fig-14-5.png) | **Figure 14.5**: Vector ﬁeld learned by a denoising autoencoder around a 1-D curved manifoldnear which the data concentrates in a 2-D ... | 530 |
| ![Figure 14.6](../assets/deep-learning-book/fig-14-6.png) | **Figure 14.6**: An illustration of the concept of a tangent hyperplane. Here we create aone-dimensional manifold in 784-dimensional s... | 533 |
| ![Figure 14.7](../assets/deep-learning-book/fig-14-7.png) | **Figure 14.7**: If the autoencoder learns a reconstruction function that is invariant to smallperturbations near the data points, it ... | 534 |
| ![Figure 14.8](../assets/deep-learning-book/fig-14-8.png) | **Figure 14.8**: Non-parametric manifold learning procedures build a nearest neighbor graphin which nodes represent training examples ... | 535 |
| ![Figure 14.9](../assets/deep-learning-book/fig-14-9.png) | **Figure 14.9**: If the tangent planes (see ﬁgure) at each location are known, then they14.6can be tiled to form a global coordinate s... | 536 |
| ![Figure 14.10](../assets/deep-learning-book/fig-14-10.png) | **Figure 14.10**: Illustration of tangent vectors of the manifold estimated by local PCAand by a contractive autoencoder. The location ... | 539 |

### Chapter 15: Representation Learning

| Figure | Caption | Page |
|--------|---------|------|
| ![Figure 15.1](../assets/deep-learning-book/fig-15-1.png) | **Figure 15.1**: Visualization via nonlinear projection of the learning trajectories of diﬀerentneural networks in function space (not... | 549 |
| ![Figure 15.2](../assets/deep-learning-book/fig-15-2.png) | **Figure 15.2**: Example architecture for multi-task or transfer learning when the outputvariablehas the same semantics for all tasks ... | 553 |
| ![Figure 15.3](../assets/deep-learning-book/fig-15-3.png) | **Figure 15.3**: Transfer learning between two domains x and y enables zero-shot learning.Labeled or unlabeled examples of x allow one... | 556 |
| ![Figure 15.4](../assets/deep-learning-book/fig-15-4.png) | **Figure 15.4**: Example of a density over x that is a mixture over three components.The component identity is an underlying explanato... | 558 |
| ![Figure 15.5](../assets/deep-learning-book/fig-15-5.png) | **Figure 15.5**: An autoencoder trained with mean squared error for a robotics task hasfailed to reconstruct a ping pong ball. The exi... | 560 |
| ![Figure 15.6](../assets/deep-learning-book/fig-15-6.png) | **Figure 15.6**: Predictive generative networks provide an example of the importance oflearning which features are salient. In this ex... | 561 |
| ![Figure 15.7](../assets/deep-learning-book/fig-15-7.png) | **Figure 15.7**: Illustration of how a learning algorithm based on a distributed representationbreaks up the input space into regions.... | 563 |
| ![Figure 15.8](../assets/deep-learning-book/fig-15-8.png) | **Figure 15.8**: Illustration of how the nearest neighbor algorithm breaks up the input spaceinto diﬀerent regions. The nearest neighb... | 565 |
| ![Figure 15.9](../assets/deep-learning-book/fig-15-9.png) | **Figure 15.9**: A generative model has learned a distributed representation that disentanglesthe concept of gender from the concept o... | 568 |

### Chapter 16: Structured Probabilistic Models for Deep Learning

| Figure | Caption | Page |
|--------|---------|------|
| ![Figure 16.1](../assets/deep-learning-book/fig-16-1.png) | **Figure 16.1**: Probabilistic modeling of natural images. (Top)Example 32× 32 pixel colorimages from the CIFAR-10 dataset (,).Samples... | 577 |
| ![Figure 16.2](../assets/deep-learning-book/fig-16-2.png) | **Figure 16.2**: A directed graphical model depicting the relay race example. Alice’s ﬁnishingtime t0 inﬂuences Bob’s ﬁnishing time t1... | 580 |
| ![Figure 16.3](../assets/deep-learning-book/fig-16-3.png) | **Figure 16.3**: An undirected graph representing how your roommate’s healthhr, yourhealth hy, and your work colleague’s health hc aﬀe... | 583 |
| ![Figure 16.5](../assets/deep-learning-book/fig-16-5.png) | **Figure 16.5**: This graph implies that E(a b c d e f, , , , , ) can be written as Ea b, (a b, ) +Eb c, (b c, ) + Ea d, (a d, ) + Eb ... | 587 |
| ![Figure 16.6](../assets/deep-learning-book/fig-16-6.png) | **Figure 16.6**: (a) The path between random variablea and random variable b through s isactive, because s is not observed. This means... | 588 |
| ![Figure 16.7](../assets/deep-learning-book/fig-16-7.png) | **Figure 16.7**: An example of reading separation properties from an undirected graph. Hereb is shaded to indicate that it is observed... | 589 |
| ![Figure 16.8](../assets/deep-learning-book/fig-16-8.png) | **Figure 16.8**: All of the kinds of active paths of length two that can exist between randomvariables a and b.Any path with arrows pr... | 590 |
| ![Figure 16.9](../assets/deep-learning-book/fig-16-9.png) | **Figure 16.9**: From this graph, we can read out several d-separation properties. Examplesinclude: | 591 |
| ![Figure 16.10](../assets/deep-learning-book/fig-16-10.png) | **Figure 16.10**: Examples of complete graphs, which can describe any probability distribution.Here we show examples with four random v... | 593 |
| ![Figure 16.11](../assets/deep-learning-book/fig-16-11.png) | **Figure 16.11**: Examples of converting directed models (top row) to undirected models(bottom row) by constructing moralized graphs. (... | 594 |
| ![Figure 16.12](../assets/deep-learning-book/fig-16-12.png) | **Figure 16.12**: Converting an undirected model to a directed model. (Left)This undirectedmodel cannot be converted directed to a dire... | 595 |
| ![Figure 16.13](../assets/deep-learning-book/fig-16-13.png) | **Figure 16.13**: An example of how a factor graph can resolve ambiguity in the interpretationof undirected networks. (Left)An undirect... | 596 |
| ![Figure 16.14](../assets/deep-learning-book/fig-16-14.png) | **Figure 16.14**: An RBM drawn as a Markov network. | 604 |
| ![Figure 16.15](../assets/deep-learning-book/fig-16-15.png) | **Figure 16.15**: Samples from a trained RBM, and its weights. Image reproduced withpermission from().LISA 2008(Left)Samples from a mod... | 605 |

### Chapter 17: Monte Carlo Methods

| Figure | Caption | Page |
|--------|---------|------|
| ![Figure 17.1](../assets/deep-learning-book/fig-17-1.png) | **Figure 17.1**: Paths followed by Gibbs sampling for three distributions, with the Markovchain initialized at the mode in both cases.... | 617 |
| ![Figure 17.2](../assets/deep-learning-book/fig-17-2.png) | **Figure 17.2**: An illustration of the slow mixing problem in deep probabilistic models.Each panel should be read left to right, top ... | 618 |

### Chapter 18: Confronting the Partition Function

| Figure | Caption | Page |
|--------|---------|------|
| ![Figure 18.1](../assets/deep-learning-book/fig-18-1.png) | **Figure 18.1**: The view of algorithmas having a “positive phase” and “negative phase.”18.1(Left)In the positive phase, we sample poi... | 625 |
| ![Figure 18.2](../assets/deep-learning-book/fig-18-2.png) | **Figure 18.2**: An illustration of how the negative phase of contrastive divergence (algo-rithm) can fail to suppress spurious modes.... | 627 |

### Chapter 19: Approximate Inference

| Figure | Caption | Page |
|--------|---------|------|
| ![Figure 19.1](../assets/deep-learning-book/fig-19-1.png) | **Figure 19.1**: Intractable inference problems in deep learning are usually the result ofinteractions between latent variables in a s... | 648 |
| ![Figure 19.2](../assets/deep-learning-book/fig-19-2.png) | **Figure 19.2**: The graph structure of a binary sparse coding model with four hidden units.(Left)The graph structure of p(h v, ). Not... | 657 |

### Chapter 20: Deep Generative Models

| Figure | Caption | Page |
|--------|---------|------|
| ![Figure 20.1](../assets/deep-learning-book/fig-20-1.png) | **Figure 20.1**: Examples of models that may be built with restricted Boltzmann machines.(a)The restricted Boltzmann machine itself is... | 673 |
| ![Figure 20.2](../assets/deep-learning-book/fig-20-2.png) | **Figure 20.2**: The graphical model for a deep Boltzmann machine with one visible layer(bottom) and two hidden layers. Connections ar... | 679 |
| ![Figure 20.3](../assets/deep-learning-book/fig-20-3.png) | **Figure 20.3**: A deep Boltzmann machine, re-arranged to reveal its bipartite graph structure. | 680 |
| ![Figure 20.4](../assets/deep-learning-book/fig-20-4.png) | **Figure 20.4**: The deep Boltzmann machine training procedure used to classify the MNISTdataset (Salakhutdinov and Hinton 2009a Sriva... | 688 |
| ![Figure 20.5](../assets/deep-learning-book/fig-20-5.png) | **Figure 20.5**: An illustration of the multi-prediction training process for a deep Boltzmannmachine. Each row indicates a diﬀerent e... | 691 |
| ![Figure 20.6](../assets/deep-learning-book/fig-20-6.png) | **Figure 20.6**: Examples of two-dimensional coordinate systems for high-dimensional mani-folds, learned by a variational autoencoder ... | 716 |
| ![Figure 20.7](../assets/deep-learning-book/fig-20-7.png) | **Figure 20.7**: Images generated by GANs trained on the LSUN dataset. (Left)Imagesof bedrooms generated by a DCGAN model, reproduced ... | 718 |
| ![Figure 20.8](../assets/deep-learning-book/fig-20-8.png) | **Figure 20.8**: A fully visible belief network predicts the i-th variable from the i −1previous ones. (Top)(Bottom)The directed graph... | 722 |
| ![Figure 20.9](../assets/deep-learning-book/fig-20-9.png) | **Figure 20.9**: A neural auto-regressive network predicts thei-th variable xi from the i −1previous ones, but is parametrized so that... | 723 |
| ![Figure 20.10](../assets/deep-learning-book/fig-20-10.png) | **Figure 20.10**: An illustration of the neural autoregressive density estimator (NADE). Thehidden units are organized in groupsh( )j s... | 725 |
| ![Figure 20.11](../assets/deep-learning-book/fig-20-11.png) | **Figure 20.11**: Each step of the Markov chain associated with a trained denoising autoen-coder, that generates the samples from the p... | 728 |
| ![Figure 20.12](../assets/deep-learning-book/fig-20-12.png) | **Figure 20.12**: Illustration of clamping the right half of the image and running the MarkovChain by resampling only the left half at ... | 730 |

## Techniques

**78 concept pages** reference this book. Indexed by chapter (one row per chapter; see linked pages for section-level detail):

| Ch. | Title | Wiki concepts |
|-----|-------|---------------|
| 1 | Introduction | [[Representation Learning]], [[Computational Graphs]] |
| 2 | Linear algebra | [[Singular Value Decomposition]], [[Principal Component Analysis]] |
| 3 | Probability & information theory | [[Entropy]], [[KL Divergence]], [[Cross-Entropy Loss]], [[Softmax]], [[Directed Graphical Models]] |
| 4 | Numerical computation | [[Log-Sum-Exp Trick]], [[Gradient Descent]] |
| 5 | Machine learning basics | [[Model Capacity]], [[Overfitting]], [[Bias-Variance Tradeoff]], [[Maximum Likelihood Estimation]], [[Bayesian Statistics]], [[Unsupervised Learning]], [[Stochastic Gradient Descent]] |
| 6 | Deep feedforward networks | [[Feedforward Neural Networks]], [[Back-Propagation]], [[Activation Functions]] |
| 7 | Regularization | [[Weight Decay]], [[Dropout]], [[Early Stopping]], [[Data Augmentation]], [[Semi-Supervised Learning]], [[Multi-Task Learning]], [[Parameter Sharing]], [[Bagging]], [[Adversarial Training]] |
| 8 | Optimization | [[Momentum]], [[RMSProp]], [[Adam]], [[Learning Rate Schedule]], [[Weight Initialization]], [[Batch Normalization]], [[Second-Order Optimization]], [[Curriculum Learning]], [[Greedy Layer-Wise Pretraining]] |
| 9 | Convolutional networks | [[Convolution]], [[Convolutional Neural Networks]], [[Pooling]] |
| 10 | Sequence modeling | [[Recurrent Neural Networks]], [[Bidirectional RNN]], [[Encoder-Decoder Architecture]], [[Recursive Neural Networks]], [[LSTM]], [[GRU]], [[Echo State Networks]], [[Vanishing Gradients]] |
| 11 | Practical methodology | [[Hyperparameter Tuning]] |
| 12 | Applications | (see [[Computer Vision]], [[Large Language Models]], [[Audio Models]]) |
| 13 | Linear factor models | [[Principal Component Analysis]], [[Independent Component Analysis]], [[Sparse Coding]] |
| 14 | Autoencoders | [[Autoencoders]], [[Denoising Autoencoders]], [[Contractive Autoencoders]], [[Variational Autoencoders]] |
| 15 | Representation learning | [[Representation Learning]], [[Greedy Layer-Wise Pretraining]], [[Transfer Learning]], [[Domain Adaptation]], [[Distributed Representations]] |
| 16 | Structured probabilistic models | [[Directed Graphical Models]], [[Undirected Graphical Models]] |
| 17 | Monte Carlo methods | [[Markov Chain Monte Carlo]], [[Gibbs Sampling]] |
| 18 | Partition function | [[Partition Function]], [[Contrastive Divergence]], [[Pseudolikelihood]], [[Score Matching]], [[Denoising Score Matching]], [[Noise-Contrastive Estimation]] |
| 19 | Approximate inference | [[MAP Inference]], [[Expectation Maximization]], [[Variational Inference]] |
| 20 | Deep generative models | [[Boltzmann Machines]], [[Restricted Boltzmann Machine]], [[Deep Belief Networks]], [[Deep Boltzmann Machine]], [[Generative Adversarial Networks]], [[Generative Stochastic Networks]] |

## Entities

- [[Ian Goodfellow]] — lead author; co-inventor of GANs; contributed generative modeling and adversarial training material.
- [[Yoshua Bengio]] — co-author; pioneer of deep learning, sequence models, and representation learning.
- [[Aaron Courville]] — co-author; researcher on probabilistic models and computer vision applications.

## Questions & Gaps

- Published in 2016: no transformer/attention chapter, limited coverage of modern LLM scale, RLHF, or diffusion models.
- Pure math drill (Ch. 2 tensor algebra, trace, determinant) and application walkthroughs (Ch. 11–12) have no dedicated concept pages; Ch. 12 defers to wiki topic hubs.
- All 168 textbook figures are listed in the **Figures** section above as cropped assets (`fig-{ch}-{num}.png`).
- Some optimization advice (e.g. pretraining heuristics) reflects pre-2016 practice; cross-check with [[Inference Engineering]] and recent scaling-law work for production LLMs.

## Related

- [[Gradient Descent]] — hub for optimization concepts (Chapters 4, 8).
- [[Computer Vision]] — CNN applications and ImageNet-era history (Chapter 9, 12.2).
- [[Large Language Models]] — RNN/encoder–decoder NLP foundations (Chapter 10, 12.4); superseded in part by transformers.
- [[Embedding and Retrieval]] — distributed representations and representation learning (Chapters 14–15).
- [[Model Compression and Efficiency]] — depth, capacity, and regularization tradeoffs (Chapters 6–7).
- [[Papers Explained Review 01 - Convolutional Neural Networks]] — paper-level CNN follow-ups in the corpus.
- [[Papers Explained Review 11 - Auto Encoders]] — autoencoder survey aligned with Chapter 14.
- [[Reinforcement Learning: An Introduction]] — complementary foundational textbook for RL (not covered here).
- [[Inference Engineering]] — modern inference stack for deployed neural models.
