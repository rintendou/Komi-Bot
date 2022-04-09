# Created by Danny Chen. 
import requests
import json

def get_quote():
    parameters = {
        'method' : 'getQuote',
        'lang' : 'en',
        'format' : 'json'
    }

    response = requests.get('http://api.forismatic.com/api/1.0/', parameters) # API which supplies quotes. Using parameters above to filter specific settings.
    text = json.loads(response.text) # Converting into JSON object
    return text["quoteText"], text['quoteAuthor']

