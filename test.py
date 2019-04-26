from crawl import *
import json
i = 0
with open('UK.json') as f:
	print('------------------')
	for line in f:
		data = json.loads(line)
		if not has_url(data['text']) and is_normal_user(data['user']):
			print(json.dumps(data['text'], indent=4))
		i += 1
print("Num of Tweets:\t", str(i))