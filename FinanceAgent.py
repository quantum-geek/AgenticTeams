from phi.agent import Agent
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