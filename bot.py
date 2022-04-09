from bot_functions.get_quote import get_quote
import credentials.setup
import time

api = credentials.setup.setup()

while True:
    try:
        quote, author = get_quote()
        tweet = quote + '\n' + '\n' + ' -' +  author
        print('\n Tweeting: ' + '\n' + tweet)
        api.update_status(tweet)
        print("Next quote in 10 seconds.")
        time.sleep(10)
    except Exception as error:
        print(error)
        break
