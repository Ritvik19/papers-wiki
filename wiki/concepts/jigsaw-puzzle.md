# Jigsaw Puzzle Pretext Task

**Type**: concept  
**Tags**: #concept

## Overview

The Jigsaw Puzzle pretext task is a self-supervised visual representation learning method designed to teach neural networks spatial composition, spatial relations, and part-whole structures of objects without manual supervision. Developed by Noroozi & Favaro (2016), the task requires a network to take a set of shuffled patches cropped from an unlabeled image and predict the correct spatial configuration that reconstructs the original image. Solving this requires the model to identify high-level semantic components (e.g., recognizing that a dog's ear goes above its muzzle) rather than focusing on low-level continuous textures.

```
                      Context-Free Network (CFN) Architecture
                      
   Shuffled Patches        Siamese CNN Encoders (Shared Weights)       Classifier
  +---+ +---+ +---+        +-------+
  | 3 | | 7 | | 1 | =====> | CNN 1 | =====+
  +---+ +---+ +---+        +-------+      |
  +---+ +---+ +---+        +-------+      | (Concatenate 9
  | 9 | | 2 | | 5 | =====> | CNN 2 | =====+   feature vectors)
  +---+ +---+ +---+        +-------+      |                     +----+
  +---+ +---+ +---+        +-------+      |                     | FC | ===> Classify
  | 4 | | 8 | | 6 | =====> | CNN 3 | =====+ ==================> |    |      Permutation
  +---+ +---+ +---+        +-------+                            | FC |      out of C
                           (And so on for 9 branches...)        +----+
```

---

## Technical Formulation & Permutation Selection

A naive implementation of a jigsaw solver would task the model with predicting the correct arrangement among all possible spatial permutations of a $3 \times 3$ grid. However, classifying across all permutations:
$$ 9! = 362,880 \text{ classes} $$
presents severe issues: many permutations are visually identical (especially in background patches like blue skies), and the output head size is too large.

### Max-Hamming Distance Selection
To solve this, Noroozi & Favaro select a specific subset of $C$ permutations (typically $C = 100$ or $C = 1000$) that are highly distinct from one another. This selection is formulated as finding a set of permutations $\mathcal{P} = \{p_1, p_2, \dots, p_C\}$ that maximizes the average Hamming distance:
$$ \arg\max_{\mathcal{P}} \sum_{i=1}^C \sum_{j \neq i}^C d_{\text{Hamming}}(p_i, p_j) $$
where $d_{\text{Hamming}}(p_i, p_j)$ is the number of patch positions that differ between permutation $p_i$ and $p_j$. 

By choosing permutations with high Hamming distance, the classification task becomes highly discriminative, and the network is forced to learn major structural changes rather than getting confused by minor positional swaps.

---

## Network Architecture: Context-Free Network (CFN)

The Context-Free Network (CFN) is a weight-sharing **Siamese CNN** architecture:
1. **Patch Extraction**: An input image is divided into a $3 \times 3$ grid. Nine patches ($64 \times 64$ pixels) are cropped from these grid blocks. Crucially, a random crop offset is applied within each block to leave a **gap** of $B$ pixels between patches.
2. **Siamese Processing**: The 9 patches are shuffled randomly according to a permutation index $c$ mapping to $p_c \in \mathcal{P}$. Each of the 9 patches is fed through an independent, identical CNN encoder branch. These branches share all weights.
3. **Feature Concatenation**: The shared CNN yields 9 feature vectors $v_1, v_2, \dots, v_9$. These are concatenated in sequence into a single joint representation vector:
   $$ V = [v_1, v_2, \dots, v_9] $$
4. **Classification Head**: $V$ is passed through fully connected layers to output a probability distribution over the $C$ selected classes:
   $$ P(p_c \mid V) = \text{Softmax}(\text{FC}(V)) $$
   
The model is optimized via cross-entropy loss:
$$ \mathcal{L} = - \sum_{c=1}^C y_c \log P(p_c \mid V) $$

---

## Trivial Shortcuts & Lens Physics Mitigations

Self-supervised visual networks are notorious "cheaters" that will exploit any low-level high-frequency statistical pattern in the data to minimize loss without learning semantic concepts. Noroozi & Favaro identified and mitigated two primary shortcuts:

### 1. Radial Chromatic Aberration
*Physics of the Shortcut:* Cameras rely on physical glass lenses that bend light to focus it on a sensor. Because different wavelengths of light (colors) bend at slightly different angles (refraction variance), light waves do not focus on the exact same focal plane. This creates a radial color shift—specifically a green-to-magenta shift—that increases in intensity further from the optical center of the lens.
*How the Model Cheats:* The model detects this subtle color-fringe gradient. By calculating the direction of the green-magenta color gradient within each patch, the model determines the radial angle of the patch relative to the image's center, reconstructing the grid layout perfectly without looking at the semantic content (e.g. shapes, textures).
*Mitigation:*
- **Color Jittering**: Randomly shifting color channels (luminance/chrominance offsets) to break the radial fringe continuity.
- **Grayscale Conversion**: Converting patches to grayscale with a high probability (e.g., $100\%$ during pretraining) to eliminate color gradients entirely.

### 2. Edge and Texture Continuity (Gap Trick)
*Physics of the Shortcut:* If patches are cropped directly adjacent to one another, pixel intensities, edges, and high-frequency noise will align seamlessly at patch boundaries.
*How the Model Cheats:* The model learns simple edge filters to match the boundary pixels of neighboring patches (acting like a pixel-level puzzle solver), completely bypassing object-level semantics.
*Mitigation:*
- **Random Gaps**: Leave a random gap of $12$ to $24$ pixels between the grid cropping regions. This prevents matching pixel gradients directly across borders, forcing the network to extrapolate semantic features across space.

---

## Appearances

- [[Self-Supervised Representation Learning]] — Covered as a geometric pretext task that teaches a network spatial composition and part-whole relationships across a grid of patches.

## Related

- [[Representation Learning]]
- [[Self-Supervised Representation Learning]]
- [[Exemplar-CNN]]
- [[Unsupervised Learning]]
