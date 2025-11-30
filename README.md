# AI_Agents
A small Python project experimenting with AI agents for task automation and orchestration.

## Features
Defines reusable agent classes and tools for different tasks.

Simple entrypoint script to run and coordinate agents.

Environment-based configuration using a .env file.

Extensible structure for adding new agents, tools, and tasks.

## Project structure
main.py – Entry script that wires up agents, tools, and tasks.

agents.py – Definitions of different agents and their behaviours.

tasks.py – Task definitions and orchestration logic.

tools.py – Utility functions or external tool integrations used by agents.

init.py – Package initialization.

## Installation
Clone the repository:

git clone https://github.com/Rudra-clrscr/AI_Agents.git

cd AI_Agents

Create and activate a virtual environment (recommended).

## Install dependencies:

pip install -r requirements.txt

Create a .env file (or update the existing one) with any API keys or configuration values required by your agents.

## Usage
Run the main script:

python main.py

Adjust agents, tasks, and tools in their respective files to customize behaviour.

Add logging or print statements in main.py and agents.py to debug flows.

## Configuration
Use the .env file for:

API keys and secrets.

Model names or endpoints.

Any runtime configuration flags for agents or tools.
