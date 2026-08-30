Source URL: https://unsloth.ai/docs/models/qwen3.6
Title: Qwen3.6 - How to Run Locally

> For the complete documentation index, see [llms.txt](https://unsloth.ai/docs/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://unsloth.ai/docs/models/qwen3.6.md).

# Qwen3.6 - How to Run Locally

Qwen3.6 is Alibaba’s new family of multimodal hybrid-thinking models, including: **Qwen3.6-27B** and **35B-A3B**. It delivers top performance for its size, supports 256K context across 201 languages. It excels in agentic coding, vision, chat tasks. Qwen3.6-27B runs on **18GB RAM** setups and 35B-A3B runs on **22GB**. You can now run and train the models in [Unsloth Studio](#unsloth-studio-guide).

{% hint style="success" %}
**July 10:** We released new [**NVFP4** quants](#nvfp4) to run Qwen3.6 2.5x faster on GPUs.

[**Qwen3.6 MTP is here**](#mtp-guide)**!** MTP enables 1.4-2.2x faster inference without accuracy loss. Run MTP directly in [Unsloth Studio](#unsloth-studio-mtp-guide). We conducted [Qwen3.6 GGUF Benchmarks](#unsloth-gguf-benchmarks) to help you pick the best quant.
{% endhint %}

<a href="/pages/NpuhjPsxi8BKhuS8nnyY#qwen3.6-inference-tutorials" class="button primary">Run Qwen3.6 Tutorials</a><a href="/pages/NpuhjPsxi8BKhuS8nnyY#mtp-guide" class="button primary">MTP Guide</a>

{% columns %}
{% column %}
Qwen3.6 GGUFs use Unsloth [Dynamic 2.0](/docs/basics/unsloth-dynamic-2.0-ggufs.md) for SOTA quant performance - so quants are calibrated on real world use-case datasets and important layers are upcasted. *Thank you Qwen for day zero access.*

* **Developer Role Support** for Codex, OpenCode and more:\
  Our uploads now support the `developer role` for agentic coding tools.
* **Tool calling:** Like [Qwen3.5](/docs/models/qwen3.5.md), we improved parsing nested objects to make tool calling succeed more.
  {% endcolumn %}

{% column %}

<div data-with-frame="true"><figure><img src="/files/PxQ3x37GwzkPPjHW6pVh" alt=""><figcaption><p>Qwen3.6 running in <a href="#unsloth-studio-guide">Unsloth Studio</a>.</p></figcaption></figure></div>
{% endcolumn %}
{% endcolumns %}

### :gear: Usage Guide

**Table: Inference hardware requirements** (units = total memory: RAM + VRAM, or unified memory)

<table><thead><tr><th>Qwen3.6</th><th>3-bit</th><th>4-bit</th><th width="128">6-bit</th><th>8-bit</th><th>BF16</th></tr></thead><tbody><tr><td><strong>27B</strong></td><td>15 GB</td><td>18 GB</td><td>24 GB</td><td>30 GB</td><td>55 GB</td></tr><tr><td><strong>35B-A3B</strong></td><td>17 GB</td><td>23 GB</td><td>30 GB</td><td>38 GB</td><td>70 GB</td></tr></tbody></table>

{% hint style="success" %}
For best performance, make sure your total available memory (VRAM + system RAM) exceeds the size of the quantized model file you’re downloading. If it doesn’t, llama.cpp can still run via SSD/HDD offloading, but inference will be slower.
{% endhint %}

{% hint style="warning" %}
Do NOT use CUDA 13.2 as you may get gibberish outputs. Use below CUDA 13.2 or CUDA 13.3.
{% endhint %}

**To train Qwen3.6, you can refer to our previous** [**Qwen3.5 fine-tuning guide**](/docs/models/qwen3.5/fine-tune.md)**.**

### Recommended Settings

* **Maximum context window:** `262,144` (can be extended to 1M via YaRN)
* `presence_penalty = 0.0 to 2.0` default this is off, but to reduce repetitions, you can use this, however using a higher value may result in **slight decrease in performance**
* **Adequate Output Length**: `32,768` tokens for most queries

{% hint style="info" %}
If you're getting gibberish, your context length might be set too low. Or try using `--cache-type-k bf16 --cache-type-v bf16` which might help.
{% endhint %}

As Qwen3.6 is hybrid reasoning, thinking and non-thinking mode have different settings:

#### Thinking mode:

{% hint style="success" %}
Qwen3.6 now has [Preserve Thinking](#turn-on-off-thinking--preserve-thinking).
{% endhint %}

| General tasks                     | Precise coding tasks (e.g. WebDev) |
| --------------------------------- | ---------------------------------- |
| temperature = 1.0                 | temperature = 0.6                  |
| top\_p = 0.95                     | top\_p = 0.95                      |
| top\_k = 20                       | top\_k = 20                        |
| min\_p = 0.0                      | min\_p = 0.0                       |
| presence\_penalty = 0.0           | presence\_penalty = 0.0            |
| repeat\_penalty = disabled or 1.0 | repeat\_penalty = disabled or 1.0  |

{% columns %}
{% column %}
Thinking mode for general tasks:

{% code overflow="wrap" %}

```bash
temperature=1.0, top_p=0.95, top_k=20, min_p=0.0, presence_penalty=0.0, repetition_penalty=1.0
```

{% endcode %}
{% endcolumn %}

{% column %}
Thinking mode for precise coding tasks:

{% code overflow="wrap" %}

```bash
temperature=0.6, top_p=0.95, top_k=20, min_p=0.0, presence_penalty=0.0, repetition_penalty=1.0
```

{% endcode %}
{% endcolumn %}
{% endcolumns %}

#### Instruct (non-thinking) mode settings:

| General tasks                     |
| --------------------------------- |
| temperature = 0.7                 |
| top\_p = 0.8                      |
| top\_k = 20                       |
| min\_p = 0.0                      |
| presence\_penalty = 1.5           |
| repeat\_penalty = disabled or 1.0 |

{% hint style="warning" %}
To [disable thinking / reasoning](#how-to-enable-or-disable-reasoning-and-thinking), use `--chat-template-kwargs '{"enable_thinking":false}'`

If you're on **Windows** Powershell, use: `--chat-template-kwargs "{\"enable_thinking\":false}"`

Use 'true' and 'false' interchangeably.
{% endhint %}

Instruct (non-thinking) for general tasks:

{% code overflow="wrap" %}

```bash
temperature=0.7, top_p=0.8, top_k=20, min_p=0.0, presence_penalty=1.5, repetition_penalty=1.0
```

{% endcode %}

## Qwen3.6 Inference Tutorials:

We'll be using Dynamic 4-bit `UD-Q4_K_XL` GGUF variants for inference workloads. Click below to navigate to designated model instructions:

<a href="/pages/JcwJOcoquFknfeDFxM7k#unsloth-studio-guide" class="button primary">Run in Unsloth Studio</a><a href="/pages/NpuhjPsxi8BKhuS8nnyY#llama.cpp-guide" class="button secondary">Run in llama.cpp</a><a href="/pages/NpuhjPsxi8BKhuS8nnyY#mtp-guide" class="button primary">MTP Guide</a><a href="/pages/NpuhjPsxi8BKhuS8nnyY#nvfp4" class="button secondary">NVFP4 Guide</a>

{% hint style="warning" %}
Do NOT use CUDA 13.2 as you may get gibberish outputs. Use below CUDA 13.2 or CUDA 13.3.
{% endhint %}

### 🦥 Unsloth Studio Guide

Qwen3.6 and Qwen3.6 MTP can now be run in [Unsloth Studio](/docs/new/studio.md), our new open-source web UI for local AI. Unsloth Studio lets you run models locally on **MacOS, Windows**, Linux and:

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

<div data-with-frame="true"><figure><img src="/files/vTGOOXiSgQ6qXSrMZMMw" alt=""><figcaption></figcaption></figure></div>
{% endcolumn %}
{% endcolumns %}

{% stepper %}
{% step %}

#### Install Unsloth

Run in your terminal:

**MacOS, Linux, WSL:**

```bash
curl -fsSL https://unsloth.ai/install.sh | sh
```

**Windows PowerShell:**

```bash
irm https://unsloth.ai/install.ps1 | iex
```

{% hint style="success" %}
**Installation will be quick and take approx 20 sec - 1 mins.**
{% endhint %}
{% endstep %}

{% step %}

#### Launch Unsloth

**MacOS, Linux, WSL and Windows:**

```bash
unsloth studio -H 0.0.0.0 -p 8888
```

<div data-with-frame="true"><figure><img src="/files/J8BaejVXrezdt6B1aeUy" alt="" width="375"><figcaption></figcaption></figure></div>

Then open `http://127.0.0.1:8888` (or your specific URL) in your browser.

**Launch Unsloth securely with HTTPS and Cloudflare**

**NEW!** Unsloth now provides a secure way to launch Unsloth over HTTPS through a free Cloudflare tunnel. Use the below (works in Windows, Mac & Linux):

```bash
unsloth studio --secure
```

{% endstep %}

{% step %}

#### Search and download Qwen3.6 or Qwen3.6 MTP

On first launch you will need to create a password to secure your account and sign in again later. Then go to the [Unsloth Chat](/docs/new/studio/chat.md) tab and search for Qwen3.6 or Qwen3.6 MTP in the search bar and download your desired model and quant.

<div data-with-frame="true"><figure><img src="/files/kNGckTKk9g9gMgbj0Wg2" alt="" width="375"><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}

#### Run Qwen3.6

Inference parameters should be auto-set when using Unsloth Studio, however you can still change it manually. You can also edit the context length, chat template and other settings.

For more information, you can view our [Unsloth Studio inference guide](/docs/new/studio/chat.md). Below, the 2-bit Qwen3.6 GGUF made 30+ tool calls, searched 20 sites and executed Python code:

{% embed url="<https://cdn-uploads.huggingface.co/production/uploads/62ecdc18b72a69615d6bd857/9lqVQm1qDX3elt6Uan5Vm.mp4>" %}
{% endstep %}
{% endstepper %}

### ⚡ MTP Guide

MTP (Multi Token Prediction) speculative decoding enables models like Qwen3.6 to have **\~1.4-2.2x faster generation with&#x20;**<mark style="background-color:$success;">**no change in accuracy**</mark>. This enables Qwen3.6 27B and 35B-A3B to have **>1.4x speed-up** over the original baseline which is especially useful for local models.

Unsloth Qwen3.6 MTP GGUFs are no longer in experimental mode, and llama.cpp has merged MTP support. Run directly in [Unsloth Studio’s UI](#unsloth-studio-guide) or via llama.cpp. **Qwen3.6 27B MTP now runs at 160 tokens/s generation and Qwen3.6 35B-A3B at 240 tokens/s on a RTX 6000 GPU.** See [#mtp-benchmarks](#mtp-benchmarks "mention").

Unsloth Studio automatically sets the ideal MTP settings optimized for your specific hardware (Mac, CPU, GPU etc.) - you can still change it later.

{% hint style="info" %}
**MTP uses slightly more VRAM than standard GGUFs**, so plan for \~1 GB additional RAM/VRAM headroom.
{% endhint %}

<a href="/pages/NpuhjPsxi8BKhuS8nnyY#unsloth-studio-mtp-guide" class="button primary">Run in Unsloth Studio</a><a href="/pages/NpuhjPsxi8BKhuS8nnyY#llama.cpp-mtp-guide" class="button secondary">Run in llama.cpp</a><a href="/pages/NpuhjPsxi8BKhuS8nnyY#nvfp4" class="button secondary">Run NVFP4</a>

| [Qwen3.6-27B-MTP-GGUF](https://huggingface.co/unsloth/Qwen3.6-27B-MTP-GGUF) | [Qwen3.6-35B-A3B-MTP-GGUF](https://huggingface.co/unsloth/Qwen3.6-35B-A3B-MTP-GGUF) |
| --------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |

<div><figure><img src="/files/PcJYNAL2D5V189UKVHV9" alt=""><figcaption></figcaption></figure> <figure><img src="/files/2zkvs1iYgzwBfLxGi6Ap" alt=""><figcaption></figcaption></figure></div>

In practice, MTP predicts several future tokens, then the main model verifies those tokens in parallel. This reduces the number of forward passes needed during generation and make output faster. **We found `--spec-draft-n-max 2` to work best in most setups.** **However, do not assume `2` is optimal, as performance is hardware-dependent. Try values from `1` through `6` and use whichever is fastest for your system.**

We also [uploaded MTP GGUFs](https://huggingface.co/unsloth/models?search=mtp) for the [**Qwen3.5**](/docs/models/qwen3.5.md) **model family** including: 0.8B, 2B, 4B, 9B, 27B, 35B-A3B, 122B-A10B and 397B-A17B. Llama.cpp is continually improving MTP performance, so expect it to get faster overtime!

**Table: MTP hardware requirements** (units = total memory: RAM + VRAM, or unified memory)

<table><thead><tr><th>Qwen3.6</th><th>3-bit</th><th>4-bit</th><th width="128">6-bit</th><th>8-bit</th><th>BF16</th></tr></thead><tbody><tr><td><strong>27B</strong></td><td>16 GB</td><td>19 GB</td><td>25 GB</td><td>31 GB</td><td>56 GB</td></tr><tr><td><strong>35B-A3B</strong></td><td>18 GB</td><td>24 GB</td><td>31 GB</td><td>39 GB</td><td>71 GB</td></tr></tbody></table>

#### 🦥 Unsloth Studio MTP Guide

Unsloth Studio automatically sets the ideal MTP settings optimized for your specific hardware (Mac, CPU, GPU etc.) - you can still change it later.

{% stepper %}
{% step %}

#### Install Unsloth

Run in your terminal:

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
unsloth studio -H 127.0.0.1 -p 8888
```

Then open `http://127.0.0.1:8888` (or your specific URL) in your browser.
{% endstep %}

{% step %}

#### Search and download Qwen3.6 MTP

On first launch you will need to create a password to secure your account and sign in again later. Then go to the [Unsloth Chat](/docs/new/studio/chat.md) tab and search for Qwen3.6 MTP in the search bar and download your desired model and quant.

<div data-with-frame="true"><figure><img src="/files/X2vsCuTdYdpQNQ6ZIMB6" alt="" width="375"><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}

#### Run Qwen3.6 MTP

Inference parameters should be auto-set when using Unsloth Studio, however you can still change it manually. You can also edit the context length, chat template and other settings.

For more information, you can view our [Unsloth Studio inference guide](/docs/new/studio/chat.md). Below, the 2-bit Qwen3.6 MTP GGUF made 10+ tool calls, searched 10 sites and executed Python code:

<div data-with-frame="true"><figure><img src="/files/GpNoIzyrR7boop0DbLNf" alt=""><figcaption></figcaption></figure></div>
{% endstep %}
{% endstepper %}

#### 🦙 Llama.cpp MTP Guide

{% stepper %}
{% step %}
Install the latest version of `llama.cpp` on [**GitHub here**](https://github.com/ggml-org/llama.cpp/pull/22673). You can follow the build instructions below as well. Change `-DGGML_CUDA=ON` to `-DGGML_CUDA=OFF` if you don't have a GPU or just want CPU inference. **For Apple Mac / Metal devices**, set `-DGGML_CUDA=OFF` then continue as usual - Metal support is on by default.

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
If you want to use `llama.cpp` directly to load models, you can do the below: (:`Q4_K_XL`) is the quantization type. You can also download via Hugging Face (point 3). This is similar to `ollama run` . Use `export LLAMA_CACHE="folder"` to force `llama.cpp` to save to a specific location. The model has a maximum of 256K context length.

Follow one of the commands for the specific models:

<a href="/pages/NpuhjPsxi8BKhuS8nnyY#mtp-qwen3.6-27b" class="button primary">27B MTP</a><a href="/pages/NpuhjPsxi8BKhuS8nnyY#mtp-qwen3.6-35b-a3b" class="button primary">35-A3B MTP</a>

#### MTP Qwen3.6-27B:

**Thinking mode:**

{% hint style="info" %}
Please see Qwen3.6's new [Preserved Thinking](#thinking-enable-disable--preserve-thinking).
{% endhint %}

General tasks:

```bash
export LLAMA_CACHE="unsloth/Qwen3.6-27B-MTP-GGUF"
./llama.cpp/llama-cli \
    -hf unsloth/Qwen3.6-27B-MTP-GGUF:UD-Q4_K_XL \
    --temp 1.0 \
    --top-p 0.95 \
    --top-k 20 \
    --min-p 0.00 \
    --spec-type draft-mtp --spec-draft-n-max 2
```

For precise coding tasks, change: `temperature=0.6`

**Non-thinking mode:**

General tasks:

```bash
export LLAMA_CACHE="unsloth/Qwen3.6-27B-MTP-GGUF"
./llama.cpp/llama-server \
    -hf unsloth/Qwen3.6-27B-MTP-GGUF:UD-Q4_K_XL \
    --temp 0.7 \
    --top-p 0.8 \
    --top-k 20 \
    --presence-penalty 1.5 \
    --min-p 0.00 \
    --spec-type draft-mtp --spec-draft-n-max 2 \
    --chat-template-kwargs '{"enable_thinking":false}'
```

#### MTP Qwen3.6-35B-A3B:

**Thinking mode:**

{% hint style="info" %}
Please see Qwen3.6's new [Preserved Thinking](#thinking-enable-disable--preserve-thinking).
{% endhint %}

General tasks:

```bash
export LLAMA_CACHE="unsloth/Qwen3.6-35B-A3B-MTP-GGUF"
./llama.cpp/llama-cli \
    -hf unsloth/Qwen3.6-35B-A3B-MTP-GGUF:UD-Q4_K_XL \
    --temp 1.0 \
    --top-p 0.95 \
    --top-k 20 \
    --min-p 0.00 \
    --spec-type draft-mtp --spec-draft-n-max 2
```

For precise coding tasks, change: `temperature=0.6`

**Non-thinking mode:**

General tasks:

```bash
export LLAMA_CACHE="unsloth/Qwen3.6-35B-A3B-MTP-GGUF"
./llama.cpp/llama-server \
    -hf unsloth/Qwen3.6-35B-A3B-MTP-GGUF:UD-Q4_K_XL \
    --temp 0.7 \
    --top-p 0.8 \
    --top-k 20 \
    --presence-penalty 1.5 \
    --min-p 0.00 \
    --spec-type draft-mtp --spec-draft-n-max 2 \
    --chat-template-kwargs '{"enable_thinking":false}'
```

{% endstep %}

{% step %}
You can also download the model manually as well via the code below (after installing `pip install huggingface_hub`). You can choose Q4\_K\_M or other quantized versions like `UD-Q4_K_XL` . We recommend using at least 2-bit dynamic quant `UD-Q2_K_XL` to balance size and accuracy. If downloads get stuck, see: [Hugging Face Hub, XET debugging](/docs/basics/troubleshooting-and-faqs/hugging-face-hub-xet-debugging.md)

```bash
hf download unsloth/Qwen3.6-35B-A3B-MTP-GGUF \
    --local-dir unsloth/Qwen3.6-35B-A3B-MTP-GGUF \
    --include "*mmproj-F16*" \
    --include "*UD-Q4_K_XL*" # Use "*UD-Q2_K_XL*" for Dynamic 2bit
```

{% endstep %}

{% step %}
Then run the model in conversation mode:

{% code overflow="wrap" %}

```bash
./llama.cpp/llama-cli \
    --model unsloth/Qwen3.6-35B-A3B-MTP-GGUF/Qwen3.6-35B-A3B-UD-Q4_K_XL.gguf \
    --mmproj unsloth/Qwen3.6-35B-A3B-MTP-GGUF/mmproj-F16.gguf \
    --temp 1.0 \
    --top-p 0.95 \
    --min-p 0.00 \
    --top-k 20 \
    --spec-type draft-mtp --spec-draft-n-max 2
```

{% endcode %}
{% endstep %}
{% endstepper %}

### 🍎 MLX Dynamic Quants

We also uploaded dynamic Qwen3.6 4bit and 8bit quants for MacOS devices! Our MLX quant algorithm is still evolving, and we’re actively refining it wherever improvements can be made.

You can run all MLX models in [Unsloth Studio](#unsloth-studio-guide)!

**Qwen3.6-27B MLX:**

| [3-bit](https://huggingface.co/unsloth/Qwen3.6-27B-UD-MLX-3bit) | [4-bit](https://huggingface.co/unsloth/Qwen3.6-27B-UD-MLX-4bit) | [MXFP4](https://huggingface.co/unsloth/Qwen3.6-27B-UD-MLX-MXFP4) | [NVFP4](https://huggingface.co/unsloth/Qwen3.6-27B-UD-MLX-NVFP4) | [6-bit](https://huggingface.co/unsloth/Qwen3.6-27B-UD-MLX-6bit) | [8-bit](https://huggingface.co/unsloth/Qwen3.6-27B-MLX-8bit) |
| --------------------------------------------------------------- | --------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | --------------------------------------------------------------- | ------------------------------------------------------------ |

**Qwen3.6-35B-A3B MLX:**

| [3-bit](https://huggingface.co/unsloth/Qwen3.6-35B-A3B-UD-MLX-3bit) | [4-bit](https://huggingface.co/unsloth/Qwen3.6-35B-A3B-UD-MLX-4bit) | [8-bit](https://huggingface.co/unsloth/Qwen3.6-35B-A3B-MLX-8bit) |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ---------------------------------------------------------------- |

To try them out use:

{% code overflow="wrap" %}

```bash
curl -fsSL https://raw.githubusercontent.com/unslothai/unsloth/refs/heads/main/scripts/install_qwen3_6_mlx.sh | sh
source ~/.unsloth/unsloth_qwen3_6_mlx/bin/activate
python -m mlx_vlm.chat --model unsloth/Qwen3.6-27B-UD-MLX-4bit
```

{% endcode %}

See below for Qwen3.6-27B KL Divergence (KLD) and Perplexity (PPL) scores (lower is better):

| Model                                                            | Mean KLD | Median KLD | PPL   | P90 KLD | P99.9 KLD | Size    |
| ---------------------------------------------------------------- | -------- | ---------- | ----- | ------- | --------- | ------- |
| [8-bit](https://huggingface.co/unsloth/Qwen3.6-27B-MLX-8bit)     | 0.0028   | 0.0003     | 4.812 | 0.0019  | 0.192     | 34.7 GB |
| [6-bit](https://huggingface.co/unsloth/Qwen3.6-27B-UD-MLX-6bit)  | 0.0037   | 0.0007     | 4.809 | 0.0032  | 0.343     | 30.5 GB |
| [4-bit](https://huggingface.co/unsloth/Qwen3.6-27B-UD-MLX-4bit)  | 0.0227   | 0.0053     | 4.821 | 0.0293  | 2.339     | 26.2 GB |
| [NVFP4](https://huggingface.co/unsloth/Qwen3.6-27B-UD-MLX-NVFP4) | 0.0325   | 0.0087     | 4.843 | 0.0466  | 3.693     | 26.2 GB |
| [MXFP4](https://huggingface.co/unsloth/Qwen3.6-27B-UD-MLX-MXFP4) | 0.0479   | 0.0153     | 4.902 | 0.0769  | 4.035     | 25.6 GB |
| [3-bit](https://huggingface.co/unsloth/Qwen3.6-27B-UD-MLX-3bit)  | 0.0734   | 0.0223     | 4.976 | 0.1261  | 5.529     | 24.1 GB |

### ⚡️NVFP4

**July 10 2026:** We’re releasing new [dynamic NVFP4 Qwen3.6 quants](/docs/basics/nvfp4.md) that run \~**2.5× faster** than other NVFP4 quants, with **better performance** and comparable file sizes. Run Qwen3.6-27B NVFP4 **2.5x faster** on **24GB VRAM** and Qwen3.6-35B-A3B **1.7x faster** on **32GB VRAM**. We also added **FP8 KV cache calibration** for 2x longer context lengths! NVFP4 requires NVIDIA's Blackwell GPUs like RTX 50X, DGX Spark (see [#dgx-spark-with-nvfp4-quants](#dgx-spark-with-nvfp4-quants "mention")), B200, B300 GPUs. For older GPUs, our GGUFs work well!

<figure><img src="/files/6X0DPBb8ijDqd6cGk4sH" alt=""><figcaption></figcaption></figure>

All benchmarks use 1x B200 128 concurrency. Higher concurrency can boost 35B to 17,561 tokens / s. We're also releasing two 35B-A3B NVFP4 versions:

* [Qwen3.6-35B-A3B-NVFP4-Fast](https://huggingface.co/unsloth/Qwen3.6-35B-A3B-NVFP4-Fast) which is a full W4A4 quant - 1.79x faster
* [Qwen3.6-35B-A3B-NVFP4](https://huggingface.co/unsloth/Qwen3.6-35B-A3B-NVFP4) which is slightly bigger but more accurate and 1.56x faster

For accuracy benchmarks, we conducted MMLU-Pro, AIME 2025, GPQA for FP8, BF16, NVIDIA's NVFP4 and our NVFP4s - we show our faster quants do similarly on all:

<figure><img src="/files/95OLTU6BPWYWYNmsJidJ" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="372.5999755859375">Qwen3.6-35B-A3B</th><th>Qwen3.6-27B</th></tr></thead><tbody><tr><td><a href="https://huggingface.co/unsloth/Qwen3.6-35B-A3B-NVFP4">Qwen3.6-35B-A3B-NVFP4</a> (1.56x Faster)</td><td><a href="https://huggingface.co/unsloth/Qwen3.6-27B-NVFP4">Qwen3.6-27B-NVFP4</a> (2.5x Faster)</td></tr><tr><td><a href="https://huggingface.co/unsloth/Qwen3.6-35B-A3B-NVFP4-Fast">Qwen3.6-35B-A3B-NVFP4-Fast</a> (1.79x Faster)</td><td></td></tr></tbody></table>

**MTP tensors are also built directly into the quants for additional speedups.** Accuracy gains come from improvements to Qwen3.6’s chat template and dataset calibration. We use our previous chat template updates to help improve coding and tool-calling consistency while reducing looping and other reported issues. Our calibration uses a mix of our dataset optimized for coding, tool-calling and chat alongside UltraChat.

For Decode speed (tokens per person), ours is 1.03x faster for 27B and 1.17x and 1.22x faster for 35B.

<figure><img src="/files/21SoRKrv07FpNP2b09iB" alt=""><figcaption></figcaption></figure>

### NVFP4 Benchmarks

NVFP4 runs 4-bit weights and matrix multiplications directly on Blackwell Tensor Cores. Our Qwen3.6 NVFP4 quants use W4A4 so they actually use the FP4 tensor cores, so they decode faster than NVIDIA's which use W4A16. We also dynamically quantize layers to retain accuracy, and we conducted MMLU-Pro, AIME 2025, GPQA for all quants including comparing to FP8 and BF16.

**Qwen3.6-27B NVFP4 Accuracy Benchmarks**

| Provider | MMLU-Pro |  GPQA | AIME 2025 |
| -------- | -------: | ----: | --------: |
| Unsloth  |    86.25 | 86.34 |     93.12 |
| NVIDIA   |    85.96 | 86.87 |     93.12 |
| FP8      |    86.11 | 86.87 |     93.75 |
| BF16     |    85.96 | 88.13 |     93.33 |

**Qwen3.6-35B-A3B NVFP4 Accuracy Benchmarks**

| Provider         | MMLU-Pro |  GPQA | AIME 2025 |
| ---------------- | -------: | ----: | --------: |
| Unsloth          |    85.85 | 86.74 |     92.29 |
| **Unsloth Fast** |    85.58 | 87.75 |     91.67 |
| NVIDIA           |    85.60 | 87.12 |     91.88 |
| FP8              |    85.75 | 86.74 |     93.12 |
| BF16             |    85.75 | 86.36 |     92.50 |

We also checked the output length of all benchmarks, and they are comparable, so the new NVFP4 quants do not think for longer which defeats the purpose of quantizing them! (Ie if it's 2x faster, but thinks 2x more, then that's useless)

<figure><img src="/files/5aW9XVFflv0cEGgWsgyJ" alt=""><figcaption></figcaption></figure>

### Marlin vs Flashinfer vs cutlass vs cute-DSL

We also found Marlin kernels to not support W4A4 well - enabling it will cause a 2.5x performance degradation - so use CUTLASS, Flashinfer-TRTLLM or Cute-DSL (auto enabled in vLLM)! Also if you have a DGX Spark, see [#dgx-spark-serving](#dgx-spark-serving "mention") you must use `--moe-backend flashinfer_b12x` or you will get 2.5x slower inference.

**So don't set any backend - vLLM auto selects the best.**

| Model           | scheme | backend             | decode tok/s | thr out tok/s |
| --------------- | ------ | ------------------- | ------------ | ------------- |
| nvidia 27B      | W4A16  | marlin (auto)       | 115.6        | 2,403         |
| unsloth 27B     | W4A4   | marlin              | 105.6        | 2,127         |
| unsloth 27B     | W4A4   | cutlass             | 113.5        | 6,681         |
| unsloth 27B     | W4A4   | flashinfer\_trtllm  | 112.6        | 6,158         |
| unsloth 27B     | W4A4   | **cute-DSL (auto)** | 125.9        | **6,863**     |
| nvidia 35B-A3B  | W4A4   | marlin (auto)       | 240.8        | 8,721         |
| unsloth 35B-A3B | W4A4   | marlin              | 215.8        | 8,619         |
| unsloth 35B-A3B | W4A4   | cutlass             | 158.3        | 11,017        |
| unsloth 35B-A3B | W4A4   | **cute-DSL (auto)** | 295.2        | **15,636**    |

#### **vLLM:**

To run NVFP4 quants, see below for commands to run Qwen3.6-27B in [vLLM](/docs/basics/inference-and-deployment/vllm-guide.md) and [SGLang](/docs/basics/inference-and-deployment/sglang-guide.md) (you can change model name to `Qwen3.6-35-A3B-NVFP4`). Also do NOT select any MoE backend - leave vLLM to select it - for eg Marlin is 2.5x slower! See [#marlin-vs-flashinfer-vs-cutlass-vs-cute-dsl](#marlin-vs-flashinfer-vs-cutlass-vs-cute-dsl "mention")If you have a DGX Spark, see [#dgx-spark-serving](#dgx-spark-serving "mention") you must use `--moe-backend flashinfer_b12x` or you will get much slower inference.

To install vLLM in a separate venv:

{% code overflow="wrap" expandable="true" %}

```bash
uv venv unsloth-nvfp4-env --python 3.13
source unsloth-nvfp4-env/bin/activate
uv pip install "vllm>=0.25.0" "flashinfer-python>=0.6.13" "nvidia-cutlass-dsl>=4.5.2" \
    --torch-backend=auto
```

{% endcode %}

Then to serve the 35B Fast variant:

```shell
vllm serve unsloth/Qwen3.6-35B-A3B-NVFP4-Fast
```

Change `unsloth/Qwen3.6-35B-A3B-NVFP4-Fast` to the NVFP4 quant names!

To enable MTP / speculative decoding (faster decode but somewhat less throughput), use:

```bash
vllm serve unsloth/Qwen3.6-35B-A3B-NVFP4-Fast
    --speculative-config '{"method": "mtp", "num_speculative_tokens": 2}'
```

If you get Torchcodec issues, be sure to do the below then relaunch vllm.

{% code overflow="wrap" expandable="true" %}

```bash
sudo apt-get update
sudo apt-get install -y ffmpeg
```

{% endcode %}

### **DGX Spark with NVFP4 quants**

To ensure DGX Spark has the correct kernels (or you will get **2x SLOWER inference**), first check:

{% code overflow="wrap" expandable="true" %}

```bash
python -c "
import torch; from vllm.utils.flashinfer import has_flashinfer_b12x_gemm as g, has_flashinfer_b12x_moe as m
cap = torch.cuda.get_device_capability(); print('cap', cap, '| b12x gemm', g(), '| b12x moe', m()); assert cap[0] == 12 and g() and m(), 'b12x unavailable: serving would degrade to marlin W4A16'"
```

{% endcode %}

which should NOT error out - if it did, please update vllm or reinstall via:

{% code overflow="wrap" expandable="true" %}

```bash
uv venv unsloth-nvfp4-env --python 3.13
source unsloth-nvfp4-env/bin/activate
uv pip install "vllm>=0.25.0" "flashinfer-python>=0.6.13" "nvidia-cutlass-dsl>=4.5.2" \
    --torch-backend=auto
```

{% endcode %}

Then to serve in vLLM for DGX Spark:

{% code overflow="wrap" expandable="true" %}

```shellscript
export CUTE_DSL_ARCH=sm_121a
vllm serve unsloth/Qwen3.6-35B-A3B-NVFP4-Fast --moe-backend flashinfer_b12x
```

{% endcode %}

If you get Torchcodec issues, be sure to do the below then relaunch vllm.

{% code overflow="wrap" expandable="true" %}

```bash
sudo apt-get update
sudo apt-get install -y ffmpeg
```

{% endcode %}

#### **SGLang:**

```bash
python -m sglang.launch_server --model-path unsloth/Qwen3.6-27B-NVFP4 --speculative-algorithm NEXTN \
     --speculative-num-steps 3 --speculative-eagle-topk 1 --speculative-num-draft-tokens 4
```

### 🦙 Llama.cpp Guide

For this guide we will be utilizing Dynamic 4-bit which works great on a 24GB RAM / Mac device for fast inference on [llama.cpp](llama.cpphttps://github.com/ggml-org/llama.cpp). Because the model is only around 72GB at full F16 precision, we won't need to worry much about performance. [See our GGUF collection](https://huggingface.co/collections/unsloth/qwen36).

<a href="/pages/NpuhjPsxi8BKhuS8nnyY#qwen3.6-27b" class="button primary">27B</a><a href="/pages/NpuhjPsxi8BKhuS8nnyY#qwen3.6-35b-a3b" class="button primary">35-A3B</a>

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
If you want to use `llama.cpp` directly to load models, you can do the below: (:`Q4_K_XL`) is the quantization type. You can also download via Hugging Face (point 3). This is similar to `ollama run` . Use `export LLAMA_CACHE="folder"` to force `llama.cpp` to save to a specific location. The model has a maximum of 256K context length.

Follow one of the commands for the specific models:

<a href="/pages/NpuhjPsxi8BKhuS8nnyY#qwen3.6-27b" class="button primary">27B</a><a href="/pages/NpuhjPsxi8BKhuS8nnyY#qwen3.6-35b-a3b" class="button primary">35-A3B</a>

#### Qwen3.6-27B:

**Thinking mode:**

{% hint style="info" %}
Please see Qwen3.6's new [Preserved Thinking](#thinking-enable-disable--preserve-thinking).
{% endhint %}

General tasks:

```bash
export LLAMA_CACHE="unsloth/Qwen3.6-27B-GGUF"
./llama.cpp/llama-cli \
    -hf unsloth/Qwen3.6-27B-GGUF:UD-Q4_K_XL \
    --temp 1.0 \
    --top-p 0.95 \
    --top-k 20 \
    --min-p 0.00
```

For precise coding tasks, change: `temperature=0.6`

**Non-thinking mode:**

General tasks:

```bash
export LLAMA_CACHE="unsloth/Qwen3.6-27B-GGUF"
./llama.cpp/llama-server \
    -hf unsloth/Qwen3.6-27B-GGUF:UD-Q4_K_XL \
    --temp 0.7 \
    --top-p 0.8 \
    --top-k 20 \
    --presence-penalty 1.5 \
    --min-p 0.00 \
    --chat-template-kwargs '{"enable_thinking":false}'
```

#### Qwen3.6-35B-A3B:

**Thinking mode:**

{% hint style="info" %}
Please see Qwen3.6's new [Preserved Thinking](#thinking-enable-disable--preserve-thinking).
{% endhint %}

General tasks:

```bash
export LLAMA_CACHE="unsloth/Qwen3.6-35B-A3B-GGUF"
./llama.cpp/llama-cli \
    -hf unsloth/Qwen3.6-35B-A3B-GGUF:UD-Q4_K_XL \
    --temp 1.0 \
    --top-p 0.95 \
    --top-k 20 \
    --min-p 0.00
```

For precise coding tasks, change: `temperature=0.6`

**Non-thinking mode:**

General tasks:

```bash
export LLAMA_CACHE="unsloth/Qwen3.6-35B-A3B-GGUF"
./llama.cpp/llama-server \
    -hf unsloth/Qwen3.6-35B-A3B-GGUF:UD-Q4_K_XL \
    --temp 0.7 \
    --top-p 0.8 \
    --top-k 20 \
    --presence-penalty 1.5 \
    --min-p 0.00 \
    --chat-template-kwargs '{"enable_thinking":false}'
```

{% endstep %}

{% step %}
You can also download the model manually as well via the code below (after installing `pip install huggingface_hub`). You can choose Q4\_K\_M or other quantized versions like `UD-Q4_K_XL` . We recommend using at least 2-bit dynamic quant `UD-Q2_K_XL` to balance size and accuracy. If downloads get stuck, see: [Hugging Face Hub, XET debugging](/docs/basics/troubleshooting-and-faqs/hugging-face-hub-xet-debugging.md)

```bash
hf download unsloth/Qwen3.6-35B-A3B-GGUF \
    --local-dir unsloth/Qwen3.6-35B-A3B-GGUF \
    --include "*mmproj-F16*" \
    --include "*UD-Q4_K_XL*" # Use "*UD-Q2_K_XL*" for Dynamic 2bit
```

{% endstep %}

{% step %}
Then run the model in conversation mode:

{% code overflow="wrap" %}

```bash
./llama.cpp/llama-cli \
    --model unsloth/Qwen3.6-35B-A3B-GGUF/Qwen3.6-35B-A3B-UD-Q4_K_XL.gguf \
    --mmproj unsloth/Qwen3.6-35B-A3B-GGUF/mmproj-F16.gguf \
    --temp 1.0 \
    --top-p 0.95 \
    --min-p 0.00 \
    --top-k 20
```

{% endcode %}
{% endstep %}
{% endstepper %}

#### Llama-server & OpenAI completion library

To deploy Qwen3.6 for production, we use `llama-server` In a new terminal say via tmux, deploy the model via:

{% code overflow="wrap" %}

```bash
./llama.cpp/llama-server \
--model unsloth/Qwen3.6-35B-A3B-GGUF/Qwen3.6-35B-A3B-UD-Q4_K_XL.gguf \
    --mmproj unsloth/Qwen3.6-35B-A3B-GGUF/mmproj-F16.gguf \
    --alias "unsloth/Qwen3.6-35B-A3B" \
    --temp 0.6 \
    --top-p 0.95 \
    --ctx-size 16384 \
    --top-k 20 \
    --min-p 0.00 \
    --port 8001
```

{% endcode %}

Then in a new terminal, after doing `pip install openai`, do:

{% code overflow="wrap" %}

```python
from openai import OpenAI
import json
openai_client = OpenAI(
    base_url = "http://127.0.0.1:8001/v1",
    api_key = "sk-no-key-required",
)
completion = openai_client.chat.completions.create(
    model = "unsloth/Qwen3.6-35B-A3B",
    messages = [{"role": "user", "content": "Create a Snake game."},],
)
print(completion.choices[0].message.content)
```

{% endcode %}

### 💡 Thinking: Enable/Disable + Preserve Thinking

Qwen3.6 also has **Preserve Thinking** which leaves the thinking trace from the previous conversation. This increases the number of tokens you use, but could increase accuracy in continued conversations. Unsloth Studio has 'Think' and Preserved Thinking toggles for Qwen3.6:

<div data-with-frame="true"><figure><img src="/files/vTGOOXiSgQ6qXSrMZMMw" alt="" width="563"><figcaption><p>Unsloth Studio has Think toggle by default and a new <a href="#preserved-thinking">Preserved Thinking</a> toggle</p></figcaption></figure></div>

To enable **preserve thinking** in llama.cpp use (change to 'true' or 'false') '`preserve_thinking`' instead of '`enable_thinking`' or '`disable_thinking`'.

{% code expandable="true" %}

```bash
--chat-template-kwargs '{"preserve_thinking":true}'
```

{% endcode %}

For normal thinking, you can enable / disable thinking in llama.cpp by following the below commands. Use '`true`' and '`false`' interchangeably.

<table data-full-width="false"><thead><tr><th width="197.76666259765625">llama-server OS:</th><th>Enable Thinking</th><th>Disable Thinking</th></tr></thead><tbody><tr><td>Linux, MacOS, WSL:</td><td><pre data-overflow="wrap"><code>--chat-template-kwargs '{"enable_thinking":true}'
</code></pre></td><td><pre data-overflow="wrap"><code>--chat-template-kwargs '{"enable_thinking":false}'
</code></pre></td></tr><tr><td>Windows / Powershell:</td><td><pre data-overflow="wrap"><code>--chat-template-kwargs "{\"enable_thinking\":true}"
</code></pre></td><td><pre data-overflow="wrap"><code>--chat-template-kwargs "{\"enable_thinking\":false}"
</code></pre></td></tr></tbody></table>

As an example for Qwen3.6-35B-A3B to enable preserve thinking (default is enabled):

```bash
./llama.cpp/llama-server \
    --model unsloth/Qwen3.6-35B-A3B-GGUF/Qwen3.6-35B-A3B-BF16.gguf \
    --alias "unsloth/Qwen3.6-35B-A3B-GGUF" \
    --temp 0.6 \
    --top-p 0.95 \
    --top-k 20 \
    --min-p 0.00 \
    --port 8001 \
    --chat-template-kwargs '{"preserve_thinking":true}'
```

And then in Python:

```python
from openai import OpenAI
import json
openai_client = OpenAI(
    base_url = "http://127.0.0.1:8001/v1",
    api_key = "sk-no-key-required",
)
completion = openai_client.chat.completions.create(
    model = "unsloth/Qwen3.6-35B-A3B-GGUF",
    messages = [{"role": "user", "content": "What is 2+2?"},],
)
print(completion.choices[0].message.content)
print(completion.choices[0].message.reasoning_content)
```

### 👨‍💻 OpenAI Codex & Claude Code <a href="#claude-codex" id="claude-codex"></a>

To run the model via local coding agentic workloads, you can [follow our guide](#claude-codex). Use the `llama-server` we just set up just then, and set the model name to the exact id it reports at `GET /v1/models` (the `--alias` value above, e.g. `unsloth/Qwen3.6-35B-A3B-GGUF`). Follow the correct Qwen3.6 parameters and usage instructions.

{% columns %}
{% column %}
{% content-ref url="/pages/w020xJgdCTBtTvfHtvye" %}
[Claude Code](/docs/basics/claude-code.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
{% content-ref url="/pages/PCjZ57h5pE0QccKyJMYD" %}
[OpenAI Codex](/docs/basics/codex.md)
{% endcontent-ref %}
{% endcolumn %}
{% endcolumns %}

After following the instructions for Claude Code for example you will see:

<div data-with-frame="true"><figure><img src="/files/6eoCtTzoTOW0ZVd51nzb" alt="" width="563"><figcaption></figcaption></figure></div>

We can then ask say `Create a Python game for Chess` :

<div><figure><img src="/files/TLpKKAoUMChIHyg0IVGN" alt="" width="563"><figcaption></figcaption></figure> <figure><img src="/files/Tibvh4yrfFNWCsEoMyZA" alt="" width="563"><figcaption></figcaption></figure> <figure><img src="/files/mVqn5oQxc8QnU7peLB3l" alt="" width="563"><figcaption></figcaption></figure></div>

## 📊 Benchmarks

### Unsloth GGUF Benchmarks

We conducted Mean KL Divergence benchmarks for Qwen3.6-35-A3B GGUFs across providers to help you pick the best quant.

* KL Divergence puts nearly all Unsloth GGUFs on the SOTA Pareto frontier
* KLD shows how well a quantized model matches the original BF16 output distribution, indicating retained accuracy.
* This makes Unsloth the top-performing in 21 of 22 sizes
* Only Q6\_K was updated for more Dynamic layers and we introduced a new `UD-IQ4_NL_XL` quant

<div data-with-frame="true"><figure><img src="/files/LJD75l9fRCA8CmMgwEB5" alt=""><figcaption><p>35B-A3B - KLD benchmarks (lower is better)</p></figcaption></figure></div>

### MTP Benchmarks

We benchmarked the new quants we made for 27B and 35B MoE. In general, dense models are much more accelerated with MTP (1.4-2x) vs MoE models (1.15-1.25x).

With this, Qwen3.6 27B can now do 140 tokens / s generation with UD-Q2\_K\_XL and Qwen3.6 35B-A3B 220 tokens / s generation! Some of the throughput numbers are noisy, so don't infer some quants are slower than others.

<figure><img src="/files/HZ5HzeITU51SnTa3wpiN" alt=""><figcaption></figcaption></figure>

In terms of average speedup, we see a 1.4x for dense models at draft tokens = 2 and for the MoE around 1.15 to 1.2x.

<figure><img src="/files/bUurusZwA36SeHijvzOM" alt=""><figcaption></figcaption></figure>

We do not recommend more than 2 draft tokens because the acceptance rate drops precipitously from 83% to 50% with 4 draft tokens, and the forward passes for MTP become less beneficial.

<figure><img src="/files/Ge8vOgu6FMhwfCZAraZW" alt=""><figcaption></figcaption></figure>

### Official Qwen Benchmarks

#### Qwen3.6-27B

<div data-with-frame="true"><figure><img src="/files/8uUSAAlap9KEZXfXXJ71" alt=""><figcaption></figcaption></figure></div>

#### Qwen3.6-35B-A3B

<div data-with-frame="true"><figure><img src="/files/8bSdWhlocJsS2NwSUPMi" alt=""><figcaption></figcaption></figure></div>

These results make the trade-off simple: use Dynamic GGUFs for the best balance of memory and quality, use MTP when you want faster generation, and use NVFP4 on Blackwell GPUs for maximum throughput. If you want the easiest path, run the model in [Unsloth Studio](#unsloth-studio-guide) and keep the recommended defaults.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://unsloth.ai/docs/models/qwen3.6.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
