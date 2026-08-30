# Papers Explained 173: ELECTRA

Papers Explained 173: ELECTRA

Papers Explained 173: ELECTRA

Efficiently Learning an Encoder that Classifies Token Replacements Accurately (ELECTRA), a unique transformer model jointly developed by…

Papers Explained 173: ELECTRA

Efficiently Learning an Encoder that Classifies Token Replacements Accurately (ELECTRA), a unique transformer model jointly developed by Stanford University and Google, employs a smaller masked language model for learning. This compact model intentionally corrupts input text by randomly masking certain portions, and the primary objective of ELECTRA is to discern between the original tokens and their replacements.

Method
An overview of replaced token detection.
The replaced token detection pre-training task rains two neural networks, a generator G and a discriminator D.

The generator is trained to perform masked language modeling (MLM).

The discriminator is trained to distinguish tokens in the data from tokens that have been replaced by generator samples. More specifically, we create a corrupted example x_corrupt by replacing the masked-out tokens with generator samples and train the discriminator to predict which tokens in x_corrupt match the original input x.

Formally, model inputs are constructed according to:

and the loss functions are:

Although similar to the training objective of a GAN, there are several key differences. First, if the generator happens to generate the correct token, that token is considered “real” instead of “fake”; this formulation is found to moderately improve results on downstream tasks.

More importantly, the generator is trained with maximum likelihood rather than being trained adversarially to fool the discriminator.

Lastly, No noise vector is supplied as input to the generator, which is typical with a GAN.

The combined loss is minimized:

Paper

ELECTRA: Pre-training Text Encoders as Discriminators Rather Than Generators 2003.10555

Hungry for more insights?

Don’t miss out on exploring other fascinating threads in this series. Simply click here and uncover the state-of-the-art research!

Do Subscribe for weekly updates!!

By Ritvik Rastogi on August 2, 2024.

Canonical link

Exported from Medium on May 4, 2026.
