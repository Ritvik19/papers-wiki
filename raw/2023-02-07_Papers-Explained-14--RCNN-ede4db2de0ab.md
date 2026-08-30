# Papers Explained 14: RCNN

Papers Explained 14: RCNN

Papers Explained 14: RCNN

Architecture

Papers Explained 14: RCNN

Architecture

RCCN consists of three modules:

The first generates category-independent region proposals. These proposals define the set of candidate detections available to our detector.
The second module is a large convolutional neural network that extracts a fixed-length feature vector from each region.
The third module is a set of class specific linear SVMs.

While R-CNN is agnostic to the particular region proposal method, Selective search is the most commonly used method to enable a controlled comparison with prior detection work.

Implementation

At test time, selective search is conducted on the images to extract around 2000 region proposals. Each proposal is warped and then forwarded through the CNN to compute features. Following this, for each class, the score of each extracted feature vector is assessed using the SVM trained for that specific class. With all scored regions within an image, a greedy non-maximum suppression is applied (independently for each class), which discards a region if it has an intersection over union (IoU) overlap with a higher-scoring selected region that is larger than a learned threshold.

Paper

Rich feature hierarchies for accurate object detection and semantic segmentation 1311.2524

Hungry for more insights?

Don’t miss out on exploring other fascinating threads in this series. Simply click here and uncover the state-of-the-art research!

Do Subscribe for weekly updates!!

By Ritvik Rastogi on February 7, 2023.

Canonical link

Exported from Medium on May 4, 2026.
