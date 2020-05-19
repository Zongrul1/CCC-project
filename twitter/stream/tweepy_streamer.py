from tweepy import API
from tweepy import Cursor
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import tweepy
import credentials
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

    def stream_tweets(self,filters):
        listener = TwitterListener()
        auth = self.twitter_authenticator.authenticate_apps()
        stream = Stream(auth, listener)
        # stream = Stream(auth, listener)
        stream.filter(locations=filters)


class TwitterListener(StreamListener):
### inherit from StreamListener, stored twitter into featched file. ###

    def on_data(self,data):
        try:
            data = json.loads(data)
            # connect couchDB

            if "realtime_tweet" in couch:
                db = couch["realtime_tweet"]
            else:
                db = couch.create("realtime_tweet")
            db.save(data)
        except BaseException as e:
            print("Error on data: %s" %str(e))
    #
    # def on_status(self, status):
    #     data= status._json
    #     # print(data['place']['name'])
    #     if "real-time twitter" in couch:
    #         db = couch["real-time twitter"]
    #     else:
    #         db=couch.create("real-time twitter")
    #     print(data)
    #     if hasattr(status,'retweeted_status'): # check if retweet
    #         try:
    #             print(status.retweeted_status.extended_tweet["full_text"])
    #         except AttributeError:
    #             print(status.retweeted_status.text)
    #     else:
    #         try:
    #             print(status.extended_tweet["full_text"])
    #         except AttributeError:
    #             print(status.text)

    def on_error(self, status_code):
        # avoid rate limit ouccurs
        if status_code == 402:
            return False

        print(status_code)



if __name__  == "__main__":
    couch = couchdb.Server("http://admin:admin@172.26.130.129:5984")
    location = [113.338953078, -43.6345972634, 153.569469029, -10.6681857235]
    twitter_streamer=TwitterStreamer()
    twitter_streamer.stream_tweets(location)


