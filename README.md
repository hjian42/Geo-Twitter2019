# dialectMap

## Description

In this project, we refer to a few papers. Feel free to add more when you find new, useful papers:

1. [A Latent Variable Model for Geographic Lexical Variation](http://www.cs.cmu.edu/~nasmith/papers/eisenstein+oconnor+smith+xing.emnlp10.pdf): the first paper that detects dialect variations using LDA
2. [Breaking Sticks and Ambiguities with Adaptive Skip-gram](https://arxiv.org/pdf/1502.07257.pdf): AdaGram Model that does word sense disambiguation, with its Julia Implementation: [github](https://github.com/sbos/AdaGram.jl). There is a python implementation, do not use it since its training won't work. To train models, Julia model is the only way.

## Dataset Statistics

### total statistics vs. CMU: 378K tweets (Raw Data)

| Number 	| USA 	| UK 	| Australia 	| Total 	| CMU-data 	|
|:------:	|:----------:	|:----------:	|:---------:	|:----------:	|:---------:	|
| tweet 	| 2,211,452 	| 558,058 	| 58,108 	| 5,655,236 	| 377,616 	|
| token 	| 41,349,313 	| 13,608,609 	| 1,070,657 	| 56,028,579 	| 4,703,173 	|
| term 	| 1,932,868 	| 838,769 	| 144,306 	| 2,593,173 	| 164,809 	|

## connect to EC2

```
chmod 400 crawling.pem
ssh -i "crawling.pem" ec2-user@ec2-52-53-201-26.us-west-1.compute.amazonaws.com

chmod 400 crawl-au.pem
ssh -i "crawl-au.pem" ec2-user@ec2-54-219-137-231.us-west-1.compute.amazonaws.com

chmod 400 crawl-usa.pem
ssh -i "crawl-usa.pem" ec2-user@ec2-13-57-195-34.us-west-1.compute.amazonaws.com
```

## set up EC2

```
sudo yum install git 
sudo yum install python-pip
git clone https://github.com/emoryjianghang/dialectMap
sudo pip install tweepy

python crawl.py
```

## set up adaGram

```
Remember to use Julia 0.4:
Github DIR: /Users/hang/.julia/v0.4/AdaGram
export PATH="/Applications/Julia-0.4.7.app/Contents/Resources/julia/bin:$PATH"
sh run.sh
```

## use adaGram

```
using AdaGram
vm, dict = load_model("models/huang_super_300D_0.05_min20_hs_t1e-17.model");
nearest_neighbors(vm, dict, "apple", 2, 10)
disambiguate(vm, dict, "apple", split("fresh tasty breakfast"))
30-element Array{Float64,1}:
```

## train Jacob's tweets with Julia

```
GEOTWEET DIR:
python prepare_adagram.py

AdaGram DIR:
# locally
sh train.sh --min-freq 20 --window 10 --workers 2 --dim 300 --prototypes 30 --alpha 0.1 --epochs 1 --sense-treshold 1e-17 /Users/hang/Desktop/GeoText.2010-10-12/dialects3_tokenized.txt  /Users/hang/Desktop/GeoText.2010-10-12/dialects3.dict ./dialects.model   

# on EC2
sh train.sh --min-freq 20 --window 10 --workers 4 --dim 300 --prototypes 30 --alpha 0.1 --epochs 3 --sense-treshold 1e-17 ~/dialects3_tokenized.txt  ~/dialects3.dict ./dialects.model

```







