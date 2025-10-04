from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate

llm = ChatOpenAI(model="gpt-4-turbo")

template = """
You are a project planning expert. Given the high-level goal below,
break it down into detailed tasks with priority, dependencies, and estimated timelines.

Goal: {goal}

Return output as JSON with fields:
[{{"task": "string", "priority": "High/Medium/Low", "duration_days": int, "depends_on": []}}]
"""

planner_prompt = PromptTemplate(template=template, input_variables=["goal"])

def plan_tasks(goal):
    return llm.predict(planner_prompt.format(goal=goal))
