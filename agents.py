from crewai import Agent
from tools import yt_tool
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
load_dotenv()

llm = ChatOpenAI(
    api_key = os.getenv("OPENAI_API_KEY"),
    model_name = "gpt-4o",
    base_url = "https://models.inference.ai.azure.com"
)

blog_research_agent = Agent(
    role = "Blog Researcher from Youtube Videos",
    goal = 'Get the relevant video content for the topic{topic} from youtube channel',
    verbose = True,
    memory = True,
    backstory = (
        "Expert in understanding videos in AI and Data Science, Machine Learning, and GEN AI and providing sugesstions"
    ),
    tools  = [yt_tool],
    llm= llm,
    allow_delegation = True,
)

blog_writer_agent =Agent(
    role = 'Blog Writer',
    goal = 'narrate compelling tech stories about the video {topic} from yoututbe channel',
    verbose = True,
    memory = True,
    backstory=(
        "With a flair in simplifying complex topics, you craft"
        "engaging narratives that captivate and educate, bringing new"
        "discoveries to light in an accessible manner."
    ),
    tools= [yt_tool],
    llm = llm,
    allow_delegation = False
)


