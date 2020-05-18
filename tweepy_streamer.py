from tweepy import API
from tweepy import Cursor
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import tweepy
import credentials
import numpy as np
import pandas as pd
import json
import couchdb

class TwitterClinet():
    def __init__(self,twitter_user=None):
        self.auth =TwitterAuthenticator().authenticate_apps()
        self.twitter_client=API(self.auth)
        self.twitter_user = twitter_user

    def get_twitter_client_api(self):
        return self.twitter_client

    def get_user_timeline_tweets(self,num_tweets):
        tweets = []
        for tweet in Cursor(self.twitter_client.user_timeline,id=self.twitter_user).items(num_tweets):
            tweets.append(tweet)
        return tweets

    def get_friends_list(self,num_friends):
        friends = []
        for friend in Cursor(self.twitter_client.friends,id = self.twitter_user).items(num_friends):
            friends.append(friend)
        return friends

    def get_home_timeline(self,num_tweets):
        home_timeline_tweets = []
        for tweet in Cursor(self.twitter_client.home_timeline,id=self.twitter_user).items(num_tweets):
            home_timeline_tweets.append(tweet)
        return home_timeline_tweets


class TwitterAuthenticator():

# # #  handels app authentication to access the twitter API # # #

    def authenticate_apps(self):
        auth = OAuthHandler(credentials.API_KEY, credentials.API_SECRET_KEY)
        auth.set_access_token(credentials.ACCESS_TOKEN, credentials.ACCESS_TOKEN_SECRET)
        return auth


class TwitterStreamer():
# # # collect twitter # # #
    def __init__(self):
        self.twitter_authenticator = TwitterAuthenticator()

    def stream_tweets(self,fechted_tweets_filename,filters):
        listener = TwitterListener(fechted_tweets_filename)
        auth = self.twitter_authenticator.authenticate_apps()
        stream = Stream(auth, listener)
        stream.filter(locations=filters)


class TwitterListener(StreamListener):
### inherit from StreamListener, stored twitter into featched file. ###
    def __init__(self,fetched_tweets_filename):
        self.fetched_tweets_filename =fetched_tweets_filename

    def on_data(self,data):
        try:
            data = json.loads(data)
            # connect couchDB

            if "test1" in couch:
                db = couch["test1"]
            else:
                db = couch.create("test1")
            # db = couch["test"]
            db.save(data)

            print(data['place']['name'])
            #write to json here
            # with open(self.fetched_tweets_filename,'a') as tf:
            #     tf.write(data)
            return True
        except BaseException as e:
            print("Error on data: %s" %str(e))
        return False

    def on_error(self, status_code):
        # avoid rate limit ouccurs
        if status_code == 402:
            return False

        print(status_code)

class TwitterProcessor():

    def tweets_to_datafram(self,tweets):
        df = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['Tweets'])
        df['id'] = np.array([tweet.id for tweet in tweets])
        return df


if __name__  == "__main__":
    couch = couchdb.Server("http://admin:admin@172.26.130.129:5984/")

    auth = OAuthHandler(credentials.API_KEY, credentials.API_SECRET_KEY)
    auth.set_access_token(credentials.ACCESS_TOKEN, credentials.ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth, wait_on_rate_limit=True)
    geo = "-25.274398,133.775136,2000km"
    keywords = ["COVID19"]

    # for i in range(5):
    #     print(i,ini_id)
    for tweet in tweepy.Cursor(api.search, q=keywords, geocode=geo,
                               lang="en",
                               tweet_mode="extended").items():
        data = tweet._json
        if "covid19_777" in couch:
            db2 = couch["covid19_777"]
        else:
            db2 = couch.create("covid19_777")
        # db = couch["test"]
        db2.save(data)
        # data is a dict.
        print(type(data))

    # hashtag_list = ['Covid19']
    location = [113.338953078, -43.6345972634, 153.569469029, -10.6681857235]
    fetched_tweets_filename = "tweets.txt"

    twitter_streamer=TwitterStreamer()
    twitter_streamer.stream_tweets(fetched_tweets_filename,location)

    # twitter_client = TwitterClinet('COVID19_AUS')
    # print(twitter_client.get_user_timeline_tweets(1))

    # twitter_processor = TwitterProcessor()
    # twitter_client = TwitterClinet()
    # api = twitter_client.get_twitter_client_api()
    # tweets = api.user_timeline('COVID19_AUS',count=400)
    # df = twitter_processor.tweets_to_datafram(tweets)
    # print(tweets[2].text)
    # attributes of tweets
    # print(dir(tweets[0]))
    # print(tweets[0].geo)
    # print(tweets[0].place)
    # print(tweets[1].id)
    # print(df.head(400))
