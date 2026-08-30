# Command R: Retrieval-Augmented Generation at Production Scale

**Source URL**: https://cohere.com/blog/command-r
**Published**: 2024-03-11

## Introduction

*Command R is a scalable generative model targeting RAG and Tool Use to enable production-scale AI for enterprise.*

Today, we are introducing Command R, a new LLM aimed at large-scale production workloads. Command R targets the emerging “scalable” category of models that balance high efficiency with strong accuracy, enabling companies to move beyond proof of concept, and into production.

Command R is a generative model optimized for long context tasks such as retrieval-augmented generation (RAG) and using external APIs and tools. It is designed to work in concert with our industry-leading Embed and Rerank models to provide best-in-class integration for RAG applications and excel at enterprise use cases. As a model built for companies to implement at scale, Command R boasts:

Command R will be available immediately on Cohere’s hosted API, and on major cloud providers in the near future. In keeping with Cohere’s core principles, it maintains a focus on privacy and data security.

Command R is the first in a series of model releases advancing capabilities crucial to enterprise adoption at scale. We’re excited to share more soon.


## Retrieval-Augmented Generation (RAG)

Retrieval-augmented generation (RAG) has become a crucial pattern in the deployment of LLMs. RAG enables enterprises to give the model access to private knowledge that it otherwise would not have. By letting the model search over private databases and use that information to form responses, the accuracy and usefulness of the model changes dramatically. The key components to RAG are:

**Retrieval: **Cohere’s Embed model significantly improves the usefulness and accuracy of the retrieval step by improving contextual and semantic understanding when searching across millions or, even billions, of documents. Meanwhile, Cohere’s Rerank model further helps to improve the value of the information retrieved, optimizing the results across custom metrics, such as relevance and personalization.

**Augmented Generation: **With the most relevant information identified, Command R can summarize, analyze, package, and generally put that information to work in ways that help employees be more productive, or to create a magical new product experience. Unique to Command R, the model’s outputs come with clear citations that mitigate the risk of hallucinations, and enable surfacing additional context from the source materials.

Even without leveraging Cohere’s Embed and Rerank models, Command R outperforms others in the scalable category of generative models. When used together, the lead expands significantly, enabling higher performance in more complicated domains.


## Tool Use

LLMs should be core reasoning engines that can automate tasks and take real-world action, not just machines that ingest and generate text. Command R achieves this with the ability to use tools (APIs), such as code interpreters and other user-defined tools that enable the model to automate highly sophisticated tasks.

Tool Use enables developers at enterprises to turn Command R into an engine for powering the automation of tasks and workflows that require using internal infrastructure like databases and software tools, as well as external tools like CRMs, search engines, and more. This unlocks the automation of time-consuming and manual tasks that span multiple systems and require complex reasoning and decision making.

Tool Use is now available via our API, read more here.


## Multilingual Capabilities

Command R is designed to serve as many people, organizations, and markets as possible. The model excels at 10 major languages of global business: English, French, Spanish, Italian, German, Portuguese, Japanese, Korean, Arabic, and Chinese. In addition, our Embed and Rerank models serve over 100 languages natively.

This enables users to draw answers from a vast set of data sources, regardless of language, and have clear and accurate dialogues provided in their native tongue.


## Longer Context Window

Command R features a longer context length, supporting up to 128k tokens in this initial release. The upgrade also comes with a price reduction on Cohere’s hosted API, and significant efficiency improvements for Cohere’s private cloud deployments. By combining a longer context window with less expensive pricing, Command R unlocks RAG use cases where additional context can drive dramatic performance improvements.


## Availability and Deployment

Cohere works with all major cloud providers as well as on-prem for regulated industries and privacy-sensitive use cases, to make our models universally available.

To understand how your company can deploy these advanced RAG applications at production scale, reach out to our sales team.

Command R with RAG is now also in Cohere's demo environment, offering a hands-on experience for anyone to interact with the model through a simple chat interface.


## Research Weights

We strongly believe in both supporting academic AI research and allowing our models to be independently evaluated. As part of this, our non-profit research lab Cohere For AI is releasing the weights for this version of Command R publicly so that it can be used for research purposes. This is part of our wider support for the ML ecosystem alongside research compute grants and open source research releases like Aya.

For all enterprise and commercial use, Command R will continue to require a commercial license, and will be continually updated alongside our Rerank and Embed models.

You can access the weights on HuggingFace.


## Looking Ahead

At Cohere, we are focused on developing AI technology that is designed for use at production scale. As enterprises begin to transition from proof-of-concept projects to real-world production deployment it's becoming crucial to leverage scalable AI solutions.

Enterprises need an AI partner they can trust, and that’s why Cohere maintains a core focus on cloud choice and strict data privacy.

We are excited to hear user feedback on Command R and to see what developers build. We will continue to deliver scalable models that help companies succeed.


## Key Features

- Model weights available on HuggingFace for research and evaluationCommand R will be available immediately on Cohere’s hosted API, and on major cloud providers in the near future. In keeping with Cohere’s core principles, it maintains a focus on privacy and data security.
- Augmented Generation: Using the information retrieved to form a more informed response.**Retrieval: **Cohere’s Embed model significantly improves the usefulness and accuracy of the retrieval step by improving contextual and semantic understanding when searching across millions or, even billions, of documents. Meanwhile, Cohere’s Rerank model further helps to improve the value of the information retrieved, optimizing the results across custom metrics, such as relevance and personalization.