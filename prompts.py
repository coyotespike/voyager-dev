#!/usr/bin/env python3

diagram_prompt = """
Produce a diagram of the current directory structure and save it to a file.

Exclude node_modules, .git, and __pycache__ directories. Use the following example as a rough guide:

your-package-name/
├── your_package_name
│   ├── __init__.py
│   └── your_script.py
├── setup.py
└── README.md
"""
prompt = """
Look at the current directory. I want to make agent.py globally accessible as a command-line interface (CLI) tool.

Restructure the directory as necessary. Then install the new package in editable mode.
"""
prompt1 = """
Look at the current directory. There is a Python CLI tool called agent, inside the agent directory.

Currently this tool does not accept a prompt. I want it to accept a command line argument for the prompt. Can you update the tool to accept a prompt?

Install it in editable mode and check that it works.
"""
