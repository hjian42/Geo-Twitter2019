from __future__ import with_statement
from collections import defaultdict
import os,sys
import twokenize
import nltk
import re

country = 'USA'
word_count = defaultdict(int)

def clean_tweets(text):
    text = re.sub(r'&[a-z]{3};', ' <sym> ', text)  # '&amp;'
    text = re.sub(r'&gt;', '>', text)
    text = re.sub(r'&lt;', '<', text) 
    text = re.sub(r'@\w+', ' <user> ', text)
    ENCODE_EMOJI = re.compile(u'([\U00010000-\U0010ffff])|([\U00002600-\U000027BF])|([\U0001f300-\U0001f64F])|([\U0001f680-\U0001f6FF])', flags=re.UNICODE)  # emoji
    text = ENCODE_EMOJI.sub(r'', text)
    text = re.sub(' +', ' ', text)
    
    return text.strip().lower()

def get_tokens(text):
  toks = twokenize.tokenize(text.lower())
  toks = [t for t in toks if not t.startswith('@') and t != 'rt' ]
  # toks = [t.replace("#","") for t in toks]
  return toks

def get_pos_tokens(text):
  pos_tokens = nltk.pos_tag(nltk.word_tokenize(text))
  return ["_".join(pair) for pair in pos_tokens]


datafile = "../tweets2019/{}.txt".format(country)
outputfile = "../tweets2019/{}_tokenized.txt".format(country)
pos_outputfile = "../tweets2019/{}_tok_pos.txt".format(country)

with open(datafile, encoding = "utf-8") as f, open(outputfile, 'w') as out, open(pos_outputfile, 'w') as out1:
  for line in f:
    parts = line.split("\t")
    if len(parts) != 6:
      print('Invalid tweets')
      continue
    username, dt, _xy, x, y, text = parts
    tok_text = " ".join(get_tokens(text))
    clean_text = clean_tweets(tok_text)
    out.write('\t'.join([username, dt, _xy, x, y, clean_text]))
    out.write('\n')


with open(outputfile, encoding = "utf-8") as f, open(pos_outputfile, 'w') as out1:
  for line in f:
    parts = line.split("\t")
    if len(parts) != 6:
      print('Invalid tweets')
      continue
    username, dt, _xy, x, y, text = parts
    tok_pos_text = " ".join(get_pos_tokens(text))
    out1.write('\t'.join([username, dt, _xy, x, y, tok_pos_text]))
    out1.write('\n')








  