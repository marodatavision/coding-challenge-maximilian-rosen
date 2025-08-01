import pytest
from unittest.mock import patch, MagicMock
from app.core.models.document_chunk import DocumentChunk
from app.services.embedding_service import embed_chunks


@pytest.fixture
def dummy_chunks():
    return [
        DocumentChunk(text="Das ist Chunk 1", metadata={"source": "doc1.pdf"}),
        DocumentChunk(text="Das ist Chunk 2", metadata={"source": "doc1.pdf"}),
    ]


def test_embed_chunks_with_mock(dummy_chunks):
    fake_embeddings = [[0.1] * 1536, [0.2] * 1536]  # Beispiel: GPT-3.5 Embedding Länge

    with patch("app.services.embedding_service.OpenAIEmbeddings") as MockEmb:
        mock_instance = MagicMock()
        mock_instance.embed_documents.return_value = fake_embeddings
        MockEmb.return_value = mock_instance

        result = embed_chunks(dummy_chunks)

    assert len(result) == 2
    assert isinstance(result[0], tuple)
    assert isinstance(result[0][0], DocumentChunk)
    assert isinstance(result[0][1], list)
    assert len(result[0][1]) == 1536
