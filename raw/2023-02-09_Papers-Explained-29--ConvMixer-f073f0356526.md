# Papers Explained 29: ConvMixer

Papers Explained 29: ConvMixer

Papers Explained 29: ConvMixer

ConvMixer is similar to the Vision Transformer (and MLP-Mixer) in many respects: it directly operates on patches, it maintains an…

Papers Explained 29: ConvMixer

ConvMixer is similar to the Vision Transformer (and MLP-Mixer) in many respects: it directly operates on patches, it maintains an equal-resolution-and-size representation throughout all layers, it does no downsampling of the representation at successive layers, and it separates “channel-wise mixing” from the “spatial mixing” of information. But unlike the Vision Transformer and MLP-Mixer, ConvMixer does all these operations via only standard convolutions.

ConvMixer consists of a patch embedding layer followed by repeated applications of a simple fully-convolutional block. We maintain the spatial structure of the patch embeddings. Patch embeddings with patch size p and embedding dimension h can be implemented as convolution with cin input channels, h output channels, kernel size p, and stride p:

The ConvMixer block itself consists of depthwise convolution (i.e., grouped convolution with groups equal to the number of channels, h) followed by pointwise (i.e., kernel size 1 × 1) convolution. ConvMixers work best with unusually large kernel sizes for the depthwise convolution. Each of the convolutions is followed by an activation and post-activation BatchNorm:

After many applications of this block, we perform global pooling to get a feature vector of size h, which we pass to a softmax classifier.

ConvMixers are evaluated on ImageNet-1k classification data

Recommended Reading: [Papers Explained Review 01: Convolutional Neural Networks]

Paper

Patches Are All You Need? 2201.09792

Implementation

ConvMixer

Hungry for more insights?

Don’t miss out on exploring other fascinating threads in this series. Simply click here and uncover the state-of-the-art research!

Do Subscribe for weekly updates!!

By Ritvik Rastogi on February 9, 2023.

Canonical link

Exported from Medium on May 4, 2026.
