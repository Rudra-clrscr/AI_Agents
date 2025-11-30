# agents.py
import os
from dotenv import load_dotenv
from crewai import Agent # Keep only the Agent import
from langchain_groq import ChatGroq # <--- CORRECT IMPORT for Groq
from tools import search_tool

load_dotenv()

# Initialize LLM using the ChatGroq wrapper
# This client successfully bypasses the conflicting CrewAI/OpenAI checks.
groq_llm = ChatGroq(
    model="llama3-8b-8192", # Using the fast, free Groq model
    temperature=0.2,
    # ChatGroq automatically looks for GROQ_API_KEY in the environment
)

# 1. Travel Research Analyst Agent
researcher = Agent(
    role='Travel Research Analyst',
    goal='Gather comprehensive data on destinations, attractions, and cultural nuances.',
    backstory=(
        "You are an expert travel researcher with extensive knowledge of destinations worldwide. "
        "You provide detailed information on attractions, costs, and travel tips based on your expertise."
    ),
    llm=groq_llm, 
    tools=[search_tool],
    verbose=True,
    allow_delegation=False
)

# 2. Budget & Logistics Planner Agent
planner = Agent(
    role='Budget & Logistics Planner',
    goal='Calculate realistic costs for flights, hotels, and activities, ensuring all plans adhere to the user\'s budget.',
    backstory=(
        "You are a skilled financial analyst and logistical wizard. You turn raw research into a financial plan, "
        "identifying cost-saving opportunities and calculating efficient transport routes. You must ensure the final "
        "itinerary is financially feasible."
    ),
    llm=groq_llm, 
    tools=[search_tool],
    verbose=True,
    allow_delegation=True
)

# 3. Itinerary Architect Agent
architect = Agent(
    role='Itinerary Architect',
    goal='Synthesize all research and financial data into a cohesive, chronological, day-by-day itinerary.',
    backstory=(
        "You are a master of trip design, crafting seamless, personalized itineraries that maximize experience "
        "while minimizing travel friction. Your output is the final, polished document for the user."
    ),
    llm=groq_llm, 
    verbose=True,
    allow_delegation=False
)