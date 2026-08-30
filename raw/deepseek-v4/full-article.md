Source URL: https://unsloth.ai/docs/models/deepseek-v4
Title: DeepSeek-V4: How to Run Locally

> For the complete documentation index, see [llms.txt](https://unsloth.ai/docs/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://unsloth.ai/docs/models/deepseek-v4.md).

# DeepSeek-V4: How to Run Locally

DeepSeek-V4 is DeepSeek's new open models including **DeepSeek-V4-Pro** with **1.6T** parameters (49B active) and **DeepSeek-V4-Flash** with **284B** parameters (13B active). The models excel at coding, agentic workflows and chat with a **1M context** window. In this guide we'll show you how to run DeepSeek-V4-Flash locally: [DeepSeek-V4-Flash GGUF](https://huggingface.co/unsloth/DeepSeek-V4-Flash-GGUF)

For **lossless** DeepSeek, use Q8 (`UD-Q8_K_XL`), which is only **7GB larger** than Q4 (`UD-Q4_K_XL`). The lossless 8-bit GGUF is **162 GB** and 3-bit is **103GB** which can run on a **110GB RAM** devic&#x65;**.** DeepSeek-V4-Flash scores 86.2% on MMLU-Pro, 88.1% on GPQA Diamond, and 56.9% on Terminal Bench 2.0.

{% hint style="success" %}
**July 7:** DeepSeek-V4 is now ready to run! We also improved the [DeepSeek-V4 chat jinja template](#deepseek-v4-chat-template-improvements), and tested over 4000 conversations to be equivalent with the official baseline.
{% endhint %}

<a href="/pages/2f4eyCpdyRknNuEtv22n#usage-guide" class="button primary">Usage Guide</a><a href="/pages/2f4eyCpdyRknNuEtv22n#run-deepseek-v4-flash-tutorials" class="button primary">Running Tutorials</a>

### :llama: llama.cpp DeepSeek V4 implementation fixes

llama.cpp added DeepSeek V4 support in [24162](https://github.com/ggml-org/llama.cpp/pull/24162) - we noticed that when using any GGUF from **any provider**, multi turn conversations would not function well when compared to DS4's Hugging Face baseline when using KV cache quantization `--cache-type-k/v q8_0` - it has since been fixed and merged in llama.cpp since July 7th 2026 with [25202](https://github.com/ggml-org/llama.cpp/pull/25202)

Specifically before the fix, calling DeepSeek quants would cause `overlayotin kinetic academyléléléléulif` and after the PR "The capital of France is Paris." which is correct.

<table><thead><tr><th>Engine</th><th width="91.54998779296875">Score</th><th width="122.60003662109375">Calculation</th><th width="114.5">Tool selection</th><th width="97.4000244140625">Parallel Tools</th><th width="112.699951171875">Multi Turn tools</th><th>Nested tools</th></tr></thead><tbody><tr><td>Official code</td><td><strong>15/15</strong></td><td>3</td><td>3</td><td>3</td><td>3</td><td>3</td></tr><tr><td>Any provider</td><td><strong>4/15</strong></td><td>1</td><td>2</td><td>0</td><td>0</td><td>1</td></tr><tr><td><strong>After</strong> <a href="https://github.com/ggml-org/llama.cpp/pull/25202">25202</a></td><td><strong>15/15</strong></td><td>3</td><td>2</td><td>3</td><td>3</td><td>3</td></tr></tbody></table>

### :speech\_balloon: DeepSeek V4 Chat template improvements

We also improved the DeepSeek-V4 chat jinja template, and tested over 4000 conversations to be equivalent with the golden baseline (official DS4)

We added `reasoning_effort` and you can select `max, high` just like official DeepSeek-V4. We prepend the correct system prompt as per DS4, and followed gpt-oss's style.

And for tool calls, `reasoning_content` was retained for DS4, but the jinja chat template would exclude them. We added it back.

**Disabling Thinking, changing reasoning effort**

DeepSeek-V4 uses reasoning by default. It also supports reasoning efforts where `reasoning_effort` can be "high", "max" or disabled.

To disable thinking, use `--chat-template-kwargs '{"enable_thinking":false}'`. If you're on **Windows** Powershell, use: `--chat-template-kwargs "{\"enable_thinking\":false}"`

You can also use `--reasoning on` or `--reasoning off` in llama.cpp as well now!

For reasoning effort customization and or to disable reasoning, use the below examples:

```bash
--chat-template-kwargs '{"reasoning_effort":"max"}'
--chat-template-kwargs '{"reasoning_effort":"high"}'
--chat-template-kwargs '{"enable_thinking":false}'
```

### 📊 Quantization Analysis

Our `UD-Q8_K_XL` quant is fully lossless. DeepSeek-V4-Flash is [quantization-aware-trained](/docs/blog/quantization-aware-training-qat.md): the official checkpoint stores its routed experts (96% of the model) natively in MXFP4 and everything else in FP8 or BF16. GGUF's MXFP4 is exactly that format, so we repack the experts bit-for-bit, and FP8 dequantizes into BF16 with no rounding. We checked every tensor against the official DeepSeek weights: all 1,328 are bit-identical, and it stays lossless at inference (KL-divergence \~0, 100% top-token agreement).

**Non**-Unsloth DeepSeek-V4-Flash GGUFs were converted without these paths thus deviating from the official weights. `UD-Q4_K_XL` keeps the same bit-exact experts and only quantizes the non-expert tensors (4% of the model) to Q8\_0, so it sits right next to Q8 in size and quality.

<div align="left"><figure><img src="/files/FlH68xA9PuAhjGaaTcZK" alt="" width="563"><figcaption></figcaption></figure> <figure><img src="/files/su10XmPsPZ0IS5YXAkR9" alt="" width="563"><figcaption></figcaption></figure></div>

Measured against the official weights, both Unsloth quants are on the quality/size frontier. UD-Q8\_K\_XL is the only lossless point. UD-Q4\_K\_XL matches other community MXFP4 formats and is more accurate than the Q4\_K-experts conversions, which are larger yet land at 0.029 KLD.

<div align="left"><figure><img src="/files/0f8iIRtHl8bZ8jA0YqCL" alt="" width="563"><figcaption></figcaption></figure></div>

The error split by layer shows why. Keeping the native MXFP4 experts means 0% weight error at every layer. Conversions that re-quantize the experts to Q4\_K or IQ2\_XXS round almost every weight: 5% for Q4\_K, over 30% for IQ2\_XXS.

<div align="left"><figure><img src="/files/jhEBHfaV5gC2W7y3Tyc4" alt="" width="563"><figcaption><p>Our MXFP4 has exactly zero error on all 8.4M weights, while Q4_K, a different 4-bit grid, must round each one (5.2% RMSE).</p></figcaption></figure></div>

We also found using Q8\_0 and F16 for some tensors  is not lossless, and it gets worse since QAT was applied by DeepSeek to make MXFP4 / FP8 work well, so we had to leave them in BF16 directly. So use UD-Q8\_K\_XL for a true lossless quant, and UD-Q4\_K\_XL downcasts some of the BF16 items to Q8\_0.

For full benchmark tables of [GGUF Benchmarks, see here](#gguf-benchmarks).

#### ⚙️ Usage Guide

DeepSeek-V4-Flash is smaller and faster than DeepSeek-V4-Pro, with **284B** parameters (13B active), and a **1M context window**. The model has 3 modes, **Non-think**, **Think** **High** and **Think** **Max**.&#x20;

It's recommended to use `UD-IQ3_XXS` which is **103GB** for best results. Because the file size does not include KV cache, context allocation, try to have at least **110GB RAM** to run the model.

The `UD-Q8_K_XL` quant is DeepSeek-V4-Flash in full original precision. It is 162GB size and it's best to have at least 169GB of available RAM/VRAM available.

**Table: Inference hardware requirements** (units = total memory: RAM + VRAM, or unified memory)

<table><thead><tr><th width="129.8004150390625">1-bit</th><th width="130.85650634765625">2-bit</th><th width="140.26702880859375">3-bit</th><th>4-bit (near Lossless)</th><th>Q8_K_XL (Lossless)</th></tr></thead><tbody><tr><td>92 GB</td><td>102 GB</td><td>110-135 GB</td><td>162 GB</td><td>169 GB</td></tr></tbody></table>

{% hint style="success" %}
For best performance, make sure your total available memory, including VRAM and system RAM, exceeds the quantized model file size by a comfortable margin.
{% endhint %}

#### Recommended Settings

DeepSeek recommends these parameters for best performance: `temperature=1.0`, `top-p=1.0`

**Think High is on by default.** If disabled, you can enable it via: `--chat-template-kwargs '{"enable_thinking":true}'` or toggle it via the UI dropdown in [Unsloth Studio](#unsloth-studio-guide). Also see [#deepseek-v4-chat-template-improvements](#deepseek-v4-chat-template-improvements "mention")

{% columns %}
{% column %}

| `temperature = 1.0` |
| ------------------- |
| `top-p = 1.0`       |
| {% endcolumn %}     |

{% column %}

* **Maximum context window:** `1,048,576`
* For Think Max, set context to at least **384K tokens**.
  {% endcolumn %}
  {% endcolumns %}

## Run DeepSeek-V4-Flash Tutorials:

For this tutorial, we will use the 3-bit quant `UD-IQ3_XXS`, as it fits on a 128GB RAM device. Replace `UD-IQ3_XXS` with `UD-Q8_K_XL` (original quality) or another quant if your machine has enough memory. You can now run DeepSeek-V4-Flash in [Unsloth Studio](#run-in-unsloth-studio).

<a href="/pages/2f4eyCpdyRknNuEtv22n#unsloth-studio-guide" class="button primary">🦥 Unsloth Studio Guide</a><a href="/pages/2f4eyCpdyRknNuEtv22n#llama.cpp-guide" class="button primary">🦙 Llama.cpp Guide</a>

### 🦥 Unsloth Studio Guide

DeepSeek-V4-Flash can now be run and trained in [Unsloth Studio](/docs/new/studio.md), our new open-source web UI for local AI. Unsloth Studio lets you run models locally on **MacOS**, **Windows**, Linux and:

{% columns %}
{% column %}

* Search, download, [run GGUFs](/docs/new/studio.md#run-models-locally) and safetensor models
* [**Self-healing** tool calling](/docs/new/studio.md#execute-code--heal-tool-calling) + **web search**
* [**Code execution**](/docs/new/studio.md#run-models-locally) (Python, Bash)
* [Automatic inference](/docs/new/studio.md#model-arena) parameter tuning (temp, top-p, etc.)
* Fast CPU + GPU inference via llama.cpp
* [Train LLMs](/docs/new/studio.md#no-code-training) 2x faster with 70% less VRAM
  {% endcolumn %}

{% column %}

<div data-with-frame="true"><figure><img src="/files/KZrnxoc7x780uuArqGA8" alt=""><figcaption></figcaption></figure></div>
{% endcolumn %}
{% endcolumns %}

{% stepper %}
{% step %}

#### Install Unsloth

Ensure you use the latest version. Run in your terminal:

**MacOS, Linux, WSL:**

```bash
curl -fsSL https://unsloth.ai/install.sh | sh
```

**Windows PowerShell:**

```bash
irm https://unsloth.ai/install.ps1 | iex
```

{% endstep %}

{% step %}

#### Launch Unsloth

**MacOS, Linux, WSL and Windows:**

```bash
unsloth studio -H 0.0.0.0 -p 8888
```

Then open `http://127.0.0.1:8888` (or your specific URL) in your browser.
{% endstep %}

{% step %}

#### Search and download DeepSeek-V4-Flash

On first launch you will need to create a password to secure your account and sign in again. Then go to the [Unsloth Chat](/docs/new/studio/chat.md) tab and search for DeepSeek-V4-Flash in the search bar and download your desired model and quant.

<figure><img src="/files/QubGAIrqmsXW4C1ndaQH" alt="" width="563"><figcaption></figcaption></figure>
{% endstep %}

{% step %}

#### Run DeepSeek-V4-Flash

Inference parameters should be auto-set when using Unsloth Studio, however you can still change it manually. Because **Think High is on by default**, you can go to the right dropdown to toggle it to Non-think or Think Max. You can also edit the context length, chat template and other settings.

For more information, you can view our [Unsloth Studio inference guide](/docs/new/studio/chat.md).

<figure><img src="/files/2qv4RoQVOM1CwfLTB9nE" alt=""><figcaption></figcaption></figure>
{% endstep %}
{% endstepper %}

### 🦙 Llama.cpp Guide

{% stepper %}
{% step %}
Obtain the latest `llama.cpp` **on** [**GitHub here**](https://github.com/ggml-org/llama.cpp). You can follow the build instructions below as well. Change `-DGGML_CUDA=ON` to `-DGGML_CUDA=OFF` if you don't have a GPU or just want CPU inference. **For Apple Mac / Metal devices**, set `-DGGML_CUDA=OFF` then continue as usual - Metal support is on by default.

```bash
apt-get update
apt-get install pciutils build-essential cmake curl libcurl4-openssl-dev -y
git clone https://github.com/ggml-org/llama.cpp
cmake llama.cpp -B llama.cpp/build \
    -DBUILD_SHARED_LIBS=OFF -DGGML_CUDA=ON
cmake --build llama.cpp/build --config Release -j --clean-first --target llama-cli llama-mtmd-cli llama-server llama-gguf-split
cp llama.cpp/build/bin/llama-* llama.cpp
```

{% endstep %}

{% step %}
You can now use `llama.cpp` directly to load and download models, just like `ollama run`. First, select the quantization type you want like `IQ3_XXS`. Also use `export LLAMA_CACHE="folder"` to force `llama.cpp` to save to a specific location. Note this download process might be very slow, so it's probably best to use the manual download process in the next section.

```bash
export LLAMA_CACHE="unsloth/DeepSeek-V4-Flash-GGUF"
./llama.cpp/llama-cli \
    -hf unsloth/DeepSeek-V4-Flash-GGUF:UD-IQ3_XXS \
    --temp 1.0 \
    --top-p 1.0 \
    --min-p 0.0
```

{% endstep %}

{% step %}
If you want to download the model manually, we can download the model via the code below (after installing `pip install huggingface_hub`). If downloads get stuck, see: [Hugging Face Hub, XET debugging](/docs/basics/troubleshooting-and-faqs/hugging-face-hub-xet-debugging.md)

```bash
hf download unsloth/DeepSeek-V4-Flash-GGUF \
    --local-dir unsloth/DeepSeek-V4-Flash-GGUF \
    --include "*UD-IQ3_XXS*" # Use "*UD-IQ4_XS*" for 4-bit
```

{% endstep %}

{% step %}
You can edit `--threads 32` for the number of CPU threads, `--ctx-size 32768` for context length, `--n-gpu-layers 2` for GPU offloading on how many layers. Try adjusting it if your GPU goes out of memory. Also remove it if you have CPU only inference.

{% code overflow="wrap" %}

```bash
./llama.cpp/llama-cli \
    --model unsloth/DeepSeek-V4-Flash-GGUF/blob/main/UD-IQ3_XXS/DeepSeek-V4-Flash-UD-IQ3_XXS-00001-of-00004.gguf \
    --temp 1.0 \
    --top-p 1.0 \
    --min-p 0.0
```

{% endcode %}
{% endstep %}
{% endstepper %}

## 📊 Benchmarks

### GGUF Benchmarks

See below for a table comparing benchmarks for quants from Unsloth and other providers. Reference = official weights. Perplexity and KL-divergence over wikitext-2 at ctx 512 on 4x B200.

<figure><img src="/files/FlH68xA9PuAhjGaaTcZK" alt="" width="563"><figcaption></figcaption></figure>

| Quant                              | Size (GB) | PPL    | Mean KLD           | RMS delta-p | Same top token | Bit-exact weights |
| ---------------------------------- | --------- | ------ | ------------------ | ----------- | -------------- | ----------------- |
| Official (reference)               | 156.4     | 4.5319 | 0                  | 0%          | 100%           | 100%              |
| **Unsloth UD-Q8\_K\_XL**           | 161.9     | 4.5319 | **\~0 (lossless)** | 0.000%      | 100.000%       | **100.000%**      |
| **Unsloth UD-Q4\_K\_XL**           | 155.1     | 4.5335 | 0.0102             | 3.40%       | 96.28%         | 97.46%            |
| bartowski MXFP4                    | 156.0     | 4.5351 | 0.0105             | 3.42%       | 96.18%         | 97.57%            |
| antirez Q4KExperts-F16 (imatrix)   | 164.6     | 4.5743 | 0.0291             | 5.87%       | 93.95%         | 0.51%             |
| antirez Q4KExperts-F16             | 164.6     | 4.5726 | 0.0290             | 5.89%       | 93.94%         | 0.93%             |
| antirez mixed L37-42-Q4K (imatrix) | 97.6      | 5.8169 | 0.3605             | 21.15%      | 79.74%         | 0.41%             |
| antirez IQ2XXS (imatrix)           | 86.7      | 6.0808 | 0.4079             | 22.23%      | 78.15%         | 0.39%             |
| antirez IQ2XXS                     | 86.7      | 6.1518 | 0.4207             | 22.74%      | 77.92%         | 0.47%             |

### Official Benchmarks

See further below for benchmarks in table format:

<figure><img src="/files/hrAfCdALTQE8kOX8M9U3" alt="" width="563"><figcaption></figcaption></figure>

| Benchmark (Metric)          | V4-Flash Non-Think | V4-Flash High | V4-Flash Max | V4-Pro Non-Think | V4-Pro High | V4-Pro Max |
| --------------------------- | :----------------: | :-----------: | :----------: | :--------------: | :---------: | :--------: |
| **Knowledge & Reasoning**   |                    |               |              |                  |             |            |
| MMLU-Pro (EM)               |        83.0        |      86.4     |     86.2     |       82.9       |     87.1    |  **87.5**  |
| SimpleQA-Verified (Pass\@1) |        23.1        |      28.9     |     34.1     |       45.0       |     46.2    |  **57.9**  |
| Chinese-SimpleQA (Pass\@1)  |        71.5        |      73.2     |     78.9     |       75.8       |     77.7    |  **84.4**  |
| GPQA Diamond (Pass\@1)      |        71.2        |      87.4     |     88.1     |       72.9       |     89.1    |  **90.1**  |
| HLE (Pass\@1)               |         8.1        |      29.4     |     34.8     |        7.7       |     34.5    |  **37.7**  |
| LiveCodeBench (Pass\@1)     |        55.2        |      88.4     |     91.6     |       56.8       |     89.8    |  **93.5**  |
| Codeforces (Rating)         |          -         |      2816     |     3052     |         -        |     2919    |  **3206**  |
| HMMT 2026 Feb (Pass\@1)     |        40.8        |      91.9     |     94.8     |       31.7       |     94.0    |  **95.2**  |
| IMOAnswerBench (Pass\@1)    |        41.9        |      85.1     |     88.4     |       35.3       |     88.0    |  **89.8**  |
| Apex (Pass\@1)              |         1.0        |      19.1     |     33.0     |        0.4       |     27.4    |  **38.3**  |
| Apex Shortlist (Pass\@1)    |         9.3        |      72.1     |     85.7     |        9.2       |     85.5    |  **90.2**  |
| **Long Context**            |                    |               |              |                  |             |            |
| MRCR 1M (MMR)               |        37.5        |      76.9     |     78.7     |       44.7       |     83.3    |  **83.5**  |
| CorpusQA 1M (ACC)           |        15.5        |      59.3     |     60.5     |       35.6       |     56.5    |  **62.0**  |
| **Agentic**                 |                    |               |              |                  |             |            |
| Terminal Bench 2.0 (Acc)    |        49.1        |      56.6     |     56.9     |       59.1       |     63.3    |  **67.9**  |
| SWE Verified (Resolved)     |        73.7        |      78.6     |     79.0     |       73.6       |     79.4    |  **80.6**  |
| SWE Pro (Resolved)          |        49.1        |      52.3     |     52.6     |       52.1       |     54.4    |  **55.4**  |
| SWE Multilingual (Resolved) |        69.7        |      70.2     |     73.3     |       69.8       |     74.1    |  **76.2**  |
| BrowseComp (Pass\@1)        |          -         |      53.5     |     73.2     |         -        |     80.4    |  **83.4**  |
| HLE w/ tools (Pass\@1)      |          -         |      40.3     |     45.1     |         -        |     44.7    |  **48.2**  |
| MCPAtlas (Pass\@1)          |        64.0        |      67.4     |     69.0     |       69.4       |   **74.2**  |    73.6    |
| GDPval-AA (Elo)             |          -         |       -       |     1395     |         -        |      -      |  **1554**  |
| Toolathlon (Pass\@1)        |        40.7        |      43.5     |     47.8     |       46.3       |     49.0    |  **51.8**  |


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://unsloth.ai/docs/models/deepseek-v4.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
