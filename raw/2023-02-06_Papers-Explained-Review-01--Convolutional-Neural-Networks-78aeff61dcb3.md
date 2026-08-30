# Papers Explained Review 01: Convolutional Neural Networks

Papers Explained Review 01: Convolutional Neural Networks

Papers Explained Review 01: Convolutional Neural Networks

A Literature Review of Convolutional Neural Networks

Papers Explained Review 01: Convolutional Neural Networks

Table of Contents

Lenet (1998)
AlexNet (2012)
VGG (2014)
InceptionNet (2014)
InceptionNetV2 and InceptionNetV3 (2015)
ResNet (2015)
InceptionNetV4 and InceptionResNet (2016)
DenseNet (2016)
Xception (2016)
ResNext (2016)
MobileNetV1 (2017)
MobileNetV2 (2018)
MobileNetV3 (2019)
EfficientNet (2019)

Lenet

Gradient-Based Learning Applied to Document Recognition

LeNet is a convolutional neural network architecture that was developed by Yann LeCun in the late 1980s and early 1990s. It is considered a pioneering work in the field of deep learning and is particularly well-known for its use in the recognition of handwritten digits.

LeNet is a relatively simple architecture that consists of multiple layers of convolutional, pooling, and fully connected layers. The convolutional layers are responsible for detecting features in the input image, while the pooling layers are used for down-sampling and reducing the spatial dimensions of the feature maps. The fully connected layers are used for classification.

LeNet was one of the first architectures to demonstrate the effectiveness of convolutional neural networks for image classification tasks. It was also one of the first architectures to use the concept of weight sharing, which is now a common technique used in modern CNNs.

LeNet architecture has inspired many other architectures like AlexNet, VGGNet and GoogleNet.

Back to Top

AlexNet

ImageNet Classification with Deep Convolutional Neural Networks

AlexNet is a convolutional neural network (CNN) architecture that was developed by Alex Krizhevsky, Ilya Sutskever, and Geoffrey Hinton in 2012. It was the winning model of the ImageNet Large Scale Visual Recognition Challenge (ILSVRC) in 2012, which is a highly competitive image classification competition.

AlexNet architecture is similar to LeNet architecture but has several important differences. The architecture of AlexNet is deeper than LeNet, it has 8 layers with 5 convolutional layers, 3 fully connected layers and a final 1000-way softmax classifier.

One of the significant innovations of AlexNet is the use of ReLU (Rectified Linear Unit) as the activation function in the convolutional layers. This non-linear activation function allows the network to learn more complex features and improve the accuracy of the model.

Additionally, AlexNet also used a technique called dropout, which randomly drops out some neurons during training to prevent overfitting.

The AlexNet architecture was a breakthrough in the field of CNNs and deep learning, it was the first architecture that showed the effectiveness of deep CNNs for image classification tasks, by beating the previous state-of-the-art by a significant margin. It also inspired many other architectures like VGGNet, GoogleNet, ResNet, and many more. AlexNet is widely used as a benchmark for other image classification architectures and it is also commonly used as a pre-trained model for transfer learning tasks.

Back to Top

VGG

Very Deep Convolutional Networks for Large-Scale Image Recognition

The VGGNet is a convolutional neural network (CNN) architecture that was developed by the Visual Geometry Group (VGG) at the University of Oxford in 2014. It is a deep architecture that is characterized by its use of a very large number of convolutional layers, typically between 16 and 19 layers deep.

The VGGNet architecture is made up of a series of convolutional layers, followed by max-pooling layers, and then several fully-connected layers. All the convolutional layers use the same filter size of 3x3 and use a stride of 1, this results in a very deep and narrow architecture which allows the model to learn more fine-grained features.

One of the key innovations of VGGNet is the use of very small convolutional filters, which allows the network to learn more fine-grained features, and also the use of a very large number of filters in each layer, which allows the network to learn more complex features. It also introduced the idea of stacking multiple convolutional layers with small filters, which is now a common practice in many CNN architectures.

This design decreases the number of parameters. Specifically, you need 3(3²)C² = 27C² weights, compared to a 7×7 conv. layer that would require 1(7²)C² = 49C² parameters (81% more).

Intuitively, it can be regarded as a regularisation on the 7×7 conv. filters, constricting them to have a 3x3 non-linear decomposition.

