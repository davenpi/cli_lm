# Idea

Switch context less by using a really cheap model at the command line.
1 million input/output tokens on gpt-4o-mini is 0.15¢/0.60¢!

## Requirements

- assumes `openai` is installed.

## Ongoing Improvements

- [ ] can't arrow backward on input! Fix.
- [x] add multi turn chat capability.
- [ ] system prompting for really concise, helpful answers
- [ ] Make multi line input possible! Trying to copy/paste code I realized multi line
    inputs will send one request per line without interruption. 
- [ ] make set up easier
- [ ] add token/cost accounting
- [ ] make it faster (import can be slow)
- [ ] add color