import credentials.setup
import os
from bot_functions.get_gif import get_gif()
from textblob import TextBlob
import time

api = credentials.setup.setup()
gifs = get_gif()

mention_id = 1

bot_id = int(api.me().id_str)

def retweet_on_enable():
    while True:
        mentions = api.mentions_timeline(since_id = mention_id)

        for mention in mentions:
            print("Mention tweet found.")
            print(f"{mention.author.screen_name} - {mention.text}")
            mention_id = mention.id

            mention_analyzed = TextBlob(mention.text)
            mention_polarity_score = mention_analyzed.polarity
            print(f"Mention tweet has a sentiment value of: {mention_polarity_score}")

            if mention.in_reply_to_status_id is None and mention.author.id != bot_id:
                if mention_polarity_score >= 0.3 and not mention.retweeted:
                    try:
                        api.retweet(api.update_status_with_media(status = "．．．" + "\n\n" + "Komi-Translation: " + "\n" + ':)', filename = os.path.join(os.path.dirname(__file__),'..','library',gifs[0])))
                        print("Retweeted.")
                    except Exception as ex:
                        print("Error.")
                else:
                    api.retweet(api.update_status_with_media(status = "．．．" + "\n\n" + "Komi-Translation: " + "\n" + ':)', filename = os.path.join(os.path.dirname(__file__),'..','library',gifs[2])))
            time.sleep(15)
