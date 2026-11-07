from prompts import WEDDING_PLANNER_AGENT_PROMPT, USER_PROMPT_MAIN_AGENT
from langchain.agents import create_agent
from models import openai_model
from agents import task_delegator_subagent1, task_delegator_subagent2
from langchain.messages import HumanMessage
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

# asking the user for their requirements for their wedding
logging.info("Gathering requirements from the user...")
user_requirements = input("Please enter your requirements and preferences for your wedding so that we can plan accordingly\n")

# patching the user requirements and preferences in the wedding planner agent prompt
UPDATED_WEDDING_PLANNER_AGENT_PROMPT = WEDDING_PLANNER_AGENT_PROMPT.format(user_requirements = user_requirements)

# creating main agent
logging.info("Initializing the main wedding planner agent...")
main_agent = create_agent(
    model = openai_model,
    tools = [task_delegator_subagent1, task_delegator_subagent2],
    name= "MainWeddingPlannerAgent",
    system_prompt=UPDATED_WEDDING_PLANNER_AGENT_PROMPT
)

# invoking the main agent
logging.info("Invoking the main wedding planner agent...")
response = main_agent.invoke({
    "messages":[
        HumanMessage(content=USER_PROMPT_MAIN_AGENT)
    ]
})

print(f"Wedding Planner Agent's response: {response["messages"][-1].content}")