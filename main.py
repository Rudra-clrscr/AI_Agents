# main.py
import os
from dotenv import load_dotenv
from crewai import Crew, Process
from agents import researcher, planner, architect
from tasks import define_tasks

# Load environment variables
load_dotenv()

def run_agca_crew():
    """Main function to set up and run the Autonomous Global Concierge Agent."""
    
    # --- 1. User Input ---
    print(" Starting Autonomous Global Concierge Agent (AGCA)")
    destination = input("Where do you want to travel? (e.g., 'Kyoto, Japan'): ")
    duration = input("How many days will your trip be? (e.g., '7 days'): ")
    budget = input("What is your maximum total budget? (e.g., '$4,000 USD'): ")
    preferences = input("What are your main interests? (e.g., 'Historical sites and high-end dining'): ")

    # --- 2. Define Tasks ---
    tasks = define_tasks(destination, duration, budget, preferences)

    # --- 3. Instantiate the Crew ---
    agca_crew = Crew(
        agents=[researcher, planner, architect],
        tasks=tasks,
        process=Process.sequential, # Tasks execute one after the other
        verbose=True # Verbose logging for detailed execution steps
    )

    # --- 4. Kickoff the Workflow ---
    print("\n\n--- Starting AGCA Workflow Execution ---")
    result = agca_crew.kickoff()

    # --- 5. Display Final Result ---
    print("\n\n==================================================")
    print("✅ Final AGCA Trip Itinerary:")
    print("==================================================")
    print(result)

if __name__ == "__main__":
    if not os.getenv("GEMINI_API_KEY"):
        print("ERROR: GEMINI_API_KEY not found in .env file.")
    elif not os.getenv("SERPER_API_KEY"):
        print("ERROR: SERPER_API_KEY not found in .env file.")
    else:
        run_agca_crew()