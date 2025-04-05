# cli_lm

Switch context less by using a really cheap LLM at the command line.

## Installation

```bash
# Install from source
git clone https://github.com/davenpi/cli_lm.git
cd cli_lm
pip install -e .

# Install from PyPI
pip install cli-lm
```

## Quick Start
The first run will prompt for your
<a href="https://platform.openai.com/docs/overview" target="_blank">Open AI API key</a>.
Just paste the key in.
**Note** you'll have to pay Open AI to get yourself an API key and start using their
models. For now this package sets `gpt-4o-mini` as the model of choice. It costs
0.15¢/0.60¢ per 1 million input/output tokens. 1 token ~ 1 word!

```shell
# Directly ask a question
clm "How do I amend a commit in git?"

# Interactive mode (input in python interpreter)
clm
> How do I list the processes listening on a given port?
```

There is multiturn chat. Just hit `Ctrl+c` or `Ctrl+d` to exit.

## Configuration
The package looks for your Open AI API key in `~/.cli_lm/.env`.

To quickly update your API key run:
```shell
echo "OPENAI_API_KEY=your_new_key" > ~/.cli_lm/.env
```

It works on a Mac, but I haven't tried it on any other system.

## Ongoing Improvements

- [x] Multi turn chat capability.
- [ ] Can't arrow backward on input! Fix.
- [ ] Improved multiline input
- [ ] System prompting for really concise, helpful answers
- [ ] Make set up easier
- [ ] Add token/cost accounting
- [ ] Make it faster (imports can be slow)
- [ ] Add color

## License
MIT