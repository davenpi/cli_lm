# Idea

Switch context less by using a really cheap model at my command line.

## How to make it work?

- add llm.py to PATH (I added it to ~/.local/bin)
- add OpenAI api_key to environment var (I put it in "~/.clilm/.env")
- run in terminal `$ llm.py` (include the `.py` part for now)

## Requirements

- assumes `openai` and `python-dotenv` are installed globally.

## Improvements

- [ ] can't arrow backward on input! Fix.
- [x] add multi turn chat capability.
- [x] system prompt for really tight answers that don't use a bunch of tokens.
- [ ] Make multi line input possible! Trying to copy/paste code I realized multi line
    inputs will send one request per line without interruption. 
- [ ] make set up easier
- [ ] add token/cost accounting
- [ ] make it faster (import can be slow)
- [ ] add color