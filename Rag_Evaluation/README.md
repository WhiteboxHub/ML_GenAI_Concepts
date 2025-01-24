# Lucid Motors RAG QA Bot

A Question-Answering system built using LangChain and Mistral AI that answers queries about Lucid Motors using their sustainability report data.

## Overview

This project implements a Retrieval Augmented Generation (RAG) system that can answer questions about Lucid Motors by referencing their sustainability report. It uses document chunking, embeddings, and vector storage to enable efficient information retrieval and natural language responses.

## Features

- PDF document loading and processing
- Text chunking for better context management
- Vector embeddings using Hugging Face's sentence-transformers
- Local caching of embeddings for improved performance
- Vector storage using Chroma DB
- Natural language question-answering using Mistral AI

## Prerequisites

- Python 3.x
- Mistral AI API key

## Required Packages

bash
pip install langchain-mistralai

pip install langchain

pip install langchain-community

pip install sentence-transformers

pip install langchain-chroma

pip install beautifulsoup4

pip install pypdf


## Setup

1. Clone the repository
2. Install the required packages
3. Set up your Mistral AI API key
4. Place your PDF documents in the `Data` directory

## Project Structure


## Usage

1. Load and process the document:

python
loader = PyPDFLoader("path/to/your/pdf")
docs = loader.load()


2. Create text chunks:

python
text_splitter = CharacterTextSplitter(
separator="\n\n",
chunk_size=500,
chunk_overlap=150
)
chunks = text_splitter.split_documents(docs)


3. Ask questions:

python
response = rag_chain_with_source.invoke("your question here")
print(response['answer'].content)


## Example Questions

- "What type of cars do they provide?"
- "What type of company is Lucid?"
- "Tell me about Lucid's referral program?"

## Evaluation
- Retrieval Evaluation

The retrieval part of the system can be evaluated using metrics such as Precision@k, Recall@k, and Mean Reciprocal Rank (MRR)

- Response Evaluation

The generation part of the system can be evaluated using metrics such as Bleu And rouge.