from tkinter.tix import Tree
import credentials.setup
import tweepy 
import time 

#api = tweepy.API(auth)
#tweetid = api.mentions_timeline(*,10,*,*,True,True)
#api = credentials.setup.setup()

def komi_reply():
    #api.update_status(status = 'your reply',in_reply_to_status_id = tweetid, auto_populate_reply_metadata = True)
    
    api = credentials.setup.setup()
    
    bot_id = int(api.verify_credentials().id_str)
    mention_id = 1

    words = ["why", "how", "when", "what", "?"]
    message = "．．．@{}"

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
                if True in [word in mention.text.lower() for word in words]:
                    try:
                        print("Attempting to reply...")
                        api.update_status(message.format(mention.author.screen_name), in_reply_to_status_id = mention.id_str, auto_populate_reply_metadata = True)
                        print("Successfully replied :)")
                    except Exception as exc:
                        print(exc)
        time.sleep(15) # The bot will only check for mentions every 15 seconds, unless you tweak this value








    

