# Direct Preference Optimization

**Type**: concept  
**Tags**: #concept

## Overview

Direct Preference Optimization (DPO) is a preference-alignment method that reparameterizes the [[RLHF]] objective so the optimal policy can be learned with a classification loss on preference pairs, avoiding an explicit RL loop and separate reward-model training at fine-tuning time.

## Appearances

- [[Papers Explained 148 - Direct Preference Optimization]] — original DPO paper summary in this wiki.
- [[Reinforcement Learning from Human Feedback]] — textbook derivation, numerical concerns, synthetic-preference variants, and comparison to online RL.

## Notes

DPO solves the KL-constrained RLHF problem in closed form on offline preference data; extensions (online DPO, discriminator-guided relabeling) address distribution shift and preference displacement.

## Related

- [[RLHF]]
- [[Post-Training]]
- [[KL Regularization]]
- [[Reinforcement Learning Topic]]
