## ✨ Coding Assistant ✨


This project aims to develop a usable coding agent, which will work iteratively in collaboration with a developer.

At the current time, BabyAgi/AutoGPT approaches are too unstable to be of very much assistance. However, there is every reason to develop an agent that learns from its environment, from its mistakes, and from your chat history. In the future we hope to allow it to develop LangChain tools as needed (Voyager).

## Usage

After installation, you can run `voyager_dev` from anywhere on the command line. You may optionally provide a prompt, `voyager_dev what is the weather today?`, or you can just hit enter and it will ask you for a prompt.

For more complex prompts, place them in a file and provide the filename as the prompt. For example, `voyager_dev myprompt.txt`. This enables multiline prompts more easily.

## Installation

You can install this from [PyPi](https://pypi.org/project/voyager-dev/) with `pip install voyager_dev`.

Alternatively, you can clone this repository. Then to install this repository as a global Python CLI tool, run `pip install -e .`

Either way, you should also put your OpenAI and Google Search API keys in your .bashrc or .zshrc file, like this:

```
export OPENAI_API_KEY=yourkeyhere
export GOOGLE_API_KEY=yourkeyhere
export GOOGLE_CSE_ID=yourkeyhere
```

You can get the latter two by creating the GOOGLE_API_KEY in the [Google Cloud credential console](https://console.cloud.google.com/apis/credentials) and a GOOGLE_CSE_ID using the [Programmable Search Engine](https://programmablesearchengine.google.com/controlpanel/create). Examine the output carefully the first time you run it, Google may return a detailed error telling you how to fix it.

Finally, install and run redis (for the memory store) with `brew install redis` and `brew services start redis`. (You can also use `redis-server` if you don't want it to run in the background.)

After that, you can simply type `voyager_dev` anywhere on the command line.

## Contributions and Issues

PRs are very welcome! See the development roadmap below for ideas. You can open an issue here, but be sure to include helpful environmental information. I am unlikely to be of assistance for Windows issues, beyond advising you to move to OSX/*nix.

## Development Roadmap

- [x] Fix the terminal tool bug
- [x] Get agent to ask for task. Maybe use prefix
- [x] Install as command-line tool
- [x] Install to PyPi (using the agent itself!)
- [x] Add CI/CD to publish to PyPi automatically when setup.py is changed
- [x] Add persistent chat history
- [x] Add project structure to every request
- [ ] On initialization, ask which files to embed
- [ ] Add a separate memory store for [Reflexion](https://github.com/noahshinn024/reflexion)
- [ ] Only send up to maximum tokens. Use embeddings (or split with most recent). It crashes if terminal output is too long. [See callback](https://python.langchain.com/en/latest/modules/callbacks/getting_started.html)
- [ ] Add logging capabilities so we can see running terminal commands in a separate terminal with tail -f /path/to/logfile
-- Also useful for sub-agents
- [ ] Allow it to interrupt execution for subprocesses that ask for user input it does not have.
- [ ] Maybe use qlora to implement Toolformer. Can reflexion/Voyager provide training data?
- [ ] Enable local LLM, a la GPT4All
- Agent does not always get input?
- [ ] [Voyager](https://github.com/MineDojo/Voyager/tree/main/voyager) approach, build up skills list
-- Actually that will need to be a separate project

## Safety

Currently the shell/terminal command is the most unsafe tool given to this agent. While the prompt includes instructions to limit the damage, this is not an adequate substitute for actual safeguards.

Enhance with:
- Local LLM
- Programmatic (not LLM) confirmation, or sandboxed LLM confirmation
- Provide subset of terminal tools to limit LLM capabilities to actions you are comfortable with
- Crypto signing tool for certain tasks
