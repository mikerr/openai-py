# generate image from text description

import webbrowser 
import openai

openai.api_key = "openai-key-here"

def getImage (description):
    response = openai.Image.create(
          prompt = description,
          n=1,
          size="512x512"
          )
    return response['data'][0]['url']

while True:
    yourdescription = input("Describe your image ?> ")
    image_url = getImage (yourdescription)
    webbrowser.open(image_url)
