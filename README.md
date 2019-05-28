# dialectMap

## Description

In this project, we refer to a few papers. 

1. [A Latent Variable Model for Geographic Lexical Variation](http://www.cs.cmu.edu/~nasmith/papers/eisenstein+oconnor+smith+xing.emnlp10.pdf): the first paper that detects dialect variations using LDA
2. [Breaking Sticks and Ambiguities with Adaptive Skip-gram](https://arxiv.org/pdf/1502.07257.pdf): AdaGram Model that does word sense disambiguation, with its Julia Implementation: [github](https://github.com/sbos/AdaGram.jl). There is a python implementation, do not use it since its training won't work. To train models, Julia model is the only way.
3. [Freshman or Fresher? Quantifying the Geographic Variation of Internet Language](https://arxiv.org/pdf/1510.06786.pdf)
4. metrics guide: The American Language, H L Mencken (to get the list of words UK vs. USA words)

## Dataset Statistics

### total statistics

| Number 	| USA 	| UK 	| Total 	|
|--------	|------------	|------------	|------------	|
| tweet 	| 2,075,394 	| 1,088,232 	| 3,163,626 	|
| token 	| 41,637,107 	| 22,012,953 	| 63,650,060 	|
| term 	| 865,784 	| 469,570 	| 1,167,790 	|

note: CMU geo data has 378K tweets

### dataset

This `224u-dataset` folder on [google drive](https://drive.google.com/drive/folders/1FHk2x0nk_hCNf8fcGL0XNNep-mvo_BXX?usp=sharing).

- `countryName.txt`: raw text data, not preprocess the emojis, @xxx, etc
- `countryName_tokenized.txt`: lower case, filtered out @xxx, emojis, and other text normalizations
- `countryName_tok_pos.txt`: word_pos format for the text section
- `usa_uk.txt`: usa + uk tweets from the tokenized version txt, for adagram















