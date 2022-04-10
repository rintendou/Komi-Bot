from bot_functions.get_quote import quote_on_enable
from bot_functions.reply import reply_on_enable
from bot_functions.retweet import retweet_on_enable

while True:
    quote_on_enable()
    reply_on_enable()
    retweet_on_enable()
    