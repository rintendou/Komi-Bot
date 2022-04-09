from fileinput import filename
import credentials.setup
import random
import os

api = credentials.setup.setup()

def get_gif():
    gifs = []
    directory = os.path.join(os.path.dirname(__file__), '..', 'library',)

    for file in os.listdir(directory):
        gifs.append(file)
    
    for value in gifs:
        print(value)

    api.update_status_with_media(status = "",filename = os.path.join(os.path.dirname(__file__), '..', 'library',gifs[random.randint(0,len(gifs)-1)]))
    return gifs

    
