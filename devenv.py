import tweepy
from tweepy import OAuthHandler, OAuth2AppHandler

CONSUMER_KEY = "k5BmUtGVy7NoctgR5ucM2CXSs"
CONSUMER_SECRET = "fJ16Fgiz6WrvVmlm82NhFLWIberSHQm7BZqT3BdXFRlj77kK6v"
ACCESS_TOKEN = "1575781950391926784-OLoIDzr5woZ7kZObH2SNC9c9rnXKVY"
ACCESS_TOKEN_SECRET = "s2FerY0EOdSI41FgvrSnJDtVWpwA3lDhNfiW6lVpNiF9x"
BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAIzGhgEAAAAA17D9WlxUR20w0Cr5qbHdRW5RwZ4%3D72A9RoXJ1QBWXbToW7Klp1MsROH017wY536qeQ57HF3Ngf7vXx"


def devenv_auth():
    auth = tweepy.OAuth2AppHandler(consumer_key=CONSUMER_KEY,
                                   consumer_secret=CONSUMER_SECRET,
                                   )
    auth = tweepy.API(auth)
    return auth


def auth_v2():
    client = tweepy.Client(bearer_token=BEARER_TOKEN)
    client = tweepy.Client(client)
    return client
