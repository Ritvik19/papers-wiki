Source URL: https://unsloth.ai/blog/mistral-benchmark
Title: Unsloth update: Mistral support + more

unsloth sticker logounsloth main Logounsloth

ModelsBlogUnsloth Studio✨Docs

Blog

6 cute pastel coloured sloths staring at their computer screens happy

Finetune Mistral 14x faster

# Dec 14, 2023 • By Daniel Han

# Dec 14, 2023

# •

# By Daniel Han

Unsloth open source:

# 

Mistral 7B

1xA100

2.2x

faster

# 

Code Llama 34B

1xA100

1.9x

faster

# 

Llama 7B

1xA100

2.2x

faster

# 

Llama 7B

1xT4

2x

faster

We’re excited to release QLoRA support for Mistral 7B, CodeLlama 34B, and all other models based on the Llama architecture! We added sliding window attention, preliminary Windows and DPO support, and will share all 59 notebooks for reproducing our numbers.  
  
You can now QLoRA finetune Mistral 7B 2.2x on 1x A100 faster with 62% less memory or 12.4GB peak VRAM. CodeLlama 34B is 1.9x faster on 1x A100, using 32% less memory or 27GB peak VRAM. It finally doesn’t OOM!

Unsloth Pro version:

# 

Mistral 7B

1xA100

14x

faster

# 

Code Llama 34B

1xA100

13x

faster

# 

Llama 7B

1xA100

21x

faster

# 

Llama 7B

2xT4

28x

faster

Our PRO version can finetune Mistral 7B a whopping 14x faster on 1x A100, using 70% less peak VRAM, and CodeLlama 34B is 13x faster on 1x A100 using 50% less VRAM or 20GB peak VRAM. Llama 7B is also 21x faster on 1x A100, with a crazy 71% reduction in peak VRAM usage. On 2x Tesla T4s, Llama 7B is 28x faster via DDP support.

Unsloth Pro version:

# 

Mistral 7B

1xA100

\-70%

peak VRAM

# 

Code Llama 34B

1xA100

\-50%

peak VRAM

# 

Llama 7B

1xA100

\-71%

peak VRAM

# 

Llama 7B

2xT4

\-44%

peak VRAM

We also added installing Flash Attention v2 directly rather than through Xformers. If you have a RTX 3060 or higher (A100, H100 etc), use the "ampere" install path!

`pip install "unsloth[cu118_ampere] @ git+https://github.com/unslothai/unsloth.git"  
  
pip install "unsloth[cu121_ampere] @ git+https://github.com/unslothai/unsloth.git"  
  
pip install "unsloth[colab_ampere] @ git+https://github.com/unslothai/unsloth.git"`

As requested, we provide a preliminary breakdown of how we made things faster with Unsloth!

Benchmarking

| 1 A100 40GB | Hugging Face | Flash Attention 2 | Unsloth Open | Unsloth Equal | Unsloth Pro | Unsloth Max |
| ----------- | ------------ | ----------------- | ------------ | ------------- | ----------- | ----------- |
| Alpaca      | 1x           | 1.04x             | 1.98x        | 2.48x         | 5.32x       | **15.64x**  |
| LAION Chip2 | 1x           | 0.92x             | 1.61x        | 1.84x         | 7.05x       | **20.73x**  |
| OASST       | 1x           | 1.19x             | 2.17x        | 2.66x         | 5.04x       | **14.83x**  |
| Slim Orca   | 1x           | 1.18x             | 2.22x        | 2.64x         | 5.04x       | **14.82x**  |

We benchmark Unsloth against Hugging Face’s original implementation, and against adding Flash Attention 2 support on 1x A100 via Google Colab. Flash Attention at most speeds up training by 1.2x, whilst with Unsloth’s open source package, training is 2.2x faster. “Unsloth Equal” is our PRO version, but under the condition that all settings and the loss curve stays the same. Under this scenario, we further boost training to 2.7x. Our MAX version can boost speeds on the LAION dataset to 21x!  
  
All benchmarks use the following setup (unless if some tests OOM, in which we decrease the batch size for all tests):

`QLoRA nf4 layers = [  
 "q_proj", "k_proj", "v_proj", "o_proj",   
 "gate_proj", "up_proj", "down_proj",  
]  
QLoRA rank = 16, alpha = 16, dropout = 0  
max_seq_length = 2048  
learning_rate = 2e-4  
weight_decay = 0.01  
max_steps = 240  
warmup_steps = 10  
batch_size = 4  
gradient_accumulation_steps = 4  
lr_scheduler_type = "linear"  
optimizer = "adamw_8bit", bfloat16  
use_gradient_checkpointing = True  
random_state = 3407`

