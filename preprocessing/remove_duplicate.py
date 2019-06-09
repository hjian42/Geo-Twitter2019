

country = "UK"
datafile = "../tweets2019/{}_tokenized.txt".format(country)
outputfile = "../tweets2019/{}_uniq_tokenized.txt".format(country)

text_set = set()
text_num = 0
with open(datafile, encoding = "utf-8") as f, open(outputfile, 'w') as out:
  for line in f:
    parts = line.split("\t")
    if len(parts) != 6:
      print('Invalid tweets')
      continue
    username, dt, _xy, x, y, text = parts
    # hash_str = username + text
    if text not in text_set:
	    out.write('\t'.join([username, dt, _xy, x, y, text]))
	    out.write('\n')

    text_set.add(text)
    text_num += 1

print(len(text_set), 'out of', text_num, 'unique %:', len(text_set)/text_num * 100)

# for UK.txt and USA.txt
# UK unique percentage
# 1008723 1088232 92.69374545133758%
# USA unique percentage
# 2025164 2075394 97.57973666686904%

# for UK_tokenized.txt and USA_tokenized.txt
# USA
# 1883153 out of 2075394 unique %: 90.73713232282641
# UK
# 941472 out of 1088232 unique %: 86.51390512317226


