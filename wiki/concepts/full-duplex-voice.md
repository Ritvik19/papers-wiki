# Full-Duplex Voice

**Type**: concept  
**Tags**: #concept

## Overview

**Full-duplex voice** describes a voice model architecture that listens and speaks at the same time, continuously processing input while generating output, rather than waiting for a detected end of the user's turn before responding. It contrasts with two earlier approaches: **cascaded voice systems**, which chain separate speech-to-text, language, and text-to-speech models and lose information at each handoff, and **turn-based voice models**, which process and generate audio in a single model but still wait for silence to decide when the user has finished speaking, which causes unnatural interruptions when a pause or background noise is mistaken for the end of a turn.

## Appearances

- [[GPT-Live]] — OpenAI's first full-duplex voice model family (GPT-Live-1, GPT-Live-1 mini). The model makes an interaction decision (speak, listen, pause, interrupt, or invoke a tool) many times per second, decoupling the always-on conversational layer from deeper work such as search or multi-step reasoning, which it delegates to a flagship model (GPT-5.5 at launch) while continuing to talk.

## Notes

- Full duplex is a property of the audio interaction loop, not of the underlying language model; GPT-Live delegates any task that needs real reasoning or tool use to a separate model and folds the result back into the ongoing conversation.
- The distinction from turn-based systems matters most for interruption handling and pacing: a full-duplex model can be talked over, can acknowledge with short filler ("mhmm," "yeah") while listening, and can stay silent when a user asks for a moment to think, none of which a strict turn-taking model can do without a fixed silence-timeout heuristic.

## Related

- [[OpenAI]]
- [[GPT-Live]]
- [[Audio Models]]
- [[Preparedness Framework]]
