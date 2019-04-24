# dialectMap

## connect to EC2

```
chmod 400 crawling.pem
ssh -i "crawling.pem" ec2-user@ec2-13-56-212-72.us-west-1.compute.amazonaws.com


chmod 400 crawl-au.pem
ssh -i "crawl-au.pem" ec2-user@ec2-54-219-137-231.us-west-1.compute.amazonaws.com
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
```