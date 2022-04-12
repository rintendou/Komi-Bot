import credentials.setup
import tweepy

api = credentials.setup.setup()
bot_id = int(api.verify_credentials().id_str)
class Moderation:
    def nuke(self):
        tweets = api.user_timeline()
        if not tweets: 
           print("Empty timeline, aborting nuke process" + '\n' + "========")
        else: 
            print("You are about to delete all of Komi's tweets. Are you sure you want to continue? (Y/N)")
            delete = input("> ")
            if delete.lower() == 'y' or delete.upper() == 'Y':
                for tweet in tweets:
                        api.destroy_status(tweet.id)
                        print("Deleted: " , tweet.id, '\n')
                print("Successfully nuked Komi's timeline." + '\n' + "========")