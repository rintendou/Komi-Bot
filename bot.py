from bot_functions.Moderation import Moderation
<<<<<<< HEAD
from bot_functions.Mention import Mention
from bot_functions.Tweet import Tweet

# Initializing all classes.
mod = Moderation()
mention = Mention()
tweet = Tweet()

# Nuke on run.
mod.nuke()

while True:
    
=======
from bot_functions.Tweet import Tweet
from bot_functions.Reply import Reply

tweet = Tweet()
reply = Reply()
mod = Moderation()

while True:
    reply.reply_mention()
>>>>>>> main
