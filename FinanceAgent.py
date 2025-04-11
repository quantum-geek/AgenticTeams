from phi.agent import Agent
"""
This script initializes a financial analysis agent using the Phi framework. The agent is configured to use the 
OpenAI GPT-4 model and YFinanceTools for stock-related data analysis. The agent is designed to summarize and 
compare analyst recommendations, stock fundamentals, and provide the latest stock prices for specified companies. 
It also includes a decision-making feature to suggest whether to buy the stocks.
Modules and Libraries:
- `phi.agent`: Provides the `Agent` class for creating AI agents.
- `phi.model.groq`: Contains the `Groq` model (commented out in this script).
- `phi.tools.yfinance`: Includes tools for fetching stock-related data such as prices, fundamentals, and analyst recommendations.
- `phi.model.openai`: Provides the `OpenAIChat` model for natural language processing.
- `dotenv`: Used to load environment variables from a `.env` file.
Key Features:
1. **Agent Configuration**:
    - Uses the `OpenAIChat` model (`gpt-4o`) for processing queries.
    - Integrates `YFinanceTools` to fetch stock prices, analyst recommendations, and fundamentals.
    - Displays tool calls and outputs in markdown format.
    - Includes specific instructions for formatting responses, such as using tables with dotted lines and including company names.
2. **Instructions for the Agent**:
    - Use tables to display data.
    - Retrieve company symbols using a function (commented out in this script) if not available.
    - Ensure company names are included in the output.
    - Use dotted lines to separate tables for better readability.
3. **Agent Query**:
    - Summarizes and compares analyst recommendations and fundamentals for TSLA, CRM, and NVDA stocks.
    - Retrieves the latest stock prices for the specified stocks.
    - Provides a "Yes" or "No" recommendation for buying each stock.
Note:
- The `get_company_symbol` function is defined but commented out. It maps company names to their symbols.
- Debug mode is available but currently disabled.
"""
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.model.openai import OpenAIChat

from dotenv import load_dotenv

load_dotenv()
'''
##Just a test tro see if the agent grabs an unknown symbol. 
def get_company_symbol(company_name: str) -> str:
    company_symbol = {
        "MSFT": "Phidata",
        "TSLA": "Tesla Inc.",
        "CRM": "Salesforce.com Inc.",
        "NVDA": "NVIDIA Corporation",
    }
    return company_symbol[company_name]
'''
agent = Agent(
    #model=Groq(id="llama-3.3-70b-versatile"),
    model=OpenAIChat(id="gpt-4o"),
    tools = [YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True)],  
    show_tool_calls=True, 
    markdown=True,
    instructions=['You must use tables to display the data.', 'If you do not have the company symbol, you can use the get_company_symbol function to get it.'
    'even if it is not a public company. Can you also make sure to include the company name in the table? I will also appreciate if you use dotted lines to separate the tables.',],

    #debug_mode=True,
)

agent.print_response("Summarize and compare analyst recommendations and fundamentals for TSLA, CRM and NVDA stocks. "
"Towards the end please get the latest stock price for all stocks."
"Also, please provide a Yes or No buy for all stocks.")