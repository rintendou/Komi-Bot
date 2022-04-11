import tweepy

# Once you have set your keys, do not edit any information or code here. Doing so will break the bot.
def setup():
    CONSUMER_KEY = 'x'
    CONSUMER_SECRET = 'x'
    ACCESS_TOKEN = 'x'
    ACCESS_TOKEN_SECRET = 'x'

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET);
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    return api