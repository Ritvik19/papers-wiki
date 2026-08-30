# Papers Explained Review 03: RCNNs

Papers Explained Review 03: RCNNs

Papers Explained Review 03: RCNNs

A Literature Review of Region-Based Convolutional Neural Networks.

Papers Explained Review 03: RCNNs

Table of Contents

RCNN (Nov 2013)
Fast RCNN (Apr 2015)
Faster RCNN (Jun 2015)
Mask RCNN (Mar 2017)
Cascade RCNN and Cascade Mask RCNN (Dec 2017)

RCNN

Rich feature hierarchies for accurate object detection and semantic segmentation

Architecture

RCCN consists of three modules:

The first generates category-independent region proposals. These proposals define the set of candidate detections available to our detector.
The second module is a large convolutional neural network that extracts a fixed-length feature vector from each region.
The third module is a set of class specific linear SVMs.

While R-CNN is agnostic to the particular region proposal method, Selective search is the most commonly used method to enable a controlled comparison with prior detection work.

Implementation

At test time, we run selective search on the images to extract around 2000 region proposals. We warp each proposal and forward propagate it through the CNN in order to compute features. Then, for each class, we score each extracted feature vector using the SVM trained for that class. Given all scored regions in an image, we apply a greedy non-maximum suppression (for each class independently) that rejects a region if it has an intersection over union (IoU) overlap with a higher scoring selected region larger than a learned threshold.

Back to Top

Fast RCNN

Fast R-CNN

Limitations of RCNN and SPPnets

Training is a multi-stage pipeline: R-CNN first finetunes a ConvNet on object proposals using log loss. Then, it fits SVMs to ConvNet features. These SVMs act as object detectors, replacing the softmax classifier learnt by fine-tuning. In the third training stage, bounding-box regressors are learned.
Training is expensive in space and time: For SVM and bounding-box regressor training, features are extracted from each object proposal in each image and written to disk. These features require hundreds of gigabytes of storage.
Object detection is slow: At test-time, features are extracted from each object proposal in each test image.

R-CNN is slow because it performs a ConvNet forward pass for each object proposal, without sharing computation.

Spatial pyramid pooling networks (SPPnets) were proposed to speed up R-CNN by sharing computation. The SPPnet method computes a convolutional feature map for the entire input image and then classifies each object proposal using a feature vector extracted from the shared feature map.

Fast RCNN Architecture

A Fast R-CNN network takes as input an entire image and a set of object proposals. The network first processes the whole image with several convolutional (conv) and max pooling layers to produce a conv feature map.

Then, for each object proposal a region of interest (RoI) pooling layer extracts a fixed-length feature vector from the feature map.

Each feature vector is fed into a sequence of fully connected (fc) layers that finally branch into two sibling output layers: one that produces softmax probability estimates over K object classes plus a catch-all “background” class and another layer that outputs four real-valued numbers for each of the K object classes. Each set of 4 values encodes refined bounding-box positions for one of the K classes.

RoI Pooling Layer

The RoI pooling layer uses max pooling to convert the features inside any valid region of interest into a small feature map with a fixed spatial extent of H × W (e.g., 7 × 7), where H and W are layer hyper-parameters that are independent of any particular RoI.

Each RoI is defined by a four-tuple (r, c, h, w) that specifies its top-left corner (r, c) and its height and width (h, w).

RoI max pooling works by dividing the h × w RoI window into an H × W grid of sub-windows of approximate size h/H × w/W and then max-pooling the values in each sub-window into the corresponding output grid cell. Pooling is applied independently to each feature map channel, as in standard max pooling.

Initializing from pre-trained networks

When a pre-trained network initializes a Fast R-CNN network, it undergoes three transformations:

The last max pooling layer is replaced by a RoI pooling layer that is configured by setting H and W to be compatible with the net’s first fully connected layer (e.g., H = W = 7 for VGG16).
The network’s last fully connected layer and softmax are replaced with the two sibling layers (a fully connected layer and softmax over K + 1 categories and category-specific bounding-box regressors).
The network is modified to take two data inputs: a list of images and a list of RoIs in those images.

Back to Top

Faster RCNN

Faster R-CNN: Towards Real-Time Object Detection with Region Proposal Networks

Faster R-CNN, is composed of two modules.
The first module is a deep fully convolutional network that proposes regions, and the second module is the Fast R-CNN detector that uses the proposed regions. The entire system is a single, unified network for object detection.

