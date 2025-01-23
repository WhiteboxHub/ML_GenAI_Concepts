from langchain.embeddings.base import Embeddings
from sentence_transformers import SentenceTransformer


class sentence_transformer_embeding_model(Embeddings):
    def __init__(self):
        self.model_name = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
        self.model = SentenceTransformer(self.model_name)
    
    def embed_documents(self,text : list):
        return [self.model.encode(d).tolist() for d in text]
    
    def embed_query(self,query : str):
        return self.model.encode([query])[0].tolist()


