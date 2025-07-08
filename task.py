from crewai import Task
from tools import yt_tool 
from agents import blog_research_agent, blog_writer_agent

research_task = Task(
    description=(
        "Search the YouTube channel for videos related to the topic: {topic}. "
        "Pick the most relevant one, fetch the transcript, and extract key points."
    ),
    expected_output="A 3-paragraph summary of the video related to {topic}.",
    tools=[yt_tool],
    agent=blog_research_agent,
)

writing_task = Task(
    description=(
        "Using the research summary from the previous task, write a blog post "
        "that narrates the main takeaways and insights from the video on {topic}."
    ),
    expected_output="A blog post that summarizes the key points from the video and adds insights.",
    tools=[yt_tool],
    agent=blog_writer_agent,
    async_execution=False,
    output_file="blog_post.md"
)
