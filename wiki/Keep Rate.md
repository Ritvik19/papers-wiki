# Keep Rate

#concept

Keep Rate is an online quality metric used by Cursor for coding agents: for a set of agent-proposed code changes, it tracks the fraction that remain in the user's codebase after fixed time intervals. A low Keep Rate flags places where users had to manually adjust the agent's output or iterate to fix it, signaling that the initial response was lower quality than operational metrics like latency or token count would suggest.

## Why It Exists

[[Continually Improving Our Agent Harness]] argues that operational metrics — latency, token efficiency, tool-call count, cache-hit rate — are necessary but cannot answer whether the agent did a good job. Public benchmarks and CursorBench give offline reads, but neither catches the reality of how users interact with a deployed agent. Keep Rate fills that gap by measuring the fate of code in the wild: code that survives is implicitly accepted, code that disappears or is rewritten is implicitly rejected.

Keep Rate is paired with a complementary signal in the same article — an LLM that reads the user's reply to the agent's first output and infers satisfaction. A user moving on to a new feature is a positive signal; a user pasting a stack trace is a negative one. Together they give Cursor a quality read that does not depend on the user explicitly rating responses.

[[Introducing Cursor Router]] reuses both Keep Rate and user-response satisfaction classification as the quality metrics for evaluating [[Cursor Router]] in online A/B tests across millions of production requests. Cursor reports relying on these same signals for every model launch and harness improvement over the past nine months.

## Related

- [[Continually Improving Our Agent Harness]]
- [[Introducing Cursor Router]]
- [[Cursor Router]]
- [[Agent Harness]]
- [[CursorBench]]
- [[Evaluation and Benchmarks]]
- [[Code Models]]
- [[Tool Call Reliability]]
