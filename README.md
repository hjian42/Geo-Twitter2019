# dialectMap

## Description

In this project, we refer to a few papers. Feel free to add more when you find new, useful papers:

1. [A Latent Variable Model for Geographic Lexical Variation](http://www.cs.cmu.edu/~nasmith/papers/eisenstein+oconnor+smith+xing.emnlp10.pdf): the first paper that detects dialect variations using LDA
2. [Breaking Sticks and Ambiguities with Adaptive Skip-gram](https://arxiv.org/pdf/1502.07257.pdf): AdaGram Model that does word sense disambiguation, with its Julia Implementation: [github](https://github.com/sbos/AdaGram.jl). There is a python implementation, do not use it since its training won't work. To train models, Julia model is the only way.
3. [Freshman or Fresher? Quantifying the Geographic Variation of Internet Language](https://arxiv.org/pdf/1510.06786.pdf)
4. metrics guide: The American Language, H L Mencken (to get the list of words UK vs. USA words)

## Dataset Statistics

### total statistics vs. CMU: 378K tweets (Raw Data)

| Number 	| USA 	| UK 	| Australia 	| Total 	| CMU-data 	|
|:------:	|:----------:	|:----------:	|:---------:	|:----------:	|:---------:	|
| tweet 	| 2,211,452 	| 558,058 	| 58,108 	| 5,655,236 	| 377,616 	|
| token 	| 41,349,313 	| 13,608,609 	| 1,070,657 	| 56,028,579 	| 4,703,173 	|
| term 	| 1,932,868 	| 838,769 	| 144,306 	| 2,593,173 	| 164,809 	|


### dataset 

This `224u-dataset` folder on [google drive](https://drive.google.com/drive/folders/1FHk2x0nk_hCNf8fcGL0XNNep-mvo_BXX?usp=sharing).

- `countryName.txt`: not preprocess the emojis, @xxx, etc
- `countryName_tokenized.txt`: filtered out @xxx and a few text normalization
- `countryName_tok_pos.txt`: word_pos format for the text section

### preprocessing

1. merge_files.py: merge_jsons()
	- e.g. UK.json + UK-no-filter.json + UK-no-filter2.json
	- OUTPUT: everything will be added to UK-no-filter.json
2. json2txt: fixed new lines inside text strings
	- OUTPUT: UK.txt
3. preprocess_tokenize.py
	- OUTPUT: UK_tokenized.txt, UK_tok_pog.txt

























