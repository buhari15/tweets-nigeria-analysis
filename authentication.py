import os
import sys
import tweepy
from tweepy import API, Client
from tweepy import OAuthHandler, Client, OAuth2AppHandler, OAuth2BearerHandler


def twitter_auth_v1():
    """"
    With this function, we authenticate our credential to connect to Twitter API using the version 1
    authentication API

    Return: The object of tweepy.OAuthHandler
    """
    try:
        consumer_key = os.environ['TWITTER_CONSUMER_KEY']
        consumer_secret = os.environ['TWITTER_CONSUMER_SECRET']
        access_token = os.environ['TWITTER_ACCESS_TOKEN']
        access_token_secret = os.environ['TWITTER_ACCESS_TOKEN_SECRET']
    except KeyError:
        sys.stderr.write("TWITTER_* the environment variables does not exists\n")
        sys.exit(1)
        auth = tweepy.OAuth2AppHandler(consumer_key, consumer_secret, access_token, access_token_secret)
        auth = tweepy.API(auth)
        return auth


def twitter_auth_v2():
    """"
        With this function, we authenticate our credential to connect to Twitter API
        using the version 2 authentication API

        Return: The object of tweepy client
        """
    try:
        bearer_token = os.environ['TWITTER_BEARER_TOKEN']
    except KeyError:
        sys.stderr.write("TWITTER_* the environment variables does not exists\n")
        sys.exit(1)
        client = tweepy.Client(bearer_token)
        client = tweepy.Client(client)
        return client



