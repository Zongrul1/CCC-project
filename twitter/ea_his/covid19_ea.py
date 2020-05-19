from tweepy import OAuthHandler

import credentials
import tweepy

import couchdb



auth = tweepy.AppAuthHandler(credentials.API_KEY, credentials.API_SECRET_KEY)
api = tweepy.API(auth, wait_on_rate_limit=True,
				   wait_on_rate_limit_notify=True)


# geo = "-25.274398,133.775136,200km"
keywords = ["COVID19 OR CORONAVIRUS OR EPIDEMIC OR PANDEMIC OR OUTBREAK"]
couch = couchdb.Server("http://admin:admin@172.26.130.129:5984/")

for tweet in tweepy.Cursor(api.search,q=keywords,count = 100,
                           lang="en",
                           tweet_mode = "extended").items():
    data = tweet._json
    if "covid19_global" in couch:
        db2 = couch["covid19_global"]
    else:
        db2 = couch.create("covid19_global")
    db2.save(data)
