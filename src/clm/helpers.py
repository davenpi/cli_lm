import argparse
import os
import sys


# Ensure the config directory exists
config_dir = os.path.expanduser("~/.clm")
os.makedirs(config_dir, exist_ok=True)
env_path = os.path.join(config_dir, ".env")


def read_env_file(file_path: str) -> dict:
    """
    Read vars from `file_path`

    Parameters
    ----------
    file_path : str
        Path to file.

    Returns
    -------
    dict
        Configuration variables in a dict.
    """
    if not os.path.exists(file_path):
        return {}

    config = {}
    try:
        with open(file_path, "r") as file:
            for line in file:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                key, value = line.split("=", 1)
                config[key.strip()] = value.strip().strip("\"'")
        return config
    except Exception as e:
        print(f"Error reading config file: {e}")
        return {}


def create_env_file(file_path: str) -> dict:
    """
    Create the .env file if it doesn't exist by prompting the user for their API key.

    Parameters
    ----------
    file_path : str
        Path to .env file.

    Returns
    -------
    dict
        dict with OpenAI API key.
    """
    print("No configuration file found. Let's set up your OpenAI API key.")
    api_key = input("Please enter your OpenAI API key: ").strip(" \"'")

    try:
        with open(file_path, "w") as file:
            file.write(f"OPENAI_API_KEY={api_key}\n")
        os.chmod(file_path, 0o600)  # Set permissions to user read/write only
        print(f"Configuration saved to {file_path}")
        return {"OPENAI_API_KEY": api_key}
    except Exception as e:
        print(f"Error creating configuration file: {e}")
        print(
            (
                "Do you have a configuration file `.env` in `~/.clm` with your API"
                ' key?\nTry `echo "OPENAI_API_KEY=your_api_key" > ~/.clm/.env` '
            )
        )
        sys.exit(1)


config = read_env_file(env_path)
if not config or "OPENAI_API_KEY" not in config:
    config = create_env_file(env_path)

API_KEY = config.get("OPENAI_API_KEY")

META_PROMPT = """
Please try to keep your answers concise. I am asking these questions in a terminal
window on my Mac. For example, if I ask for the command to do something, just provide
the answer and don't worry about recapitulating the question. Suppose I ask 'How do I
list what is in my current working directory including hidden files?' You can just
respond with `ls -a` and a short description saying something like 'this command lists
what is in the current directory, including directory entries whose name begin with a
dot (`.`)'.

That said, for more complex command line tools feel free to explain what each option
does in a few sentences. Also, when your answers are getting a little long, make sure to
add a newline so each sentence only takes up about 79 characters or so. Formatting is
really important for me.

Finally, please be lively but don't use too many emojis. Thank you!
"""


def create_parser():
    """Create and return the argument parser"""
    parser = argparse.ArgumentParser(
        description="CLI tool for prompting an LLM",
        formatter_class=argparse.RawTextHelpFormatter,
    )

    parser.epilog = """Example usage:
    $ clm "How do I amend a git commit?"

    $ clm
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
