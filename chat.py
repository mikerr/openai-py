# Ask openai free form questions (like chatGPT)

import openai

model_engine = "text-davinci-003"

openai.api_key = "openai-key-here"

def GPT(query):
    response = openai.Completion.create(
        model = model_engine,
        prompt = query,
        max_tokens = 1024,
        temperature = 0.5
        )
    return str.strip(response['choices'][0]['text']), response['usage']['total_tokens']

while True:
    question = input("What is your question ?> ")
    (result, usage) = GPT(question)
    print (result)
    # print ("used %s tokens" % usage)
