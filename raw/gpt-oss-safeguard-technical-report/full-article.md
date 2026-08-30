---
Source URL: https://openai.com/index/gpt-oss-safeguard-technical-report/
Fetched via: WebFetch (curl returns 403 on openai.com/index/*)
Date: October 29, 2025
---

# gpt-oss-safeguard technical report

Performance and baseline evaluations of gpt-oss-safeguard-120b and gpt-oss-safeguard-20b.

Two open-weight reasoning models, post-trained from the gpt-oss models, trained to reason from a provided policy to label content under that policy. Released under the Apache 2.0 license and OpenAI's gpt-oss usage policy. Text-only models compatible with the Responses API, customizable, provide full chain-of-thought, usable with different reasoning efforts (low, medium, high), and support Structured Outputs.

The report describes gpt-oss-safeguard's capabilities and baseline safety evaluations, using the underlying gpt-oss models as a baseline. OpenAI recommends using these models to classify content against a provided policy rather than as core functionality end users interact with directly; the original gpt-oss models are better suited to conversational use. Because gpt-oss-safeguard models are open, someone could use them in a chat setting, so the report verifies they meet safety standards in that usage and shares an initial multi-language performance evaluation in a chat setting (which does not directly assess policy-classification performance).

The gpt-oss-safeguard models are fine-tunes of their gpt-oss counterparts and were trained without additional biological or cybersecurity data. As a result, OpenAI determined that prior work estimating worst-case scenarios from the gpt-oss release applies to these new models as well.
