from bot.credentials import setup
import tweepy

api = setup.setup()
bot_id = int(api.verify_credentials().id_str)

class Moderation:
    def nuke(self):
        tweets = api.user_timeline(count = 200) # Only returns past 20 tweets. Figuring out a way to improve this.
        if not tweets: # If tweets is false (empty list):
           print("Empty timeline, aborting nuke process" + '\n' + "========" + '\n')
        else: # If tweets is true (list exists):
            print("You are about to delete all of Komi's tweets. Are you sure you want to continue? (Y/N)")
            delete = input("> ")
            if delete.lower() == 'y' or delete.upper() == 'Y':
                for tweet in tweets:
                        api.destroy_status(tweet.id)
                        print("Deleted: " , tweet.id, '\n')
                print("Successfully nuked Komi's timeline." + '\n' + "========")