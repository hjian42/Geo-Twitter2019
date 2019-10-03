# Geo-Twitter2019

## Description

In this project, we use a novel non-parametric skip-gram model to capture the dialectal changes of English on multiple resolutions. This repository contains the tweets ids we used for training the model. You are free to crawl the data using these ids and preprocess the data using our tools to replicate our research results. 

## Dataset

| Number 	| USA 	| UK 	| Total 	|
|--------	|------------	|------------	|------------	|
| tweet 	| 2,075,394 	| 1,088,232 	| 3,163,626 	|
| token 	| 41,637,107 	| 22,012,953 	| 63,650,060 	|
| term 	| 865,784 	| 469,570 	| 1,167,790 	|

note: CMU geo data only contain 378K tweets

### Model

To use our model implementation, you should visit the github page [DialectGram](https://github.com/yuxingch/DialectGram). There are four models in the github repository:
  - baseline models: frequency model and syntactic model
  - GEODIST model: region-specific embeddings
  - DialectGram model: a novel approach to compose dialect-sensitive word embeddings, based on Adaptive Skip-gram.

### Demo

You can play with our demo on the website: [demo]()

  
### Acknowledgement

We would like to acknowledge the following resources when we implement our models:

1. [Eisenstein, Jacob, et al. "A latent variable model for geographic lexical variation." Proceedings of the 2010 conference on empirical methods in natural language processing. Association for Computational Linguistics, 2010.](http://www.cs.cmu.edu/~nasmith/papers/eisenstein+oconnor+smith+xing.emnlp10.pdf)
2. [Bartunov, Sergey, et al. "Breaking sticks and ambiguities with adaptive skip-gram." Artificial Intelligence and Statistics. 2016.](https://arxiv.org/pdf/1502.07257.pdf)
3. [Bamman, David, Chris Dyer, and Noah A. Smith. "Distributed representations of geographically situated language." Proceedings of the 52nd Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers). 2014.](http://acl2014.org/acl2014/P14-2/pdf/P14-2134.pdf)
4. [Kulkarni, Vivek, Bryan Perozzi, and Steven Skiena. "Freshman or fresher? quantifying the geographic variation of internet language." arXiv preprint arXiv:1510.06786 (2015).](https://arxiv.org/pdf/1510.06786.pdf)
5. [Python Implementation of AdaGram](https://github.com/lopuhin/python-adagram)
6. [Julia Implementation of AdaGram](https://github.com/sbos/AdaGram.jl)


## Citation
Jiang, Hang*; Haoshen Hong*; Yuxing Chen*; and Vivek Kulkarni. 2019. DialectGram: Automatic Detection of Dialectal Changes with Multi-geographic Resolution Analysis. To appear in *Proceedings of the Society for Computation in Linguistics*. New Orleans: Linguistic Society of America. 

```
@inproceedings{Jiang:Hong:Chen:2020:SCiL,
  Author = {Jiang, Hang  and  Hong, Haoshen  and  Chen, Yuxing  and  Kulkarni, Vivek},
  Title = {DialectGram: Automatic Detection of Dialectal Changes with Multi-geographic Resolution Analysis},
  Booktitle = {Proceedings of the Society for Computation in Linguistics},
  Location = {New Orleans},
  Publisher = {Linguistic Society of America},
  Address = {Washington, D.C.},
  Year = {2020}}
```











