# Computer-use Agents

#concept

Computer-use agents are [[Large Language Models]] or [[Vision Language Models]] that act through graphical interfaces, usually by observing screens and issuing keyboard or mouse actions inside a software environment. In this wiki they sit at the intersection of [[Agentic AI]], multimodal grounding, and environment design, because their behavior depends not only on model reasoning but also on the fidelity of the software workspace they are asked to operate.

## Overview

Unlike tool-use agents that call clean APIs, computer-use agents must interpret dense visual state, recover latent workflow structure from interface layouts, and avoid brittle failure modes such as stopping early or operating on the wrong window. That makes them especially sensitive to benchmark design: short consumer tasks can overstate progress, while realistic enterprise or scientific workflows require long-horizon interaction, domain-specific data, and stronger verification.

[[Gym-Anything]] sharpens this distinction by treating environment construction as a first-class systems problem. Instead of assuming the software workspace already exists, it asks how to build hundreds of real software environments with reusable scripts, audit loops, and realistic data. [[CUA-World]] then uses those environments to push computer-use evaluation closer to economically meaningful work than classic desktop-automation benchmarks.

## Appearances

- [[Gym-Anything]] — frames environment creation and verification as a multi-agent pipeline for computer-use benchmarks.
- [[CUA-World]] — evaluates long-horizon software tasks across 200 applications.
- [[RL Environments in the LLM Era]] — provides adjacent infrastructure vocabulary for how agent environments are deployed and scored.

## Related

- [[Agentic AI]]
- [[Gym-Anything]]
- [[CUA-World]]
- [[RL Environments]]
- [[Vision Language Models]]
- [[Large Language Models]]
