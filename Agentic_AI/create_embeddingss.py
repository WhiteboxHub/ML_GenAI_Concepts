from chuking import overlap_chuking
from embedding_model import sentence_transformer_embeding_model
import faiss
from langchain_community.docstore.in_memory import InMemoryDocstore
from langchain_community.vectorstores import FAISS
import os
from uuid import uuid4
def create_store_embeddings(folder_path,chunk_size):

    embedding_model = sentence_transformer_embeding_model()
    file_path = get_text_files_path(folder_path)
    index = faiss.IndexFlatL2(len(embedding_model.embed_query('hello world')))
    vector_store = FAISS(
        embedding_function = embedding_model,
        index = index,
        docstore = InMemoryDocstore(),
        index_to_docstore_id = {}
    )
    all_text = []
    for path in file_path:
        text = overlap_chuking(path,chunk_size)
        for t in text:
            all_text.append(t)
    uuids = [str(uuid4()) for _ in range(len(all_text))]
    vector_store.add_documents(documents = all_text,ids = uuids)
    vector_store.save_local('faiss_embed_data_wiki')
    return "the storing is done successfully"

def get_text_files_path(folder_path):
    text_file_paths = []
    for root,dirs,files in os.walk(folder_path):
        for file in files:
            if file.endswith('.txt'):
                file_path = os.path.join(root,file)
                text_file_paths.append(file_path.replace('\\','/'))
    return text_file_paths
