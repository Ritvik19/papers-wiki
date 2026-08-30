# Self-Supervised Representation Learning

**Source**: `raw/2019-11-10-self-supervised/full-article.md`, `raw/2019-11-10-self-supervised/full-article.md`  
**Ingested**: 2026-05-21  
**Tags**: #summary

## Summary

Self-supervised representation learning is a powerful training paradigm that extracts rich semantic features from unlabeled data by constructing supervised pretext tasks. While standard supervised learning is highly effective, it remains severely bottlenecked by the high cost and scaling limits of human annotation. By contrast, self-supervised learning leverages the inherent structure of the data itself to construct pseudo-labels for free, using one subset of the observation to predict another. The primary goal is not the task performance itself, but rather the learned intermediate representation, which should capture high-level semantic and geometric features that transfer cleanly to downstream tasks (e.g. object recognition, video segmentation, or robotic control) with minimal labeled data.

This post catalogs and synthesizes major self-supervised pretext techniques across three primary modalities: image-based, video-based, and control-based systems. Image pretext tasks range from simple pixel distortion invariance (Exemplar-CNN, whole-image rotations) and geometric patch relationships (relative positions, jigsaw shuffles, visual feature arithmetic) to generative reconstruction objectives (context encoders, split-brain autoencoders, and bidirectional GANs). Video pretext tasks exploit the arrow of time, temporal sequence coherency (order validation, odd-one-out selection), and colorization context models to track spatial states robustly. Control pretext tasks apply metric learning to learn state representations invariant to visual noise and viewpoint differences, facilitating reinforcement learning directly in low-dimensional latent spaces.

Ultimately, self-supervised learning bridges the gap between raw unstructured observations and compact, semantic latent states. From early heuristic pretext tasks like predicting image rotation, the field has progressed toward unified information-theoretic objectives (Contrastive Predictive Coding, InfoNCE) and strict bisimulation metrics that capture only the elements of a scene relevant to control dynamics. Across all modalities, combining multiple pretext tasks, using deeper neural backbones, and designing robust data augmentation pipelines are shown to consistently yield superior downstream representation quality.

## Key Claims

- **Labels for Free via Pretext Tasks**: Supervised losses can be formulated directly from unlabeled data by setting up predictive tasks using structural, temporal, or spatial constraints. The performance on the pretext task is secondary; the objective is the high-quality intermediate representation.
- **Geometric and Spatial Inductive Biases**: Tasks like Jigsaw Puzzles, relative patch positions, and image rotation force models to recognize object components (e.g. heads, legs, textures) and their correct spatial configuration, avoiding local pixel-level shortcuts.
- **Shortcut Exploitation (Trivial Solutions)**: Self-supervised models are highly prone to exploiting trivial sensory shortcuts rather than learning semantic concepts. Key examples include "chromatic aberration" (focal length light offsets across color channels used to bypass spatial reasoning) and "video compression artifacts" (frame sequencing shortcuts).
- **Contrastive Mutual Information Optimization**: InfoNCE and Contrastive Predictive Coding (CPC) show that modeling density ratios instead of exact pixel reconstructions prevents representation collapse and scales cleanly while maximizing the mutual information lower bound between context and future views.
- **State Space Learning for Robotics**: Robotic control policies can be trained entirely on real hardware using learned representation metrics (e.g., multi-view metric learning in Grasp2Vec and Time-Contrastive Networks) to represent goals and compute rewards without ground-truth coordinate sensors.

---

## Pretext Formulations and Mathematical Derivations

### 1. Visual Primitives and Feature Counting (Noroozi et al., 2017)
To learn features invariant to scaling and additive across tiles, Noroozi et al. define transformation operators on an image $\mathbf{x} \in \mathbb{R}^{m \times n \times 3}$:
- Downsampling operator $D$: downsample by a factor of 2.
- Tiling operator $T_i$: extract the $i$-th tile from a $2 \times 2$ grid.

The target constraint is that the representation of the downsampled image equals the sum of the representations of its constituent tiles:
$$ \phi(\mathbf{x}) \approx \phi(D \circ \mathbf{x}) \approx \sum_{i=1}^4 \phi(T_i \circ \mathbf{x}) $$

The Mean Squared Error (MSE) loss is augmented with a contrastive term to prevent the trivial representation collapse $\phi(\mathbf{x}) = \mathbf{0}$:
$$ \mathcal{L} = \|\phi(D \circ \mathbf{x}) - \sum_{i=1}^4 \phi(T_i \circ \mathbf{x})\|^2_2 + \max\left(0, M - \|\phi(D \circ \mathbf{y}) - \sum_{i=1}^4 \phi(T_i \circ \mathbf{x})\|^2_2\right) $$
where $\mathbf{y}$ is a different random image and $M$ represents a scalar margin constant.

