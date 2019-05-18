from __future__ import with_statement
from odict import odict
from collections import defaultdict
import os,sys
import twokenize

datafile = "../full_text.txt"

def get_tokens(text):
  toks = twokenize.tokenize(text.lower())
  toks = [t for t in toks if not t.startswith('@') and t != 'rt' ]
  # toks = [t.replace("#","") for t in toks]
  return toks

word_xys = defaultdict(list)
word_users=defaultdict(lambda:defaultdict(int))

for line in os.popen("pv "+datafile):
  parts = line[:-1].split("\t")
  username,dt, _xy, x,y,text = parts
  
  for w in get_tokens(text):
    # x,y = float(x),float(y)
    word_xys[w].append((x,y))
    word_users[w][username] += 1

# for w in word_users:
#   if len(word_users[w]) < 30: continue
#   print "\t".join([w, " ".join(["%s,%s" % xy for xy in word_xys[w]])])
  
  

  