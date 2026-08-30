Source URL: https://huggingface.co/blog/Arm/neural-super-sampling
Title: Neural Super Sampling is here!

# Neural Super Sampling is here!

Enterprise Article. Published August 12, 2025

EricSondhi, Will Lord (Arm)

Neural Super Sampling (NSS), a next-generation AI-powered upscaling solution from Arm, is released for graphics and gaming developers to start experimenting with today.

## Elevated by Machine Learning

NSS is designed for real-time performance on future mobile devices with Arm Neural Technology. Latency depends on implementation factors such as GPU configuration, resolution, and use case. In Arm's "Enchanted Castle" demo, NSS reduced GPU workload by 50 percent: the model rendered at 540p and upscaled to 1080p in 4ms in a sustained performance setup.

## The NSS Model

Neural Super Sampling is a parameter prediction model for real-time temporal super sampling, developed by Arm and optimized for execution on Neural Accelerators (NX) in mobile GPUs. It enables high-resolution rendering at lower compute cost by reconstructing high-quality output frames from low-resolution temporal inputs. NSS is particularly suited for mobile gaming, XR, and other power-constrained graphics use cases.

## How the Model Was Trained

Arm released the Neural Graphics Dataset: a collection of reference images and image sequences, along with corresponding motion, depth, and other data required to train, validate, and test neural super sampling algorithms. The current version includes a limited set of data to demonstrate the NSS model development flow, not yet a comprehensive dataset for complete model (re)training; a future "Neural Graphics Model Gym" will provide tools to capture and convert content for training and retraining.

## Getting Started

NSS has been integrated into Unreal Engine via two plugins: the NSS Plugin for Unreal Engine, and the Unreal NNE Plugin for ML extensions for Vulkan. Quickstart guides are available for both the Vulkan ML extensions path and the Unreal Engine integration path.
