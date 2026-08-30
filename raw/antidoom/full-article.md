# Reducing Doom Loops with Final Token Preference Optimization

Source: https://www.liquid.ai/blog/antidoom

Doom loops are repetitive degeneration during inference: the model repeats a span until the context window fills. Antidoom adapts Antislop via Final Token Preference Optimization (FTPO), training on chosen/rejected pairs at the single token that starts a loop.

Results: LFM2.5-2.6B early checkpoint doom-loop rate 10.2% to 1.4%; Qwen3.5-4B 22.9% to 1% under greedy sampling. Code at github.com/Liquid4All/antidoom.
