import credentials.setup
import tweepy

api = credentials.setup.setup()

def nuke():
    print("You are about to delete all of Komi's tweets. Are you sure you want to continue? (Y/N)")
    delete = input("> ")
    if delete.lower() == 'y' or delete.upper() == 'Y':
        for tweet in tweepy.Cursor(api.user_timeline).items():
            try:
                api.destroy_status(tweet.id)
                print("Deleted: " + tweet.id)
            except Exception:
                print("Failed to delete: " + tweet.id)
        