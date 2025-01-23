from langchain_core.tools import Tool
from rag_agents import LLM_with_RAG
from web_seach_agent import web_search_agent
from calculator import calculator
from get_current_weather import get_current_weather
from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq
from langchain.agents import create_tool_calling_agent,AgentExecutor
from langchain_core.prompts import ChatPromptTemplate
load_dotenv()
def orcestartion_agent(query : str):
        
    RAG_AGENT_TOOL = Tool(
        name = "RAG AGENT",
        func = LLM_with_RAG,
        description = "This agent will give answers regarding the football or baseball sport"
    )

    WEB_SEARCH_AGENT_TOOL = Tool(
        name = "WEB SEARCH AGENT",
        func = web_search_agent,
        description = "This agent will take a URL and give summary of the information from the given url"
    )

    CALCULATOR_AGENT_TOOL = Tool(
        name = "CALCULATOR AGENT",
        func = calculator,
        description = "This agent will do the addition task for a given 2 number."
    )

    GET_CURRENT_WEATHER_AGENT = Tool(
    name = "GET CURRENT WEATHER AGENT",
    func = get_current_weather,
    description = "This agent will give the current weather for the given city." 
    )
    tools = [RAG_AGENT_TOOL,WEB_SEARCH_AGENT_TOOL,CALCULATOR_AGENT_TOOL,GET_CURRENT_WEATHER_AGENT]

 
    prompt = '''
        You are a helpful assistant tasked with answering the question using the tools provided.
        You have access to 4 tools: RAG AGENT, WEB SEARCH AGENT, CALCULATOR AGENT, and GET CURRENT WEATHER AGENT.

        The tasks of the tools are as follows:
        - You will trigger RAG AGENT for football or baseball-related sports questions.
        - You will trigger WEB SEARCH AGENT if a URL is provided in the query.
        - You will trigger CALCULATOR AGENT if there is an addition or sum task in the query.
        - You will trigger GET CURRENT WEATHER AGENT if there is a question related to the weather or temperature in a given city.

        Respond to the user with the best answer using the appropriate tool.
    '''
    groq_api = os.getenv('GROQ_api_key')
    llm= ChatGroq(temperature=0, groq_api_key=groq_api, model_name="mixtral-8x7b-32768")
    prompt_templete = ChatPromptTemplate.from_messages([
        ("system",prompt),('human',"{input}"),('placeholder','{agent_scratchpad}')
    ])
    agent = create_tool_calling_agent(llm,tools,prompt_templete)
    my_agent = AgentExecutor(agent = agent , tools =tools )
    result = my_agent.invoke({'input':query})
    return result