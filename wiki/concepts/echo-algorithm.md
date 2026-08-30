# ECHO Algorithm

**Type**: concept  
**Tags**: #concept

## Overview

**ECHO** is a reinforcement-learning method that trains an agent to predict environment tokens without a separate verifier: next-token cross-entropy is applied to tokens produced by the environment alongside usual policy learning on agent actions. The policy learns an implicit world model without an extra model, teacher, or additional rollouts.

## Appearances

- [[Inkling]] — Hugging Face demo post-trains Inkling with Tinker + OpenEnv using ECHO (`examples/echo_world_model/backends/tinker_echo_demo.py`).

## Notes

Contrasts with verifier-bounded RL where a separate judge or environment score is the only learning signal. Useful when environment observations are tokenizable and should be modeled jointly with actions.

## Related

- [[Inkling]]
- [[Tinker]]
- [[RL Environments]]
- [[Reinforcement Learning Topic]]
- [[Verifier-Bounded Learning]]
