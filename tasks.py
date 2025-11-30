# tasks.py
from crewai import Task
from agents import researcher, planner, architect

def define_tasks(destination, duration, budget, preferences):
    """Defines the sequential tasks for the AGCA crew."""
    
    # 1. Research Task (Researcher Agent)
    research_task = Task(
        description=f"Conduct a deep, real-time web search for {destination}. Find 5 key historical and food attractions, "
                    f"current travel advisories, typical costs (food, local transport), and best seasons to visit, "
                    f"focusing on the user's preferences: {preferences}.",
        expected_output="A detailed JSON summary of the research findings, including 5 specific, cost-relevant attraction details.",
        agent=researcher,
        async_execution=False
    )
    
    # 2. Budget Calculation Task (Planner Agent)
    budget_task = Task(
        description=f"Analyze the research data to estimate total travel costs for a {duration} trip, "
                    f"ensuring the overall budget does not exceed {budget}. Provide itemized estimates for flights, "
                    f"lodging, and daily activities/food. **Crucially, identify potential cost conflicts with the {budget} constraint.**",
        expected_output="A structured markdown report detailing cost breakdown and financial risk assessment against the budget.",
        agent=planner,
        context=[research_task], # Uses the output of the research task
        async_execution=False
    )
    
    # 3. Itinerary Creation Task (Architect Agent)
    itinerary_task = Task(
        description=f"Using the research and budget reports, craft a polished, day-by-day itinerary for a {duration} trip to {destination}. "
                    f"Ensure the plan aligns with the preferences ({preferences}) and respects the financial constraints. "
                    f"Output must be a beautifully formatted Markdown itinerary.",
        expected_output="A comprehensive, day-by-day travel itinerary in Markdown, ready for the client.",
        agent=architect,
        context=[research_task, budget_task], # Uses all previous data
        async_execution=False
    )
    
    return [research_task, budget_task, itinerary_task]