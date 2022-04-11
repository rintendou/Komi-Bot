import tweepy

# Do not edit any information or code here. Doing so will break the bot.
def setup():
    CONSUMER_KEY = 'ozzHaV3OSWqGJr3mGwnLhv0Yj'
    CONSUMER_SECRET = '0ALlin8meCfGYQDarlLMZwC009WUVbENAv8Ul9r4wdwcAd8eut'
    ACCESS_TOKEN = '1508485359449124867-RDNNjzrCtRa1Tz7sHC3vcenfQc1BOc'
    ACCESS_TOKEN_SECRET = 'LCy01dzCgX1Tjw2bFWX7MZzGDf3YnKPy3TCU1dIOv6hpL'

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET);
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    return api