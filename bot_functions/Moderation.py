import credentials.setup
import tweepy

api = credentials.setup.setup()

class Moderation:
    def nuke(self):
        tweets = tweepy.Cursor(api.user_timeline).items()
        if tweets != None:
            print("You are about to delete all of Komi's tweets. Are you sure you want to continue? (Y/N)")
            delete = input("> ")
            if delete.lower() == 'y' or delete.upper() == 'Y':
                for tweet in tweets:
                        api.destroy_status(tweet.id)
                        print("Deleted: " , tweet.id, '\n')
                print("Successfully nuked Komi's timeline." + '\n' + "========")
        else: 
            print("Empty timeline, skipping nuke process" + '\n' + "========")