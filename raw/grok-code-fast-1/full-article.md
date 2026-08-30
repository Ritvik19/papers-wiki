# Grok Code Fast 1

Aug 28, 2025

We're thrilled to introduce grok-code-fast-1, a speedy and economical reasoning model that excels at agentic coding.

## A speedy daily driver

While today's models are undeniably powerful, they often don't feel purpose-built for agentic coding workflows, where loops of reasoning and tool calls can feel frustratingly slow. As heavy users of agentic coding tools, our engineers saw room for a more nimble, responsive solution optimized for our day-to-day tasks.

We built `grok-code-fast-1` from scratch, starting with a brand-new model architecture. To lay a robust foundation, we carefully assembled a pre-training corpus rich with programming-related content. For post-training, we curated high-quality datasets that reflect real-world pull requests and coding tasks.

Throughout the training process, we collaborated closely with our launch partners to refine and sharpen the model's behavior inside their agentic platforms. `grok-code-fast-1` has mastered the use of common tools like grep, terminal, and file editing, and thus should feel right at home in your favorite IDE.

We've teamed up with select launch partners to offer `grok-code-fast-1` for free for a limited time, including GitHub Copilot, Cursor, Cline, Roo Code, Kilo Code, opencode, and Windsurf.

## Blazing fast

Our inference and supercomputing teams developed several innovative techniques to dramatically accelerate our serving speed, creating a uniquely responsive experience where the model will have already called dozens of tools before you even finish reading the first paragraph of the thinking trace. We've also invested in prompt caching optimizations, regularly achieving cache hit rates above 90% when used with our launch partners.

## A versatile programmer

`grok-code-fast-1` is exceptionally versatile across the full software development stack and is particularly adept at TypeScript, Python, Java, Rust, C++, and Go. It can complete common programming tasks with minimal oversight, ranging from building zero-to-one projects and providing insightful answers to codebase questions to performing surgical bug fixes.

## An economical choice

We designed `grok-code-fast-1` to be widely accessible, priced at:

- $0.20 per million input tokens
- $1.50 per million output tokens
- $0.02 per million cached input tokens

`grok-code-fast-1` was crafted to shine in the tasks developers face every day, striking a compelling balance between performance and cost. Its strength lies in delivering strong performance in a economical, compact form factor, making it a versatile choice for tackling common coding tasks quickly and cost-effectively.

### Model Performance

Tokens per Second vs Output Price

- Tokens per second (TPS): 190
- Output price per 1M tokens: $18

### Methodology

TPS metrics were calculated by directly measuring response generation speed via each model provider's API, considering only the final response tokens.

- Gemini 2.5 Pro, GPT-5, and Claude Sonnet 4: Measured using their respective public APIs.
- Grok Code Fast 1 and Grok 4: Measured using the xAI API.
- Qwen3-Coder: Hosted on DeepInfra at low precision (fp4), which reduces response quality.

We took a holistic approach to evaluating model performance, blending public benchmarks with real-world testing. On the full subset of SWE-Bench-Verified, `grok-code-fast-1` scored 70.8% using our own internal harness.

While benchmarks like SWE-Bench provide valuable insights, we've found they don't fully reflect the nuances of real-world software engineering, particularly the end-user experience in agentic coding workflows.

To guide our model training, we pair these benchmarks with routine human assessments, where experienced developers rate the model's end-to-end performance on everyday tasks. We've also built automated evaluations to track key aspects of behavior, helping us balance trade-offs in design.

When developing `grok-code-fast-1`, we focused on usability and user satisfaction, guided by real-world human evaluations. The result is a model rated by programmers as fast and reliable for everyday coding tasks.

## Grok Code for everyone

For a limited time, we're excited to offer `grok-code-fast-1` for free on exclusive launch partners. Here's what our launch partners had to say about our model, which was recently released in stealth under the codename `sonic`.

The model is generally available via the xAI API, priced at $0.20 / 1M input tokens, $1.50 / 1M output tokens, and $0.02 / 1M cached input tokens.

## What to expect in the next few weeks

Last week, we quietly released `grok-code-fast-1` under the codename `sonic`. During this stealth phase, our team carefully monitored community channels and deployed multiple new model checkpoints to address feedback.

As we advance this new model family, we're excited to iterate rapidly on your input. We highly value the developer community's support and encourage you to freely share all feedback, positive and negative.

We'll focus on delivering consistent updates to `grok-code-fast-1`, with improvements arriving in days rather than weeks. A new variant that supports multimodal inputs, parallel tool calling, and extended context length is already in training.

Read the `grok-code-fast-1` model card here. We're excited to see what you build!
