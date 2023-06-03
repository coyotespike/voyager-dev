#!/usr/bin/env python3
import argparse

from langchain.prompts import MessagesPlaceholder
from langchain.memory import ConversationBufferMemory

from langchain.chat_models import ChatOpenAI
from langchain.llms import OpenAI
from langchain.agents import load_tools, initialize_agent, AgentType, Tool

from langchain.agents.agent_toolkits import FileManagementToolkit


chat_history = MessagesPlaceholder(variable_name="chat_history")
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

llm = ChatOpenAI(temperature=0.0)
math_llm = OpenAI(temperature=0.0)
tools = load_tools(
    ["human", "llm-math", "terminal", "python_repl", "google-search"],
    llm=math_llm,
)

file_toolkit = FileManagementToolkit().get_tools()


tools = tools + file_toolkit

terminal_bugfix = 'The input for the terminal tool is either a string or "action_input": {"commands": []} with commands inside the array. Check with me before you run any terminal commands.'

prefix = """
Here are some general instructions for every task:

You should never just ask questions. Instead you should use the tool provided to get human input.

If you attempt the same action several times with the same failed result, you should ask for help using the human tool, or use another tool to solve the problem.

Also remember to check your work, and to check the environment you are working in.

You should only modify files or directories in the current directory. Check what directory you are currently in. You should not modify files or directories in other directories.

If asked to update a file, make sure you have the correct file, then carefully consider the entirety of the file, and any related files, before making changes.

You may use the human input tool to get confirmation.
"""

agent_chain = initialize_agent(
    tools,
    llm,
    agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    prefix=prefix,
    suffix=terminal_bugfix,
    memory=memory,
    agent_kwargs = {
        "memory_prompts": [chat_history],
        "input_variables": ["input", "agent_scratchpad", "chat_history"]
    }
)
# Create a parser
parser = argparse.ArgumentParser(description='Process a prompt.')
# Add a positional argument for the prompt with a default value of None
parser.add_argument('prompt', type=str, nargs='?', default=None, help='The prompt for the agent')
# Parse the arguments
args = parser.parse_args()

# If a prompt is not provided, ask for human input.
if not args.prompt:
    args.prompt = input("Please provide a prompt: ")

agent_chain.run(prefix + args.prompt + terminal_bugfix)
