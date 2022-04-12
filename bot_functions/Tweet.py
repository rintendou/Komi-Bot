import requests
import json
import credentials.setup
import time

api = credentials.setup.setup()

class Tweet:
    def get_quote(self): 
        parameters = { 
            'method' : 'getQuote',
            'lang' : 'en',
            'format' : 'json'
        }

        response = requests.get('http://api.forismatic.com/api/1.0/', parameters) # API which supplies quotes. Using parameters above to filter specific settings.
        text = json.loads(response.text) # Converting into JSON object
        return text["quoteText"] #, text['quoteAuthor']

    def daily_quote(self):
        while True:
            try:
                quote = self.get_quote() # Uses helper function above.
                tweet = "．．．" + "\n\n" + "Komi-Translation: " + "\n" + quote
                print('\n Tweeting: ' + '\n' + tweet)
                api.update_status(tweet) # Actually tweeting
                print("Next quote in 10 seconds.")
                time.sleep(86400) # Halts the loop for 'x' amount of time
                break
            except Exception as error:
                print(error)
                break
