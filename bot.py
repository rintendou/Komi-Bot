from bot_functions.Moderation import Moderation
from bot_functions.Mention import Mention
from bot_functions.Tweet import Tweet

# Initializing all classes.
mod = Moderation()
mention = Mention()
tweet = Tweet()

# Nuke on run.
mod.nuke()

while True:
    