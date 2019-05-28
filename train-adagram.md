## Preprocessing Steps

1. merge_files.py: merge_jsons()
	- e.g. UK.json + UK-no-filter.json + UK-no-filter2.json
	- output: everything will be added to UK-no-filter.json
2. json2txt: remove new lines existing inside text strings
	- output: UK.txt
3. preprocess_tokenize.py
	- output: UK_tokenized.txt, UK_tok_pos.txt
4. merge_files.py: count_stats() 

## set up EC2 (if first time user)

```
sudo yum install git 
sudo yum install python-pip
git clone https://github.com/emoryjianghang/dialectMap
sudo pip install tweepy

python crawl.py
```

## use adaGram on a local machine

```
cd /Users/hang/.julia/v0.4/AdaGram
export PATH="/Applications/Julia-0.4.7.app/Contents/Resources/julia/bin:$PATH"
sh run.sh

# example
sh train.sh --min-freq 20 --window 10 --workers 2 --dim 300 --prototypes 30 --alpha 0.1 --epochs 1 --sense-treshold 1e-17 /Users/hang/Desktop/GeoText.2010-10-12/dialects3_tokenized.txt  /Users/hang/Desktop/GeoText.2010-10-12/dialects3.dict ./dialects.model   

```

## use pre-trained model with adaGram

```
using AdaGram
vm, dict = load_model("models/huang_super_300D_0.05_min20_hs_t1e-17.model");
nearest_neighbors(vm, dict, "apple", 2, 10)
disambiguate(vm, dict, "apple", split("fresh tasty breakfast"))
```






