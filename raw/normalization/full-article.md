# In-layer normalization techniques for training very deep neural networks

Nikolas Adaloglou on 2020-10-15 · 10 mins  
Source: https://theaisummer.com/normalization/

If you open any introductory machine learning textbook, you will find the idea of input scaling. It is undesirable to train a model with gradient descent with non-normalized features.

In this article, we will review and understand the most common normalization methods. Different methods have been introduced for different tasks and architectures. We will attempt to associate the tasks with the methods although some approaches are quite general.

## Why?

Let's start with an intuitive example to understand why we want normalization inside any model.

Imagine what will happen if the input features are lying in different ranges. Imagine that one input feature lies in the range [0,1] and another in the range [0,10000]. As a result, the model will simply ignore the first feature, given that weight is initialized in a small and close range. You don't even need exploding gradients to occur. Yeap, that's another problem you will face.

Similarly, we encounter the same issues inside the layers of deep neural networks. This concern is independent of the architecture (transformers, convolutional neural networks, recurrent neural networks, GANs).

If we think out of the box, any intermediate layer is conceptually the same as the input layer: it accepts features and transforms them.

To this end, we need to develop ways to train our models more effectively. Effectiveness can be evaluated in terms of training time, performance, and stability.

Below you can see a graph depicting the trends in normalization methods used by different papers through time.

Source: papers with code

## Notations

Throughout this article, NN will be the batch size, while HH refers to the height, WW to the width, and CC to the feature channels. The greek letter μ() refers to mean and the greek letter σ() refers to standard deviation. The batch features are xx with a shape of [N, C, H, W]. For the referenced style image I use the symbol yy while for the segmentation mask I use the symbol mm or just mask.

x,y,m ∈ R^{N × C × H × W}

Besides, we will visualize the 4D activation maps x by merging the spatial dimensions. Now we have a 3D shape.

## Batch normalization (2015)

Batch Normalization (BN) normalizes the mean and standard deviation for each individual feature channel/map.

First of all, the mean and standard deviation of image features are first-order statistics. So, they relate to the global characteristics (such as the image style). In this way, we somehow blend the global characteristics. Such a strategy is effective when we want our representation to share these characteristics. This is the reason that we widely utilize BN in downstream tasks (i.e. image classification).

From a mathematical point of view, you can think of it as bringing the features of the image in the same range.

Specifically, we demand from our features to follow a Gaussian distribution with zero mean and unit variance.

BN(x) = γ((x - μ(x))/σ(x)) + β

μ_c(x) = (1/NHW) Σ_{n,h,w} x_{nchw}

σ_c(x) = sqrt((1/NHW) Σ_{n,h,w} (x_{nchw} - μ_c(x))^2)

Notably, the spatial dimensions, as well as the image batch, are averaged. This way, we concentrate our features in a compact Gaussian-like space, which is usually beneficial.

In fact, γ and β correspond to the trainable parameters that result in the linear/affine transformation, which is different for all channels.

### Advantages and disadvantages of using batch normalization

Advantages:
- BN accelerates the training of deep neural networks.
- For every input mini-batch we calculate different statistics. This introduces some sort of regularization.
- Every mini-batch has a different mini-distribution. We call the change between these mini-distributions Internal Covariate Shift. BN was thought to eliminate this phenomenon. Later, Santurkar et al. show that this is not exactly the case why BN works.
- BN also has a beneficial effect on the gradient flow through the network.

Disadvantages:
- Inaccurate estimation of batch statistics with small batch size.
- Problems when batch size is varying (training vs inference, pretraining vs fine tuning).

## Synchronized Batch Normalization (2018)

As the training scale went big, some adjustments to BN were necessary. Synchronized BN indicates that the mean and standard-deviation are communicated across workers (GPUs, TPUs etc).

## Layer normalization (2016)

In BN, the statistics are computed across the batch and the spatial dims. In contrast, in Layer Normalization (LN), the statistics (mean and variance) are computed across all channels and spatial dims. Thus, the statistics are independent of the batch.

And to be honest nobody spoke about it until the Transformers paper came out.

## Instance Normalization (2016)

Instance Normalization (IN) is computed only across the features' spatial dimensions. So it is independent for each channel and sample.

Surprisingly, the affine parameters in IN can completely change the style of the output image.

## Weight normalization (2016)

In Weight Normalization instead of normalizing the activations x directly, we normalize the weights:

w = (g/||v||) v

## Adaptive Instance Normalization (2017)

AdaIN receives an input image x (content) and a style input y, and simply aligns the channel-wise mean and variance of x to match those of y:

AdaIN(x,y) = σ(y)((x - μ(x))/σ(x)) + μ(y)

## Group normalization (2018)

Group normalization (GN) divides the channels into groups and computes the first-order statistics within each group. GN's computation is independent of batch sizes.

For groups=number of channels we get instance normalization, while for groups=1 the method is reduced to layer normalization.

## Weight Standardization (2019)

Weight Standardization is a natural evolution of Weight Normalization. Different from standard methods that focus on activations, WS considers the smoothing effects of weights.

WS controls the first-order statistics of the weights of each output channel individually. GN + WS have been successfully applied with tremendous success in transfer learning (BiT).

## SPADE (2019)

SPADE (Spatially-Adaptive Normalization) uses segmentation maps to produce spatially varying γ and β tensors via convolutions, enabling semantic image synthesis.

## Conclusion

We presented the most famous in-layer normalization methods for training very deep models.
