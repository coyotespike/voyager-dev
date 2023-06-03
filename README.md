## ✨ Coding Assistant ✨


This project aims to develop a usable coding agent, which will work iteratively in collaboration with a developer.

# Usage

You can install this from PyPi with `pip install voyager_dev`.

Alternatively, you can clone this repository. Then to install this repository as a global Python CLI tool, run `pip install -e .`

Either way, you should also put your OpenAI and Google Search API keys in your .bashrc or .zshrc file, like this:

```
export OPENAI_API_KEY=yourkeyhere
export GOOGLE_API_KEY=yourkeyhere
export GOOGLE_CSE_ID=yourkeyhere
```

After that, you can simply type `voyager_dev` anywhere on the command line.

# Development Roadmap

- [x] Fix the terminal tool bug
- [x] Get agent to ask for task. Maybe use prefix
- [x] Install as command-line tool
- [x] Install to PyPi (using the agent itself!)
- Agent does not always get input
- Add persistent chat history per directory.
- Only send up to maximum tokens. Use embeddings (or split with most recent)
- Add logging capabilities so we can see running terminal commands in a separate terminal with tail -f /path/to/logfile
-- Also useful for sub-agents

- [Voyager](https://github.com/MineDojo/Voyager/tree/main/voyager) approach, build up skills list
- Add a separate memory store for [Reflexion](https://github.com/noahshinn024/reflexion)
- Maybe switch to Chroma for embeddings
- Maybe use qlora to implement Toolformer. Can reflexion/Voyager provide training data?
