# tools.py
import os
from crewai_tools import SerperDevTool
from dotenv import load_dotenv

load_dotenv() # Ensure the .env file is loaded here if not done in agents.py

# Initialize the tool
# This variable name MUST match what you import (search_tool)
search_tool = SerperDevTool()