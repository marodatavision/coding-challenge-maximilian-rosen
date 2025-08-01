import pytest
from app.core.models.query import Query
from app.core.models.answer import Answer
from app.core.models.document_chunk import DocumentChunk
from app.core.interfaces.llm_client import LLMClient
from app.core.interfaces.retriever import Retriever
from app.services.query_service import QueryService


class MockRetriever(Retriever):
    def retrieve(self, query: Query, top_k: int = 5):
        return [
            DocumentChunk(text="SIRIUS HRI 330W hat 1500 Stunden Lebensdauer.", metadata={"seite": "23"}),
            DocumentChunk(text="Ideal für Operationssäle sind Halogen-Metalldampflampen.", metadata={"seite": "42"}),
        ]


class MockLLMClient(LLMClient):
    def answer(self, query: Query, context: str):
        return Answer(text=f"Mock-Antwort basierend auf Kontext:\n{context[:60]}...")


def test_query_service_integration():
    # Arrange
    retriever = MockRetriever()
    llm_client = MockLLMClient()
    service = QueryService(retriever, llm_client)
    query = Query(text="Welche Leuchte eignet sich für den OP-Saal?")

    # Act
    answer = service.run(query)

    # Assert
    assert isinstance(answer, Answer)
    assert "Mock-Antwort" in answer.text
    assert "Operationssäle" in answer.text or "SIRIUS" in answer.text
