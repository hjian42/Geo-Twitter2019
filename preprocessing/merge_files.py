import json

countries = ['UK', 'USA']

def merge_jsons():
	for c in countries:
		i = 0
		file_main = '../tweets2019/{}-no-filter.json'.format(c)
		file_added = '../tweets2019/{}.json'.format(c)
		with open(file_main, 'a') as f_main, open(file_added) as f_added:
			for line in f_added:
				f_main.write(line)
				i += 1
			print("{}:\tNum of Tweets Appended:\t".format(c), str(i))

# Append Statistics
# AUS:	Num of Tweets Appended:	 7140
# UK:	Num of Tweets Appended:	 143800
# USA:	Num of Tweets Appended:	 572500

def merge_txts():
	f_main = open('../tweets2019/dialects3.txt', 'w')
	i = 0
	for c in countries:
		file_added = '../tweets2019/{}.txt'.format(c)
		with open(file_added) as f_added:
			for line in f_added:
				f_main.write(line)
				i += 1
		print("{} added new tweets, in total:\t".format(c), str(i))
	f_main.close()

# merge_txts()
# merging txt files
# AUS added new tweets, in total:	 58108
# UK added new tweets, in total:	 616166
# USA added new tweets, in total:	 2827618

def count_stats():
	main_tweet_count = 0
	main_token_count = 0
	main_term_set = set()
	for c in countries:
		tweet_count = 0
		token_count = 0
		term_set = set()
		file_added = '../cmu-tweet.txt'
		with open(file_added) as f_added:
			for line in f_added:
				tokens = line.split()
				tweet_count += 1
				token_count += len(tokens)
				[term_set.add(token) for token in tokens]
				[main_term_set.add(token) for token in tokens]
				main_tweet_count += 1
		print("{} added new tweets".format(c))
		print("{} tweets".format(tweet_count))
		print("{} tokens".format(token_count))
		print("{} terms".format(len(term_set)))
		main_tweet_count += tweet_count
		main_token_count += token_count
	print('\n')
	print("TOTAL\t {} tweets".format(main_tweet_count))
	print("TOTAL\t {} tokens".format(main_token_count))
	print("TOTAL\t {} terms".format(len(main_term_set)))

# count_stats()





















