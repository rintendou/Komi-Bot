# Created by Danny Chen. 

import requests
import json
import credentials.setup
import time

api = credentials.setup.setup()

def get_quote():
    parameters = {
        'method' : 'getQuote',
        'lang' : 'en',
        'format' : 'json'
    }

    response = requests.get('http://api.forismatic.com/api/1.0/', parameters) # API which supplies quotes. Using parameters above to filter specific settings.
    text = json.loads(response.text) # Converting into JSON object
    return text["quoteText"] #, text['quoteAuthor']

def quote_on_enable():
    while True:
        try:
            quote = get_quote()
            tweet = "．．．" + "\n\n" + "Komi-Translation: " + "\n" + quote
            print('\n Tweeting: ' + '\n' + tweet)
            api.update_status(tweet)
            print("Next quote in 10 seconds.")
            time.sleep(60)
        except Exception as error:
            print(error)
            break
