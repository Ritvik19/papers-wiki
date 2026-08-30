# Tool Call Reliability

#concept

Tool call reliability is the practice of measuring, classifying, and alerting on errors that occur when an agent calls a tool exposed by its [[Agent Harness]]. Because failed tool calls remain in the conversation transcript, they waste tokens, induce [[Context Rot]], and can derail an entire session, so the harness treats per-tool error rates as a first-class production signal alongside accuracy.

## Cursor's Classification

[[Continually Improving Our Agent Harness]] describes the operational scheme Cursor uses:

- **Unknown errors** are treated as bugs unconditionally. The harness alerts whenever the unknown-error rate for any tool exceeds a fixed threshold.
- **Expected errors** capture cases where the model or environment is at fault rather than the harness. Categories include `InvalidArguments` and `UnexpectedEnvironment` (model mistakes and contradictions in the context window), `ProviderError` (vendor outages from tools like `GenerateImage` or `WebSearch`), `UserAborted`, and `Timeout`.
- **Anomaly detection** catches expected errors that have spiked. Baselines are computed per-tool and per-model because different models err at different rates, so a flat threshold would either miss real regressions or fire on benign differences.

A focused Cursor sprint earlier in 2026 drove all tool calls to at least two and often three nines of reliability and cut unknown tool-call errors by an order of magnitude. The harness now also runs a weekly automation that searches logs for new or recently spiked issues, files Linear tickets with investigations, and lets Cloud Agents kick off fixes in parallel — what the article calls an automated "software factory" for the harness.

## Why It Matters For Agents

Reliability is upstream of agent quality, not adjacent to it. A failed tool call typically remains visible to the model in subsequent turns, biasing later decisions and consuming the context window the agent could otherwise use for productive work. This makes tool call reliability one of the load-bearing pieces of dynamic-context agent design, because every dynamic affordance the harness adds is also a new failure surface to monitor.

## Related

- [[Agent Harness]]
- [[Continually Improving Our Agent Harness]]
- [[Dynamic Context]]
- [[Context Rot]]
- [[Papers Explained 445 - Context Rot]]
- [[Evaluation and Benchmarks]]
- [[Agentic AI]]
