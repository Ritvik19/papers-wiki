# Intrinsic Curiosity Module (ICM)

**Type**: concept  
**Tags**: #concept

## Overview

ICM (Pathak et al., 2017) is an exploration bonus method for deep RL that uses a **self-supervised inverse dynamics model** to learn a feature space for a forward dynamics predictor. The forward prediction error in this feature space serves as the intrinsic reward $r^i_t = \|\hat{\phi}(s_{t+1}) - \phi(s_{t+1})\|_2^2$.

The key insight is that encoding via the inverse dynamics model $g: (\phi(s_t), \phi(s_{t+1})) \mapsto a_t$ forces the feature space to capture only environment factors that are **controllable by the agent**, ignoring noise that cannot influence behaviour. This partially mitigates the [[Noisy-TV Problem]].

Architecture summary:
- **Inverse model**: predicts action taken from consecutive state embeddings — trains the encoder $\phi$.
- **Forward model**: predicts next state embedding given current state embedding and action.
- **Intrinsic reward**: L2 error of the forward model in $\phi$ space.

## Appearances

- [[Exploration Strategies in Deep Reinforcement Learning]] — Described as a core method in forward-dynamics-based exploration; compared against raw pixels, random features, and VAE encoding in large-scale Burda et al. 2018 experiments.

## Notes

- ICM's inverse-dynamics encoder does **not fully eliminate** the noisy-TV problem; if the agent can control access to the noise source (e.g., choosing to look at the TV), the noise enters the controllable factor space.
- Random features (RF) proved surprisingly competitive with IDF/ICM features for in-distribution exploration but are inferior in feature transfer experiments.
- ICM features (IDF) are also reused in the [[Never Give Up (NGU)]] episodic novelty module as the embedding function for k-NN memory lookup.

## Related

- [[Random Network Distillation (RND)]] — Alternative prediction-based bonus that avoids learning dynamics.
- [[Never Give Up (NGU)]] — Uses IDF embedding from ICM as its episodic novelty encoder.
- [[Noisy-TV Problem]] — The failure mode ICM was partly designed to address.
- [[Exploration Strategies in Deep Reinforcement Learning]] — Survey where ICM is detailed.
