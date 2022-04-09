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

def quote_on_enable(): # Purpose to run code infinitely.
    while True:
        try:
            quote = get_quote() # Uses helper function above.
            tweet = "．．．" + "\n\n" + "Komi-Translation: " + "\n" + quote
            print('\n Tweeting: ' + '\n' + tweet)
            api.update_status(tweet) # Actually tweeting
            print("Next quote in 10 seconds.")
            time.sleep(10) # Halts the loop for 'x' amount of time
        except Exception as error:
            print(error)
            break
