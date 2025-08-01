from abc import ABC, abstractmethod
from typing import List
from core.models.query import Query
from core.models.document_chunk import DocumentChunk


class Retriever(ABC):
    """
    Interface zur Vektorrecherche im RAG-Prozess.
    Implementierungen kapseln z. B. FAISS, Chroma, Pinecone etc.
    """

    @abstractmethod
    def retrieve(self, query: Query, top_k: int = 5) -> List[DocumentChunk]:
        """
        Sucht die relevantesten Chunks zum gegebenen Query.

        Args:
            query (Query): Die Anfrage des Nutzers.
            top_k (int): Anzahl der zu ladenden ähnlichsten Chunks.

        Returns:
            List[DocumentChunk]: Relevante Abschnitte aus dem Dokumentenbestand.
        """
        pass
