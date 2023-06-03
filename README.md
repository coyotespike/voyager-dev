## ✨ Coding Assistant ✨


This project aims to develop a usable coding agent, which will work iteratively in collaboration with a developer.

At the current time, BabyAgi/AutoGPT approaches are too unstable to be of very much assistance. However, there is every reason to develop an agent that learns from its environment, from its mistakes, and from your chat history, and develops tools as needed.

# Usage

You can install this from PyPi with `pip install voyager_dev`.

Alternatively, you can clone this repository. Then to install this repository as a global Python CLI tool, run `pip install -e .`

Either way, you should also put your OpenAI and Google Search API keys in your .bashrc or .zshrc file, like this:

```
export OPENAI_API_KEY=yourkeyhere
export GOOGLE_API_KEY=yourkeyhere
export GOOGLE_CSE_ID=yourkeyhere
```

You can get the latter two by creating the GOOGLE_API_KEY in the [Google Cloud credential console](https://console.cloud.google.com/apis/credentials) and a GOOGLE_CSE_ID using the [Programmable Search Engine](https://programmablesearchengine.google.com/controlpanel/create). Examine the output carefully the first time you run it, Google may return a detailed error telling you how to fix it.

After that, you can simply type `voyager_dev` anywhere on the command line.

# Contributions and Issues

PRs are very welcome! See the development roadmap below for ideas. You can open an issue here, but be sure to include helpful environmental information. I am unlikely to be of assistance for Windows issues, beyond advising you to move to OSX/*nix.

# Development Roadmap

- [x] Fix the terminal tool bug
- [x] Get agent to ask for task. Maybe use prefix
- [x] Install as command-line tool
- [x] Install to PyPi (using the agent itself!)
- [ ] On initialization, ask which files to embed
- [ ] Add project structure and current location to every request
- Agent does not always get input
- Add persistent chat history per directory.
- Only send up to maximum tokens. Use embeddings (or split with most recent). It crashes if terminal output is too long.
- Add logging capabilities so we can see running terminal commands in a separate terminal with tail -f /path/to/logfile
-- Also useful for sub-agents
- Allow it to interrupt execution for subprocesses that ask for user input it does not have.
- [Voyager](https://github.com/MineDojo/Voyager/tree/main/voyager) approach, build up skills list
- Add a separate memory store for [Reflexion](https://github.com/noahshinn024/reflexion)
- Maybe switch to Chroma for embeddings
- Maybe use qlora to implement Toolformer. Can reflexion/Voyager provide training data?
- Enable local LLM, a la GPT4All

# Safety

Currently the shell/terminal command is the most unsafe tool given to this agent. While the prompt includes instructions to limit the damage, this is not an adequate substitute for actual safeguards.

Enhance with:
- Local LLM
- Programmatic (not LLM) confirmation, or sandboxed LLM confirmation
- Crypto signing tool for certain tasks
