from phi.agent import Agent
"""
This script defines a team of AI agents using the `phi` library to perform tasks related to web searches and financial data analysis. 
The agents are configured with specific models, tools, and instructions to handle their respective tasks.
Modules Imported:
- `phi.agent`: Provides the `Agent` class for creating AI agents.
- `phi.model.openai`: Includes the `OpenAIChat` model for natural language processing tasks.
- `phi.model.groq`: (Commented out) Includes the `Groq` model for alternative NLP tasks.
- `phi.tools.duckduckgo`: Provides the `DuckDuckGo` tool for web searches.
- `phi.tools.yfinance`: Provides the `YFinanceTools` for fetching financial data.
- `dotenv`: Used to load environment variables from a `.env` file.
Agents Defined:
1. `web_agent`: 
    - Name: "Web Agent"
    - Model: `OpenAIChat` (GPT-4o)
    - Tools: `DuckDuckGo` for web searches.
    - Instructions: Focuses on stock market-related factual information and includes sources in responses.
    - Features: Displays tool calls and formats responses in Markdown.
2. `finance_agent`: 
    - Name: "Finance Agent"
    - Role: Fetches financial data.
    - Model: `OpenAIChat` (GPT-4o)
    - Tools: `YFinanceTools` for stock prices, analyst recommendations, and company information.
    - Instructions: Uses tables for data presentation and includes sources in responses.
    - Features: Displays tool calls and formats responses in Markdown.
3. `agent_team`: 
    - A team of agents (`web_agent` and `finance_agent`).
    - Model: `OpenAIChat` (GPT-4o)
    - Instructions: Combines the capabilities of both agents, ensuring sources are included and data is presented in tables.
    - Features: Displays tool calls and formats responses in Markdown.
Functionality:
- The `agent_team` is tasked with summarizing analyst recommendations and sharing the latest news for a given stock (e.g., "CRM").
- The response is streamed and formatted for clarity.
Note:
- The `Groq` model is included in comments as an alternative but is not actively used in this script.
"""
from phi.model.openai import OpenAIChat
from phi.model.groq import Groq
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.yfinance import YFinanceTools
from dotenv import load_dotenv

load_dotenv()

web_agent = Agent(
    name="Web Agent",
    #model=Groq(id="llama-3.3-70b-versatile"),
    model=OpenAIChat(id="gpt-4o"),
    tools=[DuckDuckGo()],
    instructions=["Please always include the sources. Do NOT answer anything that is not a fact and is not related to Stock Market"],
    show_tool_calls=True,
    markdown=True
)

finance_agent = Agent(
    name="Finance Agent",
    role="Get financial data",
    #model=Groq(id="llama-3.3-70b-versatile"),
    model=OpenAIChat(id="gpt-4o"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True)],
    instructions=["Use tables to display the data.", "Please always include the sources."],
    show_tool_calls=True,
    markdown=True,
)

agent_team = Agent(
    #model=Groq(id="llama-3.3-70b-versatile"),
    model=OpenAIChat(id="gpt-4o"),
    team=[web_agent, finance_agent],
    instructions=["Please always include the sources", "Use tables to display the data"],
    show_tool_calls=True,
    markdown=True,
)

agent_team.print_response("Summarize analyst recommendations and share the latest news for CRM", stream=True)