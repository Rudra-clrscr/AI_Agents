# main.py
import os
import sys
from dotenv import load_dotenv
from crewai import Crew, Process
from agents import researcher, planner, architect
from tasks import define_tasks

# Load environment variables
load_dotenv()

def run_agca_crew(destination=None, duration=None, budget=None, preferences=None):
    """Main function to set up and run the Autonomous Global Concierge Agent."""

    # --- 1. User Input ---
    print(" Starting Autonomous Global Concierge Agent (AGCA)")
    if destination is None:
        destination = input("Where do you want to travel? (e.g., 'Kyoto, Japan'): ")
    if duration is None:
        duration = input("How many days will your trip be? (e.g., '7 days'): ")
    if budget is None:
        budget = input("What is your maximum total budget? (e.g., '$4,000 USD'): ")
    if preferences is None:
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
    if not os.getenv("GROQ_API_KEY"):
        print("ERROR: GROQ_API_KEY not found in .env file.")
    elif not os.getenv("SERPER_API_KEY"):
        print("ERROR: SERPER_API_KEY not found in .env file.")
    else:
        # Parse command-line arguments
        if len(sys.argv) == 5:
            destination = sys.argv[1]
            duration = sys.argv[2]
            budget = sys.argv[3]
            preferences = sys.argv[4]
            run_agca_crew(destination, duration, budget, preferences)
        else:
            run_agca_crew()