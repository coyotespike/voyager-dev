#!/usr/bin/env python3

diagram_prompt = """
Create a Python script in the current directory that will create a simple tree diagram of all files in the current directory (except for .git, dist, build, node_modules, any .egg-info directory, and any __pycache__ directory).

This python script should be named create_directory_diagram.py and should save the diagram into a file named directory_structure, if that file doesn't exist.

Use the following example as a rough guide for the output this script should produce:

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
