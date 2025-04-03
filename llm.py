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


META_PROMPT = """
Please try to keep your answers concise. I am asking these questions in a terminal
window on my Mac. For example, if I ask for the command to do something, just provide
the answer and don't worry about recapitulating the question. Suppose I ask 'How do I
list what is in my current working directory including hidden files?' You can just
respond with `ls -a` and a short description saying something like 'this command lists
what is in the current directory, including directory entries whose name begin with a
dot (`.`).

That said, for more complex command line tools feel free to explain what each option
does in a few sentences. Also, when your answers are getting a little long, make sure to
newline so each sentence only take up about 79 characters or so. Formatting is really
important for me.

Thank you! I appreciate your help.
"""

prompt = input("Ask away:\n")


completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    store=True,
    messages=[
        {"role": "system", "content": META_PROMPT},
        {"role": "user", "content": prompt},
    ],
)

print("-----------\n")
print(completion.choices[0].message.content)
print("\n-----------")
