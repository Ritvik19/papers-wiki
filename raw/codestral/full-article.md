Source URL: https://mistral.ai/news/codestral/
Title: Codestral
Published: May 29, 2024

---

# Codestral

## A model fluent in 80+ programming languages

## Setting the Bar for Code Generation Performance

## Get started with Codestral

## Developer community feedbacks

We introduce Codestral, our first-ever code model. Codestral is an open-weight generative AI model explicitly designed for code generation tasks. It helps developers write and interact with code through a shared instruction and completion API endpoint. As it masters code and English, it can be used to design advanced AI applications for software developers.

Codestral is trained on a diverse dataset of 80+ programming languages, including the most popular ones, such as Python, Java, C, C++, JavaScript, and Bash. It also performs well on more specific ones like Swift and Fortran. This broad language base ensures Codestral can assist developers in various coding environments and projects.

Codestral saves developers time and effort: it can complete coding functions, write tests, and complete any partial code using a fill-in-the-middle mechanism. Interacting with Codestral will help level up the developer&#39;s coding game and reduce the risk of errors and bugs.

**Performance.** As a 22B model, Codestral sets a new standard on the performance/latency space for code generation compared to previous models used for coding.

Figure 1: With its larger context window of 32k (compared to 4k, 8k or 16k for competitors), Codestral outperforms all other models in RepoBench, a long-range eval for code generation..

We compare Codestral to existing code-specific models with higher hardware requirements.

**Python.** We use four benchmarks: HumanEval pass@1, MBPP sanitised pass@1 to evaluate Codestral&#39;s Python code generation ability, CruxEval to evaluate Python output prediction, and RepoBench EM to evaluate Codestral&#39;s Long-Range Repository-Level Code Completion.

**SQL.** To evaluate Codestral&#39;s performance in SQL, we used the Spider benchmark.

Additional languages. Additionally, we evaluated Codestral&#39;s performance in multiple HumanEval pass@1 across six different languages in addition to Python: C++, bash, Java, PHP, Typescript, and C#, and calculated the average of these evaluations.

FIM benchmarks. Codestral&#39;s Fill-in-the-middle performance was assessed using HumanEval pass@1 in Python, JavaScript, and Java and compared to DeepSeek Coder 33B, whose fill-in-the-middle capacity is immediately usable.

