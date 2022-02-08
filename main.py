import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
import json

consumer_key = "CONSUMER-KEY"
consumer_secret = "CONSUMER-SECRET"
access_token = "ACCESS-TOKEN"
access_secret = "ACCESS-SECRET"

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token,access_secret)

api = tweepy.API(auth)

def process_or_store(tweet):
    print(json.dumps(tweet))

"""
# Reading my own timeline
for status in tweepy.Cursor(api.home_timeline).items(10):
    # Processing a Single Status
    print(status.text)
"""
"""
# List of all my followers
for friend in tweepy.Cursor(api.friends).items():
    proccess_or_store(friend._json)
"""

# Gathering all incoming tweets about #superbowl
class MyListener(StreamListener):

    def on_data(self, data):
        try:
            with open('python.json', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True

    def on_error(self, status):
        print(status)
        return True


twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['#superbowl'])