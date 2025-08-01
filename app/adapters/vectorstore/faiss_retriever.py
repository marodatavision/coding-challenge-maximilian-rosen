from typing import List
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.schema.document import Document
from core.interfaces.retriever import Retriever
from core.models.query import Query
from core.models.document_chunk import DocumentChunk
from app.config import settings


class FAISSRetriever(Retriever):
    """
    Konkrete Implementierung des Retriever-Interfaces mit FAISS.
    Baut bei Instanziierung einen FAISS-Vektorindex aus übergebenen Chunks.
    """

    def __init__(self, chunks: List[DocumentChunk]):
        self.embeddings = OpenAIEmbeddings(openai_api_key=settings.openai_api_key)

        docs = [
            Document(page_content=chunk.text, metadata=chunk.metadata)
            for chunk in chunks
        ]

        self.store = FAISS.from_documents(documents=docs, embedding=self.embeddings)

    def retrieve(self, query: Query, top_k: int = 5) -> List[DocumentChunk]:
        """
        Sucht die relevantesten Chunks basierend auf semantischer Ähnlichkeit.
        """

        results = self.store.similarity_search(query.text, k=top_k)

        return [
            DocumentChunk(text=doc.page_content, metadata=doc.metadata or {})
            for doc in results
        ]
