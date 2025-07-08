from crewai import Crew, Process
from agents import blog_research_agent, blog_writer_agent
from tools import yt_tool
from task import research_task, writing_task

crew = Crew(
    agents=[blog_research_agent, blog_writer_agent],
    tasks=[research_task, writing_task],
    process=Process.sequential,
    memory=True,
    cache=True,
    max_rpm=100,
    share_crew=True
)

if __name__ == "__main__":
    print("🚀 Starting CrewAI blog creation...")
    result = crew.kickoff(inputs={"topic": "Linear Regression"})
    print("\n✅ Final Output:\n")
    print(result)
