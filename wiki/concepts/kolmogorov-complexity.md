# Kolmogorov Complexity

**Type**: concept  
**Tags**: #concept

## Overview

Kolmogorov complexity K(x) of an object x is the length of the shortest binary program (on a universal Turing machine) capable of generating x. It is the theoretical lower bound for the information content of any object — a measure of how "compressible" or "random" x truly is.

Kolmogorov complexity is **not computable** in general (it is equivalent to the halting problem), so it cannot be used directly. Practical algorithms (gzip, bz2, zstd) approximate it by finding compressed representations that are short but not necessarily optimal.

The related notion of **information distance** between two objects x and y is defined as:

> E(x, y) = max{K(x|y), K(y|x)} = K(xy) − min{K(x), K(y)}

This measures the length of the shortest program to transform x into y (or y into x). [[Normalized Compression Distance]] (NCD) is a normalized, computable approximation of this distance.

## Appearances

- [[Papers Explained: Text Classification with Gzip]] — theoretical grounding for using compression length as an approximation to information content in text similarity.
- [[gzip Predicts Data-dependent Scaling Laws]] — gzip compressibility is used as a practical proxy for Kolmogorov complexity to characterize data complexity and predict scaling law parameters.

## Notes

- Kolmogorov complexity is related to algorithmic information theory and connects to notions of randomness and compressibility in theoretical computer science.
- The incomputability means all practical uses rely on approximation via real compressors.
- A shorter Kolmogorov complexity implies more structure/regularity; a longer one implies near-randomness.

## Related

- [[Normalized Compression Distance]] — the practical, computable approximation of Kolmogorov-based information distance.
- [[k-Nearest Neighbors]] — used together with NCD to build a training-free text classifier.
- [[Scaling Laws]] — the gzip scaling laws paper connects Kolmogorov complexity to neural scaling behavior through compressibility.
