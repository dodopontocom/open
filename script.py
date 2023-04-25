#!/usr/bin/env python3
          
import os
import json
import requests

api_key = os.environ['CHAT_GPT']
url = 'https://api.openai.com/v1/engines/davinci-codex/completions'

headers = {
  'Content-Type': 'application/json',
  'Authorization': f'Bearer {api_key}'
}

data = {
  'prompt': 'Hello, Chat GPT! Can you generate some text for me?',
  'max_tokens': 100,
  'temperature': 0.5,
  'n': 1,
  'stop': '.'
}

response = requests.post(url, headers=headers, data=json.dumps(data))
response_json = response.json()

print(response_json['choices'][0]['text'])
