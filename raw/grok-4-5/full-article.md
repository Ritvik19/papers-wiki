# Introducing Grok 4.5

**Source URL**: https://x.ai/news/grok-4-5
**Date**: Jul 8, 2026

Grok 4.5 is SpaceXAI's smartest model built for coding, agentic tasks, and knowledge work.

Today, we're launching Grok 4.5, SpaceXAI's smartest model built to excel at coding, agentic tasks, and knowledge work. It's our strongest model ever and was trained alongside Cursor.

## Real-world engineering excellence

Grok 4.5 was trained on datasets spanning knowledge in coding, science, engineering, and math. With both intelligent and efficient reasoning, Grok 4.5 excels at real engineering tasks and exceeds comparable leading models at these tasks.

DeepSWE 1.1 chart (pass@1): Grok 4.5 66.1%, Fable max 64.31%, GPT 5.5 xhigh 62.0%, Grok 4 55.75%, Opus 4.8 max 40.12%, Opus 4.7 max (eval by Datacurve with each model provider's harnesses by Artificial Analysis). Competitor figures from respective developers' published system cards or benchmark leaderboards.

## Training Grok 4.5

Grok 4.5 was trained across tens of thousands of NVIDIA GB300 GPUs, with training and stability techniques designed for large-scale runs. Beyond raw token volume, we invested heavily in data filtering and curation: deduplication, quality scoring, and domain-focused selection so that the data mixture stayed high-coverage and high-signal.

We scaled reinforcement learning with a strong focus on per-token intelligence. Our RL training covers hundreds of thousands of tasks, centered on multi-step software engineering and other technical work, with automated and model-based grading. Our stack is built for highly asynchronous training, so agentic rollouts can run for many hours while learning continues across tens of thousands of GPUs. The result is more intelligent and efficient reasoning on real engineering and agentic tasks.

### Built with one prompt

Grok 4.5 is incredibly capable at coding, from challenging Rust and C/C++ tasks to end-to-end app building from prompt to production. Below are some examples built by the model with one prompt. Grok 4.5 is highly proficient at creating well-designed, end-to-end functional apps even with minimal specification.

Example prompt: "Make a beautiful simulation of the universe and solar system. should be sped up with adjustable time, realistic motion, orbits, stars. use threejs. Make the HUD well styled and conform to modern design principles."

## Faster than flash models

Grok 4.5 is served at fast-model speeds of 80 TPS. Combined with twice greater token efficiency than the latest leading models at the same tasks, the model delivers intelligent results to you more quickly and at far lower costs.

Token efficiency (avg. output tokens per SWE Bench Pro task): Grok 4.5 uses 4.2× fewer tokens than Opus 4.8 (max); ~70k token baseline shown in chart.

## Excels at Office work

Grok 4.5 is now the default model in Grok Build. In addition to its coding proficiency, Grok Build is capable of building complex Excel models that involve research from the web, multi-sheet formula use, and even leaves stickies or notes behind for future reference.

In PowerPoint and Word, Grok 4.5 is similarly meticulous. The model is capable of using native PowerPoint shapes to build complex diagrams, designing intuitive slide content, and writing clear prose in Word.

## Pricing

Grok 4.5 is delivered at an incredibly competitive cost compared to other leading models. Grok 4.5 is priced at $2 per million input tokens and $6 per million output tokens. The model also achieves roughly 2x the token efficiency of comparable leading models, solving tasks in under half the number of steps. Overall, Grok 4.5 delivers the highest intelligence per unit of time and cost.

## Getting started

Grok 4.5 is available today in Grok Build, in Cursor on all plans, and from the SpaceXAI console. API model id: `grok-4.5`.

Note: Grok 4.5 is not yet available in the EU in any SpaceXAI products or the API console. EU availability is expected in mid-July.

Free Grok 4.5 usage for a limited time in Grok Build and Cursor.
