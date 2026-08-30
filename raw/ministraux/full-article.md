# Un Ministral, des Ministraux

**Source URL**: https://mistral.ai/news/ministraux/
**Published**: October 16, 2024
**Author**: Mistral AI team

## Introducing the world’s best edge models

On the first anniversary of the release of Mistral 7B, the model that revolutionized independent frontier AI innovation for millions, we are proud to introduce two new state-of-the-art models for on-device computing and at-the-edge use cases. We call them les Ministraux: Ministral 3B and Ministral 8B.

These models set a new frontier in knowledge, commonsense, reasoning, function-calling, and efficiency in the sub-10B category, and can be used or tuned to a variety of uses, from orchestrating agentic workflows to creating specialist task workers. Both models support up to 128k context length (currently 32k on vLLM) and Ministral 8B has a special interleaved sliding-window attention pattern for faster and memory-efficient inference.

### Use cases

Our most innovative customers and partners have increasingly been asking for local, privacy-first inference for critical applications such as on-device translation, internet-less smart assistants, local analytics, and autonomous robotics. Les Ministraux were built to provide a compute-efficient and low-latency solution for these scenarios. From independent hobbyists to global manufacturing teams, les Ministraux deliver for a wide variety of use cases.

Used in conjunction with larger language models such as Mistral Large, les Ministraux are also efficient intermediaries for function-calling in multi-step agentic workflows. They can be tuned to handle input parsing, task routing, and calling APIs based on user intent across multiple contexts at extremely low latency and cost.

### Benchmarks

We demonstrate the performance of les Ministraux across multiple tasks where they consistently outperform their peers. We re-evaluated all models with our internal framework for fair comparison.

#### Pretrained Models

![Pretrain Table](/_astro/4d41fad5-e10d-4839-be0d-894723cbf8ec_ZGh2x7.webp?dpl=6a22ec9594e7d400080f6dd3)

Table 1:Ministral 3B and 8B models compared to Gemma 2 2B, Llama 3.2 3B, Llama 3.1 8B and Mistral 7B on multiple categories

![Pretrain With Gemma](/_astro/190afc33-554d-4da7-adb6-95ab8e43a503_Zr7WNj.webp?dpl=6a22ec9594e7d400080f6dd3)

Figure 1:Ministral 3B and 8B base models compared to Gemma 2 2B, Llama 3.2 3B, Llama 3.1 8B and Mistral 7B

#### Instruct Models

![Instruct Table With Gemma](/_astro/e388324e-cfcf-4875-9bdb-d46d1fc4caf4_fK6wR.webp?dpl=6a22ec9594e7d400080f6dd3)

Table 2:Ministral 3B and 8B Instruct models compared to Gemma 2 2B, Llama 3.2 3B, Llama 3.1 8B, Gemma 2 9B and Mistral 7B on different evaluation categories.

![Instruct Plot 3b No Qwen With Mistral Logo](/_astro/36e0a7af-6d54-43ee-98ee-50143185cad4_dUDvq.webp?dpl=6a22ec9594e7d400080f6dd3)

Figure 2:A comparison of the 3B family of Instruct models - Gemma 2 2B, Llama 3.2 3B and Ministral 3B. The figure showcases the improvements of Ministral 3B over the much larger Mistral 7B.

![Instruct Plot 8b With Mistral Logo](/_astro/36b5e423-25a5-486a-92f0-f6daf9f0fafd_1Vr9pF.webp?dpl=6a22ec9594e7d400080f6dd3)

Figure 3:A comparison of the 8B family of Instruct models - Gemma 2 9B, Llama 3.1 8B, Mistral 7B and Ministral 8B.

### Availability and pricing

Both models are available starting today.

Model

API

Pricing on la Plateforme

License

Ministral 8B

ministral-8b-latest

$0.1 / M tokens (input and output)

Mistral Commercial LicenseMistral Research License

Ministral 3B

ministral-3b-latest

$0.04 / M tokens (input and output)

Mistral Commercial License

For self-deployed use,please reach out to usfor commercial licenses. We will also assist you in lossless quantization of the models for your specific use-cases to derive maximum performance.

The model weights forMinistral 8B Instructare available for research use. Both models will be available from ourcloud partnersshortly.

### More to come

At Mistral AI, we continue pushing the state-of-the-art for frontier models. It’s been only a year since the release of Mistral 7B, and yet our smallest model today (Ministral 3B) already outperforms it on most benchmarks. We can’t wait for you to try out les Ministraux and give us feedback.

![More to come](/_astro/c7e1cbb0-a254-4527-8984-57655bfbdaab_Z24yvCj.webp?dpl=6a22ec9594e7d400080f6dd3)
