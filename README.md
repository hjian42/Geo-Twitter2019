# dialectMap

## Description

In this project, we use skip-gram models to capture the dialectal changes between the United States and the United Kingdom on social media.

## Dataset Statistics

### total statistics

| Number 	| USA 	| UK 	| Total 	|
|--------	|------------	|------------	|------------	|
| tweet 	| 2,075,394 	| 1,088,232 	| 3,163,626 	|
| token 	| 41,637,107 	| 22,012,953 	| 63,650,060 	|
| term 	| 865,784 	| 469,570 	| 1,167,790 	|

note: CMU geo data contain 378K tweets

### dataset

This `geo-tweets2019-dataset` folder on [google drive](https://drive.google.com/drive/folders/1FHk2x0nk_hCNf8fcGL0XNNep-mvo_BXX?usp=sharing).

- `countryName.txt`: raw text data, not preprocess the emojis, @xxx, etc
- `countryName_tokenized.txt`: lower case, filtered out @xxx, emojis, and other text normalizations
- `countryName_tok_pos.txt`: word_pos format for the text section

### Model

To use our model implementation, you should visit the github page [GEODIST-PyTorch](https://github.com/yuxingch/GEODIST-PyTorch). There are four models in the github repository:
  - baseline models: frequency model and syntactic model
  - GEODIST model: obtain region-specific embeddings
  - AdaGram model: a wrapper of AdaGram model to use in our framework
  
### References

1. [A Latent Variable Model for Geographic Lexical Variation](http://www.cs.cmu.edu/~nasmith/papers/eisenstein+oconnor+smith+xing.emnlp10.pdf): the first paper that detects dialect variations using LDA
2. [Breaking Sticks and Ambiguities with Adaptive Skip-gram](https://arxiv.org/pdf/1502.07257.pdf): AdaGram Model that does word sense disambiguation, with its Julia Implementation: [github](https://github.com/sbos/AdaGram.jl).
3. [Freshman or Fresher? Quantifying the Geographic Variation of Internet Language](https://arxiv.org/pdf/1510.06786.pdf)














