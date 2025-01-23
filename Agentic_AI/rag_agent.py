import os
from groq import Groq
from langchain_community.vectorstores import FAISS 
from embedding_model import sentence_transformer_embeding_model
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()
def format_text(docs : list):
    text = ""
    for d in docs:
        text += d.page_content+'\n'
    return text
# format_text([(page_content:'test'),{'page_content':'new test'}])


def similarity_search(query):
    my_embed_model = sentence_transformer_embeding_model()
    embed_file = FAISS.load_local('faiss_embed_data_wiki',embeddings=my_embed_model,allow_dangerous_deserialization=True)
    res = embed_file.similarity_search(query,k = 5)
    text = format_text(res)
    return text


def LLM_with_RAG(query):
    prompt = '''
            <role> you are a assistant with capabilities of question answers on topic realted to football and baseball</role>
            <Task> you will be given a question and context you should try to answer the given question using the context only
            if the context doesn't contain any of the relative information on the question you will say i don't know.
            NOTE: you should not give answers that are beyond the content from the provided context.
            <context> {context}</context>
            <question> {question}</question>
            '''
    context = similarity_search(query)
    new_prompt = prompt.format(context=context,question=query)
    groq_api = os.getenv('GROQ_api_key')
    client = Groq(
        api_key=groq_api
    )
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": new_prompt,
            }
        ],
        model="llama-3.3-70b-versatile",
    )

    print(chat_completion.choices[0].message.content)
    return chat_completion.choices[0].message.content