Region Proposal Network

To generate region proposals, we slide a small network over the convolutional feature map output by the last shared convolutional layer. This small network takes as input an n × n spatial window of the input convolutional feature map. Each sliding window is mapped to a lower-dimensional feature.

This feature is fed into two sibling fullyconnected layers — a box-regression layer (reg) and a box-classification layer (cls).

Anchors

At each sliding-window location, we simultaneously predict multiple region proposals, where the number of maximum possible proposals for each location is denoted as k. So the reg layer has 4k outputs encoding the coordinates of k boxes, and the cls layer outputs 2k scores that estimate probability of object or not object for each proposal. The k proposals are parameterized relative to k reference boxes, which we call anchors. An anchor is centered at the sliding window in question, and is associated with a scale and aspect ratio (Figure 3, left). By default we use 3 scales and 3 aspect ratios, yielding k = 9 anchors at each sliding position. For a convolutional feature map of a size W × H (typically ∼2,400), there are W H k anchors in total.

Loss Function
For training RPNs, we assign a binary class label (of being an object or not) to each anchor. We assign a positive label to two kinds of anchors:

The anchor/anchors with the highest Intersection-overUnion (IoU) overlap with a ground-truth box
An anchor that has an IoU overlap higher than 0.7 with any ground-truth box.

Note that a single ground-truth box may assign positive labels to multiple anchors.

Sharing Features for RPN and Fast R-CNN
As per the experiments mentioned in the original paper, we first train RPN, and use the proposals to train Fast R-CNN. The network tuned by Fast R-CNN is then used to initialize RPN, and this process is iterated.

Back to Top

Mask RCNN

Mask R-CNN

Faster R-CNN consists of two stages. The first stage, called a Region Proposal Network (RPN), proposes candidate object bounding boxes. The second stage, which is in essence Fast R-CNN, extracts features using RoIPool from each candidate box and performs classification and bounding-box regression.

Mask R-CNN adopts the same two-stage procedure, with an identical first stage (which is RPN). In the second stage, in parallel to predicting the class and box offset, Mask R-CNN also outputs a binary mask for each RoI.

Formally, during training, we define a multi-task loss on each sampled RoI as L = Lcls + Lbox + Lmask.

The mask branch has a Km² — dimensional output for each RoI, which encodes K binary masks of resolution m × m, one for each of the K classes. To this we apply a per-pixel sigmoid, and define Lmask as the average binary cross-entropy loss. For an RoI associated with ground-truth class k, Lmask is only defined on the k-th mask (other mask outputs do not contribute to the loss).

Back to Top

Casecade RCNN and Cascade Mask RCNN

Cascade R-CNN: Delving into High Quality Object Detection

Cascade RCNN is an extension of the R-CNN framework, with multiple detection stages arranged in a cascade. The primary motivation behind Cascade R-CNN is to address the issue of overfitting during training and the mismatch between optimal IoUs for detectors and input samples during inference.

In Cascade R-CNN, the architecture consists of multiple detector stages, each building upon the outputs of the previous stage. The detectors in deeper stages of the cascade become more selective against close false positives. This is achieved by adjusting bounding boxes rather than mining hard negatives. The output of each stage is used to train the next, and the sequential training procedure adapts the detectors to increasingly higher IoUs. This mitigates the overfitting problem and leads to effectively trained detectors. During inference, the cascade procedure is applied to progressively refine hypotheses, resulting in improved matches with the increasing detector quality at each stage.

Cascade Mask R-CNN, on the other hand, is an extension of Cascade R-CNN that adds instance segmentation capability to the architecture. This means that in addition to detecting objects, the model can also segment and classify each pixel within the detected objects. To achieve this, a mask head is introduced into the cascade architecture.

Back to Top

References

Rich feature hierarchies for accurate object detection and semantic segmentation
Fast R-CNN
Faster R-CNN: Towards Real-Time Object Detection with Region Proposal Networks
Mask R-CNN
Cascade R-CNN: Delving into High Quality Object Detection

Hungry for more insights?

Don’t miss out on exploring other fascinating threads in this series. Simply click here and uncover the state-of-the-art research!

By Ritvik Rastogi on February 7, 2023.

Canonical link

Exported from Medium on May 4, 2026.
