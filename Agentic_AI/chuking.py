
from langchain_text_splitters import RecursiveCharacterTextSplitter

def overlap_chuking(file_path,chunk_size = 200):

    chunk_overlap = int((chunk_size /100)*15)
    text = ""
    with open(file_path,mode='r',encoding='utf-8') as file:
        text = file.read()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = chunk_size,
        chunk_overlap = chunk_overlap
    )
    text_chunks = text_splitter.create_documents([text])
    print(len(text_chunks))
    return text_chunks