from langchain.vectorstores import FAISS
from core.models import DocumentChunk

def build_store(chunk_embeddings: list[tuple[DocumentChunk, list[float]]]):
    texts = [c.text for c,_ in chunk_embeddings]
    embs = [emb for _,emb in chunk_embeddings]
    store = FAISS.from_embeddings(embs, texts)
    return store

def retrieve(store, query: str, k: int = 5):
    results = store.similarity_search(query, k=k)
    return results
