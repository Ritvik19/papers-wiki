# Papers Explained 16: Faster RCNN

Papers Explained 16: Faster RCNN

Papers Explained 16: Faster RCNN

Faster R-CNN, is composed of two modules.
The first module is a deep fully convolutional network that proposes regions, and the second…

Papers Explained 16: Faster RCNN

Faster R-CNN, is composed of two modules.
The first module is a deep fully convolutional network that proposes regions, and the second module is the Fast R-CNN detector that uses the proposed regions. The entire system is a single, unified network for object detection.

Region Proposal Network

To generate region proposals, we slide a small network over the convolutional feature map output by the last shared convolutional layer. This small network takes as input an n × n spatial window of the input convolutional feature map. Each sliding window is mapped to a lower-dimensional feature.

This feature is fed into two sibling fullyconnected layers — a box-regression layer (reg) and a box-classification layer (cls).

Anchors

At each sliding-window location, multiple region proposals are simultaneously predicted, where the number of maximum possible proposals for each location is denoted as k. So the reg layer has 4k outputs encoding the coordinates of k boxes, and the cls layer outputs 2k scores that estimate probability of object or not object for each proposal. The k proposals are parameterized relative to k reference boxes, which we call anchors. An anchor is centered at the sliding window in question, and is associated with a scale and aspect ratio (Figure 3, left). By default we use 3 scales and 3 aspect ratios, yielding k = 9 anchors at each sliding position. For a convolutional feature map of a size W × H (typically ∼2,400), there are W H k anchors in total.

Loss Function
For training RPNs, a binary class label (of being an object or not) is assigned to each anchor. A positive label is assigned to two kinds of anchors:

The anchor/anchors with the highest Intersection-overUnion (IoU) overlap with a ground-truth box
An anchor that has an IoU overlap higher than 0.7 with any ground-truth box.

Note that a single ground-truth box may assign positive labels to multiple anchors.

Sharing Features for RPN and Fast R-CNN
As per the experiments mentioned in the original paper, first RPN is trained, and the proposals are used to train Fast R-CNN. The network tuned by Fast R-CNN is then used to initialize RPN, and this process is iterated.

Paper

Faster R-CNN: Towards Real-Time Object Detection with Region Proposal Networks 1506.01497

Hungry for more insights?

Don’t miss out on exploring other fascinating threads in this series. Simply click here and uncover the state-of-the-art research!

Do Subscribe for weekly updates!!

By Ritvik Rastogi on February 7, 2023.

Canonical link

Exported from Medium on May 4, 2026.
