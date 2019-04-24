from crawl import *
import json

with open('UK.json') as f:
	print('------------------')
	for line in f:
		data = json.loads(line)
		if not has_url(data['text']) and is_normal_user(data['user']):
			print(json.dumps(data['text'], indent=4))