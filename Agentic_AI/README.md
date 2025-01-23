
# Setup Order for Agentic AI with Groq Integration

This document outlines the correct order of steps to set up and run the Agentic AI system that integrates various agents with an LLM powered by Groq.

## Step-by-Step Setup Process

Follow these steps in the exact order to ensure the successful creation and orchestration of the agents:

### 1. **Run Web Scraper File and Scrape the Data**

   - **Purpose**: The first step is to scrape data from the web. This will provide the content that will be used by other agents, especially the Web Search Agent.
   - **Action**: Run the web scraper script to collect and store data from the desired web pages.
   - **File**: `web_scraper.py` (or a similar name depending on your scraper setup).

### 2. **Create the Embedding Model File**

   - **Purpose**: This file will define the embedding model used to convert textual data into embeddings.
   - **Action**: Implement the `sentence_transformer_embeding_model` class that loads a pre-trained model and provides functions to generate document embeddings.
   - **File**: `embedding_model.py`.

### 3. **Create the Chunking File**

   - **Purpose**: The chunking process divides long texts into smaller, manageable chunks for embedding and further processing.
   - **Action**: Create the `overlap_chunking` function that handles the chunking of text data.
   - **File**: `chunking.py`.

### 4. **Create the Create Embedding File**

   - **Purpose**: This file is responsible for creating embeddings for the text data, storing them in a vector store, and saving them locally.
   - **Action**: Create the function `create_store_embeddings` that takes scraped text, generates embeddings, and stores them in a FAISS index.
   - **File**: `create_embeddings.py`.

### 5. **Create the RAG Agent**

   - **Purpose**: The RAG agent retrieves relevant information from the vector store and generates context-specific responses.
   - **Action**: Define the `LLM_with_RAG` function that integrates with the FAISS vector store and processes queries.
   - **File**: `rag_agents.py`.

### 6. **Create the Web Search Agent**

   - **Purpose**: The Web Search Agent is used to summarize information from URLs.
   - **Action**: Implement the `web_search_agent` function, which loads and processes web pages, then summarizes the content using Groq.
   - **File**: `web_search_agent.py`.

### 7. **Create the Calculator Agent**

   - **Purpose**: The Calculator Agent handles simple arithmetic tasks such as addition.
   - **Action**: Implement the `calculator` function that processes arithmetic queries.
   - **File**: `calculator.py`.

### 8. **Create the Get Weather Agent**

   - **Purpose**: The Weather Agent fetches current weather data for a specified city.
   - **Action**: Implement the `get_current_weather` function, which retrieves weather details based on the city name.
   - **File**: `get_current_weather.py`.

### 9. **Create the Orchestration Agent**

   - **Purpose**: The Orchestration Agent is responsible for integrating all the previously created agents and managing the flow of tasks.
   - **Action**: Define the `orcestartion_agent` function, which coordinates with the other agents to provide the best response based on the user's query.
   - **File**: `orcestartion_agent.py`.

### 10. **Create the Main Jupyter Notebook (`main.ipynb`)**

   - **Purpose**: This is the main entry point for interacting with the orchestration system. You will use this notebook to input queries and see how the agents work together to provide answers.
   - **Action**: Create a Jupyter Notebook that calls the `orcestartion_agent` and demonstrates how to interact with the system.
   - **File**: `main.ipynb`.

---

## Additional Information

- **Environment Variables**: Make sure to include your Groq API key in the `.env` file as shown below:

    ```plaintext
    GROQ_api_key=<your_groq_api_key>
    ```

- **Libraries to Install**: Make sure you have all the necessary dependencies installed:

    ```bash
    pip install langchain_core rag_agents web_search_agent calculator get_current_weather dotenv langchain_groq
    ```

- **Running the Project**: After following the steps above, execute the `main.ipynb` file to interact with the system. This will initiate the orchestration and allow you to test queries.

---


# Agentic AI: Integrating Multiple Agents with LLM using Groq

This repository contains the creation and orchestration of four specialized agents, each designed to handle specific tasks. These agents are bound together using a Large Language Model (LLM) integrated with Groq, allowing the AI system to intelligently choose and execute tasks based on user queries.

## Overview

The main objective of this project is to demonstrate how to use multiple agents to process different types of queries, such as:
1. Sports-related questions (RAG Agent)
2. Web search and summarization (Web Search Agent)
3. Simple arithmetic calculations (Calculator Agent)
4. Weather information retrieval (Weather Agent)

These agents are connected to an LLM powered by Groq for dynamic query execution.

## Agents Created

### 1. **RAG Agent**:
   - **Function**: Handles queries related to sports, specifically football and baseball.
   - **Description**: This agent uses Retrieval-Augmented Generation (RAG) to fetch relevant context and provide accurate answers.

### 2. **Web Search Agent**:
   - **Function**: Summarizes content from a given URL.
   - **Description**: This agent fetches the content of a web page and generates a summary of the important information.

### 3. **Calculator Agent**:
   - **Function**: Performs addition tasks for two given numbers.
   - **Description**: This agent processes basic arithmetic operations and returns the result.

### 4. **Weather Agent**:
   - **Function**: Provides current weather information for a given city.
   - **Description**: This agent returns weather information such as temperature and conditions for the requested city.

