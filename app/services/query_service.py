from app.core.interfaces.llm_client import LLMClient
from app.core.interfaces.retriever import Retriever
from app.core.models.query import Query
from app.core.models.answer import Answer


class QueryService:
    """
    Koordiniert den RAG-Prozess:
    1. Dokumentrecherche (Retriever)
    2. Antwortgenerierung (LLMClient)
    """

    def __init__(self, retriever: Retriever, llm_client: LLMClient):
        self.retriever = retriever
        self.llm_client = llm_client

    def run(self, query: Query) -> Answer:
        """
        Führt einen Query aus: Suche + Antwortgenerierung
        """
        chunks = self.retriever.retrieve(query)
        context = "\n\n".join([chunk.text for chunk in chunks])
        return self.llm_client.answer(query, context)
