# Grok Voice Agent API

Source: https://x.ai/news/grok-voice-agent-api
Published: Dec 17, 2025

Today, we're excited to launch the Grok Voice Agent API, empowering developers to build voice agents that speak dozens of languages, call tools, and search realtime data.

The Grok Voice Agent API is built on the same stack that powers Grok Voice for millions in our mobile apps and Tesla vehicles, and we're thrilled to open up this proven technology to all via the xAI API.

## Smart and fast

Grok Voice Agents are the fastest, most intelligent voice agents available on the market.

We built the entire voice stack in-house, training our own voice activity detection (VAD), tokenizer, and audio models from scratch. This fine-grained control over every component of the stack allows us to rapidly iterate and improve Grok's intelligence and speed.

The Grok Voice Agent API ranks #1 on Big Bench Audio, the leading audio reasoning benchmark that measures voice agents' capabilities to solve complex problems. With an average time-to-first-audio of less than 1 second, Grok is nearly 5 times faster than the closest competitor.

### Big Bench Audio: Intelligence vs Latency

Audio reasoning benchmark (independently verified by Artificial Analysis)

Score: 95%

Time to First Audio: <1 s (vs ~5 s for competitors)

## Pricing

The Grok Voice Agent API leads the industry in cost-efficiency. Developers are billed at a simple flat rate of $0.05 per minute of audio duration.

*OpenAI charges by input and output tokens. $0.10 / min is a highly conservative blended estimate. In production, pricing typically exceeds $0.10 / min.*

## Multilingual fluency

Grok Voice Agents can speak dozens of languages with native-level proficiency, accurately capturing nuances in dialects and pronunciations. Grok Voice Agents were trained to automatically respond in the language spoken by the user and can seamlessly switch languages mid-conversation. Developers can also instruct Grok to always respond in a specific language via system prompt.

In blind head-to-head human evaluations against the OpenAI Realtime API, Grok is consistently rated as the preferred model across axes such as pronunciation, accent, and prosody.

## Grok Voice in Tesla

Tesla was a critical design partner for the Grok Voice Agent API, which now powers Grok in millions of vehicles.

Grok feels like a natural extension of your Tesla, thanks to specialized tools that let it access vehicle status, look up directions, and control navigation. Grok uses these tools in tandem to provide a seamless route planning experience. For instance, ask Grok to plan a road trip, and it will search X for recommendations, calculate optimal routes, and add stops, generating a full itinerary in seconds.

Grok Voice Agents can perform tasks and look up information in real time. With our API, developers can effortlessly integrate their own custom tools or tap into xAI's powerful real-time search capabilities across X and the web.

```json
{
    "type": "session.update",
    "session": {
        "instructions": "You're an in-car assistant for Tesla.",
        "voice": "ara",
        "tools": [
            { "type": "web_search" },
            { "type": "x_search" },
            {
                "type": "function",
                "name": "nav_search"
            }
        ]
    }
}
```

## Natural, expressive voices

We're excited to offer multiple expressive voices to the Grok Voice Agent API, including Ara, Eve, and Leo. Our voices sound natural in everyday conversations and also excel at pronouncing domain-specific terminology in fields like healthcare, finance, and legal.

To enhance realism, developers can even prompt the model to use auditory cues such as `[whisper]`, `[sigh]`, and `[laugh]`.

## Start building

The Grok Voice Agent API is compatible with the OpenAI Realtime API specification and also available via the official xAI LiveKit Plugin.

We've also built a voice playground that you can use to test various voices directly from your browser.

We're excited to continue iterating quickly. In the next few weeks, we'll also be releasing:

- Standalone text-to-speech and speech-to-text endpoints
- Audio models with even stronger performance in pronunciation and latency

We can't wait to hear what you build!
