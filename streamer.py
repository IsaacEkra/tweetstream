from tweetParser import TweetParser
import credentials
import tweepy
import sys
import time
import os

parser = TweetParser()

class StreamListener(tweepy.StreamListener):
    """docstring for StreamListener."""

    #Overwrite __init__ call original from super class StreamListener
    def __init__(self):
        self.start = time.time()
        super(StreamListener, self).__init__()

    #Ignore any retweets.
    def on_status(self, status):
        if status.retweeted:
            return

        #Parsing individual tweets for content.
        if (time.time() - self.start) < float(parser.get_limit()):
            parser.set_handle(status.user.screen_name)
            parser.set_tweet(status.text)
            parser.set_time(status.created_at)
            parser.set_url("https://twitter.com/" + parser.get_handle() + "/status/" + str(status.id_str))

            #Printing and storing tweets
            parser.log()
            print(status.text)
            os.linesep
            return True
        else:
            return False

    #Timeout and other errors handling.
    def on_error(self, status_code):
        if status_code == 420:
            return False

#Setting up topic filter list
def setup():
    filterList = []
    start = None
    if sys.argv[1].isdigit():
        start = 2
    else:
        start = 1

    for x in range(start, len(sys.argv)):
        filterList.append(str(sys.argv[x]))
    return filterList

#Check for streaming time limit (Defaults to 30 seconds if not specified)
def validTime():
    if sys.argv[1].isdigit():
        parser.set_limit(sys.argv[1])
    else:
        parser.set_limit(30)

#Authentication to Twitter's API End Point References.
def run():
    #Reading Authentication information from credentials file
    auth = tweepy.OAuthHandler(credentials.TWITTER_APP_KEY, credentials.TWITTER_APP_SECRET)
    auth.set_access_token(credentials.TWITTER_KEY, credentials.TWITTER_SECRET)
    api = tweepy.API(auth)

    #Setting up streaming environment
    stream_listener = StreamListener()
    parser.set_topics(setup())
    parser.set_limit(sys.argv[1])
    validTime()

    #Streaming tweets using the Tweepy library.
    stream = tweepy.Stream(auth=api.auth, listener=stream_listener)
    stream.filter(track=parser.get_topics())

#Main
if __name__ == '__main__':
    run()
