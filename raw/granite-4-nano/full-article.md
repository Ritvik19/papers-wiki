Source URL: https://huggingface.co/blog/ibm-granite/granite-4-nano
Title: Granite 4.0 Nano: Just how small can you go?

# Granite 4.0 Nano: Just how small can you go?

Enterprise Article. Published October 28, 2025

Kate Soule, Rameswar Panda (IBM Granite)

Today we are excited to share Granite 4.0 Nano, our smallest models yet, released as part of IBM's Granite 4.0 model family. Designed for the edge and on-device applications, these models demonstrate excellent performance for their size and represent IBM's continued commitment to develop powerful, useful models that don't require hundreds of billions of parameters to get the job done.

Like all Granite 4.0 models, the Nano models are released under an Apache 2.0 license with native architecture support on popular runtimes like vLLM, llama.cpp, and MLX. The models were trained with the same improved training methodologies, pipelines, and over 15T tokens of training data developed for the original Granite 4.0 models. This release includes variants benefiting from the Granite 4.0's new, efficient hybrid architecture, and like all Granite language models, the Granite 4.0 Nano models also carry with them IBM's ISO 42001 certification for responsible model development, giving users added confidence that models are built and governed to global standards.

Specifically, Granite 4.0 Nano comprises of 4 instruct models and their base model counterparts:

- **Granite 4.0 H 1B** – A ~1.5B parameter, dense LLM featuring a hybrid-SSM based architecture.
- **Granite 4.0 H 350M** – A ~350M parameter, dense LLM featuring a hybrid-SSM based architecture.
- **Granite 4.0 1B and Granite 4.0 350M** – Alternative traditional transformer versions of our 1B and 350M Nano models, designed to enable workloads where hybrid architectures may not yet have optimized support (e.g. Llama.cpp).

Building sub-billion to ~1 billion parameter models is an active and competitive space, with advancements in performance and architectures recently made by a number of model developers such as Alibaba (Qwen), LiquidAI (LFM), Google (Gemma) and others. When compared to these other models, Granite 4.0 Nano models demonstrate a significant increase in capabilities that can be achieved with a minimal parameter footprint, as measured by a series of general benchmarks across General Knowledge, Math, Code, and Safety domains.

Chart 1. Average accuracy of 0.2B-2B parameter models across Knowledge, Math, Code, and Safety benchmarks.

In addition to more general benchmarks, Granite Nano models outperformed several similarly sized models on tasks critical for agentic workflows, including instruction following and tool calling, as measured by IFEval and Berkley's Function Calling Leaderboard v3 (BFCLv3) benchmarks.

Chart 2. Accuracy on IFEval and BFCLv3 benchmarks.

Full details of the Granite 4.0 Nano can be found on the Hugging Face model cards. Moving forward, expect to see more releases from IBM as we continue to grow the Granite 4.0 family and work to make AI a more efficient and effective tool for developers.

## Collections mentioned in this article

- Granite 4.0 Language Models — Efficient language models for multilingual generation, coding, RAG, and AI assistant workflows. 11 items.
- Granite 4.0 Nano — Ultra-compact language models designed for the edge and on-device deployment. 9 items.
