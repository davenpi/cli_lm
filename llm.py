#!/usr/bin/env python3
"""
Send a user prompt and display the model response.
"""
from openai import OpenAI
from helpers import API_KEY, META_PROMPT, create_parser, get_user_prompt


def main():
    # Parse arguments
    parser = create_parser()
    args = parser.parse_args()

    # Get the prompt
    prompt = get_user_prompt(args)

    # Initialize the client
    client = OpenAI(api_key=API_KEY)

    # Send to the model
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        store=True,
        messages=[
            {"role": "system", "content": META_PROMPT},
            {"role": "user", "content": prompt},
        ],
    )

    # Display the response
    print("-----------\n")
    print(completion.choices[0].message.content)
    print("\n-----------")


if __name__ == "__main__":
    main()
