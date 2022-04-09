from bot_functions.get_quote import quote_on_enable
from bot_functions.reply_mention import komi_reply
from bot_functions.retweet import retweet_on_enable

while True:
    quote_on_enable()
    komi_reply()
    retweet_on_enable()
    