### 2. Context Encoder Inpainting (Pathak et al., 2016)
A context encoder is trained to fill in dropped pixels using a binary mask $\hat{M}$ (0 for dropped regions, 1 for remaining). The loss combines reconstruction (L2) loss and adversarial loss:
$$ \mathcal{L}(\mathbf{x}) = \mathcal{L}_\text{recon}(\mathbf{x}) + \mathcal{L}_\text{adv}(\mathbf{x}) $$
$$ \mathcal{L}_\text{recon}(\mathbf{x}) = \|(1 - \hat{M}) \odot (\mathbf{x} - F(\hat{M} \odot \mathbf{x})) \|_2^2 $$
$$ \mathcal{L}_\text{adv}(\mathbf{x}) = \max_D \mathbb{E}_{\mathbf{x}} [\log D(\mathbf{x}) + \log(1 - D(F(\hat{M} \odot \mathbf{x})))] $$
where $F$ is the encoder-decoder inpainter and $D$ is the discriminator.

### 3. Bidirectional GAN (BiGAN) (Donahue et al., 2017)
BiGAN trains an encoder $E$ to map input $\mathbf{x}$ to latent $\mathbf{z}$ alongside the standard generator $G$. The discriminator $D$ classifies joint pairs $(\mathbf{x}, \mathbf{z})$ as real $(\mathbf{x}, E(\mathbf{x}))$ or fake $(G(\mathbf{z}), \mathbf{z})$:
$$ \min_{G, E} \max_D V(D, E, G) = \mathbb{E}_{\mathbf{x} \sim p_\mathbf{x}} \left[\mathbb{E}_{\mathbf{z} \sim E(\cdot|\mathbf{x})}[\log D(\mathbf{x}, \mathbf{z})]\right] + \mathbb{E}_{\mathbf{z} \sim p_\mathbf{z}} \left[\mathbb{E}_{\mathbf{x} \sim G(\cdot|\mathbf{z})}[\log(1 - D(\mathbf{x}, \mathbf{z}))]\right] $$

### 4. Contrastive Predictive Coding (CPC) & InfoNCE Loss (van den Oord et al., 2018)
CPC uses an encoder $z_t = g_\text{enc}(x_t)$ and an autoregressive decoder $c_t = g_\text{ar}(z_{\leq t})$. It models a density ratio function to preserve the mutual information $I(x; c)$ without high-cost generative modeling:
$$ f_k(x_{t+k}, c_t) = \exp(z_{t+k}^\top W_k c_t) \propto \frac{p(x_{t+k}|c_t)}{p(x_{t+k})} $$

Given a batch of $N$ samples containing one positive future observation $x_{t+k}$ and $N-1$ negative samples, the InfoNCE loss is:
$$ \mathcal{L}_N = - \mathbb{E}_X \Big[\log \frac{f_k(x_{t+k}, c_t)}{\sum_{i=1}^N f_k (x_i, c_t)}\Big] $$

### 5. Multi-View Robotic Metric Learning (Grasp2Vec & TCN)
Robotic visual tracking and metric learning optimize state embeddings using distance metrics.
- **Triplet Loss** (used in Time-Contrastive Networks):
$$ \mathcal{L}_\text{triplet}(\mathbf{x}^a, \mathbf{x}^p, \mathbf{x}^n) = \max(0, \|\phi(\mathbf{x}^a) - \phi(\mathbf{x}^p) \|_2^2 - \|\phi(\mathbf{x}^a) - \phi(\mathbf{x}^n) \|_2^2 + M) $$
where $\mathbf{x}^a$ is the anchor view, $\mathbf{x}^p$ is a synchronized view from a different camera (positive), and $\mathbf{x}^n$ is a view from a different timestep (negative).

- **Grasp2Vec Object-Centric Loss** (Jang & Devin et al., 2018):
Minimizes the distance between the difference in scene embeddings before/after a grasp and the embedding of the grasped object:
$$ \mathcal{L}_\text{grasp2vec} = \text{NPair}(\phi_s(s_\text{pre}) - \phi_s(s_\text{post}), \phi_o(o)) + \text{NPair}(\phi_o(o), \phi_s(s_\text{pre}) - \phi_s(s_\text{post})) $$
$$ \text{NPair}(a, p) = \sum_{i<B} -\log\frac{\exp(a_i^\top p_j)}{\sum_{j<B, i\neq j}\exp(a_i^\top p_j)} + \lambda (\|a_i\|_2^2 + \|p_i\|_2^2) $$

