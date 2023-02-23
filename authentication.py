import os
import sys
import tweepy
from tweepy import API, Client
from tweepy import OAuthHandler, Client, OAuth2AppHandler, OAuth2BearerHandler


def twitter_auth_v1():
    """"
    With this function, we authenticate our credential to connect to Twitter API using the version
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
        api_v1 = tweepy.API(auth)
        return api_v1


def twitter_auth_v2():
    """"
        With this function, we authenticate our credential to connect to Twitter API
        using the version authentication API

        Return: The object of tweepy.OAuthHandler
        """
    try:
        bearer_token = os.environ['TWITTER_BEARER_TOKEN']
    except KeyError:
        sys.stderr.write("TWITTER_* the environment variables does not exists\n")
        sys.exit(1)
        auth_v2 = tweepy.OAuth2BearerHandler(bearer_token)
        api_v2 = tweepy.API(auth_v2)

        return api_v2


def get_auth_api_v1():
    """"
    This function return the API client version 1
    """
    auth = twitter_auth_v1()
    api = API(auth)
    return api


def get_auth_api_v2():
    """"
    This function return the API client version 2
    """
    auth_2 = twitter_auth_v2()
    client = Client(auth_2)
    return client
