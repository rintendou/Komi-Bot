import credentials.setup
api = credentials.setup.setup()
def nuke():
    #Grabbing ID of user
    userID = int(api.verify_credentials().id_str)

    #Emulation of do-while loop
    #Executes until timeline length is 0
    while True:
        #Grabs timeline of bot
        tweets = api.user_timeline(screen_name = userID, count = 200, include_rts = False, tweet_mode = 'extended')
        #Loops through each tweet ID and destroys it
        for info in tweets:
            api.destroy_status(info.id)
        #Emulation of do-while loop
        if tweets.len() != 0:
            break