import tweepy
from tweepy import Stream
from tweepy.streaming import StreamListener 
from tweepy import OAuthHandler
import json
import re

LOCATION_UK = [-11.22,49.96,1.69,59.37]
LOCATION_USA = [-130.16,25.58,-62.93,49.34] # no alaska
LOCATION_AUS = [112.467, -55.05, 168, -9.133]

@classmethod
def parse(cls, api, raw):
    status = cls.first_parse(api, raw)
    setattr(status, 'json', json.dumps(raw))
    return status

def has_url(text):
    if re.search(r'http', text):
        return True
    else:
        return False

def is_normal_user(user):

    if user['followers_count'] and user['followers_count'] < 1000:
        if user['friends_count'] and user['friends_count'] < 1000:
            return True

    return False

class MyListener(StreamListener):
    
    def on_data(self, data):
        global data_list
        try:
            if len(data_list) == 20:
                if data_list:
                    with open('AUS.json', 'a') as f:
                        print('Write ', NUM_OF_TWEETS['count'], 'tweets')
                        for data in data_list:
                            f.write(data)
                data_list = []
            else:
                data_json = json.loads(data)
                if not has_url(data_json['text']) and is_normal_user(data_json['user']):
                    data_list.append(data)
                    NUM_OF_TWEETS['count'] += 1
            NUM_OF_TWEETS['seen'] += 1
            if NUM_OF_TWEETS['seen'] % 20 == 0:
                print('seen:\t', NUM_OF_TWEETS['seen'], 'count:\t', NUM_OF_TWEETS['count'])
            return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True
 
    def on_error(self, status):
        print(status)
        return True
 
#filter the tweets
if __name__ == '__main__':

    data_list = []
    NUM_OF_TWEETS = {'count': 0, 'seen': 0}

    access_token = "1108546352688971778-N0kJHmUM6mKa5wBQGy0qRxQ5myHtiO"
    access_secret = "FdRkD5QfoxO0B6zNGxKy1P3m3qvs6EF36USl8LHFO6Wp5"
    consumer_key = "BhihQwFhwxwEGpgjn27t8koRy"
    consumer_secret = "2ctEwnFvu3eAhCr8bvtUdaTKyLvkljQOiaRoUYtz8rmJ6TljmN"

    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)

    api = tweepy.API(auth)

    # Status() is the data model for a tweet
    tweepy.models.Status.first_parse = tweepy.models.Status.parse
    tweepy.models.Status.parse = parse
    twitter_stream = Stream(auth, MyListener())
    twitter_stream.filter(locations=LOCATION_AUS, languages=["en"])




