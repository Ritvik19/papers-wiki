# Grasp2Vec

**Type**: concept  
**Tags**: #concept

## Overview

Grasp2Vec is a self-supervised, object-centric visual metric representation learning framework developed by Jang & Devin et al. (2018) specifically for robotic manipulation and reinforcement learning. Grasp2Vec leverages the physical structure of robotic interactions—specifically the action of picking up and removing an object from a scene—to learn semantic, localized representations of objects without any human labels. The core intuition is a vector arithmetic identity: the difference between the representation of the visual scene *before* a grasp and the scene *after* a grasp should equal the representation of the grasped *object* itself.

```
                      Grasp2Vec Vector Subtraction Framework
                      
     Scene s_pre              Scene s_post                 Grasped Object o
   +--------------+         +--------------+               +-------------+
   | (Apple, Cup) |         |    (Cup)     |               |   (Apple)   |
   |   O      U   |         |      U       |               |      O      |
   +--------------+         +--------------+               +-------------+
          ||                       ||                             ||
          \/                       \/                             \/
     Scene Encoder            Scene Encoder                 Object Encoder
      \phi_s(s)                \phi_s(s)                       \phi_o(o)
          ||                       ||                             ||
          \/                       \/                             \/
      [Vector A]  =========>   [Vector B]                         ||
          \                       /                               ||
           \_____________________/                                ||
                      |                                           ||
                      \/                                          \/
         Vector Subtraction: (A - B) =======================> [Vector C]
         
                         Minimize N-Pair Contrastive Loss
```

---

## Technical Formulation & Loss Function

Let a single robot grasping interaction trial $i$ yield a triplet:
- $s_{\text{pre}}^{(i)}$: The visual image of the workspace before the robot performs a grasp.
- $s_{\text{post}}^{(i)}$: The visual image of the workspace after the robot performs a grasp.
- $o^{(i)}$: A close-up visual image of the object currently held in the robot's gripper (isolated via background subtraction or cropping).

We parameterize a convolutional scene encoder $\phi_s$ and an object encoder $\phi_o$. The subtraction vector $v^{(i)}$ represents the semantic difference caused by the grasp:
$$ v^{(i)} = \phi_s(s_{\text{pre}}^{(i)}) - \phi_s(s_{\text{post}}^{(i)}}) $$
The target embedding is the representation of the grasped object:
$$ u^{(i)} = \phi_o(o^{(i)}) $$

### N-Pair Contrastive Loss
To prevent the encoders from mapping all inputs to a trivial constant vector, the network is trained over a batch of $M$ grasping trials using an **N-Pair Contrastive Loss**. The objective forces the subtraction vector $v^{(i)}$ to align closely with the correct grasped object representation $u^{(i)}$ (positive pair) while pushing it away from all other objects $u^{(j)}$ ($j \neq i$) held in the gripper across the batch:
$$ \mathcal{L}_{\text{Grasp2Vec}} = - \frac{1}{M} \sum_{i=1}^M \log \left( \frac{\exp(v^{(i)\top} u^{(i)})}{\sum_{j=1}^M \exp(v^{(i)\top} u^{(j)})} \right) $$

Minimizing this loss establishes a highly structured metric space where visual subtraction matches semantic category embeddings.

---

## Self-Supervised Object Localization Mechanics

The learned representations are not just global pool summaries; they preserve highly detailed spatial properties. This enables **weakly-supervised object localization** using the dense convolutional feature maps before spatial pooling.

Let $\Phi_s^{\text{dense}}(s) \in \mathbb{R}^{H \times W \times D}$ be the dense convolutional feature map output of a scene $s$, where $H \times W$ is the spatial resolution and $D$ is the feature dimension. Let $u = \phi_o(o) \in \mathbb{R}^D$ be the target object query embedding.

The spatial activation map $A \in \mathbb{R}^{H \times W}$ is computed by taking the channel-wise dot product at each coordinate:
$$ A_{y, x} = \sum_{d=1}^D \Phi_s^{\text{dense}}(s)_{y, x, d} \cdot u_d $$

Applying a spatial softmax over $A$ yields a localized probability distribution:
$$ P(\text{Object location} = (y, x)) = \frac{\exp(A_{y, x})}{\sum_{y'} \sum_{x'} \exp(A_{y', x'}) $$

This localization map successfully highlights the target object in the workspace without ever having been trained on bounding boxes or pixel masks, providing the robot with coordinates to execute subsequent targeted grasps.

---

## Goal-Conditioned Reinforcement Learning (RL)

For goal-conditioned policies where a robot is tasked with grasping a specific target object $g$ (represented as an image goal), Grasp2Vec provides a robust, dense reward function without human supervision.

The reward is formulated as the cosine similarity between the current scene subtraction vector and the goal object representation:
$$ R(s_{\text{pre}}, s_{\text{post}}, g) = \frac{(\phi_s(s_{\text{pre}}) - \phi_s(s_{\text{post}}))^\top \phi_o(g)}{\|\phi_s(s_{\text{pre}}) - \phi_s(s_{\text{post}})\|_2 \cdot \|\phi_o(g)\|_2} $$

This reward naturally reaches its maximum value of $1.0$ only when the robot successfully lifts the object matching the target goal $g$ out of the workspace, enabling sample-efficient pixel-to-action policy training.

---

## Appearances

- [[Self-Supervised Representation Learning]] — Detailed as a multi-view robotic metric learning algorithm that uses self-supervised interactions to bootstrap spatial and object representations.

## Related

- [[Representation Learning]]
- [[Self-Supervised Representation Learning]]
- [[Contrastive Learning]]
