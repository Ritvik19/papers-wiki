Source URL: https://cohere.com/blog/command-r-plus-microsoft-azure
Title: Introducing Command R+: A Scalable LLM Built for Business
Published: April 4, 2024

---

# Introducing Command R+: A Scalable LLM Built for Business

Command R+ is a state-of-the-art RAG-optimized model designed to tackle enterprise-grade workloads, and is available first on Microsoft Azure.

## Overview

Command R+ is a 104B state-of-the-art LLM designed to handle enterprise-grade workloads. It is the most powerful and scalable LLM in the Command R-series, which focuses on balancing efficiency with accuracy to enable businesses to move from proof-of-concept to production with AI. Command R+ features a 128k-token context window and offers:

- Advanced Retrieval Augmented Generation (RAG) with citation, which reduces hallucinations.
- Multilingual coverage in 10 key languages, supporting global business operations.
- Tool Use, which automates sophisticated business processes.

Developers and businesses can access Cohere's latest model first on Azure, starting today, and soon to be available on Oracle Cloud Infrastructure (OCI), as well as additional cloud platforms in the coming months.

Command R+ consistently beats Mistral Large and is on-par with GPT4-Turbo across multilingual, RAG, and tool-use capabilities on Azure-available models.

## Industry Leading RAG Solution

RAG has become a foundational building block for enterprises adopting LLMs and customizing them with their own proprietary data. Command R+ builds upon Command R's exceptional performance at RAG use cases.

Command R+ is optimized for advanced RAG to provide enterprise-ready, highly reliable, and verifiable solutions. The new model improves response accuracy and provides in-line citations that mitigate hallucinations and enable surfacing additional context from source materials.

![Human preference and multi-hop REACT evaluation](images/fig-3.png)

*Left: Human head-to-head preference results using a holistic grading scheme combining text fluency, citation quality, and overall utility. Right: Accuracy of multi-hop REACT agents powered by various models with access to the same search tools retrieving from Wikipedia (HotpotQA) and the internet.*

## Automating Complex Business Workflows With Tool Use

A major promise of large language models is their ability to not only ingest and produce text, but to act as core reasoning engines: capable of making decisions and using tools to automate difficult tasks.

New in Command R+, Cohere now supports **Multi-Step Tool Use** which allows the model to combine multiple tools over multiple steps to accomplish difficult tasks. Command R+ can even correct itself when it tries to use a tool and fails.

![Function-calling evaluation](images/fig-4.png)

*Evaluation of conversational tool-use and single-turn function-calling capabilities, using Microsoft's ToolTalk (Hard) benchmark and Berkeley's Function Calling Leaderboard (BFCL).*

## Multilingual Support for Global Business Operations

Command R+ is designed to serve as many people, organizations, and markets as possible. The model excels at 10 major languages of global business (English, French, Spanish, Italian, German, Portuguese, Japanese, Korean, Arabic, and Chinese).

This multilingual capability enables users to generate accurate responses from a vast set of data sources, regardless of their native language, helping power product features and tools for geographically diverse global companies.

![Multilingual evaluation](images/fig-5.png)

*Comparison on FLoRES (in French, Spanish, Italian, German, Portuguese, Japanese, Korean, Arabic, and Chinese) and WMT23 (in German, Japanese, and Chinese) translation tasks.*

Not only is Command R+ a strong multilingual model, but the R-series of models features a tokenizer that compresses non-English text much better than the tokenizer used for other models in the market, capable of achieving up to a 57% reduction in cost.

![Tokenizer token-cost comparison](images/fig-6.png)

*Comparison of the number of tokens produced by the Cohere, Mistral (Mixtral), and OpenAI tokenizers for different languages (as a multiple of the number of tokens produced by the Cohere tokenizer).*

## Performance and Availability

![Azure performance comparison](images/fig-2.png)

*Left: Performance comparison of models available on Azure across three key capabilities: Multilingual, RAG, and Tool Use. Right: Comparison of input and output token costs per million for models available on Azure.*

Model weights are available on Hugging Face for research and evaluation. Command R+ is available through Cohere's API and on Microsoft Azure.
