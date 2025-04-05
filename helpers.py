import argparse
import os
import sys

from dotenv import dotenv_values


config = dotenv_values(os.path.expanduser("~/.clilm/.env"))
API_KEY = config["OPENAI_API_KEY"]

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
add a newline so each sentence only take up about 79 characters or so. Formatting is
really important for me. Thank you!
"""


def create_parser():
    """Create and return the argument parser"""
    parser = argparse.ArgumentParser(
        description="CLI tool for prompting an LLM",
        formatter_class=argparse.RawTextHelpFormatter,
    )

    parser.epilog = """Example usage:
    $ llm "How do I amend a git commit?"

    $ llm
    > Ask away:
    > How do I amend a git commit?
    [response will appear here]
    """

    parser.add_argument(
        "prompt",
        nargs="?",
        default=None,
        help="Prompt for the LLM. If you pass this, remember to put your prompt in"
        + ' "quotes"! ',
    )

    return parser


def get_prompt(args):
    """Get the prompt from args or request input"""
    if args.prompt:
        prompt = args.prompt
        # clear the prompt so we can continue in multiturn
        args.prompt = None
    else:
        prompt = input("Ask away:\n")
    return prompt
