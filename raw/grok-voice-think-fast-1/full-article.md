# Grok Voice Think Fast 1.0

Source: https://x.ai/news/grok-voice-think-fast-1
Published: Apr 23, 2026

Today, we're excited to announce a step change in xAI's Voice Agent capabilities: Introducing `grok-voice-think-fast-1.0` — our new flagship voice model.

This new model excels at complex, ambiguous, multi-step workflows across customer support, sales, and enterprise applications. It is especially well-suited for high-stakes scenarios that demand precise data entry and high-volume tool calling to address the user's request.

## Built for the messiness of the real world

We built `grok-voice-think-fast-1.0` through tight collaboration with partners like Starlink to combine top-tier intelligence with low response latency and organic conversational ability.

Our model prioritizes snappy responses and unparalleled cost effectiveness without compromising on accuracy or tool orchestration. The result is a model that lets teams confidently deploy complex, multi-turn voice experiences across almost any conceivable use case: Customer support, phone sales, appointment booking, restaurant reservations, and more.

This new model takes the top spot on the τ-voice Bench leaderboard, which evaluates full-duplex voice agents under realistic conditions including noise, accents, interruptions, and turn-taking.

### τ-voice Leaderboard domains

- **Retail** — order handling, returns, promotions in noisy environments
- **Airline** — booking changes, delays, and complex itineraries
- **Telecom** — plan changes, billing disputes, technical troubleshooting

Compared models: Grok Voice Think Fast 1.0, Grok Voice Fast 1.0, Gemini 3.1 Flash Live, GPT Realtime 1.5.

The model has been battle-tested in the toughest real-world conditions: telephony audio, background noise, heavy accents, and frequent interruptions. It natively supports 25+ languages, making it ideal for global deployments.

## Precise data entry and read-back

Collecting and confirming user information is critical for many workflows. Grok Voice is able to seamlessly collect email addresses, physical street addresses, phone numbers, full names, account numbers, and other structured data—even when information is spoken quickly or with a strong accent. It gracefully handles speech disfluencies and accepts natural corrections as a human would.

Workflow stages:

1. **Processing user input** — handles spoken corrections and extracts the intended address.
2. **Calling custom tool** — invokes the address lookup tool with the corrected query parameter.
3. **Confirming the result** — reads back the normalized address with location for user confirmation.

## Real-time reasoning with zero added latency

Grok Voice Think Fast performs reasoning in the background, allowing it to think through challenging queries and workflows in real-time with no impact on response latency. This enables intelligent answers while retaining the dexterity needed for natural conversation.

## Harder to fool

Voice models often default to confident, plausible-sounding answers, despite being completely wrong. We've built `grok-voice-think-fast-1.0` to reason through edge cases before responding, catching obvious mistakes that other models get wrong.

**Prompt:** Which months of the year are spelled with the letter X?

**grok-voice-think-fast-1.0:** None of the months are spelled with the letter X. You can check them all, but X doesn't appear in any month name.

**Other Models:** Only one month is spelled with the letter X. It's February.

## Powering customer support and sales for Starlink

Grok Voice enables Starlink's phone sales and customer support experience at +1 (888) GO STARLINK. This requires working across numerous languages, helping customers through customer support scenarios, and onboarding new customers via sales:

- **20% conversion rate.** In 1 out of every 5 of sales inquiries, the customer purchases Starlink service while on the phone with Grok.
- **70% resolution rate.** The majority of customer support inquiries are resolved autonomously by the Grok Voice agent with no human in the loop.
- **28 tools.** This single agent uses dozens of distinct tools across hundreds of support and sales workflows.
- **Accuracy is critical.** Grok handles high-stakes decisions; the model autonomously performs hardware troubleshooting workflows, issues hardware replacements, and grants service credits.
