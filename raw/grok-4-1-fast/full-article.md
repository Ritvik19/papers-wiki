# Grok 4.1 Fast and Agent Tools API

Nov 19, 2025

Bringing the next generation of tool-calling agents to the xAI API

Today, we're excited to launch two powerful new additions to the xAI API:

- Grok 4.1 Fast, our best tool-calling model with a 2M context window. It reasons and completes agentic tasks accurately and rapidly, excelling at complex real-world use cases such as customer support and finance.
- The Agent Tools API, which gives agents access to real-time X data, web search, remote code execution, and more.

Paired together, Grok 4.1 Fast and the Agent Tools API empower developers to build production-grade agents that specialize in tool calling and agentic search.

## Trained for the real world

We built Grok 4.1 Fast specifically for real-world enterprise use cases.

Through RL training in simulated environments, Grok 4.1 Fast was exposed to a wide variety of tools covering dozens of domains. This diverse training gives Grok 4.1 Fast exceptional performance on τ²-bench Telecom, a challenging benchmark that evaluates agentic tool use in real-world customer support scenarios.

## State-of-the-art tool calling

As developers build increasingly capable autonomous agents that plan over long horizons and operate independently, models must deliver intelligence without compromising speed and cost.

Grok 4.1 Fast is our answer: a model that combines frontier tool-calling performance with blazing-fast inference and cost effectiveness.

A common challenge for agentic models is that performance degrades as context length increases. We trained Grok 4.1 Fast using long-horizon reinforcement learning with a strong emphasis on multi-turn scenarios, ensuring consistent performance across its full 2-million-token context window.

# Agent Tools API

We're also launching the Agent Tools API, a suite of powerful server-side tools that allow Grok 4.1 Fast to operate as a fully autonomous agent.

With just a few lines of code, developers can enable Grok to browse the web, search X posts, execute code, retrieve uploaded documents, and more.

```python
import os
from xai_sdk import Client
from xai_sdk.tools import code_execution, web_search, x_search, collections_search, mcp

client = Client(api_key=os.getenv("XAI_API_KEY"))
chat = client.chat.create(
    model="grok-4-1-fast-reasoning",
    tools=[
        web_search(),
        x_search(),
        code_execution(),
        collections_search(collection_ids=["..."]),
        mcp(server_url="..."),
    ],
)
```

These tools run entirely on xAI's infrastructure, so developers no longer need to manage API keys, rate limits, sandboxes, or retrieval pipelines. Grok decides when and how to use them, often invoking multiple tools in parallel across several turns, until it has everything it needs to deliver a final answer.

## A full-featured toolset

The Agent Tools API is a versatile suite that lets you significantly extend the capabilities of our base Grok models. Key features include:

### Search Tools

Harness realtime X and internet search for fast, comprehensive insights into current events and trends.

### Files Search

Intelligently search and retrieve relevant documents from your uploaded files, with citations.

### Code Execution

Execute Python code in a secure sandbox to analyze data and run simulations.

### MCP Tools

Connect seamlessly to external MCP servers, enabling access to powerful custom third-party tools.

## The best agent for deep research

Real-time information retrieval and deep research are core strengths of Grok 4.1 Fast. With our native integration into the X ecosystem and powerful web-browsing capabilities, search agents powered by the xAI API are state-of-the-art on challenging agentic search benchmarks.

| Research-Eval | FRAMES | X Browse* |
| --- | --- | --- |
| Agent Tools API + Grok 4.1 Fast | 63.9 ($0.046) | 87.6 ($0.048) | 56.3 ($0.091) |
| GPT-5 | 45.5 ($0.107) | 86.0 ($0.058) | 24.2 ($0.198) |
| Claude Sonnet 4.5 | 41.2 ($0.065) | 85.0 ($0.078) | 14.6 ($0.126) |
| Gemini 3 Pro | 55.9 | 90.9 | 26.5 |

*X Browse is an internal benchmark that evaluates an agent's multihop search and browsing capabilities on X.

Grok 4.1 Fast sets a new standard in factuality, cutting the hallucination rate in half compared to Grok 4 Fast while still delivering performance on par with Grok 4 when evaluated on FActScore.

## Start Building

We're releasing two variants of Grok 4.1 Fast on the API:

- `grok-4-1-fast-reasoning` for maximal intelligence
- `grok-4-1-fast-non-reasoning` for instant responses

### Input pricing

- Input tokens: $0.20 / 1M tokens
- Cached input tokens: $0.05 / 1M tokens

### Output pricing

- Output tokens: $0.5 / 1M tokens
- Tool calls: From $5 / 1000 successful invocations

Start building with Grok 4.1 Fast today via the xAI API.
