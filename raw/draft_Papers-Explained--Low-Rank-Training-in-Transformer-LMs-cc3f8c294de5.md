# Papers Explained: Low-Rank Training in Transformer LMs

Papers Explained: Low-Rank Training in Transformer LMs

Papers Explained: Low-Rank Training in Transformer LMs

This paper investigates applying low-rank parametrization to the feedforward networks (FFNs) in Transformer-based language models, which…

Papers Explained: Low-Rank Training in Transformer LMs

This paper investigates applying low-rank parametrization to the feedforward networks (FFNs) in Transformer-based language models, which account for over 60% of parameters and computational costs, from scratch at large scales (up to 1.3B parameters).

Experiment Setup

A basic Transformer architecture with Rotary Embedding and a basic FFN module composed of two linear layers and a GeLU activation function is employed. The model ranges from 110M to 1.3B parameters and is trained on the RefinedWeb dataset. A random selection of 0.5B tokens is used as the validation set, while the number of training tokens is allocated based on the scaling law.

Only the FFN modules are replaced with low-rank parametrization, using ranks that are half or a quarter of the original hidden state dimension, reducing FFN parameters to 63% or 32% of the original size. The first FFN module remains unchanged to avoid significant performance degradation.
Model and Training configuration.
Analysis
Performance of low-rank parametrization with 63% and 32% of the original FFN module’s parameters.
As model size increases, the performance of low-rank models gets closer to dense models.
Low-rank models exhibit steeper scaling curves, especially at lower parameter percentages (e.g., 32% vs 63%), suggesting greater scaling potential and possible superiority at a fixed computational budget.
Wider, structured networks can match or exceed dense networks when optimized for training FLOPs.
Increased FFN width with low-rank parametrization leads to better GPU utilization, achieving 1.4× and 2.6× speed-ups with 63% and 32% of parameters, respectively, compared to the baseline width of 1536.
The performance of GQA v/s wide, structured networks.
A model with both structured attention and FFN achieves up to 8% to 17% higher throughput than comparable GQA models while maintaining or slightly improving perplexity.

Paper

Investigating Low-Rank Training in Transformer Language Models: Efficiency and Scaling Analysis 2407.09835

That’s a wrap!

If you enjoyed this breakdown, follow for more. I publish new paper explanations most weekdays.

More papers in this series, organized by lab and topic, are in the start here guide.

What paper should I cover next? Let me know in the responses.

View original.

Exported from Medium on August 22, 2026.
