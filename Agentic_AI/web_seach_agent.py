from langchain_community.document_loaders import WebBaseLoader
from langchain_core.tools import tool
from typing import Annotated
from dotenv import load_dotenv
import os
from groq import Groq

# Load environment variables from .env file
load_dotenv()
@tool
def web_search_agent(url : Annotated[str,"it is a valid url for a web page"]):
    '''
    scrping the web page and geting the data from the web page

    Parameters:
    url (str): it is a valid url for a web page

    Returns:
    str: The summarized information for the given url.
    '''
    loader = WebBaseLoader(url)
    text = loader.load()
    data = " ".join(text[0].page_content.split())
    prompt = '''
           <Role> you are a assitant tasked with summarization of the given context the summary should be of 100 - 400 words length.the summary should contain the important information. the grammer is not the important part.</Role>
           <Context>{context}</Context>
            '''
    updated_prompt = prompt.format(context=data)
    groq_api = os.getenv('GROQ_api_key')

    client = Groq(
        api_key=groq_api
    )
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": updated_prompt,
            }
        ],
        model="llama-3.3-70b-versatile",
    )

    print(chat_completion.choices[0].message.content)
    return chat_completion.choices[0].message.content