from langchain.agents import create_agent
from langchain.tools import tool
from langchain.messages import HumanMessage
from tools import search_web
from models import openai_model
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

# creating the sub-agents
logging.info("Initializing SubAgent1...")
sub_agent1 = create_agent(
    model=openai_model,
    tools=[search_web],
    name="SubAgent1"
)

logging.info("Initializing SubAgent2...")
sub_agent2 = create_agent(
    model=openai_model,
    tools=[search_web],
    name="SubAgent2"
)

@tool(parse_docstring=True)
def task_delegator_subagent1(query:str) ->str:
    """Search the web for a given topic by delegating the task to SubAgent1 to do.

    Args:
        query: The topic or question to search the web for.
    """
    logging.info(f"Delegating query to SubAgent1: {query}")
    response = sub_agent1.invoke({
        "messages":[
            HumanMessage(content=query)
        ]
    })

    return response["messages"][-1].content

@tool(parse_docstring=True)
def task_delegator_subagent2(query:str) ->str:
    """Search the web for a given topic by delegating the task to SubAgent2 to do.

    Args:
        query: The topic or question to search the web for.
    """
    logging.info(f"Delegating query to SubAgent2: {query}")
    response = sub_agent2.invoke({
        "messages":[
            HumanMessage(content=query)
        ]
    })

    return response["messages"][-1].content