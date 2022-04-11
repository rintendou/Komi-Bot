import credentials.setup 
import time 

api = credentials.setup.setup()

def reply_on_enable():
    bot_id = int(api.verify_credentials().id_str)
    mention_id = 1

    message = "@{} ．．．"

    while True:
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
