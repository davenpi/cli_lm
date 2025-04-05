#!/usr/bin/env python
"""
Send a user prompt and display the model response.
"""
from openai import OpenAI
from clm.helpers import API_KEY, META_PROMPT, create_parser, get_prompt

# Initialize the client
client = OpenAI(api_key=API_KEY)

history = [{"role": "developer", "content": META_PROMPT}]


def main():
    # Parse arguments
    parser = create_parser()
    args = parser.parse_args()

    while True:
        try:
            # Get the prompt and update history
            prompt = get_prompt(args)
            history.append({"role": "user", "content": prompt})
            # Send to the model
            completion = client.chat.completions.create(
                model="gpt-4o-mini",
                store=True,
                messages=history,
            )
            # Update history with model response
            history.append(completion.choices[0].message)

            # Display the response
            print("-----------\n")
            print(completion.choices[0].message.content)
            print("\n-----------")

        except KeyboardInterrupt:
            print("\nUntil next time!\n")
            return


if __name__ == "__main__":
    main()
