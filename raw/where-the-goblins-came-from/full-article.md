---
Source URL: https://openai.com/index/where-the-goblins-came-from/
Fetched via: WebFetch (curl returns 403 on openai.com/index/*)
Date: April 29, 2026
---

# Where the goblins came from

Starting with GPT‑5.1, OpenAI's models began mentioning goblins, gremlins, and other creatures in their metaphors with increasing frequency, a subtle habit that (unlike bugs visible through a tanking eval or spiking training metric) crept in without an obvious root cause.

## The first signs of creatures

First clearly noticed in November 2025 after the GPT‑5.1 launch, when users complained about the model being oddly overfamiliar in conversation, prompting an investigation into verbal tics. Use of "goblin" in ChatGPT had risen by 175% after GPT‑5.1's launch, and "gremlin" by 52%. At the time this did not seem especially alarming.

## Solving the mystery

With GPT‑5.4, OpenAI and users noticed an even bigger uptick, triggering another analysis that surfaced the root cause: creature language was especially common in production traffic from users who had selected the "Nerdy" ChatGPT personality. The Nerdy system prompt described an "unapologetically nerdy, playful and wise AI mentor" that should "undercut pretension through playful use of language." Nerdy accounted for only 2.5% of all ChatGPT responses but 66.7% of all "goblin" mentions.

Using Codex to compare RL training outputs containing goblin/gremlin mentions against outputs from the same task without them, one reward signal stood out: the signal designed to encourage the Nerdy personality consistently scored creature-word outputs higher, with positive uplift in 76.2% of audited datasets. Tracking mention rates over training with and without the Nerdy prompt showed goblin/gremlin mentions increasing by nearly the same relative proportion in both conditions, indicating the behavior transferred from Nerdy-personality training to the model more broadly, even though the reward was applied only in the Nerdy condition.

This created a feedback loop: playful style is rewarded → some rewarded examples contain a distinctive lexical tic → the tic appears more often in rollouts → model-generated rollouts are used for supervised fine-tuning (SFT) → the model becomes more comfortable producing the tic. A search of GPT‑5.5's SFT data found many "goblin" and "gremlin" datapoints, plus a family of other odd creature tic-words: raccoons, trolls, ogres, and pigeons (most uses of "frog" turned out to be legitimate).

## The end of the goblins

The "Nerdy" personality was retired in March 2026 after the GPT‑5.4 launch. In training, the goblin-affine reward signal was removed and training data containing creature-words was filtered. GPT‑5.5 had already started training before the root cause was found; when OpenAI employees noticed a strong goblin affinity while testing GPT‑5.5 in Codex, a developer-prompt instruction was added to mitigate it.

## Why it matters

The goblins illustrate how reward signals can shape model behavior in unexpected ways and how models can generalize rewards from one situation to unrelated ones. The investigation produced new tools for OpenAI's research team to audit model behavior and fix behavior problems at their root.
