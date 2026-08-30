# GPT-Live

**Source**: `raw/introducing-gpt-live/full-article.md`, `raw/gpt-live-deploymentsafety/full-article.md`
**Ingested**: 2026-07-10
**Tags**: #summary

## Summary

GPT-Live is OpenAI's full-duplex voice model family, launched in two sizes, GPT-Live-1 and GPT-Live-1 mini, and rolled out as the new default for ChatGPT Voice. Unlike earlier cascaded voice systems (speech-to-text, then an LLM, then text-to-speech) or the turn-based Advanced Voice Mode that waited for silence to detect the end of a turn, GPT-Live listens and speaks continuously. It decides many times per second whether to speak, listen, pause, interrupt, or call a tool, which lets it acknowledge the user mid-sentence, handle interruptions, and stay quiet when someone needs a moment to think.

GPT-Live is not the model doing the heavy thinking. For anything that needs web search, deeper reasoning, or complex work, it delegates to a frontier model in the background (GPT-5.5 at launch) and folds the result back into the conversation once ready, without breaking the flow of speech. GPT-Live-1 and GPT-Live-1 mini in instant mode use GPT-5.5 Instant for this delegation, while GPT-Live-1 Medium and High route to GPT-5.5 Thinking at medium or high reasoning effort.

OpenAI evaluated the voice-native safety behavior of GPT-Live against the models behind Advanced Voice Mode, using both production audio (shared by users who opted in, after privacy and PII screening) and synthetic audio built from safety-policy-grounded text. Across most categories GPT-Live matched or beat Advanced Voice Mode; the exceptions were small, not statistically significant dips on emotional reliance for GPT-Live-1 (0.88 to 0.82) and on sexual content for GPT-Live-1 mini (0.97 to 0.95). Red-teaming across languages, covering child-coded voice, impersonation, speaker identification, self-harm, and emotional reliance, led OpenAI to prioritize mitigation work on sexual content, emotional reliance, and self-harm before launch, while voice cloning and impersonation attempts were already policy-compliant by default.

Under the Preparedness Framework, OpenAI's Safety Advisory Group found that neither model, running without delegation, could plausibly be rated High in any tracked risk category (biological/chemical, cybersecurity, AI self-improvement). Self-improvement evaluations were skipped because GPT-Live is less capable than GPT-5.5 Thinking on standard intelligence evals. When GPT-Live delegates biological/chemical or cybersecurity-relevant work to a flagship model, that work inherits the delegate model's own safeguards, and automated monitors can interrupt or end a call if the conversation turns harmful. GPT-Live's own cybersecurity exposure is limited at launch because it has no independent tool access and no code execution.

## Key Claims

- Two models launched: GPT-Live-1 (default for Go, Plus, and Pro users) and GPT-Live-1 mini (default for Free users).
- Full-duplex architecture makes speak/listen/pause/interrupt/tool-call decisions many times per second, instead of relying on silence-based turn detection.
- Delegates search, reasoning, and agentic work to GPT-5.5 (Instant or Thinking, depending on reasoning-effort setting) while continuing to talk.
- More than 150 million people use ChatGPT Voice/Dictation weekly.
- Human evaluations show GPT-Live strongly preferred over Advanced Voice Mode on overall preference, turn-taking, interruptions, conversational flow, and naturalness.
- Outperforms Advanced Voice Mode on GPQA (expert scientific reasoning) and BrowseComp (agentic web search), and on an internal telecom-support benchmark (τ³-Voice).
- Voice-native safety evaluations show GPT-Live matching or beating Advanced Voice Mode on nearly all measured categories, with two small non-significant regressions (emotional reliance for GPT-Live-1, sexual content for GPT-Live-1 mini).
- Preparedness Framework assessment: neither model rates High in any tracked category when operating without delegation.
- Uses only a fixed set of predefined voices, with safeguards against imitating real people's voices.
- Does not support voice with video or screen sharing at launch; legacy Standard/Advanced Voice Mode remain available for that.

## Figures

No article figures extracted; openai.com blocks direct HTML download so figures could not be downloaded, and WebFetch markdown does not preserve chart images.

## Entities

- [[OpenAI]]: developer of GPT-Live and operator of ChatGPT Voice.

## Questions & Gaps

- No numeric scores are given for the GPQA, BrowseComp, or τ³-Voice comparisons against Advanced Voice Mode, only qualitative descriptions such as "substantially outperforms" or "strong gains."
- No firm timeline is given for API access, only that it is planned.
- The article does not list which languages show non-native accent or fluency gaps.

## Related

- [[OpenAI]]
- [[Audio Models]]
- [[Safety and Alignment]]
- [[Full-Duplex Voice]]
- [[Preparedness Framework]]
