from asyncore import poll
from bot_functions.get_quote import quote_on_enable
from bot_functions.reply_mention import komi_reply
from bot_functions.create_poll import poll_on_enable

while True:
    poll_on_enable()