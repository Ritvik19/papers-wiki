# Grok 4 Fast

Sep 19, 2025

Pushing the Frontier of Cost-Efficient Intelligence

We're thrilled to present Grok 4 Fast, our latest advancement in cost-efficient reasoning models. Built on xAI's learnings from Grok 4, Grok 4 Fast delivers frontier-level performance across Enterprise and Consumer domains—with exceptional token efficiency. This model pushes the boundaries for smaller and faster AI, making high-quality reasoning accessible to more users and developers. Grok 4 Fast features state-of-the-art (SOTA) cost-efficiency, cutting-edge web and X search capabilities, a 2M token context window, and a unified architecture that blends `reasoning` and `non-reasoning` modes in one model.

## Advancing Cost-Efficient Intelligence

Grok 4 Fast sets a new frontier in cost-efficient intelligence, outperforming Grok 3 Mini across reasoning benchmarks while slashing token costs.

| Benchmark pass@1 | Grok 4 Fast | Grok 4 | Grok 3 Mini (High) | GPT-5 (High) | GPT-5 Mini (High) |
| --- | --- | --- | --- | --- | --- |
| GPQA Diamond | 85.7% | 87.5% | 79.0% | 85.7% | 82.3% |
| AIME 2025 (no tools) | 92.0% | 91.7% | 83.0% | 94.6% | 91.1% |
| HMMT 2025 (no tools) | 93.3% | 90.0% | 74.0% | 93.3% | 87.8% |
| HLE (no tools) | 20.0% | 25.4% | 11.0% | 24.8% | 16.7% |
| LiveCodeBench (Jan-May) | 80.0% | 79.0% | 70.0% | 86.8% | 77.4% |

We used large-scale reinforcement learning to maximize the intelligence density of Grok 4 Fast. In our evaluations, Grok 4 Fast achieves comparable performance to Grok 4 on benchmarks while using 40% fewer thinking tokens on average.

This 40% increase in Grok 4 Fast's token efficiency, combined with a significantly lower price per token, results in a 98% reduction in price to achieve the same performance on frontier benchmarks as Grok 4. As verified by an independent review from Artificial Analysis, Grok 4 Fast exhibits a state-of-the-art (SOTA) price-to-intelligence ratio compared to other publicly available models on the Artificial Analysis Intelligence Index.

## Native Tool Use with SOTA Search

Grok 4 Fast was trained end-to-end with tool-use reinforcement learning (RL). It excels at deciding when to invoke tools like code execution or web browsing.

For instance, Grok 4 Fast exhibits frontier agentic search capabilities, seamlessly browsing the web and X to augment queries with real-time data. It hops through links, ingests media (including images and videos on X), and synthesizes findings at light speed.

| Benchmark pass@1 | Grok 4 Fast | Grok 4 | Grok 3 (No Reasoning) |
| --- | --- | --- | --- |
| BrowseComp | 44.9% | 43.0% | — |
| SimpleQA | 95.0% | 94.0% | 82.0% |
| Reka Research Eval | 66.0% | 58.0% | 37.0% |
| BrowseComp (zh) | 51.2% | 45.0% | 10.8% |
| X Bench Deepsearch (zh) | 74.0% | 66.0% | 27.0% |
| X Browse* | 58.0% | 53.2% | 20.8% |

*X Browse is an internal benchmark evaluating agent's multihop search and browsing capabilities on X.

## Frontier of General Post-training

Grok 4 Fast also establishes a new cost-effective frontier on general domain. We are excited to share Grok 4 Fast's result on LMArena, where it has been privately battle-testing on the Search and Text Arenas.

In LMArena's Search Arena, `grok-4-fast-search` (code name: `menlo`) claims #1 with 1163 Elo — a commanding margin of 17 over `o3-search`. Its superior reasoning efficiency and intelligence density enable it to surpass much larger models on real-world, search-related tasks.

In LMArena's Text Arena, `grok-4-fast` (code name: `tahoe`) ranks #8, performing on par with `grok-4-0709` and highlighting its remarkable intelligence density. Notably, it significantly outperforms peers in its weight class, where all comparable size models rank 18th or below.

## Unified Model: Reasoning and Non-Reasoning

Previously, separate reasoning modes required distinct models. Grok 4 Fast introduces a unified architecture where `reasoning` (long chain-of-thought) and `non-reasoning` (quick responses) are handled by the same model weights, steered via system prompts. This unification reduces end-to-end latency as well as token costs, making Grok 4 Fast ideal for real-time applications.

In grok.com, this results in smooth transitions: responding instantly for simple queries or engaging in extended reasoning for complex ones. In the xAI API, developers can fine-tune this behavior, optimizing for speed or depth.

## Grok 4 Fast in grok.com, iOS, and Android apps

Grok 4 Fast is available now for all users. In `Fast` and `Auto` modes, you will see a significant improvement in search and information seeking queries. Additionally, difficult queries in `Auto` mode will use Grok 4 Fast, which will provide a much faster experience without loss of quality. For the first time, all users, including free users, will have access to our latest model without restrictions, marking a step toward democratizing advanced AI.

## Grok 4 Fast on OpenRouter, Vercel AI Gateway, and the xAI API

We're rolling out Grok 4 Fast as two models: `grok-4-fast-reasoning` and `grok-4-fast-non-reasoning`, each with a 2M token context window. This allows developers to tune the amount of test-time compute applied to their use cases.

| Token Type | <128k tokens | ≥128k tokens |
| --- | --- | --- |
| Input tokens | $0.20 / 1M | $0.40 / 1M |
| Output tokens | $0.50 / 1M | $1.00 / 1M |
| Cached input tokens | $0.05 / 1M | — |

## What's Next

We will continuously ship model improvements to Grok 4 Fast based on your feedback on x.com. Stay tuned for further integrations, including enhanced multimodal capabilities and agentic features.

Read the Grok 4 Fast model card here.
