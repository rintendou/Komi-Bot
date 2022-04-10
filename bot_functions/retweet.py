import credentials.setup
import os
from textblob import TextBlob

api = credentials.setup.setup()

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
                        api.retweet(api.update_status_with_media(status = "．．．" + "\n\n" + "Komi-Translation: " + "\n" + ':)', filename = os.path.join(os.path.dirname(__file__),'..','library',gifs[1]) ))
