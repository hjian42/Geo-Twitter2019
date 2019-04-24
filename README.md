# dialectMap

## connect to EC2

```
chmod 400 crawling.pem
ssh -i "crawling.pem" ec2-user@ec2-13-56-212-72.us-west-1.compute.amazonaws.com


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
sh train.sh /Users/hang/Desktop/GeoText.2010-10-12/tokenized.txt  /Users/hang/Desktop/GeoText.2010-10-12/test.dict ./tweet.model
```







