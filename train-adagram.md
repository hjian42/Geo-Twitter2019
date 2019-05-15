## set up EC2 (if first time user)

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







