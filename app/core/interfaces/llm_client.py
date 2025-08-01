from abc import ABC, abstractmethod
from app.core.models.query import Query
from app.core.models.answer import Answer


class LLMClient(ABC):
    """
    Interface für ein beliebiges Language Model zur Beantwortung von Benutzeranfragen.
    Ermöglicht austauschbare Implementierungen (OpenAI, Local LLM etc.).
    """

    @abstractmethod
    def answer(self, query: Query, context: str) -> Answer:
        """
        Verarbeitet eine Anfrage auf Basis eines gegebenen Kontextes (RAG-Ansatz).

        Args:
            query (Query): Die Nutzerfrage.
            context (str): Der konsolidierte Kontext (aus Vektor-Retrieval).

        Returns:
            Answer: Die erzeugte Antwort.
        """
        pass
