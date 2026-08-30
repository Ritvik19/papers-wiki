Source URL: https://huggingface.co/blog/mmdp
Title: Efficient MultiModal Data Pipeline

# Efficient MultiModal Data Pipeline

Published July 8, 2025

Aritra Roy Gosthipaty, Luis (lusxvr), Andres Marafioti, Sergio Paniego, Pedro Cuenca

You've got everything ready: data, model, a beefy GPU setup. You hit "run" and wait, and wait some more. The GPUs are barely breaking a sweat while the wallet gets lighter by the hour. After some detective work on the nanoVLM project, the team discovered the real culprit wasn't the model or hardware, it was the data pipeline being incredibly wasteful:

- Idle GPUs: the model was literally waiting around for data to show up.
- Padding hell: every batch was stuffed with useless padding tokens that contributed nothing to training.

This post builds an efficient pipeline in five stages, adding or removing from the previous step each time and commenting on what went right and what did not.

## Stage 0: Preparation

A separate repository (`ariG23498/mmdp`) laser-focused on the data pipeline was created, easier to follow than reading the code once integrated into the nanoVLM repository, and useful for bootstrapping other data pipelines.

## Stage 1: Visualizing the Dataset

Before optimizing anything, the team needed to understand what they were working with: a multimodal dataset with images, text prompts, and responses. Getting familiar with the training data (via a script that shows a random sample) is crucial for success.

## Stage 2: Naive Padding

The first training attempt used the obvious, very frequent approach: tokenize everything, find the longest sequence in each batch, pad everything else to match. The results were painful: roughly 60% of each batch was wasted on empty padding tokens, i.e. the GPU processing absolutely nothing while still being paid for.

## Stage 3: Constrained Padding

The next move was to set a global maximum length and stick to it; samples that were too long were dropped (the batch ends up one sample smaller due to this filtering). This helped, but batches were still padded to the same fixed length regardless of actual content: better than before, but still wasteful.

## Stage 4: Packing Smarter with Knapsacks

The team rethought batching entirely as a knapsack problem: pack a training batch (the "backpack," with a maximum token limit `max_length`) with as many sequences (each an "item," with "weight" equal to token count) as possible without exceeding the limit, minimizing wasted space. They first tested with a toy dataset (integers 1-25 as sequence lengths) to avoid the complexity of images and text.

To support dynamic batching, the team built an iterable-style dataset (subclassing `torch.utils.data.IterableDataset`) that generates batches on the fly and shards data across workers, plus a producer-consumer pattern using Python queues so the packing thread and the main thread overlap.

Two packing strategies were compared. Greedy packing walks through the data sequentially, adding items to a pack until full, then starting a new one; it is fast but leaves gaps, especially in later batches. Bin-packing (specifically First Fit Decreasing) sorts sequences longest-first and fits each into the first pack with room, starting a new pack only if none fits; this produces noticeably tighter batches with less wasted space, "like playing Tetris" with the data.

## Stage 5: Knapsacks for Multimodal Data

Applying knapsack packing to the real multimodal dataset (images, prompts, responses) means packing efficiently while respecting both token limits and image budgets; image budgeting balances the number of images per sample so no GPU processes disproportionately more images than another. A new `ConstantLengthDataset` class handles this: it reads samples, filters out ones that are too long or have too many images, packs samples into batches using a greedy knapsack strategy that balances token and image count, and pads the final batches to a fixed length with much less padding than before.

The balanced knapsack strategy for the data pipeline is adapted from NVIDIA's "Eagle 2: Building Post-Training Data Strategies from Scratch for Frontier Vision-Language Models" paper.

## Conclusion

What started as a "why is training so slow?" investigation led to a full rethink of multimodal data handling. Key lessons:

- Padding everything to the longest sequence is a reasonable first approach, but wasteful.
- Think of batching as a packing problem.
- Consider all constraints (text length, image memory, etc.).
- Test with toy data first to validate the approach.

Further reading: the nanoVLM blog post, the nanoVLM GitHub repository, and this pipeline's code (`ariG23498/mmdp`).

### Community follow-up

A commenter (tonywu71) suggested shuffling the original dataset before visualizing greedy packing (since an unshuffled dataset makes greedy packing look artificially clean), and pointed to NVIDIA's EAGLE 2 paper (figures 9-10) showing that balancing the number of examples per batch, not just the number of images, also helps training. The blog post's author acknowledged the point and invited a documented contribution.
