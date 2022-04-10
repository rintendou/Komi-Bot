import credentials.setup
from bot_functions.get_gif import get_gif
from textblob import TextBlob
import time

api = credentials.setup.setup()

mention_id = 1 # Starting from first item in mention stack

bot_id = int(api.verify_credentials().id_str) # Grabbing Bot ID

def retweet_on_enable():
    while True:
        mentions = api.mentions_timeline(since_id = mention_id) # Grabbing all mentions

        for mention in mentions: 
            print("Mention tweet found.")
            print(f"Mention tweet: {mention.author.screen_name} - {mention.text}")
            mention_id = mention.id

            mention_analyzed = TextBlob(mention.text) # TextBlob API analyzing the polarity of a tweet.
            mention_polarity_score = mention_analyzed.polarity # Scoring hte analyzed tweet.
            print(f"Mention tweet has a sentiment value of: {mention_polarity_score}")

            if mention.in_reply_to_status_id is None and mention.author.id != bot_id: 
                if mention_polarity_score >= 0.3 and not mention.retweeted: # Checking for positive polarity score and assuring that it has not been retweeted already.
                    try:
                        api.retweet(api.update_status(status = "．．．" + "\n\n" + "Komi-Translation: " + "\n" + ':)'))
                        print("Positive polarity detected, retweeting.")
                    except Exception as ex:
                        print(ex)
                        break
                else: # Same logic, but negative polarity.
                    try:
                        api.retweet(api.update_status(status = "．．．" + "\n\n" + "Komi-Translation: " + "\n" + ':(' ))
                        print("Negative polarity detected, retweeting.")
                    except Exception as ex:
                        print(ex)
                        break
        time.sleep(15)

