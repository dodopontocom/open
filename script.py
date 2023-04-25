#!/usr/bin/env python3

import openai
import os

openai.api_key = os.environ['CHAT_GPT']
#api_key = os.environ['CHAT_GPT']

prompt = "Hello, world!"
model = "text-davinci-002"
try:
    response = openai.Completion.create(engine=model, prompt=prompt, max_tokens=5)

    if 'choices' in response.keys() and len(response['choices']) > 0:
        first_choice = response['choices'][0]
        if 'text' in first_choice.keys():
            print(first_choice['text'])
        else:
            print("No 'text' key found in first choice")
    else:
        print("No 'choices' key found in response")
except openai.error.RateLimitError as e:
    print("Rate limit exceeded.")
