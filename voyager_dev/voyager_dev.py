#!/usr/bin/env python3
# Used to run the agent from the command line
import argparse
import os

# Memory
from langchain.memory import ConversationBufferMemory
from langchain.memory.chat_message_histories import RedisChatMessageHistory

# Models
from langchain.chat_models import ChatOpenAI
from langchain.llms import OpenAI

# Agents and Tools
from langchain.agents import load_tools, initialize_agent, AgentType, Tool
from langchain.agents.agent_toolkits import FileManagementToolkit

# Create and read in the file directory_structure
from create_directory_diagram import create_tree_diagram
create_tree_diagram()
with open("directory_structure", "r") as f:
    directory_structure = f.read()

message_history = RedisChatMessageHistory(url='redis://localhost:6379/0', ttl=600, session_id='my-session')
memory = ConversationBufferMemory(memory_key="chat_history", chat_memory=message_history)

llm = ChatOpenAI(temperature=0.0, model_name="gpt-4")
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

Directory structure:
{directory_structure}

"""

agent_chain = initialize_agent(
    tools,
    llm,
    agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    memory=memory,
    agent_kwargs = {
        "prefix": prefix,
        "suffix": suffix,
        "input_variables": ["input", "agent_scratchpad", "chat_history", "directory_structure"],
    }
)
# agent_chain = AgentExecutor.from_agent_and_tools(agent=agent, tools=tools, verbose=True, memory=memory)
# Create a parser
parser = argparse.ArgumentParser(description='Process a prompt.')
# Add a positional argument for the prompt with a default value of None
parser.add_argument('prompt', type=str, nargs='?', default=None, help='The prompt for the agent')
# Parse the arguments
args = parser.parse_args()



# Create a parser
parser = argparse.ArgumentParser(description='Process a prompt.')
# Add a positional argument for the prompt with a default value of None
parser.add_argument('prompt', type=str, nargs='?', default=None, help='The prompt for the agent')
# Parse the arguments
args = parser.parse_args()

# If a prompt is not provided, ask for human input.
def main():
    if not args.prompt:
        args.prompt = input("Please provide a prompt: ")
    agent_chain.run(prefix + args.prompt + terminal_bugfix)

if __name__ == "__main__":
    main()