| 1 A100 40GB          | Hugging Face                                                                                      | Flash Attention 2                                                                               | Unsloth Open                                                                                    | Unsloth Equal                                                                                   | Unsloth Pro | Unsloth Max |
| -------------------- | ------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------- | ----------- |
| Mistral 7B Slim Orca | 1x                                                                                                | 1.15x                                                                                           | 2.15x                                                                                           | 2.53x                                                                                           | 4.61x       | **13.69x**  |
| code                 | [Code](https://colab.research.google.com/drive/1mePk3KzwTD81hr5mcNcs%5FAX3Kbg%5FHa0x?usp=sharing) | [Code](https://colab.research.google.com/drive/1dgHxjvTmX6hb0bPcLp26RXSE6%5Fn9DKj7?usp=sharing) | [Code](https://colab.research.google.com/drive/1SKrKGV-BZoU4kv5q3g0jtE%5FOhRgPtrrQ?usp=sharing) | [Code](https://colab.research.google.com/drive/18yOiyX0T81mTwZqOALFSCX%5FtSAqju6aD?usp=sharing) |             |             |
| seconds              | 1813                                                                                              | 1571                                                                                            | 842                                                                                             | 718                                                                                             | 393         | 132         |
| memory MB            | 32853                                                                                             | 19385                                                                                           | 12465                                                                                           | 10271                                                                                           |             |             |
| memory saved %       | 40.99                                                                                             | 62.06                                                                                           | 68.74                                                                                           |                                                                                                 |             |             |

On Mistral 7B for 1x A100, Flash Attention v2 boosts training by 1.15x, whilst Unsloth Open boosts it by 2.15x, and we reduce memory by 62%. Again, "Unsloth Equal" which runs an equalized training run boosts speeds by 2.53x, and uses 69% less peak VRAM. Unsloth MAX boosts training by 13.7x.  
  
You can click on "Code" to access our shared notebooks for reproducibility purposes. "Unsloth Equal" only shows the training losses and obscures our other codepaths.

| 1 A100 40GB    | Hugging Face                                                                                    | Flash Attention 2                                                                               | Unsloth Open                                                                                  | Unsloth Equal                                                                                 | Unsloth Pro | Unsloth Max |
| -------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | ----------- | ----------- |
| Code Llama 34B | OOM ❌                                                                                           | 0.99x                                                                                           | 1.87x                                                                                         | 2.61x                                                                                         | 4.27x       | 12.82x      |
| code           | [Code](https://colab.research.google.com/drive/1ykfz3BqrtC%5FAUFegCzUQjjfUNlxp6Otc?usp=sharing) | [Code](https://colab.research.google.com/drive/12ZypxQh7OC6kBXvWZI-5d05I4m-B%5FhoR?usp=sharing) | [Code](https://colab.research.google.com/drive/1gdHyAx8XJsz2yNV-DHvbHjR1iCef5Qmh?usp=sharing) | [Code](https://colab.research.google.com/drive/1fm7wqx9MJ0kRrwKOfmLkK1Rmw-pySahB?usp=sharing) |             |             |
| seconds        | 1953                                                                                            | 1982                                                                                            | 1043                                                                                          | 748                                                                                           | 458         | 152         |
| memory MB      | 40000                                                                                           | 33217                                                                                           | 27413                                                                                         | 22161                                                                                         |             |             |
| memory saved % | 16.96                                                                                           | 31.47                                                                                           | 44.60                                                                                         |                                                                                               |             |             |

On CodeLlama 34B, we used a batch size of 1 on a sequence length of 4096\. Unfortunately, Hugging Face's original implementation OOMs on batch size = 2, so we had to do a benchmark on bsz = 1\. Flash Attention v2 does not noticeably change the runtime, whilst Unsloth Open is 1.87x faster, and uses 32% less peak VRAM. "Unsloth Equal" is 2.6x faster, and uses 45% less memory, and MAX is 12.8x faster.

| 2 T4 DDP       | Hugging Face                                                          | Flash Attention                                                   | Unsloth Open                                                      | Unsloth Equal | Unsloth Pro | Unsloth Max |
| -------------- | --------------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- | ------------- | ----------- | ----------- |
| LAION Chip2    | 1x                                                                    | 1.12x                                                             | 5.28x                                                             | 4.21x         | 10.01x      | **28.32x**  |
| code           | [Code](https://www.kaggle.com/danielhanchen/hf-original-laion-t4-ddp) | [Code](https://www.kaggle.com/danielhanchen/hf-sdpa-laion-t4-ddp) | [Code](https://www.kaggle.com/danielhanchen/unsloth-laion-t4-ddp) |               |             |             |
| seconds        | 5418                                                                  | 4854                                                              | 1027                                                              | 1286          | 541         | 191         |
| memory MB      | 7316                                                                  | 7316                                                              | 5732                                                              | 5934          |             |             |
| memory saved % | 0.00                                                                  | 21.65                                                             | 18.89                                                             |               |             |             |

Via Kaggle's 2 Tesla T4 instance, we find that Unsloth Open trains 5.3x faster on 1 GPU only. We multiply the gradient accumulation steps by 2 to be fair, since the open source version does not support multi GPU. "Unsloth Equal" is 4.21x faster via DDP. DDP has an overhead, since gradients must be synchronized at each step. Unsloth MAX trains 28x faster!  
  
At the end of this blog post, we provide the whole table of all benchmarks, and all 59 notebook links for reproducibility purposes.

Performance breakdowns bit by bit

| No. | Method                          | Time (s) | Peak VRAM (GB) | Time saved (%) | VRAM saved (%) | Final error |
| --- | ------------------------------- | -------- | -------------- | -------------- | -------------- | ----------- |
| 1   | Huggingface Original PEFT QLoRA | 594      | 16.7           | 1.0202         |                |             |
| 2   | Reduce data upcasting           | 465      | 15.5           | 21.7%          | 7.2%           | 1.0203      |
| 3   | Bitsandbytes bfloat16           | 424      | 15.3           | 8.9%           | 1.3%           | 1.0208      |
| 4   | SDPA                            | 418      | 14.9           | 1.4%           | 2.6%           | 1.0214      |
| 5   | SDPA causal = True              | 384      | 14.9           | 8.1%           | 0.0%           | 1.0219      |
| 6   | Xformers                        | 353      | 9.1            | 8.1%           | 38.9%          | 1.021       |
| 7   | Flash Attention 2               | 353      | 9.1            | 0.0%           | 0.0%           | 1.0215      |
| 8   | Fast RoPE Embeddings            | 326      | 9              | 7.6%           | 1.1%           | 1.0211      |
| 9   | Fast RMS Layernorm              | 316      | 9              | 3.1%           | 0.0%           | 1.021       |
| 10  | Fast Cross Entropy Loss         | 315      | 7.4            | 0.4%           | 17.8%          | 1.021       |
| 11  | Manual Autograd MLP             | 302      | 6.8            | 4.0%           | 8.1%           | 1.0222      |
| 12  | Manual Autograd QKV             | 297      | 6.8            | 1.7%           | 0.0%           | 1.0217      |

We provide a breakdown of each optimization we did for the Open Source version of Unsloth on a A10G GPU via AWS. By implementing our changes, we can speed training by 2x, and use 61% less peak VRAM. This section is somewhat more maths heavy, so be warned!

1\. Reduce data upcasting 

By reducing upcasting of weights during QLoRA, we can easily save 7.2% of VRAM, and make training take 21.7% less time.

2\. Bitsandbytes bfloat16

Bitsandbytes internally uses float16, so we have to do an extra memory copy to convert it to bfloat16\. We fix this internally, saving 9% time.

3\. Scaled Dot Product Attention

We use Pytorch's fast implementation of attention, saving 1.4% time. 

4, 5, 6\. Causal Masking, Xformers, Flash Attention 2 

By using a causal mask and not a separate attention mask, we made things 8.1% faster, since we don't need to read the attention matrix. We then switch over to using Xformers, which makes things 8.1% faster and save a whopping 39% of VRAM usage. Switching to Flash Attention v2 had no noticeable effect, since Xformers calls FA2 internally anyways.

7\. Fast RoPE Embeddings

By implementing RoPE Embeddings in OpenAI's Triton, we save another 7.6% of time. But to do so, we must find the derivative of the RoPE function through manual inspection. Notice RoPE can be rewritten as a matrix multiplication between a rotation matrix R and the original matrix Q. If we do this, the derivative is simply R transpose.

8\. Fast RMS Layernorm

Unfortunately, the RMS Layernorm's derivative is much more involved. If you carefully use the chain rule and carefully derive the derivative, we get an ugly derivative for the RMS Layernorm. We again implement this into OpenAI's Triton language, which boosts training by 3.1%.

9\. Fast Cross Entropy Loss

loss \= CrossEntropyLoss ( logits , labels ) C E l o s s \= 1 n ∑ − y i log ⁡ p i C E l o s s \= 1 n ∑ − y i log ⁡ exp ⁡ ( x i ) ∑ exp ⁡ x i C E i \= − y i log ⁡ exp ⁡ ( x i ) ∑ exp ⁡ x i \= − y i ( x i − log ⁡ ∑ exp ⁡ x i ) \= y i ( logsumexp ( x ) − x ) \= { 0 if y \= 0 logsumexp ( x ) − x otherwise d C d x i \= y i ⋅ exp ( x − logsumexp ( x ) ) − d d x i x k ⋅ y i \\begin{align} \\text{loss} = \\text{CrossEntropyLoss}(\\text{logits}, \\text{labels}) \\\\ CE\_{loss} = \\frac{1}{n} \\sum{ - y\_i \\log{p\_i}} \\\\ CE\_{loss} = \\frac{1}{n} \\sum{ - y\_i \\log{\\frac{\\exp(x\_i)}{\\sum{\\exp{x\_i}}}}} \\\\ CE\_i = - y\_i \\log{\\frac{\\exp(x\_i)}{\\sum{\\exp{x\_i}}}} \\\\ = -y\_i (x\_i - \\log{\\sum{\\exp{x\_i}}}) \\\\ = y\_i ( \\text{logsumexp}(x) - x ) \\\\ = \\left\\{ \\\\ \\begin{array}{ c l } 0 & \\quad \\textrm{if } y = 0 \\\\ \\text{logsumexp}(x)-x & \\quad \\textrm{otherwise} \\\\ \\end{array} \\\\ \\right. \\\\ \\frac{dC}{dx\_i} = y\_i \\cdot \\text{exp} \\big( x - \\text{logsumexp}(x) \\big) - \\frac{d}{dx\_i} x\_k \\cdot y\_i \\end{align} 

The Cross Entropy Loss is again a bit more involved. We use the log trick where x = exp(log(x)) to derive the derivative. We also use Wikipedia to find the derivative of the infamous logsumexp function is in fact the softmax function! We slash VRAM usage by 17%.

10, 11\. Manual Autograd

By bracketing correctly, we can massively reduce the actual number of FLOPs during LoRA finetuning! Normally Pytorch's autograd engine backpropagates through the graph from the end to the start. We find by fusing multiple operations into 1, and bracketing correctly through Chained Matrix Multiplication, the actual # of FLOPs is reduced.

( X ( m , d ) T × d W ( m , h ) ) × B ( h , r ) T (X\_{(m,d)}^T \\times dW\_{(m,h)}) \\times B\_{(h,r)}^T 

If you bracket incorrectly, like what Pytorch's autograd currently does, you first do the multiplication of X.T and dW. Take X to be of size (bsz, seq\_len, d). We then reshape X to be of size (m, d), where m is simply bsz \* seq\_len. d is the attention dimension. In Llama 7b it's 4096, whilst in Llama 70b it's 8192.  
  
dW is of size (m, h) where h is the MLP intermediate size. For Llama 7b it's 11,008 and Llama 70b it's 28,672\. And B.T is the LoRA weight of size (h, r), where r is the rank of the LoRA matrix, which can be a small 16 or 64.

( X ( m , d ) T × d W ( m , h ) ) × B ( h , r ) T X ( m , d ) T × d W ( m , h )  takes ( m × d × h )  FLOPs ( X T × d W ) ( d , h ) × B ( h , r ) T  takes ( h × r × d )  FLOPs FLOPs \= ( m × d × h ) + ( h × r × d ) \= ( h × d ) ( m + r ) \\begin{align} (X\_{(m,d)}^T \\times dW\_{(m,h)}) \\times B\_{(h,r)}^T \\\\ X\_{(m,d)}^T \\times dW\_{(m,h)} \\text{ takes } (m \\times d \\times h) \\text{ FLOPs} \\\\ (X^T \\times dW)\_{(d,h)} \\times B\_{(h,r)}^T \\text{ takes } (h \\times r \\times d) \\text{ FLOPs} \\\\ \\text{FLOPs} = (m \\times d \\times h) + (h \\times r \\times d) = (h \\times d)(m + r) \\end{align} 

We find that the slow path takes around (h \* d)(m + r) FLOPs.

X ( m , d ) T × ( d W ( m , h ) × B ( h , r ) T ) d W ( m , h ) × B ( h , r ) T  takes ( h × m × r )  FLOPs X ( m , d ) T × ( d W × B T ) ( m , r )  takes ( m × d × r )  FLOPs FLOPs \= ( h × m × r ) + ( m × d × r ) \= ( m × r ) ( h + d ) \\begin{align} X\_{(m,d)}^T \\times (dW\_{(m,h)} \\times B\_{(h,r)}^T) \\\\ dW\_{(m,h)} \\times B\_{(h,r)}^T \\text{ takes } (h \\times m \\times r) \\text{ FLOPs} \\\\ X\_{(m,d)}^T \\times (dW \\times B^T)\_{(m,r)} \\text{ takes } (m \\times d \\times r) \\text{ FLOPs} \\\\ \\text{FLOPs} = (h \\times m \\times r) + (m \\times d \\times r) = (m \\times r)(h + d) \\end{align} 

And the fast path, where we instead bracket on the 2nd term takes (m \* r)(h + d) FLOPs. We can then divide the slow path by the fast path to get a speedup fraction:

Slow Fast \= ( m + r ) ( h × d ) ( m × r ) ( h + d ) \\frac{\\text{Slow}}{\\text{Fast}} = \\frac{(m + r)(h \\times d)}{(m \\times r)(h + d)} 

To simplify the above, notice normally r is quite small, say 16 or 64\. m can be very big, as a batch size of 4 and a sequence length of 4096 can make m = 4 \* 4096 = 16,384\. This makes (m + r) insignificant, and we drop the addition term. We cannot do this for (m \* r), since a multiplication of 16 much bigger than an addition of 16.

Slow Fast ≈ ( m ) ( h × d ) ( m × r ) ( h + d ) Slow Fast ≈ h × d r ( h + d ) \\begin{align} \\frac{\\text{Slow}}{\\text{Fast}} \\approx \\frac{(m)(h \\times d)}{(m \\times r)(h + d)} \\\\ \\frac{\\text{Slow}}{\\text{Fast}} \\approx \\frac{h \\times d}{r(h + d)} \\\\ \\end{align} 

If we do this, we get a simplified expression, where the speedup is a function of the MLP intermediate size h, the attention size d and the LoRA rank r.  
  
For Llama 7b where h = 11,008 and d = 4,096 and r = 16, we get a speedup of 186.58.  
For Llama 70b where h = 28,672 and d = 8,192 and r = 16, we get a speedup of 398.22.

Other features

* 152334H managed to make Unsloth work with DPO! It's still preliminary support, but it seems like it works via TRL.
* RandomInternetPreson managed to make Unsloth work on WSL! So Windows support is currently in preliminary!
* Other bug fixes - supports all vocab sizes up to 2^16 (65536), group query attention now works correctly.
* GQA on older GPUs is now fully supported via Xformers - we had to manually reshape K and V to make Xformers get tricked into doing a normal attention calculation. Sadly Xformers does not support the backward pass for GQA.

FAQ

* Q: Do you support Mixtral?  
We're working on it!
* Q: How we do buy PRO or MAX?  
We're working on a platform now. Stay tuned!
* Q: Do we reduce FLOPs?  
Yes.
* Q: Does full finetuning work on the Open Source version?  
No. See Issue. All optimizations are turned off, so you will see no noticeable speed improvement, other than from Flash Attention and some Triton kernels.
* Q: Is LoRA, so not QLoRA supported?  
Yes. Pass in load\_in\_4bit to be False.
* Q: Does the PRO / MAX support full finetuning, pretraining?  
Yes.

Thank you for reading! 🦥

Daniel Han  
13 December 2023

Full benchmarking tables

| 1 T4 16GB      | Hugging Face                                                                                  | Flash Attention                                                                               | Unsloth Open                                                                                  | Unsloth Pro Equal                                                                             | Unsloth Pro | Unsloth Max |
| -------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | ----------- | ----------- |
| Alpaca         | 1x                                                                                            | 1.09x                                                                                         | 1.69x                                                                                         | 1.79x                                                                                         | 2.93x       | **8.3x**    |
| code           | [Code](https://colab.research.google.com/drive/1XpLIV4s8Bj5uryB-X2gqM88oRGHEGdaB?usp=sharing) | [Code](https://colab.research.google.com/drive/1LyXu6CjuymQg6ddHX8g1dpUvrMa1nn4L?usp=sharing) | [Code](https://colab.research.google.com/drive/1gsv4LpY7C32otl1rgRo5wXTk4HIitXoM?usp=sharing) | [Code](https://colab.research.google.com/drive/1VtULwRQwhEnVdNryjm27zXfdSM1tNfFK?usp=sharing) |             |             |
| seconds        | 1599                                                                                          | 1468                                                                                          | 942                                                                                           | 894                                                                                           | 545         | 193         |
| memory MB      | 7199                                                                                          | 7059                                                                                          | 6459                                                                                          | 5443                                                                                          |             |             |
| memory saved % | 1.94                                                                                          | 10.28                                                                                         | 24.39                                                                                         |                                                                                               |             |             |

| 1 T4 16GB      | Hugging Face                                                                                  | Flash Attention                                                                                 | Unsloth Open                                                                                  | Unsloth Pro Equal                                                                             | Unsloth Pro | Unsloth Max |
| -------------- | --------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | ----------- | ----------- |
| LAION Chip2    | 1x                                                                                            | 0.99x                                                                                           | 1.80x                                                                                         | 1.75x                                                                                         | 4.15x       | **11.75x**  |
| code           | [Code](https://colab.research.google.com/drive/1EtdStADehE4FVJnU2Cu6O8p9jDYdqG2L?usp=sharing) | [Code](https://colab.research.google.com/drive/1Ik4jO68odUiQIJ%5FszZ3xok5fk58WpA5Q?usp=sharing) | [Code](https://colab.research.google.com/drive/1E2nR4V3bXIWBQIUE7uR39lYPr3UikzqH?usp=sharing) | [Code](https://colab.research.google.com/drive/13jbj8D8FOt9KyXwZt9Yf2MsYkD8CyCVR?usp=sharing) |             |             |
| seconds        | 952                                                                                           | 955                                                                                             | 529                                                                                           | 543                                                                                           | 229         | 81          |
| memory MB      | 6037                                                                                          | 6033                                                                                            | 5797                                                                                          | 4855                                                                                          |             |             |
| memory saved % | 0.07                                                                                          | 3.98                                                                                            | 19.58                                                                                         |                                                                                               |             |             |

| 1 T4 16GB      | Hugging Face                                                                                    | Flash Attention                                                                               | Unsloth Open                                                                                  | Unsloth Pro Equal                                                                                 | Unsloth Pro | Unsloth Max |
| -------------- | ----------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ----------- | ----------- |
| OASST          | 1x                                                                                              | 1.19x                                                                                         | 1.95x                                                                                         | 1.86x                                                                                             | 2.58x       | **7.3x**    |
| code           | [Code](https://colab.research.google.com/drive/1aXzGgEM3yYB6SWy%5FXR81nQFWME40ksSy?usp=sharing) | [Code](https://colab.research.google.com/drive/1-5MdIOp0cM0scC-CdRZhh8OYhnGHqct4?usp=sharing) | [Code](https://colab.research.google.com/drive/1n-fgduZhRUsSjgpqNtVkXA3rSfE7iBdg?usp=sharing) | [Code](https://colab.research.google.com/drive/1z%5FGlHr2M%5FbB4lQrPhdWC7dseZv23cBIy?usp=sharing) |             |             |
| seconds        | 2640                                                                                            | 2222                                                                                          | 1355                                                                                          | 1421                                                                                              | 1024        | 362         |
| memory MB      | 14827                                                                                           | 10391                                                                                         | 8413                                                                                          | 7031                                                                                              |             |             |
| memory saved % | 29.92                                                                                           | 43.26                                                                                         | 52.58                                                                                         |                                                                                                   |             |             |

| 1 T4 16GB      | Hugging Face                                                                                  | Flash Attention                                                                               | Unsloth Open                                                                                      | Unsloth Pro Equal                                                                               | Unsloth Pro | Unsloth Max |
| -------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------- | ----------- |
| Slim Orca      | 1x                                                                                            | 1.21x                                                                                         | 1.77x                                                                                             | 1.85x                                                                                           | 2.71x       | **7.67x**   |
| code           | [Code](https://colab.research.google.com/drive/15yLlJx9IE84kzx7ikky45pRcarPyUtEs?usp=sharing) | [Code](https://colab.research.google.com/drive/16IShIBmjKULWy87I-xURpj4nztTkAF13?usp=sharing) | [Code](https://colab.research.google.com/drive/1CJG3XLg%5FOQpCz71eB7Uqx7wuK%5Fn2b-a8?usp=sharing) | [Code](https://colab.research.google.com/drive/1UmwuWHtlrC6MAfl9mX7A%5FTRfo5iSHDa-?usp=sharing) |             |             |
| seconds        | 2735                                                                                          | 2262                                                                                          | 1545                                                                                              | 1478                                                                                            | 1009        | 356         |
| memory MB      | 13933                                                                                         | 10489                                                                                         | 7661                                                                                              | 6563                                                                                            |             |             |
| memory saved % | 24.72                                                                                         | 45.02                                                                                         | 52.90                                                                                             |                                                                                                 |             |             |

| 2 T4 DDP       | Hugging Face                                                           | Flash Attention                                                    | Unsloth Open                                                       | Unsloth Equal | Unsloth Pro | Unsloth Max |
| -------------- | ---------------------------------------------------------------------- | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------- | ----------- | ----------- |
| Alpaca         | 1x                                                                     | 0.99x                                                              | 4.95x                                                              | 4.44x         | 7.28x       | **20.61x**  |
| code           | [Code](https://www.kaggle.com/danielhanchen/hf-original-alpaca-t4-ddp) | [Code](https://www.kaggle.com/danielhanchen/hf-sdpa-alpaca-t4-ddp) | [Code](https://www.kaggle.com/danielhanchen/unsloth-alpaca-t4-ddp) |               |             |             |
| seconds        | 9882                                                                   | 9946                                                               | 1996                                                               | 2227          | 1357        | 480         |
| memory MB      | 9176                                                                   | 9128                                                               | 6904                                                               | 6782          |             |             |
| memory saved % | 0.52                                                                   | 24.76                                                              | 26.09                                                              |               |             |             |

| 2 T4 DDP       | Hugging Face                                                          | Flash Attention                                                   | Unsloth Open                                                      | Unsloth Equal | Unsloth Pro | Unsloth Max |
| -------------- | --------------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- | ------------- | ----------- | ----------- |
| LAION Chip2    | 1x                                                                    | 1.12x                                                             | 5.28x                                                             | 4.21x         | 10.01x      | **28.32x**  |
| code           | [Code](https://www.kaggle.com/danielhanchen/hf-original-laion-t4-ddp) | [Code](https://www.kaggle.com/danielhanchen/hf-sdpa-laion-t4-ddp) | [Code](https://www.kaggle.com/danielhanchen/unsloth-laion-t4-ddp) |               |             |             |
| seconds        | 5418                                                                  | 4854                                                              | 1027                                                              | 1286          | 541         | 191         |
| memory MB      | 7316                                                                  | 7316                                                              | 5732                                                              | 5934          |             |             |
| memory saved % | 0.00                                                                  | 21.65                                                             | 18.89                                                             |               |             |             |

| 2 T4 DDP       | Hugging Face                                                               | Flash Attention                                                        | Unsloth Open                                                           | Unsloth Equal | Unsloth Pro | Unsloth Max |
| -------------- | -------------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ------------- | ----------- | ----------- |
| OASST (bsz=1)  | 1x                                                                         | 1.14x                                                                  | 5.56x                                                                  | 5.09x         | 5.64x       | **15.97x**  |
| code           | [Code](https://www.kaggle.com/danielhanchen/hf-original-oasst-bsz1-t4-ddp) | [Code](https://www.kaggle.com/danielhanchen/hf-sdpa-oasst-bsz1-t4-ddp) | [Code](https://www.kaggle.com/danielhanchen/unsloth-oasst-bsz1-t4-ddp) |               |             |             |
| seconds        | 4503                                                                       | 3955                                                                   | 811                                                                    | 885           | 798         | 282         |
| memory MB      | 11896                                                                      | 11628                                                                  | 6616                                                                   | 7105          |             |             |
| memory saved % | 2.25                                                                       | 44.38                                                                  | 40.27                                                                  |               |             |             |

| 2 T4 DDP          | Hugging Face                                                                  | Flash Attention                                                           | Unsloth Open                                                              | Unsloth Equal | Unsloth Pro | Unsloth Max |
| ----------------- | ----------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------- | ----------- | ----------- |
| Slim Orca (bsz=1) | 1x                                                                            | 0.97x                                                                     | 5.54x                                                                     | 4.68x         | 6.88x       | **19.46x**  |
| code              | [Code](https://www.kaggle.com/danielhanchen/hf-original-slimorca-bsz1-t4-ddp) | [Code](https://www.kaggle.com/danielhanchen/hf-sdpa-slimorca-bsz1-t4-ddp) | [Code](https://www.kaggle.com/danielhanchen/unsloth-slimorca-bsz1-t4-ddp) |               |             |             |
| seconds           | 4042                                                                          | 4158                                                                      | 729                                                                       | 863           | 588         | 208         |
| memory MB         | 11010                                                                         | 11042                                                                     | 6492                                                                      | 7410          |             |             |
| memory saved %    | \-0.29                                                                        | 41.04                                                                     | 32.70                                                                     |               |             |             |

| 2 T4 DDP       | Hugging Face                                                          | Flash Attention                                                   | Unsloth Open                                                      | Unsloth Equal | Unsloth Pro | Unsloth Max |
| -------------- | --------------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- | ------------- | ----------- | ----------- |
| OASST (bsz=2)  | OOM ❌                                                                 | OOM ❌                                                             | ✓                                                                 | ✓             | ✓           | ✓           |
| code           | [Code](https://www.kaggle.com/danielhanchen/hf-original-oasst-t4-ddp) | [Code](https://www.kaggle.com/danielhanchen/hf-sdpa-oasst-t4-ddp) | [Code](https://www.kaggle.com/danielhanchen/unsloth-oasst-t4-ddp) |               |             |             |
| seconds        | OOM                                                                   | OOM                                                               | 2719                                                              | 3391          | 2794        | 987         |
| memory MB      | OOM                                                                   | OOM                                                               | 8134                                                              | 9600          |             |             |
| memory saved % | OOM                                                                   | OOM                                                               |                                                                   |               |             |             |

| 2 T4 DDP          | Hugging Face                                                             | Flash Attention                                                      | Unsloth Open                                                         | Unsloth Equal | Unsloth Pro | Unsloth Max |
| ----------------- | ------------------------------------------------------------------------ | -------------------------------------------------------------------- | -------------------------------------------------------------------- | ------------- | ----------- | ----------- |
| Slim Orca (bsz=2) | OOM ❌                                                                    | OOM ❌                                                                | ✓                                                                    | ✓             | ✓           | ✓           |
| code              | [Code](https://www.kaggle.com/danielhanchen/hf-original-slimorca-t4-ddp) | [Code](https://www.kaggle.com/danielhanchen/hf-sdpa-slimorca-t4-ddp) | [Code](https://www.kaggle.com/danielhanchen/unsloth-slimorca-t4-ddp) |               |             |             |
| seconds           | OOM                                                                      | OOM                                                                  | 2990                                                                 | 3444          | 2351        | 831         |
| memory MB         | OOM                                                                      | OOM                                                                  | 7594                                                                 | 8881          |             |             |
| memory saved %    | OOM                                                                      | OOM                                                                  |                                                                      |               |             |             |

| 1 A100 40GB    | Hugging Face                                                                                  | Flash Attention 2                                                                             | Unsloth Open                                                                                    | Unsloth Equal                                                                                 | Unsloth Pro | Unsloth Max |
| -------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | ----------- | ----------- |
| Alpaca         | 1x                                                                                            | 1.04x                                                                                         | 1.98x                                                                                           | 2.48x                                                                                         | 5.32x       | **15.64x**  |
| code           | [Code](https://colab.research.google.com/drive/1u4dBeM-0vGNVmmO6X7cScAut-Hyt4KDF?usp=sharing) | [Code](https://colab.research.google.com/drive/1fgTOxpMbVjloQBvZyz4lF4BacKSZOB2A?usp=sharing) | [Code](https://colab.research.google.com/drive/1YIPY%5F18xm-K0iJDgvNkRoJsgkPMPAO3G?usp=sharing) | [Code](https://colab.research.google.com/drive/1ANW8EFL3LVyTD7Gq4TkheC1Z7Rxw-rHp?usp=sharing) |             |             |
| seconds        | 1040                                                                                          | 1001                                                                                          | 525                                                                                             | 419                                                                                           | 196         | 67          |
| memory MB      | 18235                                                                                         | 15365                                                                                         | 9631                                                                                            | 8525                                                                                          |             |             |
| memory saved % | 15.74                                                                                         | 47.18                                                                                         | 53.25                                                                                           |                                                                                               |             |             |

| 1 A100 40GB    | Hugging Face                                                                                    | Flash Attention 2                                                                             | Unsloth Open                                                                                  | Unsloth Equal                                                                                 | Unsloth Pro | Unsloth Max |
| -------------- | ----------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | ----------- | ----------- |
| LAION Chip2    | 1x                                                                                              | 0.92x                                                                                         | 1.61x                                                                                         | 1.84x                                                                                         | 7.05x       | **20.73x**  |
| code           | [Code](https://colab.research.google.com/drive/1gjL1TaKwc%5Fxv2TcxJC8QWEWBG1msh3g2?usp=sharing) | [Code](https://colab.research.google.com/drive/15vlPjMr8xDj5BFhGdqunGaOQSMqXPEXU?usp=sharing) | [Code](https://colab.research.google.com/drive/1zPwvf-BmHyHlPMBxDsY8zS0BnQ-KKbCc?usp=sharing) | [Code](https://colab.research.google.com/drive/1X2uHy-arRsZxqWHvKHwwW102JaMwChD2?usp=sharing) |             |             |
| seconds        | 581                                                                                             | 631                                                                                           | 361                                                                                           | 315                                                                                           | 82          | 28          |
| memory MB      | 7763                                                                                            | 8047                                                                                          | 7763                                                                                          | 6441                                                                                          |             |             |
| memory saved % | \-3.66                                                                                          | 0.00                                                                                          | 17.03                                                                                         |                                                                                               |             |             |

| 1 A100 40GB    | Hugging Face                                                                                  | Flash Attention 2                                                                             | Unsloth Open                                                                                    | Unsloth Equal                                                                                 | Unsloth Pro | Unsloth Max |
| -------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | ----------- | ----------- |
| OASST          | 1x                                                                                            | 1.19x                                                                                         | 2.17x                                                                                           | 2.66x                                                                                         | 5.04x       | **14.83x**  |
| code           | [Code](https://colab.research.google.com/drive/10NzDreFbuWELGUuBv0MOoC7y3MBewaNx?usp=sharing) | [Code](https://colab.research.google.com/drive/1TwdkJ1sHsuEH-kgeCPqSFeCpOnCfz6Ou?usp=sharing) | [Code](https://colab.research.google.com/drive/1AkwjUkOF0XeRBMT%5FS8Uhh74kitEsZHla?usp=sharing) | [Code](https://colab.research.google.com/drive/1roMkp2UjbeK2t3DkNz50cRs1MT92RPFT?usp=sharing) |             |             |
| seconds        | 1852                                                                                          | 1558                                                                                          | 852                                                                                             | 696                                                                                           | 367         | 125         |
| memory MB      | 26431                                                                                         | 16565                                                                                         | 12267                                                                                           | 11223                                                                                         |             |             |
| memory saved % | 37.33                                                                                         | 53.59                                                                                         | 57.54                                                                                           |                                                                                               |             |             |

| 1 A100 40GB    | Hugging Face                                                                                  | Flash Attention 2                                                                             | Unsloth Open                                                                                  | Unsloth Equal                                                                                   | Unsloth Pro | Unsloth Max |
| -------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------- | ----------- |
| Slim Orca      | 1x                                                                                            | 1.18x                                                                                         | 2.22x                                                                                         | 2.64x                                                                                           | 5.04x       | **14.82x**  |
| code           | [Code](https://colab.research.google.com/drive/1UNo1xsMl8YH7xnWnIVjDFnCAPfc0RGgu?usp=sharing) | [Code](https://colab.research.google.com/drive/1zbphER-SKhbSWGjHTfnBLPFyTgIVvaeH?usp=sharing) | [Code](https://colab.research.google.com/drive/156si33585iv4Uh-VILFglUmIMrNCNuc2?usp=sharing) | [Code](https://colab.research.google.com/drive/1%5FmhZy7dfl9jEnJRuJBZJ5y3OwW06jgQA?usp=sharing) |             |             |
| seconds        | 1824                                                                                          | 1545                                                                                          | 821                                                                                           | 691                                                                                             | 362         | 123         |
| memory MB      | 24557                                                                                         | 15681                                                                                         | 10595                                                                                         | 9007                                                                                            |             |             |
| memory saved % | 36.14                                                                                         | 56.86                                                                                         | 63.32                                                                                         |                                                                                                 |             |             |

| 1 A100 40GB          | Hugging Face                                                                                      | Flash Attention 2                                                                               | Unsloth Open                                                                                    | Unsloth Equal                                                                                   | Unsloth Pro | Unsloth Max |
| -------------------- | ------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------- | ----------- |
| Mistral 7B Slim Orca | 1x                                                                                                | 1.15x                                                                                           | 2.15x                                                                                           | 2.53x                                                                                           | 4.61x       | **13.69x**  |
| code                 | [Code](https://colab.research.google.com/drive/1mePk3KzwTD81hr5mcNcs%5FAX3Kbg%5FHa0x?usp=sharing) | [Code](https://colab.research.google.com/drive/1dgHxjvTmX6hb0bPcLp26RXSE6%5Fn9DKj7?usp=sharing) | [Code](https://colab.research.google.com/drive/1SKrKGV-BZoU4kv5q3g0jtE%5FOhRgPtrrQ?usp=sharing) | [Code](https://colab.research.google.com/drive/18yOiyX0T81mTwZqOALFSCX%5FtSAqju6aD?usp=sharing) |             |             |
| seconds              | 1813                                                                                              | 1571                                                                                            | 842                                                                                             | 718                                                                                             | 393         | 132         |
| memory MB            | 32853                                                                                             | 19385                                                                                           | 12465                                                                                           | 10271                                                                                           |             |             |
| memory saved %       | 40.99                                                                                             | 62.06                                                                                           | 68.74                                                                                           |                                                                                                 |             |             |

| 1 A100 40GB    | Hugging Face                                                                                    | Flash Attention 2                                                                               | Unsloth Open                                                                                  | Unsloth Equal                                                                                 | Unsloth Pro | Unsloth Max |
| -------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | ----------- | ----------- |
| Code Llama 34B | OOM ❌                                                                                           | 0.99x                                                                                           | 1.87x                                                                                         | 2.61x                                                                                         | 4.27x       | 12.82x      |
| code           | [Code](https://colab.research.google.com/drive/1ykfz3BqrtC%5FAUFegCzUQjjfUNlxp6Otc?usp=sharing) | [Code](https://colab.research.google.com/drive/12ZypxQh7OC6kBXvWZI-5d05I4m-B%5FhoR?usp=sharing) | [Code](https://colab.research.google.com/drive/1gdHyAx8XJsz2yNV-DHvbHjR1iCef5Qmh?usp=sharing) | [Code](https://colab.research.google.com/drive/1fm7wqx9MJ0kRrwKOfmLkK1Rmw-pySahB?usp=sharing) |             |             |
| seconds        | 1953                                                                                            | 1982                                                                                            | 1043                                                                                          | 748                                                                                           | 458         | 152         |
| memory MB      | 40000                                                                                           | 33217                                                                                           | 27413                                                                                         | 22161                                                                                         |             |             |
| memory saved % | 16.96                                                                                           | 31.47                                                                                           | 44.60                                                                                         |                                                                                               |             |             |

# Unslow AI training now!

Get started for free

Company

About📰 NewsletterPrivacy PolicyTerms of Service

Product

Introduction🐋 DockerDownloadDocumentation🦥 Models

Community

Twitter (X)

Reddit

Hugging Face

Discord

LinkedIn

unsloth sticker logounsloth

\[email protected\]

© 2026 unsloth. All rights reserved.

Join Our Discord