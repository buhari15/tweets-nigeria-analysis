import csv
import json

import tweepy
from tweepy import Cursor, API
import pandas as pd
from authentication import twitter_auth_v1, twitter_auth_v2

# Abuja the capital city of Nigeria latitude and longitude coordinates are used. Because the tweets coming from Kaduna
# state are not much. Furthermore, it is only about 200klm from Abuja to Kaduna. 500 max range is used to cover Kaduna
# as well as Abuja to have enough tweets for further processing.
latitude = 9.0765  # geographical centre of search
longitude = 7.3986  # geographical centre of search
max_range = 500  # search range in kilometres
num_results = 1000


if __name__ == '__main__':
    api = twitter_auth_v1()

    with open('tweets_ng.jsonl', 'w') as f:
        query = '* -is:retweet'
        tweets = tweepy.Cursor(api.search_tweets, query, geocode="%f,%f,%dkm" % (latitude, longitude, max_range),
                              count=1000).items(20000)

        for tweet in tweets:
            f.write(json.dumps(tweet._json) + "\n")


