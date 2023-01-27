# generate a variation of an existing image

import webbrowser 
import openai

openai.api_key = "openai-key-here"

def getVariant (image_data):
    response = openai.Image.create_variation(
    image=image_data,
    n=1,
    size="256x256"
    )
    return response['data'][0]['url']

# image must be square
image_data = open("image.png", mode="rb")
image_url = getVariant(image_data)
webbrowser.open(image_url)
