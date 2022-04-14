import json
import tweepy
import credentials.setup

api = credentials.setup.setup()

all_followers = json.dumps(api.get_followers(), indent = 1)

with open("data/json/all_followers.json", 'w') as json:
    json.write(all_followers)