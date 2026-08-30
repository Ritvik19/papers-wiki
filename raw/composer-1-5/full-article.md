# Introducing Composer 1.5

**Source URL**: https://cursor.com/blog/composer-1-5  
**Canonical HTML**: `raw/composer-1-5/full-article.html`

A few months ago, we released our first agentic coding model, [Composer 1](https://cursor.com/blog/composer). Since then, we've made significant improvements to the model's coding ability.

Our new release, Composer 1.5, strikes a strong balance between speed and intelligence for daily use. Composer 1.5 was built by scaling reinforcement learning 20x further on the same pretrained model. The compute used in our post-training of Composer 1.5 even surpasses the amount used to pretrain the base model.

We see continued improvements on coding ability as we scale. Measured by our internal benchmark of real-world coding problems, we find that the model quickly surpasses Composer 1 and continues to climb in performance. The improvements are most significant on challenging tasks.

Composer 1.5 is a thinking model. In the process of responding to queries, the model generates thinking tokens to reason about the user's codebase and plan next steps. We find that these thinking stages are critical to the model's intelligence. At the same time, we wanted to keep Composer 1.5 fast and interactive for day-to-day use. To achieve a balance, the model is trained to respond quickly on easy problems with minimal thinking, while on hard problems it will think until it has found a satisfying answer.

To handle longer running tasks, Composer 1.5 has the ability to self-summarize. This allows the model to continue exploring for a solution even when it runs out of available context. We train self-summarization into Composer 1.5 as part of RL by asking it to produce a useful summary when context runs out in training. This may trigger several times recursively on hard examples. We find that self-summarization allows the model to maintain its original accuracy as context length varies.

Composer 1.5 is a significantly stronger model than Composer 1 and we recommend it for interactive use. Its training demonstrates that RL for coding can be continually scaled with predictable intelligence improvements.

Learn more about Composer 1.5 pricing [here](https://cursor.com/blog/increased-agent-usage).

---

**Footnote 1 — Terminal-Bench 2.0**: Terminal-Bench 2.0 is an agent evaluation benchmark for terminal use maintained by the Laude Institute. Anthropic model scores use the Claude Code harness and OpenAI model scores use the Simple Codex harness. Cursor's score was computed using the official [Harbor evaluation framework](https://github.com/laude-institute/harbor) (the designated harness for Terminal-Bench 2.0) with default benchmark settings. They ran 2 iterations per model-agent pair and report the average. For other models besides Composer 1.5, they took the max score between the [official leaderboard](https://www.tbench.ai/leaderboard/terminal-bench/2.0) score and the score recorded running in their infrastructure.
