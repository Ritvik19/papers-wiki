# Papers Explained 480: olmOCR 2

Papers Explained 480: olmOCR 2

Papers Explained 480: olmOCR 2

Papers Explained 480: olmOCR 2

olmOCR 2 is a specialized, 7B vision language model (VLM) trained using reinforcement learning with verifiable rewards (RLVR), where the rewards are a diverse set of binary unit tests. To scale unit test creation, a pipeline is developed for generating synthetic documents with diverse and challenging layouts, known ground-truth HTML source code, and extracted test cases.

The data and models are available at HuggingFace.

Why Unit Tests?

olmOCR-Bench measures the performance of OCR systems by defining a set of unit test cases for each document. These test cases can check for any of the following properties:

Text Presence: Checks that certain phrases appear exactly in the document
Text Absence: Checks that certain phrases do not appear (e.g., headers, footers, or page numbers)
Natural Reading Order: Checks sentences for reading order correctness
Table Accuracy: Checks the relative position of cells (with specific values) in a table
Math Formula Accuracy: Checks that a given math formula visually renders the same way with KaTeX
Baseline Robustness: Checks that long repeated n-grams or non-target language characters do not appear.

While popular OCR benchmarks often use a form of edit distance against a ground truth olmOCR-Bench is developed around binary unit tests for two key properties:

Equal treatment of ‘‘ties’’: Floating document elements like tables or figures lack a definitive ground truth representation. Unit tests can allow for these different-yet-equivalently-correct representations of the same OCR’d content to yield similar scores, while edit distance often rewards/penalizes these cases differently.
Continuous score doesn’t necessarily measure ‘‘correctness’’: The use of edit distance as a continuous scoring function rewards/penalizes OCR output in a manner that doesn’t correlate with practical notions of correctness, such as placing greater emphasis on correct ordering of main body text rather than caption placement or post-rendered correctness of a LaTeX formula rather than the LaTeX form itself.

Scaling Unit Test Generation for RLVR

Documents containing relevant, difficult-to-OCR material are sampled. A general VLM is iteratively prompted to first create, and then refine, the HTML code that best represents the rasterized image of a page.

Layout analysis is first performed using the VLM with a picture of a randomly sampled page from PDF documents. The VLM is asked to identify the general layout of the page, such as the number of columns, presence of images or tables, headers and footers, and so on. This step provides guidance during HTML page generation to improve coverage of unit test elements.
Content rendering is then performed by prompting the general VLM again with the previous model output and the same document image, and asking it to “render this document as clean, semantic HTML” fitting into the same dimensions as the original.
Output refinement is achieved by rendering the HTML generated at the previous step, converting it to an image, and passing it to the general VLM along with the original document image and the generated HTML. The general VLM is prompted to refine its HTML to better match the original.

Claude-sonnet-4–20250514 is used as the general VLM for creating olmOCR-Bench-compatible test cases based on the semantics of the HTML the VLM produced. The final data mix, olmOCR2-synthmix-1025, consists of 2,186 PDF pages, across which 30,381 test cases are created.

Alongside olmOCR2-synthmix-1025, a refreshed mix for supervised fine-tuning, olmOCR-mix-1025, is used. The dataset contains 267,962 pages from over 100,000 PDFs sampled from diverse sources, including 9,828 pages from national archives. Compared to olmOCR-mix-0225, the new mix has been re-processed using GPT-4.1 instead of GPT-4o, has more consistent equation formatting (with \[ and \( for block and inline math), uses HTML format for tables, and includes basic alt text for images.

Training

A Qwen2.5-VL-7B-Instruct model that has been fine-tuned on olmOCR-mix-1025 is trained for one epoch on olmOCR2-synthmix-1025. For each document, 28 completions are generated. Each completion gets scored using the standard olmOCR-Bench scoring rules, where each test case is either a pass or fail, and the reward is the fraction from 0.0 to 1.0 of passing test cases. Besides the unit test above, two additional rewards are included to ensure correct output format: a binary reward for whether the model completion ends with the EOS token, and a reward between 0 and 1 to ensure that the model outputs document metadata at the top of its response (e.g., primary language, rotation correction factor). To maximize performance, it is beneficial to train multiple models, and average, or soup, their weights. In detail, six models with different random seeds are trained, and their weights are souped at the end.

Evaluation
OCR model performance comparison.
Dynamic temperature scaling: The first version of olmOCR set a default temperature of 0.8. Sampling at a lower temperature tends to give better results but at the risk of VLM inference encountering repetition loops. To take advantage of low temperatures while mitigating this repetition issue, dynamic temperature scaling is used. This scaling starts at 0.1 and continually increases to 0.2, 0.3 and so on up to a max of 0.8. Each increase is triggered off a failure in the model to generate an EOS token (and thus repeat infinitely). This resulted in significant improvement in overall benchmark performance.

Better prompting: An unintended bug was found in which the order of image and text was mismatched between training and inference prompts. Standardizing prompt order by always including text first in all settings improved benchmark performance substantially. Experimenting with the reverse order found no meaningful difference in OCR performance. However, placing any fixed text first allows for prompt caching by the inference engine.

New trainer: A reimplementation of the trainer for VLM finetuning was conducted, incorporating minor hyperparameter adjustments (e.g., avoiding weight decay on the bias and layer norm weights). No meaningful benchmark score difference was found from this change.

YAML: The first olmOCR was trained to output JSON objects. A switch to YAML was made, which reduced the retry rate dramatically. This is speculated to be because the model does not need to remember how many open quotes there are currently in the JSON and can simply output an EOS token as soon as it is done.

Image Resizing: Initial olmOCR used 1024px on the longest edge; olmOCR 2 uses 1288px instead. Bigger images do appear to yield slightly better performance across many model families, though they take more dedicated compute.

Qwen 2.5 VL: Switching from Qwen 2 VL, which was the base model in olmOCR, to Qwen 2.5 VL resulted in a slight improvement in benchmark score.

Handle blank pages: A bug was caught in the data loader for the olmOCR model where all instances of blank pages were being skipped. The model, never having been trained on blank pages, would hallucinate in such cases. The data loader was fixed and the model was retrained, though this didn’t impact benchmark scores.

Finally, olmOCR 2 demonstrates a significant improvement in benchmark performance. The best model, reported here, is the result of:

A single epoch of SFT training on olmOCR-mix-1025,
A single epoch of RL training over synthetic data olmOCR2-synthmix-1025,
Repeating the RL training for six random seeds and averaging (or “souping”) the checkpoints. Importance sampling was used at both the token level (3 runs) and the sequence level (3 runs).

Paper

olmOCR 2: Unit Test Rewards for Document OCR 2510.19817

Hungry for more insights?

Don’t miss out on exploring other fascinating threads in this series. Simply click here and uncover the state-of-the-art research!

Do Subscribe for weekly updates!!

By Ritvik Rastogi on October 29, 2025.

Canonical link

Exported from Medium on May 4, 2026.
