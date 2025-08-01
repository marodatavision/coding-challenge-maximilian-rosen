import pytest
from app.core.models.query import Query
from app.core.models.answer import Answer
from app.core.models.document_chunk import DocumentChunk
from app.core.interfaces.llm_client import LLMClient
from app.core.interfaces.retriever import Retriever
from app.services.query_service import QueryService


# ✅ Mocks
class MockRetriever(Retriever):
    def retrieve(self, query: Query, top_k: int = 5):
        return [
            DocumentChunk(text="SIRIUS HRI 330W hat 1500 Stunden Lebensdauer.", metadata={"seite": "23"}),
            DocumentChunk(text="Gut geeignet für OPs sind Halogenlampen.", metadata={"seite": "12"}),
        ]


class MockLLMClient(LLMClient):
    def answer(self, query: Query, context: str):
        return Answer(text=f"[MOCK-ANTWORT] Kontext:\n{context[:40]}...")


@pytest.fixture
def service():
    return QueryService(retriever=MockRetriever(), llm_client=MockLLMClient())


# 🧪 TESTFÄLLE

def test_normaler_query(service):
    query = Query(text="Welche Leuchte eignet sich für OP-Säle?")
    answer = service.run(query)
    assert isinstance(answer, Answer)
    assert "MOCK-ANTWORT" in answer.text


def test_leerer_query(service):
    query = Query(text="")
    answer = service.run(query)
    assert "MOCK-ANTWORT" in answer.text  # weil LLM mock ist, kein echter Fehler
    assert len(answer.text) > 0


def test_extrem_langer_query(service):
    query = Query(text="Was ist das?" * 1000)
    answer = service.run(query)
    assert "MOCK-ANTWORT" in answer.text
    assert len(answer.text) > 10


def test_retriever_liefert_nichts():
    class EmptyRetriever(Retriever):
        def retrieve(self, query: Query, top_k: int = 5):
            return []

    service = QueryService(retriever=EmptyRetriever(), llm_client=MockLLMClient())
    query = Query(text="Was ist die Lebensdauer?")
    answer = service.run(query)
    assert "MOCK-ANTWORT" in answer.text
    assert "[MOCK-ANTWORT]" in answer.text


def test_llm_liefert_leere_antwort():
    class SilentLLM(LLMClient):
        def answer(self, query: Query, context: str):
            return Answer(text="")

    service = QueryService(retriever=MockRetriever(), llm_client=SilentLLM())
    query = Query(text="Was ist die Lebensdauer?")
    answer = service.run(query)
    assert isinstance(answer, Answer)
    assert answer.text == ""
