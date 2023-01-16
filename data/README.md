# This American Life (TAL) Speech Recognition and Diarization Dataset

based on "Speech Recognition and Multi-Speaker Diarization of Long Conversations" (https://arxiv.org/abs/2005.08072)

@inproceedings{interspeech_2020_multispk_asr_sd,
  author    = {Huanru Henry Mao and
               Shuyang Li and
               Julian J. McAuley and
               Garrison W. Cottrell},
  title     = {Speech Recognition and Multi-Speaker Diarization of Long Conversations},
  booktitle = {Interspeech 2020, 21st Annual Conference of the International Speech
               Communication Association, Shanghai, China, 25-29 October 2020},
  year      = {2020},
  url       = {https://arxiv.org/abs/2005.08072},
}

# transcription

In terms of transcription, planning to use for fine-tuning the ASR model and GPT-2 model.
So do some of preprocessing, including:
- concatenate the whole conversation into one comma separated string (test, train, valid)
- The sequence of each conversation in the same episode is maintained.

* If you want to use the original data, please refer to the original data source.