## LLM Integration with Groq

The agents are bound with a Large Language Model (LLM) powered by Groq. This integration allows the AI system to intelligently decide which agent to use based on the input query. The LLM takes the query, interprets it, and invokes the appropriate agent based on the task at hand.

### Tools Used:
- **Groq API**: Powers the LLM to handle complex tasks and integrates the agents.
- **LangChain**: Framework for building and managing the agents and prompts.
- **dotenv**: Manages environment variables securely.


# Wikipedia Scraper

`web_scraping.py` This Python script scrapes text content from a Wikipedia page and saves it to a text file.

### Description

The script uses the `requests` library to fetch the Wikipedia page and `BeautifulSoup` from the `bs4` library to parse the HTML content. It extracts all the paragraph (`<p>`) text from the page and saves it into a file named `baseball_wiki.txt`.

**Note**: You can change the URL in the code to scrape any Wikipedia page by updating the `url` variable.


# Sentence Transformer Embedding Model

`embedding_model.py` This Python class `sentence_transformer_embeding_model` is designed to integrate the **Sentence-Transformers** library for creating embeddings from text data. It inherits from the `Embeddings` class in `langchain` and provides methods to embed both documents and queries.

### Description

The class uses the pre-trained model `paraphrase-multilingual-MiniLM-L12-v2` from **Sentence-Transformers** to encode sentences into embeddings.

### Features:
- Embedding of text documents using `embed_documents()`
- Embedding of queries using `embed_query()`
- Supports multi-language embeddings


# FAISS Vector Store Creation with Overlap Chunking

`chunking.py` This Python script creates a FAISS vector store by embedding text data using a pre-trained sentence transformer model. The text data is chunked with overlap and indexed using the FAISS library for efficient similarity searches.

### Description

The script performs the following tasks:

1. Loads text files from a specified folder.
2. Splits the text into smaller overlapping chunks using **overlap chunking**.
3. Embeds the chunks using a **Sentence-Transformer** model.
4. Stores the embeddings in a **FAISS vector store** for efficient retrieval.
5. Saves the FAISS index locally.

The FAISS index is designed to be used with the **sentence-transformers** model to convert text into embeddings and search for semantically similar texts.


# FAISS Vector Store Creation

`create_embeddingss.py` This Python script creates a FAISS vector store by embedding text data using a pre-trained sentence transformer model. The text data is split into chunks and indexed using the FAISS library for efficient similarity searches.

### Description

The script performs the following tasks:

1. Loads text files from a specified folder.
2. Splits the text into smaller chunks using **overlap chunking**.
3. Embeds the chunks using a **Sentence-Transformer** model.
4. Stores the embeddings in a **FAISS vector store** for efficient retrieval.
5. Saves the FAISS index locally.

The FAISS index is designed to be used with the **sentence-transformers** model to convert text into embeddings and search for semantically similar texts.


# Create a Groq API Key

1. Visit [Groq Console - API Keys](https://console.groq.com/keys).
2. Log in to your Groq account.
3. Navigate to the **API Keys** section.
4. Click **Create API Key** and name it (e.g., "RAG Agent Project").
5. Copy the generated key and paste it into your `.env` file as follows:

   ```plaintext
   GROQ_api_key=<your_groq_api_key>```

# RAG Agent

`rag_agent.py` is a Python script designed to implement a Retrieval-Augmented Generation (RAG) system. The script enables natural language queries to be answered using context retrieved from a pre-generated FAISS vector store. It employs a large language model (LLM) for generating responses.

### Description
- **Retrieval-Augmented Generation (RAG):** Combines context retrieval and LLM for accurate answers.
- **FAISS Vector Store:** Leverages a FAISS index to perform similarity searches on the dataset.
- **Custom Prompting:** Includes a structured prompt to restrict LLM responses to the provided context.
- **Environment Configuration:** Uses environment variables to manage API keys securely.


# Web Search Agent for Summarization

`web_serach_agent.py` This Python script provides a tool that scrapes content from a specified web page, processes the text, and generates a summary using a Groq-powered large language model (LLM).

### Description

The script uses the following components:

- **Web scraping:** It uses `WebBaseLoader` from LangChain to scrape a webpage and extract the text content.
- **Summarization:** The content is summarized using a Groq-powered LLM, which provides a summary of the scraped content in 100-400 words.
- **Environment variables:** The Groq API key is stored in a `.env` file for secure access.


# Weather Tool

`get_current_weather.py`This Python tool provides a simple way to get the current weather or temperature for a given city. The tool is built using LangChain's tool functionality and returns a predefined weather description.

### Description

The tool takes a city name as input and returns the weather description for that city. In this version, it simply returns a message indicating the weather as "sunny."

# Orcestartion Agent

The `orcestartion_agent.py` is a versatile assistant that can respond to various queries using multiple tools. It handles sports-related queries, web search summaries, simple arithmetic, and current weather conditions. The agent intelligently selects the right tool for the task based on the input query.

### Description

- **RAG Agent**: Answers questions related to football and baseball sports.
- **Web Search Agent**: Summarizes information from a provided URL.
- **Calculator Agent**: Performs addition tasks for two given numbers.
- **Weather Agent**: Provides the current weather for a given city.
