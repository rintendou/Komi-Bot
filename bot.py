from asyncore import poll
from bot_functions.get_quote import quote_on_enable
from bot_functions.reply_mention import komi_reply

while True:
    quote_on_enable()
    komi_reply()