---

## Figures

| Figure | Description & Caption |
|---|---|
| ![fig-1](../assets/2019-11-10-self-supervised/fig-1.webp) | **Constructing Self-Supervised Tasks**: Yann LeCun's summary diagram showing how raw visual, text, or control sequences can be masked or split to frame self-supervised pretext objectives. |
| ![fig-2](../assets/2019-11-10-self-supervised/fig-2.webp) | **Exemplar-CNN Patch Distortion**: A primary patch (e.g. a deer head) undergoes translation, rotation, scaling, and color shifts to define a single surrogate class for training classification representations. |
| ![fig-3](../assets/2019-11-10-self-supervised/fig-3.webp) | **Whole-Image Rotation Pretext**: Rotating an image at $0^\circ, 90^\circ, 180^\circ,$ and $270^\circ$ and training the model to classify the rotation. Forces learning high-level semantic boundaries. |
| ![fig-4](../assets/2019-11-10-self-supervised/fig-4.webp) | **Relative Patch Position**: Predicting which of the 8 grid positions a secondary patch is relative to a central anchor patch, teaching spatial composition. |
| ![fig-5](../assets/2019-11-10-self-supervised/fig-5.webp) | **Chromatic Aberration**: Physical lens focal shifts of different wavelengths that allow raw models to cheat on patch position tasks using color splits instead of semantic structure. |
| ![fig-6](../assets/2019-11-10-self-supervised/fig-6.webp) | **Jigsaw Puzzle Pretext**: Shuffling a 3x3 grid of patches and training a shared Siamese CNN to predict the correct permutation index out of a predefined subset. |
| ![fig-7](../assets/2019-11-10-self-supervised/fig-7.webp) | **Feature Counting**: Enforcing scaling and tiling constraints ($1 \text{ image} = 1 \text{ downsampled} = \sum 4 \text{ tiles}$) to learn visual primitive representation scalars. |
| ![fig-8](../assets/2019-11-10-self-supervised/fig-8.webp) | **Context Encoder Architecture**: Reconstruction of missing rectangular image patches via combined L2 and adversarial discriminator losses. |
| ![fig-9](../assets/2019-11-10-self-supervised/fig-9.webp) | **Split-Brain Autoencoder**: Disjoint splitting of color channels (e.g. predicting L from ab, and ab from L) to build cross-channel feature predictive networks. |
| ![fig-10](../assets/2019-11-10-self-supervised/fig-10.webp) | **Bidirectional GAN (BiGAN)**: Learning encoder $E(\mathbf{x})$ mappings alongside generator $G(\mathbf{z})$, judged jointly by a unified discriminator $D(\mathbf{x}, \mathbf{z})$. |
| ![fig-11](../assets/2019-11-10-self-supervised/fig-11.webp) | **Contrastive Predictive Coding (CPC) Audio**: Compress raw audio into latent $z_t$ and context $c_t$ to predict future latent frames via contrastive InfoNCE loss against noise clips. |
| ![fig-12](../assets/2019-11-10-self-supervised/fig-12.webp) | **CPC on Images**: Encoding overlapping grid patches with a Siamese ResNet and predicting patches below the context boundary using a masked convolutional context encoder. |
| ![fig-13](../assets/2019-11-10-self-supervised/fig-13.webp) | **Video Object Tracking**: Enforcing tracked patch frames $\mathbf{x}$ and $\mathbf{x}^+$ to map closer in latent cosine similarity space than a random patch $\mathbf{x}^-$. |
| ![fig-14](../assets/2019-11-10-self-supervised/fig-14.webp) | **Frame Order Validation**: Sampling video frames chronologically or out-of-order, and training a Siamese triplet network to classify order validity. |
| ![fig-15](../assets/2019-11-10-self-supervised/fig-15.webp) | **Arrow of Time**: Binary temporal classification task determining whether a video sequence is playing forward or backward. |
| ![fig-16](../assets/2019-11-10-self-supervised/fig-16.webp) | **Video Colorization Reference Mechanism**: Attention-based pointing mechanism that copies color channels from a reference color frame to target grayscale frames. |
| ![fig-17](../assets/2019-11-10-self-supervised/fig-17.webp) | **Colorization-Based Visual Tracking**: Leveraging video colorization reference models to track segmentation masks and keypoints dynamically in time without any fine-tuning. |
| ![fig-18](../assets/2019-11-10-self-supervised/fig-18.webp) | **Grasp2Vec Invariant Representation**: Minimizing the difference between scene states before and after a robot grasp to capture the singular representation of the grasped object. |
| ![fig-19](../assets/2019-11-10-self-supervised/fig-19.webp) | **Grasp2Vec Object Localization**: Spatial activation maps generated by taking the dot product of the object embedding and the spatial scene feature maps. |
| ![fig-20](../assets/2019-11-10-self-supervised/fig-20.webp) | **Time-Contrastive Networks (TCN)**: Aligning states across synchronized multi-angle camera views at identical timesteps while separating representations of different timesteps. |
| ![fig-21](../assets/2019-11-10-self-supervised/fig-21.webp) | **mfTCN Temporal Stacking**: Sampling multi-frame temporal lookback windows with 3D convolutions to capture position and velocity representations. |
| ![fig-22](../assets/2019-11-10-self-supervised/fig-22.webp) | **Reinforcement Learning with Imagined Goals (RIG)**: Visual goal-conditioned policy training operating entirely in a $\beta$-VAE latent representation space. |
| ![fig-23](../assets/2019-11-10-self-supervised/fig-23.webp) | **RIG Policy Training**: Detailed programmatic sequence for training RIG, leveraging latent space relabeling and HER. |
| ![fig-24](../assets/2019-11-10-self-supervised/fig-24.webp) | **Context-Conditioned RIG (CC-RIG)**: CC-VAE integration that generates realistic imagined goals with high object, shape, and color variance. |
| ![fig-25](../assets/2019-11-10-self-supervised/fig-25.webp) | **CC-RIG Imagined Goal Samples**: Samples of high-fidelity imagined robotic table configurations with varying block shapes, positions, and colors. |
| ![fig-26](../assets/2019-11-10-self-supervised/fig-26.webp) | **DeepMDP State Space**: Learning representations by training a latent forward transition model to capture action-conditioned transitions and rewards. |
| ![fig-27](../assets/2019-11-10-self-supervised/fig-27.webp) | **Decoupled Bisimulation Metric (DBC)**: Learning state representations that discard control-irrelevant details (like background distractors) using a bisimulation metric. |
| ![fig-28](../assets/2019-11-10-self-supervised/fig-28.webp) | **DBC Algorithm**: Training loop for decoupled bisimulation metric representation learning and policy optimization. |

