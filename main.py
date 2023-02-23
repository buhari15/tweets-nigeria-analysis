import csv
import json

import tweepy
from tweepy import Cursor, API
import pandas as pd
from authentication import get_auth_api_v1, get_auth_api_v2
from devenv import devenv_auth, auth_v2
from datetime import datetime

latitude = 9.0765  # geographical centre of search
longitude = 7.3986  # geographical centre of search
max_range = 500  # search range in kilometres
num_results = 1000

# def tweet_search():
#     query = '*'
#     return query


# def get_tweet_search():
#     api = authentication_data()
#     query = tweet_search()
#     query = api.search_tweets(q=query, geocode="%f,%f,%dkm" % (latitude, longitude, max_range), count=1000)
#     for tweet in query:
#         data = tweet.text
#     return data
#
#
# def get_trends():
#     api = authentication_data()
#     woeid_Kaduna = 23424908
#     trends = api.get_place_trends(woeid_Kaduna)
#     for t in trends:
#         for trend in t['trends']:
#             print(trend['name'])


if __name__ == '__main__':
    api = devenv_auth()

    # with open('tweets_ng.jsonl', 'w') as f:
    #     query = '* -is:retweet place_country:NG'
    #     now = datetime.now()
    #     # end_time ='2023-02-21T00:00:00Z'
    #     query = tweepy.Paginator(client.search_all_tweets, tweet_fields=['context_annotations', 'created_at'],  query=query, end_time=now,
    #                              max_results=20000).flatten(limit=20000)
    #     for tweet in query:
    #         f.write(tweet)

    with open('tweets_ng.jsonl', 'w') as f:
        query = '* -is:retweet'
        tweets = tweepy.Cursor(api.search_tweets, query, geocode="%f,%f,%dkm" % (latitude, longitude, max_range),
                              count=1000).items(20000)
        # query = client.search_tweets(q=query, geocode="%f,%f,%dkm" % (latitude, longitude, max_range),
        #                              count=10000,
        #                              )
        # # query = tweepy.Cursor(client.search_tweets, count=10)
        for tweet in tweets:
            f.write(json.dumps(tweet._json) + "\n")

        # for tweet in Cursor(client.search_tweets(q=query, geocode="%f,%f,%dkm" %
        #                                                        (latitude, longitude, max_range), count=1000,)):
        #     for status in tweet:
        #         f.write(json.dumps(status._json)+"\n")

        # query = client.search_tweets(q=query, geocode="%f,%f,%dkm" % (latitude, longitude, max_range), count=1000,
        #                              )
        # for tweet in query:
        #     f.write(tweet)