Codestral is a 22B open-weight model licensed under the new [ *Mistral AI Non-Production License* ](/news/mistral-ai-non-production-license-mnpl/), which means that you can use it for research and testing purposes. Codestral can be downloaded on [ HuggingFace ](https://huggingface.co/mistralai/Codestral-22B-v0.1).

If you want to use the model in the course of commercial activity, Commercial licenses are also available on demand by [ reaching out to the team ](/contact/).

With this release, comes the addition of a new endpoint: codestral.mistral.ai. This endpoint should be preferred by users who use our Instruct or Fill-In-the-Middle routes inside their IDE. The API Key for this endpoint is managed at the personal level and isn&#39;t bound by the usual organization rate limits. We&#39;re allowing use of this endpoint for free during a beta period of 8 weeks and are gating it [ behind a waitlist ](https://console.mistral.ai/codestral) to ensure a good quality of service. This endpoint should be preferred by developers implementing IDE plugins or applications where customers are expected to bring their own API keys.

Codestral is also immediately available on the usual API endpoint: api.mistral.ai where queries are billed per tokens. This endpoint and integrations are better suited for research, batch queries or third-party application development that exposes results directly to users without them bringing their own API keys.

You can create your account on [ la Plateforme ](https://console.mistral.ai) and start building your applications with Codestral by following [ this guide ](https://docs.mistral.ai/capabilities/code_generation/). Like all our other models, Codestral is available in our self-deployment offering starting today: [ contact sales ](/contact/).

We worked with community partners to expose Codestral to popular tools for developer productivity and AI application-making.

**Application frameworks.** Codestral is integrated into LlamaIndex and LangChain starting today, which allows users to build agentic applications with Codestral easily

**VSCode/JetBrains integration.** [ Continue.dev ](https://docs.mistral.ai/capabilities/code_generation/#integration-with-continuedev) and [ Tabnine ](https://docs.mistral.ai/capabilities/code_generation/#integration-with-tabnine) are empowering developers to use Codestral within the VSCode and JetBrains environments and now enable them to generate and chat with the code using Codestral.

[ Here ](https://www.youtube.com/watch?v=mjltGOJMJZA) is how you can use the Continue.dev VSCode plugin for code generation, interactive conversation, and inline editing with Codestral, and [ here ](https://www.youtube.com/watch?v=pFa4NLK9Lbw) is how users can use the Tabnine VSCode plugin to chat with Codestral.

For detailed information on how various integrations work with Codestral, please check [ our documentation ](https://docs.mistral.ai/capabilities/code_generation/) for set-up instructions and examples.

*&quot;A public autocomplete model with this combination of speed and quality hadn&#39;t existed before, and it&#39;s going to be a phase shift for developers everywhere.&quot;*

-- Nate Sesti, CTO and co-founder of Continue.dev

*&quot;We are excited about the capabilities that Mistral unveils and delighted to see a strong focus on code and development assistance, an area that JetBrains cares deeply about.&quot;*

-- Vladislav Tankov, Head of JetBrains AI

*&quot;We used Codestral to run a test on our Kotlin-HumanEval benchmark and were impressed with the results. For instance, in the case of the pass rate for T=0.2, Codestral achieved a score of 73.75, surpassing GPT-4-Turbo&#39;s score of 72.05 and GPT-3.5-Turbo&#39;s score of 54.66.&quot;*

-- Mikhail Evtikhiev, Researcher at JetBrains

*&quot;As a researcher at the company that created the first developer focused GenAI tool, I&#39;ve had the pleasure of integrating Mistal&#39;s new code model into our chat product. I am thoroughly impressed by its performance. Despite its relatively compact size, it delivers results on par with much larger models we offer to customers. We tested several key features, including code generation, test generation, documentation, onboarding processes, and more. In each case, the model exceeded our expectations. The speed and accuracy of the model will significantly impact our product&#39;s efficiency vs the previous Mistral model, allowing us to provide quick and precise assistance to our users. This model stands out as a powerful tool among the models we support, and I highly recommend it to others seeking high-quality performance.&quot;*

-- Meital Zilberstein, R&amp;D Lead @ Tabnine

*&quot;Cody speeds up the inner loop of software development, and developers use features like autocomplete to alleviate some of the day-to-day toil that comes with writing code. Our internal evaluations show that Mistral&#39;s new Codestral model significantly reduces the latency of Cody autocomplete while maintaining the quality of the suggested code. This makes it an excellent model choice for autocomplete where milliseconds of latency translate to real value for developers.&quot;*

*--* Quinn Slack, CEO and co-founder of Sourcegraph

*&quot;I&#39;ve been incredibly impressed with Mistral&#39;s new Codestral model for AI code generation. In my testing so far, it has consistently produced highly accurate and functional code, even for complex tasks. For example, when I asked it to complete a nontrivial function to create a new LlamaIndex query engine, it generated code that worked seamlessly, despite being based on an older codebase.&quot;*

-- Jerry Liu, CEO and co-founder of LlamaIndex

*&quot;Code generation is one of the most popular LLM use-cases, so we are really excited about the Codestral release. From our initial testing, it&#39;s a great option for code generation workflows because it&#39;s fast, has favorable context window, and the instruct version supports tool use. We tested with LangGraph for self-corrective code generation using the instruct Codestral tool use for output, and it worked really well out-of-the-box (see our *[ *video detailing this* ](https://youtu.be/zXFxmI9f06M)*).&quot;*

-- Harrison Chase, CEO and co-founder of LangChain
