import re
from collections import defaultdict

countries = ['USA', 'UK']
# concatenation of usa tweets + uk tweets
out = open('../tweets2019/usa_uk.txt', 'w') 
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

for country in countries:
    datafile = "../tweets2019/{}_tokenized.txt".format(country)
    with open(datafile, encoding = "utf-8") as f:
        for line in f:
            parts = line.split("\t")
            if len(parts) != 6:
                print('Invalid tweets')
                continue
            username, dt, _xy, x, y, text = parts
            clean_text = clean_tweets(text)
            for w in clean_text.split():
                if w:
                    word_count[w] += 1
            # print(clean_text)
            out.write(clean_text)
            out.write('\n')
out.close()

with open("../tweets2019/usa_uk.dict", 'w') as out:
  for w in word_count:
    print(w, word_count[w])
    out.write("".join([w, '\t', str(word_count[w]), '\n']))