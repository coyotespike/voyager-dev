## ✨ Coding Assistant ✨


This project aims to develop a usable coding agent, which will work iteratively in collaboration with a developer.

### Future Goals

Inspired by Jim Fan et al's work on Voyager, this agent will create tools as needed, by writing TypeScript files. The project also aims to adopt a Reflexion approach.

Your agent will therefore adapt to your work habits, building tools and course-correcting experience based on your history with this agent.

# Usage

To install this repository as a global Python CLI tool, run `pip install -e .`

You should also put your OpenAI and Google Search API keys in your .bashrc or .zshrc file, like this:

```
export OPENAI_API_KEY=yourkeyhere
export GOOGLE_API_KEY=yourkeyhere
export GOOGLE_CSE_ID=yourkeyhere
```

After that you can simply type `voyager_dev` anywhere on the command line.

# Development Roadmap

- Fix the terminal tool bug
- Agent does not always get input
- Get agent to ask for task. Maybe use prefix
- Add persistent chat history per directory.
- Only send up to maximum tokens. Use embeddings (or split with most recent)
- Add logging capabilities so we can see running terminal commands in a separate terminal with tail -f /path/to/logfile
-- Also useful for sub-agents
- Install as command-line tool

- eventually, [Voyager](https://github.com/MineDojo/Voyager/tree/main/voyager) approach, build up skills list
- Add a separate memory store for [Reflexion](https://github.com/noahshinn024/reflexion)
- Maybe switch to Chroma for embeddings
- Maybe use qlora to implement Toolformer. Can reflexion/Voyager provide training data?
