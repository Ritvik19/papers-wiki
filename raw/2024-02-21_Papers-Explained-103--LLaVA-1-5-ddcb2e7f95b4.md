# Papers Explained 103: LLaVA 1.5

Papers Explained 103: LLaVA 1.5

Papers Explained 103: LLaVA 1.5

LLaVA 1.5 is a 13B model that uses 12M publicly available data along with simple modifications to LLaVA, namely, using CLIP-ViT-L-336px…

Papers Explained 103: LLaVA 1.5

LLaVA 1.5 is a 13B model that uses 12M publicly available data along with simple modifications to LLaVA, namely, using CLIP-ViT-L-336px with an MLP projection and adding academic-task-oriented VQA data with simple response formatting prompts to establish stronger baselines that achieve state-of-the-art across 11 benchmarks.

The project is available on GitHub.

Recommended Reading [Papers Explained 102: LLaVA 1]

Improved Baselines of LLaVA

LLaVA has showcased commendable proficiency in visual reasoning capabilities, but fall short on academic benchmarks that typically require short-form answers.This was attributed to the fact that LLaVA has not been pre trained on large-scale data, as other approaches do. In this note, the scaling effect of data, models and input image resolution are studied on a selection of three datasets and then compare the final model against existing LMMs on a diverse set of 12 benchmarks.
Scaling results on data, model, and resolution.
Response formatting prompts

The inability to balance between short- and long-form VQA is mainly due to ambiguous prompts on the response format and not fine tuning the LLM.

Ambiguous prompts on the response format. For example, `Q: {Question} A: {Answer}`. Such prompts do not clearly indicate the desirable output format, and can overfit an LLM behaviorally to short-form answers even for natural visual conversations.

To address this, a single response formatting prompt that clearly indicates the output format, is appended at the end of VQA questions when promoting short answers: `Answer the question using a single word or phrase`.

When fine tuned with such prompts, LLaVA is able to properly adjust the output format according to the user’s instructions, and does not require additional processing of the VQA data using ChatGPT.

By merely including VQAv2 in training, LLaVA’s performance on MME significantly improves (1323.8 vs 502.8) and outperforms InstructBLIP by 111 points.

MLP vision-language connector

Inspired by the improved performance in self-supervised learning by changing from a linear projection to an MLP, it is found that improving the vision-language connector’s representation power with a two layer MLP can improve LLaVA’s multimodal capabilities, compared with the original linear projection design.
Hyperparameters of LLaVA-1.5.
LLaVA-1.5 uses the same set of hyperparameters as the original LLaVA, except that we halve the learning rate in pretraining due to the usage of the MLP projection layer instead of the original linear projection layer design.

Academic task oriented data

Four additional datasets that are used in InstructBLIP are included: OKVQA, A-OKVQA OCRVQA and TextCaps. A-OKVQA is converted to multiple choice questions and a specific response formatting prompt is used: `Answer with the option’s letter from the given choices directly`.

With only a subset of the datasets InstructBLIP uses, LLaVA already surpasses it on all three tasks suggesting LLaVA’s effective design.

Further adding region-level VQA datasets (Visual Genome, RefCOCO) improves the model’s capability of localizing fine-grained visual details.

Additional scaling

The input image resolution is further scaled up to allow LLM to clearly “see” the details of images, and the GQA dataset is added as an additional visual knowledge source. ShareGPT data is also incorporated and the LLM is scaled up to 13B.

Training Data
Instruction-following Data Mixture of LLaVA-1.5.
The final training data mixture contains a variety of datasets: VQA, OCR, region-level VQA, visual conversation and language conversation data. Multiple strategies are used to reduce training cost and enhance efficiency:

For all VQA datasets, QA pairs from the same training image are merged into a single conversation.
For ShareGPT, invalid conversations are filtered out. Unlike Vicuna, long conversations that surpass 2048 tokens are truncated rather than splitting to multiple conversations. This results in ∼40K conversations.
Each QA pair in A-OKVQA is augmented k times, where k is the number of choices per question, to counterbalance the lack of multiple-choice data.
80K conversations are sampled from OCRVQA.
For Visual Genome, 10 annotations are sampled for images with additional annotations.
For RefCOCO, conversations are dissected into segments, each containing fewer than 10 conversations.
Language conversations are often longer than visual ones. Hence for each batch, conversations are sampled only from a single modality, and this speeds up the training by 25%, and the final outcome is not affected.

All data splits are concatenated together and sampled

with the same probability.

Evaluation
Comparison with SoTA methods on 12 benchmarks.
LLaVA achieves the best performance on 11/12 benchmarks, and ranks the second on the other, while using significantly less pretraining and instruction tuning data.
It achieves top performance with a simple architecture, academic compute, and public datasets, providing a reproducible and affordable baseline for future research.
Visual instruction tuning is highlighted as more crucial for improving LMM capabilities than extensive pretraining.
LLaVA-1.5, even with a smaller model size, surpasses the 80B IDEFICS model in multimodal instruction-following capabilities.
It exhibits zero-shot multilingual capabilities without specific fine-tuning for multilingual multimodal instruction following.
LLaVA-1.5 outperforms Qwen-VL-Chat in Chinese multimodal instruction following on MMBenchCN by 7.3%.
The computational cost of training LLaVA-1.5 is approximately double that of its predecessor due to increased image input resolution.

LLaVA-1.5 demonstrates zero-shot format instruction generalization, effectively handling “Unanswerable” responses and constrained JSON formats.
The response format prompt effectively instructs the model to do so (11.1% → 67.8% on unanswerable questions)
Response format prompt for evaluation.
Despite reduced hallucination, LLaVA-1.5 can still produce misinformation, necessitating cautious use in critical applications.
Futher limitations include the model’s use of full image patches, which may extend training iterations, and its inability to process multiple images or excel in certain problem-solving domains.

Paper

Improved Baselines with Visual Instruction Tuning 2310.03744

Recommended Reading [Multi Modal Transformers]

Hungry for more insights?

Don’t miss out on exploring other fascinating threads in this series. Simply click here and uncover the state-of-the-art research!

Do Subscribe for weekly updates!!

By Ritvik Rastogi on February 21, 2024.

Canonical link

Exported from Medium on May 4, 2026.
