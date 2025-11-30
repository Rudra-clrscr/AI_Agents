# agents.py
import os
from dotenv import load_dotenv
from crewai import Agent
from langchain_google_genai import ChatGoogleGenerativeAI
from tools import search_tool

load_dotenv()

# Initialize Gemini LLM
gemini_llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-pro",
    verbose=True,
    temperature=0.2,
    google_api_key=os.getenv("GEMINI_API_KEY")
)

# 1. Travel Research Analyst Agent
researcher = Agent(
    role='Travel Research Analyst',
    goal='Gather comprehensive, up-to-date data on destinations, attractions, and cultural nuances.',
    backstory=(
        "You are an expert travel researcher with an uncanny ability to find the most relevant, "
        "unique, and up-to-date information for any destination. Your reports are the foundation "
        "for the entire trip, focusing on real-time data."
    ),
    llm=gemini_llm,
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
    llm=gemini_llm,
    tools=[search_tool],  # Needs search to check price ranges
    verbose=True,
    allow_delegation=True # Can delegate research back to the researcher if a cost is too high
)

# 3. Itinerary Architect Agent
architect = Agent(
    role='Itinerary Architect',
    goal='Synthesize all research and financial data into a cohesive, chronological, day-by-day itinerary.',
    backstory=(
        "You are a master of trip design, crafting seamless, personalized itineraries that maximize experience "
        "while minimizing travel friction. Your output is the final, polished document for the user."
    ),
    llm=gemini_llm,
    verbose=True,
    allow_delegation=False
)