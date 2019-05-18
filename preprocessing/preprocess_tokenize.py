from __future__ import with_statement
from collections import defaultdict
import os,sys
import twokenize
import nltk


country = 'USA'
word_count = defaultdict(int)

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

# with open(datafile, encoding = "utf-8") as f, open(outputfile, 'w') as out, open(pos_outputfile, 'w') as out1:
#   for line in f:
#     parts = line.split("\t")
#     if len(parts) != 6:
#       # print('Invalid tweets')
#       continue
#     username, dt, _xy, x, y, text = parts
#     tok_text = " ".join(get_tokens(text))
#     out.write('\t'.join([username, dt, _xy, x, y, tok_text]))
#     out.write('\n')


with open(outputfile, encoding = "utf-8") as f, open(pos_outputfile, 'w') as out1:
  for line in f:
    parts = line.split("\t")
    if len(parts) != 6:
      # print('Invalid tweets')
      continue
    username, dt, _xy, x, y, text = parts
    tok_pos_text = " ".join(get_pos_tokens(text))
    out1.write('\t'.join([username, dt, _xy, x, y, tok_pos_text]))
    out1.write('\n')


# with open("../tweets2019/{}.dict".format(country), 'w') as out:
#   for w in word_count:
#     print(w, word_count[w])
#     out.write("".join([w, '\t', str(word_count[w]), '\n']))








  