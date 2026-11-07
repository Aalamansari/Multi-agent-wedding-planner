# Multi-Agent Wedding Planner

A small LangChain project that plans a wedding using a multi-agent setup. A main planner agent takes your requirements and preferences, then delegates web research to two sub-agents that search the web with Tavily.

## How it works

```
User requirements (terminal input)
        |
        v
MainWeddingPlannerAgent
   |-- task_delegator_subagent1 --> SubAgent1 --> search_web (Tavily)
   |-- task_delegator_subagent2 --> SubAgent2 --> search_web (Tavily)
        |
        v
Wedding plan printed to the terminal
```

- **Main agent:** acts as the wedding expert. Your input is inserted into its system prompt, and it decides what to research and which sub-agent to ask.
- **Sub-agents:** two agents that each have the `search_web` tool. The main agent calls them through delegator tools that wrap each sub-agent as a tool.
- **Search:** `search_web` calls the Tavily search API and returns the raw results.

## Project structure

| File | Purpose |
|------|---------|
| `main.py` | Entry point. Collects your requirements, builds the main agent, and prints its response. |
| `agents.py` | Creates the two sub-agents and the delegator tools the main agent uses to call them. |
| `tools.py` | Defines the `search_web` tool backed by Tavily. |
| `models.py` | Configures the chat model (OpenAI, via `init_chat_model`). |
| `prompts.py` | System prompt for the main agent and the user prompt. |

## Requirements

- Python 3.13 or newer
- An OpenAI API key
- A Tavily API key
- [uv](https://docs.astral.sh/uv/) (the project includes a `uv.lock`)

## Setup

1. Install dependencies:

   ```bash
   uv sync
   ```

2. Create a `.env` file in the project root:

   ```env
   OPENAI_API_KEY=your-openai-key
   TAVILY_API_KEY=your-tavily-key
   ```

## Usage

```bash
uv run main.py
```

When prompted, describe your wedding requirements, for example:

```
I have a budget of 14000 USD and I prefer an open lawn wedding in the afternoon when there is less heat and it is a little bit cold.
```

The agent will research options with its sub-agents and print a plan.

## Notes

- The model is set in `models.py`. Function tools are not supported on Chat Completions when a default reasoning effort is applied, so the model is configured with `reasoning_effort="none"`.
- Tools that use `@tool(parse_docstring=True)` need a Google-style docstring with an `Args:` section documenting every parameter.
