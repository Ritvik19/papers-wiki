# Papers Explained 487: CLAP

Papers Explained 487: CLAP

Papers Explained 487: CLAP

Papers Explained 486: CLAP

Contrastive Language-Audio Pretraining (CLAP) learns to connect language and audio by using two encoders and a contrastive learning to bring audio and text descriptions into a joint multimodal space.

Method

The input consists of audio and text pairs passed to an audio encoder and a text encoder. Both representations are connected in a joint multimodal space with linear projections. The space is learned with the (dis)similarity of audio and text pairs in a batch using contrastive learning. The pretrained encoders with their projection layers can be used to compute audio and text embeddings and enable Zero-Shot Classification.

Contrastive Language-Audio Pretraining:

Input: The method takes a batch of N audio-text pairs, represented as {Xa, Xt}, where Xa is the processed audio (F spectral components x T time bins) and Xt is the text.
Encoding: Audio and text are passed through audio (fa(.)) and text (ft(.)) encoders, respectively, resulting in representations ˆXa (N x V) and ˆXt (N x U).
Projection: The audio and text representations are projected into a joint multimodal space of dimension d using learnable linear projections La and Lt, resulting in embeddings Ea (N x d) and Et (N x d).
Similarity Measurement: A similarity matrix C (N x N) is computed as the scaled dot product of Et and the transpose of Ea, using a temperature parameter τ. The diagonal of C represents correct audio-text pairs.
Loss Function: A symmetric cross-entropy loss (L) is calculated based on the similarity matrix C. This loss is the average of the log of the diagonal of the softmax of C along both the text and audio axes.
Training: The audio encoder, text encoder, and linear projections are jointly trained by minimizing the loss L.

Zero-Shot Linear Classification:

Embeddings: Given a target dataset with C classes and N test audios, audio and text embeddings are computed for all audios and classes using the pre-trained encoders and projection layers.
Similarity: The cosine similarity is calculated between each test audio embedding and all class label embeddings, resulting in N logits per audio (one for each class).
Probability Distribution: The logits are converted into a probability distribution using softmax (for binary or multiclass classification) or sigmoid (for multilabel classification).

Dataset

The training dataset for CLAP was built using 128,010 audio and text pairs from four datasets: FSD50k, ClothoV2, AudioCaps, and MACS.

FSD50k (36k clips, 0.3–30 seconds) provided audio from freesound.org, with captions created by concatenating the title and description metadata, ignoring class labels.
ClothoV2 (7k clips, 15–30 seconds) had 5 captions per clip, resulting in 5 audio-text pairs per clip.
AudioCaps (46k clips, 10 seconds) contained audio from AudioSet with one crowdsourced caption per clip.
MACS (4k clips, 10 seconds) had multiple captions per clip, which were paired with the same audio to create 17k pairs. Some clips from the datasets were unavailable at the time of download.
Training dataset statistics.
Downstream Tasks

16 datasets from 8 different domains are used as downstream tasks:

ESC50: Environmental classification with 50 events, 2k files of 5 seconds each, 5-fold cross-validation, and accuracy as the metric.
FSD50K: Sound event classification with 200 events, 51k files ranging from 0.3 to 30 seconds each, train/val/test split, and mAP as the metric.
UrbanSound8K: Urban sound classification with 10 sounds, 8k files of 4 seconds each, 10-fold cross-validation, and accuracy as the metric.
DCASE2017 Task4: Sound event classification with 17 sounds recorded in a domestic environment, 30k files of 10 seconds each, train/val/test split, and accuracy as the metric.
AudioSet: Sound event classification with 527 sounds from YouTube videos, 2M files of 10 seconds each, train/val/test split, and accuracy as the metric.
TUT 2017: Acoustic scene classification with 15 acoustic scenes in outdoor and indoor environments, 52k files of 10 seconds each, train/val/test split, and accuracy as the metric.
GTZAN Music Speech: Binary classification to distinguish between speech and music, 120 files of 30 seconds each, 10-fold cross-validation, and accuracy as the metric.
GTZAN Genres: Music genre classification with 10 genres, 1k files of 30 seconds each, 10-fold cross-validation, and accuracy as the metric.
Mridangam Stroke: Music stroke classification with 10 strokes from Mridangam, 1k files of 0.81 seconds each, 5-fold cross-validation, and accuracy as the metric.
Mridangam Tonic: Music tonic classification with 6 tonics from Mridangam, 1k files of 0.81 seconds each, 5-fold cross-validation, and accuracy as the metric.
Beijing Opera Percussions: Instrument classification with 4 percussion instruments from Beijing Opera, 236 files of 4.77 seconds each, 5-fold cross-validation, and accuracy as the metric.
CREMA-D: Emotion recognition with 6 emotions, 7k files of 5 seconds each, 5-fold cross-validation, and accuracy as the metric.
RAVDESS: Emotion recognition with 8 emotions, 2.5k files of 5 seconds each, 5-fold cross-validation, and accuracy as the metric.
Speech Commands V2: Keyword spotting with 13 commands, 100k files of 1 second each, train/val/test split, and accuracy as the metric.
Vocal Sound: Human vocal sound classification with 6 vocalizations, 21k files of 5 seconds each, train/val/test split, and accuracy as the metric.
LibriCount: Speaker count estimation with simulated cocktail party audios (0–10 speakers), 5k files of 5 seconds each, 5-fold cross-validation, and accuracy as the metric.
Datasets used as Downstream Tasks.
Model Architecture

Log Mel spectrogram representations of audio with a sampling rate of 44.1 KHz, hop size of 320 secs, window size 1024 secs, and 64 Mel bins in the range of 50–8000 Hz were used. During training, each audio clip is randomly truncated to a continuous segment of 5 secs, or padded if shorter. The captions were not altered.

The CNN14 model was chosen as the audio encoder. The model has 80.8 million parameters, an embedding size of 2048, and was pretrained with 2M audio clips from AudioSet.

The text encoder chosen is BERT base uncased. The model has 110 million parameters. The max text sequence length was limited to 100 chars for computational efficiency. The [CLS] token from the final layer of BERT is used as the text embedding with a size of 768. Both, the audio and text embeddings are projected into a multimodal space with two learnable projection matrices resulting in an output dimension of 1024.

Training involved unfreezing both encoders for 40 epochs.

Evaluation

Zero-Shot (ZS) Performance

CLAP (ZS) achieved State-of-the-Art (SoTA) on established Sound Event Classification (SEC) datasets like FSD50K, US8K, and ESC50.
For ESC50, CLAP achieved 82.6% accuracy, surpassing human performance (81%) and AudioCLIP (69%) by an absolute 12%.
For US8K, CLAP achieved 73% accuracy, outperforming AudioCLIP (65%) by an absolute 8%.
For the multi-label dataset FSD50K, CLAP beat Wav2CLIP (3%) by an absolute 27% mAP.
On GTZAN’s Music vs Speech Classification, CLAP achieved 100% accuracy, even outperforming supervised models.
CLAP (ZS) performed better than random on all downstream tasks, showing good to slightly better than random performance on some music and speech-related tasks (e.g., 47% acc in Instrument Classification, 50% acc in Vocal Sound dataset, up to 4% acc improvement in ER and KWS).
CLAP (Best) achieved SoTA on 5 datasets: GTZAN Music vs Speech Classification (100% acc), GTZAN Music Genre Classification (91.3% acc), Mri. Stroke Classification (97.94% acc), Mri. Tonic Classification (95.34% acc), and Vocal Sounds Classification (97.95% acc).
CLAP underperformed SoTA by at most 7% in other tasks, with the lowest performance on ER’s RAVDESS (64% acc vs SoTA of 81%).

The best average CLAP (ZS) score was obtained by unfreezing both encoders, while the worst score was obtained by freezing both encoders.
Surprisingly, unfreezing the text encoder performed better than unfreezing the audio encoder.

Paper

CLAP: Learning Audio Concepts From Natural Language Supervision 2206.04769

Hungry for more insights?

Don’t miss out on exploring other fascinating threads in this series. Simply click here and uncover the state-of-the-art research!

Do Subscribe for weekly updates!!

By Ritvik Rastogi on November 6, 2025.

Canonical link

Exported from Medium on May 4, 2026.
