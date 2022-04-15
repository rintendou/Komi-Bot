import json
from bot.credentials import setup

api = setup.setup()

follower_history = api.get_follower_ids()

print(follower_history)

def get_follower_history(): 
    with open("/data/json/follower_history.json", "w") as history:
        json.dump(follower_history, history)