The VGGNet architecture was able to achieve state-of-the-art results on the ImageNet Large Scale Visual Recognition Challenge (ILSVRC) in 2014, and it also was used as a backbone for many image classification tasks and object detection tasks. The VGGNet architecture is also commonly used as a pre-trained model for transfer learning tasks, it is also known for its ability to extract features from images which are useful for other tasks like image captioning, style transfer and many more.

Back to Top

InceptionNet

Going Deeper with Convolutions

The Inception Net architecture is a convolutional neural network (CNN) architecture developed by Google in 2014. It is also known as GoogLeNet and it was the winner of the 2014 ImageNet Large Scale Visual Recognition Challenge (ILSVRC).

The Inception Net architecture is characterized by its use of multiple parallel convolutional layers, known as Inception Modules, which are designed to recognize different features at multiple scales. This allows the network to learn both high-level and low-level features, and the architecture can be very deep, with tens of layers.

Each Inception Module consists of multiple parallel branches with different filter sizes, and each branch performs a convolution operation and then a pooling operation. The outputs from each branch are then concatenated and passed through a 1x1 convolutional layer, which reduces the number of channels, before being fed into the next layer.

In addition to its parallel branches, the Inception Net architecture also uses global average pooling instead of traditional fully connected layers, which reduces the number of parameters and helps prevent overfitting.

Needless to say, it is a pretty deep classifier. As with any very deep network, it is subject to the vanishing gradient problem.

To prevent the middle part of the network from “dying out”, the authors introduced two auxiliary classifiers. They essentially applied softmax to the outputs of two of the inception modules, and computed an auxiliary loss over the same labels. The total loss function is a weighted sum of the auxiliary loss and the real loss. Weight value used in the paper was 0.3 for each auxiliary loss.

In summary, the Inception Net architecture’s significance in the field of Convolutional Neural Networks is due to its innovative use of parallel branches to recognize features at multiple scales, which allows the network to learn both high-level and low-level features, and its use of global average pooling, which reduces the number of parameters and helps prevent overfitting.

Back to Top

InceptionNetV2 and InceptionNetV3

Rethinking the Inception Architecture for Computer Vision

Inception v2 and Inception v3 were presented in the same paper. The authors proposed a number of upgrades which increased the accuracy and reduced the computational complexity. Inception v2 explores the following:

Factorize 5x5 convolution to two 3x3 convolution operations to improve computational speed.
Moreover, they factorize convolutions of filter size nxn to a combination of 1xn and nx1 convolutions. This method was found to be 33% more cheaper than the single 3x3 convolution.
The filter banks in the module were expanded (made wider instead of deeper) to remove the representational bottleneck. If the module was made deeper instead, there would be excessive reduction in dimensions, and hence loss of information

Inception Net v3 incorporated all of the above upgrades stated for Inception v2, and in addition used the following:

RMSProp Optimizer.
Factorized 7x7 convolutions.
BatchNorm in the Auxillary Classifiers.
Label Smoothing (A type of regularizing component added to the loss formula that prevents the network from becoming too confident about a class. Prevents over fitting).

Back to Top

ResNet

Deep Residual Learning for Image Recognition

ResNet (Residual Network) is a convolutional neural network (CNN) architecture developed by Microsoft in 2015. It was the winner of the 2015 ImageNet Large Scale Visual Recognition Challenge (ILSVRC) and is considered one of the most important developments in the field of deep learning.

The ResNet architecture is characterized by its use of residual connections, which are shortcuts that bypass one or more layers in the network. These residual connections help to alleviate the problem of vanishing gradients, which can occur when training very deep networks.

ResNet has had a significant impact on the field of deep learning, as it demonstrated that it is possible to train very deep networks that can achieve high accuracy on a variety of tasks. ResNet has also been used as a pre-trained model for transfer learning tasks, and has been used as a building block for other architectures, such as ResNeXt and DenseNet.

Back to Top

InceptionNetV4 and InceptionResNet

Inception-v4, Inception-ResNet and the Impact of Residual Connections on Learning

Inception v4 and Inception-ResNet were introduced in the same paper.

For Inception v4 the idea was to make the modules more uniform and to simplify some of the modules. This can enable us to boost performance by adding more of these uniform modules.

The stem of Inception v4 was modified. The stem, refers to the initial set of operations performed before introducing the Inception blocks.

Three simplified inception modules were introduced:

Inception v4 introduced specialized “Reduction Blocks” which are used to change the width and height of the grid. The earlier versions didn’t explicitly have reduction blocks, but the functionality was implemented.

