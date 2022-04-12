# Create dictionary that holds followers.
# Key-Value pair, user_id and following (boolean).

import tweepy
import credentials.setup

api = credentials.setup.setup()

followerList = api.get_followers()