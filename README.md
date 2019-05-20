# dialectMap

## Description

In this project, we refer to a few papers. Feel free to add more when you find new, useful papers:

1. [A Latent Variable Model for Geographic Lexical Variation](http://www.cs.cmu.edu/~nasmith/papers/eisenstein+oconnor+smith+xing.emnlp10.pdf): the first paper that detects dialect variations using LDA
2. [Breaking Sticks and Ambiguities with Adaptive Skip-gram](https://arxiv.org/pdf/1502.07257.pdf): AdaGram Model that does word sense disambiguation, with its Julia Implementation: [github](https://github.com/sbos/AdaGram.jl). There is a python implementation, do not use it since its training won't work. To train models, Julia model is the only way.
3. [Freshman or Fresher? Quantifying the Geographic Variation of Internet Language](https://arxiv.org/pdf/1510.06786.pdf)
4. metrics guide: The American Language, H L Mencken (to get the list of words UK vs. USA words)

## Dataset Statistics

### total statistics vs. CMU: 378K tweets (Raw Data)

| Number 	| USA 	| UK 	| Total 	|
|:------:	|:----------:	|:---------:	|:----------:	|
| tweet 	| 2,211,452 	| 1,088,232 	| 3,163,626 	| 
| token 	| 41,349,313 	| 22,267,331 	| 63,616,644 	| 
| term 	| 1,932,868 	| 1,156,624 	| 2,789,423 	| 


### dataset

This `224u-dataset` folder on [google drive](https://drive.google.com/drive/folders/1FHk2x0nk_hCNf8fcGL0XNNep-mvo_BXX?usp=sharing).

- `countryName.txt`: not preprocess the emojis, @xxx, etc
- `countryName_tokenized.txt`: filtered out @xxx and a few text normalization
- `countryName_tok_pos.txt`: word_pos format for the text section

### preprocessing

1. merge_files.py: merge_jsons()
	- e.g. UK.json + UK-no-filter.json + UK-no-filter2.json
	- output: everything will be added to UK-no-filter.json
2. json2txt: remove new lines existing inside text strings
	- output: UK.txt
3. preprocess_tokenize.py
	- output: UK_tokenized.txt, UK_tok_pos.txt
4. merge_files.py: count_stats()