Inspired by the performance of the ResNet, a hybrid inception module was proposed. There are two sub-versions of Inception ResNet, namely v1 and v2.

Inception-ResNet v1 has a computational cost that is similar to that of Inception v3.
Inception-ResNet v2 has a computational cost that is similar to that of Inception v4.
Both sub-versions have the same structure for the inception modules and the reduction blocks. Only difference is the hyper-parameter settings.

The idea is to introduce residual connections that add the output of the convolution operation of the inception module, to the input.

For residual addition to work, the input and output after convolution must have the same dimensions. Hence, we use 1x1 convolutions after the original convolutions, to match the depth sizes.

The pooling operation inside the main inception modules were replaced in favor of the residual connections.

Networks with residual units deeper in the architecture caused the network to “die” if the number of filters exceeded 1000. Hence, to increase stability, the authors scaled the residual activations by a value around 0.1 to 0.3.

The original paper didn’t use BatchNorm after summation to train the model on a single GPU (To fit the entire model on a single GPU).

It was found that Inception-ResNet models were able to achieve higher accuracies at a lower epoch.

The final network layout for both Inception v4 and Inception-ResNet are as follows:

Back to Top

DenseNet

Densely Connected Convolutional Networks

DenseNet is a convolutional neural network (CNN) architecture developed in 2017. It is characterized by its use of dense connections.

In traditional CNNs, each layer only receives input from the previous layer, but in DenseNet, each layer receives input from all the previous layers. This creates a dense network of connections between the layers, which allows the network to learn more diverse features and reduces the risk of vanishing gradients. Additionally, the dense connections help to alleviate the vanishing gradients problem, which is a common issue in deep neural networks.

Another significant aspect of the DenseNet architecture is its use of transition layers, which reduce the spatial resolution of the feature maps between dense blocks. This allows the network to effectively balance between the computational cost and the accuracy of the network.

Back to Top

Xception

Xception: Deep Learning with Depthwise Separable Convolutions

The Xception (Extreme Inception) architecture is a convolutional neural network (CNN) architecture developed by Google in 2017. It is designed as an extension of the Inception architecture.

Xception is based on InceptionV3 but instead of using inception modules, it uses depthwise separable convolutions. As results, it’s efficient and it performs much better with the same number of parameters as Inception V3.

Depthwise separable convolutions, also called depthwise convolutions perform independently over each channel of the input image, concatenate and apply 1x1 convolution(also called pointwise convolution) to the results. It’s like learning the spatial features of each image channel before mixing their output channels together with 1x1 convolutions.

Back to Top

ResNext

Aggregated Residual Transformations for Deep Neural Networks

ResNeXt (Residual Network with Extreme Optimization) is a convolutional neural network (CNN) architecture developed by Facebook AI Research in 2016. It builds on the success of the ResNet architecture and is designed for image classification.

The ResNeXt architecture introduces the concept of grouped convolutions, where the filters in a convolutional layer are divided into multiple groups. This allows the network to learn more diverse features and improves its performance. The ResNeXt architecture also makes use of residual connections, similar to the ResNet architecture, which allows the network to learn residual representations and reduces the risk of vanishing gradients.

Grouped convolutions are special kind of convolutions where the input and output channels are divided into parallel groups, and convolutions are separately computed within each group and the results are concatenated. If the number of groups are equal to the number of channels, such grouped convolutions are called depth-wise convolution. A depth-wise convolution followed by 1x1 or pointwise convolution is called depth-wise separable convolution.

Another significant aspect of the ResNeXt architecture is its use of cardinality, which is a measure of the number of grouped convolutions in the network. The ResNeXt architecture has a high cardinality, which allows it to learn more diverse features and improves its accuracy.

Back to Top

MobileNetV1

MobileNets: Efficient Convolutional Neural Networks for Mobile Vision Applications

MobileNetv1 is a convolutional neural network (CNN) architecture developed by Google in 2017. It is designed for mobile and embedded devices, where computational resources are limited. MobileNetv1 is characterized by its use of depthwise separable convolutions and its compact design.

In traditional CNNs, each convolution layer uses a 3x3 filter to learn the features from the input image. This filter is applied to each channel of the input feature map, and the output feature map has the same number of channels as the input feature map. MobileNetv1 uses a different approach called depthwise separable convolutions, which separates the computation into two parts: a depthwise convolution and a pointwise convolution. The depthwise convolution applies a 3x3 filter to each channel of the input feature map, and the pointwise convolution combines the results from all the channels.

