#!/usr/bin/env python3
"""
Get a user prompt and process it.
"""
import os

from dotenv import dotenv_values
from openai import OpenAI

config = dotenv_values(os.path.expanduser("~/.clilm/.env"))

api_key = config["OPENAI_API_KEY"]

client = OpenAI(api_key=api_key)

prompt = input("Ask away:\n")

completion = client.chat.completions.create(
    model="gpt-3.5-turbo", store=True, messages=[{"role": "user", "content": prompt}]
)

# Print the content
print("-----------\n")
print(completion.choices[0].message.content)
print("-----------")
