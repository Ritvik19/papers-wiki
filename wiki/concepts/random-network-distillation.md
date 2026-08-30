# Random Network Distillation (RND)

**Type**: concept  
**Tags**: #concept

## Overview

RND (Burda et al., 2018) provides an exploration bonus by defining a **task-independent prediction target** via a fixed randomly-initialised neural network $f(s_t)$. A trained predictor network $\hat{f}(s_t; \theta)$ learns to match this target; the intrinsic reward is the prediction error:

$$r^i(s_t) = \|\hat{f}(s_t; \theta) - f(s_t)\|_2^2$$

Novel states yield higher error because the predictor has seen fewer similar training examples. Crucially, **no environment dynamics modelling is required**, making the method simple and stable.

Two implementation details are essential:
1. **Non-episodic setting**: intrinsic return should not be reset at episode boundaries; cross-episode accumulation of prediction knowledge is important.
2. **Reward normalisation**: RND uses a running estimate of the standard deviation of intrinsic returns to normalise bonuses.

RND consistently reaches >50% of rooms in Montezuma's Revenge purely on intrinsic rewards.

## Appearances

- [[Exploration Strategies in Deep Reinforcement Learning]] — Described as a "random networks" approach that avoids environment-dynamics learning; contrasted with ICM/VIME; used as the life-long novelty module in NGU.

## Notes

- The RND paper itself acknowledges the method handles **local exploration** (short-term decisions, e.g., interact with an object or not) but not **global exploration** requiring coordinated long-horizon decisions.
- Despite this caveat, [[Never Give Up (NGU)]] uses RND as a life-long novelty provider across episodes, combined with an episodic novelty module for short-horizon novelty.
- The scale of the random network determines feature dimensionality; prediction normalisation is required since the target is random.

## Related

- [[Intrinsic Curiosity Module (ICM)]] — Forward-dynamics approach for similar exploration goals.
- [[Never Give Up (NGU)]] — Combines RND (life-long) with episodic novelty module.
- [[Agent57]] — Extends NGU (which uses RND) to achieve human-level performance on all 57 Atari games.
- [[Exploration Strategies in Deep Reinforcement Learning]] — Source survey.