---

## Entities

- [[Lilian Weng]] — ML researcher, educator, and author of Lil'Log; wrote this unified pretext survey.
- [[Yann LeCun]] — Pioneer in self-supervised learning; his visual masking talk serves as the foundational framing (Fig 1).
- [[Tomas Mikolov]] — Created Word2Vec and popularized NLP-based pretext predictive task frameworks (Skip-Gram/CBOW).
- [[Yoshua Bengio]] — Co-author of early representation pretraining surveys and neural language models.
- [[Kaiming He]] — Co-creator of ResNet backbones heavily utilized in Siamese pretext visual encoders.
- [[DeepMind]] — Developed CPC/InfoNCE bounds and key state-representation architectures.

---

## Questions & Gaps

- **Suboptimal Shortcut Elimination**: While chromatic aberration and compression artifacts are addressed, self-supervised networks consistently find complex mathematical shortcuts in pixel spaces. Robust automated detection of these shortcut channels remains an open research question.
- **Downstream Task Alignment**: Choosing the optimal pretext task for a specific downstream application remains highly empirical. For instance, why visual feature counting transfers better to some tasks while rotation validation is superior for others is poorly understood from a theoretical perspective.
- **Bisimulation Robustness**: Bisimulation state abstractions (like DBC) work exceptionally well under controlled dynamics but can fail when unexpected out-of-distribution distractors display visual dependencies matching transition rewards.

---

## Related

- [[Grokking Self-Supervised (Representation) Learning: How It Works in Computer Vision and Why]] — AI Summer pedagogy for contrastive CV SSL: augmentation ablations, log-softmax loss intuition, BYOL/DINO, mode collapse.
- [[Contrastive Representation Learning]] — Lilian Weng's subsequent survey focusing entirely on contrastive metric learning, SimCLR, BYOL, and InfoNCE properties.
- [[Contrastive Learning]] — Visual and text training paradigm utilizing InfoNCE, triplet, or metric margin losses.
- [[Representation Learning]] — Overarching concept of automated feature extraction from high-dimensional data.
- [[InfoNCE Loss]] — The core density ratio contrastive objective derived from Noise Contrastive Estimation.
- [[Triplet Loss]] — Spatial margin objective widely used in visual tracking and Time-Contrastive Networks.
- [[Autoencoders]] — Foundational generative pretext reconstruction models.
- [[Unsupervised Learning]] — Broad paradigm of learning patterns from unlabeled datasets.
