class TweetParser(object):

    def __init__(self):
        self.topics = []
        self.handle = None
        self.tweet = None
        self.time = None
        self.url = None
        self.limit = None

    #Setters
    def set_topics(self, topics):
        self.topics = topics

    def set_handle(self, handle):
        self.handle = handle

    def set_tweet(self, tweet):
        self.tweet = tweet

    def set_time(self, time):
        self.time = time

    def set_url(self, url):
        self.url = url

    def set_limit(self, limit):
        self.limit = limit

    #Getters
    def get_topics(self):
        return self.topics

    def get_handle(self):
        return self.handle

    def get_tweet(self):
        return self.tweet

    def get_time(self):
        return self.time

    def get_url(self):
        return self.url

    def get_limit(self):
        return self.limit

    # Storing tweets in log file for later analysis
    def log(self):
        with open('log.txt', 'a', encoding='utf-8') as f:
            f.write("Handle: {0}\nTweet: {1}\nTime and Date: {2}\nSource: {3}\n\n".format(self.get_handle(), self.get_tweet(), self.get_time(), self.get_url()))
        f.close()
