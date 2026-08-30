---
Source URL: https://openai.com/index/introducing-gpt-live/
Fetched via: WebFetch (curl returns 403 on openai.com/index/*)
Date: July 8, 2026
---

# Introducing GPT‑Live

A new generation of voice models for natural human-AI interaction, now powering ChatGPT Voice.

GPT‑Live is built on a **full-duplex architecture**: it can listen and speak at the same time. It can show it's paying attention with phrases like "mhmm" or "yeah," engage in quick back-and-forth, or stay quiet when the user needs a moment to think.

GPT‑Live is also OpenAI's smartest voice model yet. For questions requiring web search, deeper reasoning, or complex work, it delegates to the latest frontier model in the background and brings the result back into the conversation when ready, while continuing to talk and maintain conversational flow. At launch, GPT‑Live uses GPT‑5.5 in the background; the delegated model updates as new frontier models release.

Two versions launched: **GPT‑Live‑1** and **GPT‑Live‑1 mini**, rolling out to ChatGPT users globally, with API access planned.

## Previous approaches

**Cascaded voice systems** (original ChatGPT Voice) chained a speech-to-text model, an LLM, and a text-to-speech model in sequence: enabled talking to frontier models for the first time but lost information across models and produced slow, stilted responses.

**Turn-based voice models** (ChatGPT Advanced Voice Mode) processed and generated audio within a single model, reducing latency, but still operated in discrete turns, waiting for the user to stop speaking; silence-based turn detection meant a brief pause or background noise could be mistaken for end-of-turn, causing unnatural interruptions.

## The new approach

**Continuous interaction**: GPT‑Live continuously processes input while generating output via full-duplex architecture, making interaction decisions (speak, listen, pause, interrupt, invoke a tool) many times per second, enabling more natural back-and-forth, better sense of time, and live translation.

**Delegation for deeper work**: GPT‑Live (continuous interaction) is decoupled from deeper work (search, reasoning, agentic capability), which it delegates to models like GPT‑5.5 while keeping the conversation going.

## Evaluations

New human evaluations measure pleasantness and conversational flow. GPT‑Live‑1 and GPT‑Live‑1 mini are strongly preferred over Advanced Voice Mode in matched 5–10 minute conversations (overall preference, turn-taking, interruptions, conversational flow, naturalness).

- GPQA: GPT‑Live‑1 substantially outperforms Advanced Voice Mode (expert-level scientific reasoning: biology, chemistry, physics).
- BrowseComp: strong gains over Advanced Voice Mode (agentic web search, hard-to-locate information).
- τ³-Voice Telecom (internal variant): outperforms Advanced Voice Mode on realistic multi-turn telecom support tasks.

GPT‑Live‑1 (instant) and GPT‑Live‑1 mini use GPT‑5.5 Instant in the background; GPT‑Live‑1 Medium and High use GPT‑5.5 Thinking with medium/high reasoning effort.

## New ChatGPT Voice experience

More than 150 million people talk to ChatGPT weekly via Voice/Dictation features. The updated experience adds: more natural conversations (interruptible, acknowledges with "mhmm"/"got it," remastered nine voices); smarter answers (frontier model access, selectable reasoning level: Instant/Medium/High); better listening (waits during pauses, respects "stay quiet" requests, better background-noise filtering); and visual answer cards (weather, stocks, sports) shown during voice conversations.

## Safety designed for voice

Expanded safety testing with new audio-native evaluations and synthetic audio evaluations focused on self-harm, psychosis/mania, emotional reliance, violence, and sexual content, informed by learnings from Advanced Voice Mode. GPT‑Live performed comparably to or better than Advanced Voice Mode across nearly all evaluated areas.

Built-in real-time safeguards: can steer toward a safer response, surface safety messaging/resources, or end the conversation in higher-risk cases; adapted crisis-helpline support flows for voice on self-harm topics. Teen protections trained directly into the model; parents can control ChatGPT Voice access via Parental Controls and may be notified in higher-risk self-harm/suicidal-intent situations. Longer-term post-launch monitoring focused on emotional reliance. GPT‑Live uses only predefined voices with safeguards against imitating real people's voices (designed for conversation, not voice impersonation).

## Availability & limitations

Rolling out globally on iOS, Android, and ChatGPT.com. GPT‑Live‑1 becomes the default for Go, Plus, and Pro users; GPT‑Live‑1 mini the default for Free users. Optimized for the most popular ChatGPT languages (some languages may show non-native accent or fluency gaps). At launch, does not support voice with video or screen sharing (legacy Standard/Advanced Voice Mode remain available for those features).
