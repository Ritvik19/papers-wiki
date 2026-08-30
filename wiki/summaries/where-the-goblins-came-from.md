# Where the Goblins Came From

**Source**: `raw/where-the-goblins-came-from/full-article.md`
**Ingested**: 2026-07-10
**Tags**: #summary

## Summary

Starting with GPT-5.1, OpenAI's models began mentioning goblins, gremlins, and other creatures in their metaphors with increasing frequency. Unlike a bug visible through a tanking eval score or a spiking training metric, this verbal tic crept in without an obvious cause, and OpenAI's post traces how it found the source and fixed it.

The behavior was first clearly noticed in November 2025 after the GPT-5.1 launch, when users complained the model felt oddly overfamiliar in conversation, prompting an investigation into verbal tics. Use of "goblin" in ChatGPT had risen 175% after the GPT-5.1 launch, and "gremlin" by 52%, though this did not seem especially alarming at the time. With GPT-5.4, OpenAI and users noticed an even bigger uptick, which triggered another analysis. That analysis found the root cause: creature language was especially common in production traffic from users who had selected the "Nerdy" ChatGPT personality. The Nerdy system prompt described an "unapologetically nerdy, playful and wise AI mentor" that should "undercut pretension through playful use of language." Nerdy accounted for only 2.5% of all ChatGPT responses but 66.7% of all "goblin" mentions.

Using Codex to compare RL training outputs that contained goblin or gremlin mentions against outputs from the same task without them, one reward signal stood out: the signal designed to encourage the Nerdy personality consistently scored creature-word outputs higher, with a positive uplift in 76.2% of audited datasets. Tracking mention rates over the course of training, with and without the Nerdy prompt, showed goblin and gremlin mentions increasing by nearly the same relative proportion in both conditions. That indicated the behavior had transferred from Nerdy-personality training to the model more broadly, even though the reward was applied only in the Nerdy condition. This created a feedback loop: playful style gets rewarded, some of the rewarded examples happen to contain a distinctive lexical tic, the tic appears more often in rollouts, those rollouts get used for supervised fine-tuning, and the model becomes more comfortable producing the tic. A search of GPT-5.5's supervised fine-tuning data found many "goblin" and "gremlin" datapoints, plus a family of other odd creature tic-words: raccoons, trolls, ogres, and pigeons (most uses of "frog" turned out to be legitimate).

The "Nerdy" personality was retired in March 2026 after the GPT-5.4 launch. In training, the goblin-affine reward signal was removed and training data containing creature words was filtered out. GPT-5.5 had already started training before the root cause was identified, so once OpenAI employees noticed a strong goblin affinity while testing GPT-5.5 in Codex, a developer-prompt instruction was added as a mitigation. OpenAI frames the episode as an illustration of how reward signals can shape model behavior in unexpected ways, and how models can generalize a behavior that was rewarded in one narrow situation to unrelated ones. The investigation also produced new tools for OpenAI's research team to audit model behavior and trace behavior problems to their root cause.

## Key Claims

- Goblin and gremlin mentions in ChatGPT rose 175% and 52% respectively after the GPT-5.1 launch in November 2025.
- The "Nerdy" ChatGPT personality accounted for 2.5% of all ChatGPT responses but 66.7% of all "goblin" mentions.
- A reward signal built to encourage the Nerdy personality scored creature-word outputs higher in 76.2% of audited RL datasets.
- Creature-word mention rates rose by a similar relative proportion in training with and without the Nerdy prompt, evidence that the tic generalized beyond the narrow context where it was rewarded.
- GPT-5.5's supervised fine-tuning data contained many goblin and gremlin datapoints, plus related creature tics (raccoons, trolls, ogres, pigeons).
- OpenAI retired the Nerdy personality, removed the goblin-affine reward signal, filtered creature-word training data, and added a developer-prompt mitigation for GPT-5.5, which had already begun training.

## Figures

No article figures extracted; openai.com blocks direct HTML download so figures could not be downloaded, and WebFetch markdown does not preserve chart images.

## Entities

- [[OpenAI]]: ran the investigation, using Codex as an analysis tool, into how the creature-word tic emerged and spread across model generations.

## Questions & Gaps

- The source does not explain the underlying mechanism by which SFT on model-generated rollouts spreads a stylistic reward from one training condition (Nerdy) into the base model's general behavior, beyond noting that it happened.
- It is unclear whether removing the reward signal and filtering training data fully eliminated the tic in GPT-5.5, or only reduced it alongside the developer-prompt mitigation.
- The source does not say whether similar audits found other unnoticed stylistic tics beyond the creature-word family.

## Related

- [[OpenAI]]
- [[Safety and Alignment]]
- [[Reward Hacking]]: this case is a narrower phenomenon than classic reward hacking (the model was not exploiting a flaw to score higher on its actual objective), but it demonstrates the same underlying mechanism of a proxy reward signal shaping behavior in ways that generalize beyond its intended scope.
