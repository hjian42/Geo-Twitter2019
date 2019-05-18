import json

countries = ['UK', 'USA']
# countries = ['UK']

for c in countries:
	i = 0
	file_main = '../tweets2019/{}-no-filter.json'.format(c)
	file_out = '../tweets2019/{}.txt'.format(c)
	with open(file_main) as f_main, open(file_out, 'w') as f_out:
		for line in f_main:
			try:
				tweet_json = json.loads(line)
			except ValueError:
				print('Decoding JSON has failed')
				continue
			tweet_user = 'USER_' + tweet_json['user']['id_str']
			tweet_date = tweet_json['created_at']
			if tweet_json['place']:
				tweet_x = tweet_json['place']['bounding_box']['coordinates'][0][0][0]
				tweet_y = tweet_json['place']['bounding_box']['coordinates'][0][0][1]
				tweet_x, tweet_y = str(tweet_x), str(tweet_y)
			elif tweet_json["coordinates"]:
				# print(tweet_json["coordinates"]['coordinates'])
				tweet_x = tweet_json['coordinates']['coordinates'][0]
				tweet_y = tweet_json['coordinates']['coordinates'][1]
				tweet_x, tweet_y = str(tweet_x), str(tweet_y)
			else:
				# print(tweet_json['user']['location'])
				print('coordinates are NULL')
				continue
			# print(tweet_x, tweet_y)
			tweet_xy = ','.join([tweet_x, tweet_y])
			tweet_text = tweet_json['text'].strip()
			tweet_text = " ".join(tweet_text.split())
			f_out.write('\t'.join([tweet_user, tweet_date, tweet_xy, tweet_x, tweet_y, tweet_text]))
			f_out.write('\n')
			# print(tweet_text)
			i += 1
			# if i == 5:
			# 	break
		print("{}:\tNum of Tweets in Total:\t".format(c), str(i))
		



# raw: total statistics vs. CMU: 378K tweets
# AUS:	Num of Tweets Total:	 52420
# UK:	Num of Tweets Total:	 507920
# USA:	Num of Tweets Total:	 2075395

# after parsing
# AUS:	Num of Tweets in Total:	 52420
# UK:	Num of Tweets in Total:	 507792
# USA:	Num of Tweets in Total:	 2075394
