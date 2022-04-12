from fileinput import filename
from gzip import GzipFile # Not used currently, could be useful
import credentials.setup
import requests
import json
import random
import time
import os

api = credentials.setup.setup()

class Tweet:
    sleepTime = 10  # amount of time the bot should sleep before tweeting again

    def get_quote(self): 
        parameters = { 
            'method' : 'getQuote',
            'lang' : 'en',
            'format' : 'json'
        }

        response = requests.get('http://api.forismatic.com/api/1.0/', parameters) # API which supplies quotes. Using parameters above to filter specific settings.
        text = json.loads(response.text) # Converting into JSON object
        return text["quoteText"] #, text['quoteAuthor']

    def tweet_quote(self):
        try:
            quote = self.get_quote() # Uses helper function above.
            tweet = "．．．" + "\n\n" + "Komi-Translation: " + "\n" + quote
            print('\n Tweeting: ' + '\n' + tweet)
            api.update_status(tweet) # Actually tweeting
            print("Next quote in " + str(self.sleepTime) + " seconds.")
            time.sleep(self.sleepTime) # Halts the loop for 'x' amount of time
        except Exception as error:
            print(error)

    def tweet_gif(self):
        gifs = [] # stored gifs
        library = os.path.join(os.path.dirname(__file__), '..', 'library',)

        for file in os.listdir(library): # appending files into gifs array
            gifs.append(file)

        gif_file = random.choice(gifs)
        try:
            tweet = "．．．"
            print('\n Tweeting: ' + '\n' + tweet)
            api.update_status_with_media(status = tweet,filename = os.path.join(library,gif_file)) # Tweeting gif
            print("Next quote in " + str(self.sleepTime) + " seconds.")
            time.sleep(self.sleepTime)
        except Exception as error:
            print(error)