import os
# TEMP (easy): put your key here first; later move to secrets
os.environ["OPENAI_API_KEY"] = "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"

from crewai import Agent, Task, Crew

def run_analysis(data):

    agent = Agent(
        role="Dental Specialist",
        goal="Suggest treatment plan based on OPG and complaint",
        backstory="Experienced dentist"
    )

    task = Task(
        description=f"""
        Patient:
        Age: {data['age']}
        Complaint: {data['complaint']}
        OPG: {data['opg_description']}

        Give a simple treatment plan.
        """,
        agent=agent
    )

    crew = Crew(
        agents=[agent],
        tasks=[task]
    )

    result = crew.kickoff()
    return str(result)