This allows MobileNetv1 to reduce the number of parameters and computation required, while still retaining the ability to learn complex features. Additionally, the compact design of MobileNetv1 allows it to be deployed on mobile and embedded devices, where computational resources are limited.

Back to Top

MobileNetV2

MobileNetV2: Inverted Residuals and Linear Bottlenecks

MobileNetv2 is a convolutional neural network (CNN) architecture developed by Google in 2018. It is designed for mobile and embedded devices, where computational resources are limited. MobileNetv2 builds upon the MobileNetv1 architecture and is characterized by its use of inverted residuals and linear bottlenecks.

MobileNetv2 uses the concept of inverted residuals, where a residual block is used to connect the input and output of the layer, and the computation is performed on the residual. The inverted residual block contains a pointwise convolution, which is used to increase the number of channels, followed by a depthwise convolution, which is used to learn the features, and a linear bottleneck, which is used to reduce the number of channels and reduce computation.

This design allows MobileNetv2 to achieve a good balance between accuracy and computational cost. Additionally, the use of linear bottlenecks helps to reduce the number of parameters in the network, which is important for deployment on mobile and embedded devices where memory is limited.

Back to Top

MobileNetV3

Searching for MobileNetV3

The main contribution of MobileNetV3 is the use of AutoML to find the best possible neural network architecture for a given problem. This contrast with the hand-crafted design of previous versions of the architecture. Specifically, MobileNetV3 leverages two AutoML techniques: MnasNet and NetAdapt. MobileNetV3 first searches for a coarse architecture using MnasNet, which uses reinforcement learning to select the optimal configuration from a discrete set of choices. After that, the model fine-tunes the architecture using NetAdapt, a complementary technique that trims under-utilized activation channels in small decrements.

Another novel idea of MobileNetV3 is the incorporation of an squeeze-and-excitation block into the core architecture. The core idea of the squeeze-and-excitation blocks is to improve the quality of representations produced by a network by explicitly modelling the interdependencies between the channels of its convolutional features.

An interesting optimization of MobileNetV3 was the redesign of some of the expensive layers in the architecture. Some of the layers in MobileNetV2 were foundational to the accuracy of the models but also introduced concerning levels of latency. By incorporating some basic optimizations, MobileNetV3 was able to remove three expensive layers of its predecessor architecture without sacrificing accuracy.

Back to Top

EfficientNet

EfficientNet: Rethinking Model Scaling for Convolutional Neural Networks

EfficientNet is a convolutional neural network (CNN) architecture developed by Google in 2020. It is designed for image classification and is characterized by its use of efficient building blocks and model scaling.

EfficientNet uses a compound scaling method to scale the network in terms of its depth, width, and resolution. This allows the network to achieve a high accuracy with a relatively low computational cost. The network also makes use of efficient building blocks, such as inverted residuals and linear bottlenecks, which help to reduce the computational cost while still allowing the network to learn complex features.

The compound scaling method is based on the idea of balancing dimensions of width, depth, and resolution by scaling with a constant ratio. The equations below show how it is achieved mathematically:

such that:

Another significant aspect of the EfficientNet architecture is its use of automated neural architecture search (NAS), which is a method for automating the design of neural networks. The EfficientNet architecture was designed using NAS, which allowed the network to be optimized for both accuracy and computational efficiency.

Back to Top

References

Gradient-Based Learning Applied to Document Recognition
ImageNet Classification with Deep Convolutional Neural Networks
Very Deep Convolutional Networks for Large-Scale Image Recognition
Going Deeper with Convolutions
Rethinking the Inception Architecture for Computer Vision
Deep Residual Learning for Image Recognition
Inception-v4, Inception-ResNet and the Impact of Residual Connections on Learning
Aggregated Residual Transformations for Deep Neural Networks
Xception: Deep Learning with Depthwise Separable Convolutions
Densely Connected Convolutional Networks
MobileNets: Efficient Convolutional Neural Networks for Mobile Vision Applications
MobileNetV2: Inverted Residuals and Linear Bottlenecks
Searching for MobileNetV3
EfficientNet: Rethinking Model Scaling for Convolutional Neural Networks

Hungry for more insights?

Don’t miss out on exploring other fascinating threads in this series. Simply click here and uncover the state-of-the-art research!

By Ritvik Rastogi on February 6, 2023.

Canonical link

Exported from Medium on May 4, 2026.
