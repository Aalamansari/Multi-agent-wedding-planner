from langchain.tools import tool
from tavily import TavilyClient
from dotenv import load_dotenv
import logging
from typing import Any, Dict

# configure logging mechanism
logging.basicConfig(
   level=logging.INFO,
   format="%(asctime)s | %(levelname)s | %(message)s"
)

load_dotenv()
tavily_client = TavilyClient()

@tool(parse_docstring=True)
def search_web(query: str) -> Dict[str, Any]:
    """Search the web for the given query and return the results.

    Args:
        query: The search query.
    """
    logging.info(f"Searching the web for topic: {query}")

    return tavily_client.search(query)