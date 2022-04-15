from bot.credentials import setup
import time 
import tweepy
from textblob import TextBlob

api = setup.setup()

class Mention:
    def mention_reply(self):
        bot_id = int(api.verify_credentials().id_str)
        mention_id = 1
        message = "@{} ．．．"

        mentions = api.mentions_timeline(since_id=mention_id) # Finding mention tweets
        for mention in mentions:
            print("Mention tweet found")
            print(f"{mention.author.screen_name} - {mention.text}")
            mention_id = mention.id
            # Checking if the mention tweet is not a reply, we are not the author, and
            # that the mention tweet contains one of the words in our 'words' list
            # so that we can determine if the tweet might be a question.
            if mention.in_reply_to_status_id is None and mention.author.id != bot_id:
                try:
                    print("Attempting to reply...")
                    api.update_status(message.format(mention.author.screen_name), in_reply_to_status_id = mention.id_str, auto_populate_reply_metadata = True)
                    print("Successfully replied :)")
                except Exception as exc:
                    print(exc)
                    break
        time.sleep(15) # The bot will only check for mentions every 15 seconds, unless you tweak this value
        

    def mention_retweet_draft(self): # Spaghetti code.
        mention_id = 1 # Starting from first item in mention stack
        bot_id = int(api.verify_credentials().id_str) # Grabbing Bot ID

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
                        break
                    except Exception as ex:
                        print(ex)
                        break
                else: # Same logic, but negative polarity.
                    try:
                        api.retweet(api.update_status(status = "．．．" + "\n\n" + "Komi-Translation: " + "\n" + ':(' ))
                        print("Negative polarity detected, retweeting.")
                        break
                    except Exception as ex:
                        print(ex)
                        break
        time.sleep(15)

    def mention_retweet(self):
        bot_id = int(api.verify_credentials().id_str)
        query = "@BotKomi Retweet this."

        mentions = api.mentions_timeline(count = 1)

        for mention in mentions:
            tweet_text = mention.text
            if tweet_text != query:
                break


