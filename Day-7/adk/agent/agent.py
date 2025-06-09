import datetime
from zoneinfo import ZoneInfo
from google.adk.agents import Agent
from agent.tools.utils.get_time import get_current_time
from agent.tools.utils.text_summarizer import summarize

model = "gemini-2.5-pro-preview-05-06"

root_agent = Agent(
    name="weather_time_agent",
    model=model,
    description=(
        "Agent to help with whatever user wants."
    ),
    instruction=(
        "You are a helpful agent who can answer user questions."
    ),
    tools=[get_current_time, summarize],
)