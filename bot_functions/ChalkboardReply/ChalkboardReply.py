import credentials.setup
from PIL import Image, ImageFont, ImageDraw

api = credentials.setup.setup

def autoFormat(input):
    output = ""
    while len(input) != 0:
        tempOutput = ""
        while(len(tempOutput) < 18 and len(input) != 0):
            if(" " in input):
                tempOutput += input[0:input.index(' ')+1]
                input = input[input.index(' ')+1:len(input)]
            else:
                tempOutput += input
                input = ""
        output += tempOutput + "\n"
    return output

text = autoFormat("If you see this, something went wrong...")

#The following code has been yoinked from Mention.py ty ;)
def mention():
    bot_id = int(api.verify_credentials().id_str)
    mention_id = 1

    words = ["komireply"]
    message = "@{}"

    while True:
        mentions = api.mentions_timeline(since_id=mention_id) # Finding mention tweets
        for mention in mentions:
            print("Mention tweet found")
            print(f"{mention.author.screen_name} - {mention.text}")
            mention_id = mention.id
            # Checking if the mention tweet is not a reply, we are not the author, and
            # that the mention tweet contains one of the words in our 'words' list
            # so that we can determine if the tweet might be a question.
            if mention.in_reply_to_status_id is None and mention.author.id != bot_id:
                if True in [word in mention.text.lower() for word in words]:
                    try:
                        print("Attempting to reply...")
                        text = autoFormat(mention.text)
                        editableImage.text((629,75),text,(255,255,255),font)
                        image.save("bot_functions\ChalkboardReply\output.jpg")
                        api.update_status_with_media(status = message.format(mention.author.screen_name), file = "bot_functions\ChalkboardReply\output.jpg", in_reply_to_status_id = mention.id_str, auto_populate_reply_metadata = True)
                        print("Successfully replied")
                    except Exception as exc:
                        print(exc)
                        break

image = Image.open("bot_functions\ChalkboardReply\ChalkboardImage.jpg")
font = ImageFont.truetype('bot_functions\ChalkboardReply\Eraser.ttf',40)

editableImage = ImageDraw.Draw(image)
mention()