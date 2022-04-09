from asyncore import poll
from bot_functions.get_quote import quote_on_enable
<<<<<<< HEAD
from bot_functions.get_gif import get_gif

# while True:
#     quote_on_enable()
get_gif()
=======
from bot_functions.reply_mention import komi_reply

while True:
<<<<<<< HEAD
    quote_on_enable()
    komi_reply()
=======
    poll_on_enable()
>>>>>>> d7e50cc3a7125137d331f033514c2dc54d51a712
>>>>>>> a4c91506fbfea0737d3d5d0234afb54c4ba8ede2
