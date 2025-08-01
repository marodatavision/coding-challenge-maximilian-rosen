from langchain_openai import OpenAIEmbeddings
from app.core.models.document_chunk import DocumentChunk
from app.config import settings


embeddings_model = OpenAIEmbeddings(openai_api_key=settings.openai_api_key)

def embed_chunks(chunks: list[DocumentChunk]) -> list[tuple[DocumentChunk, list[float]]]:
    return [(chunk, embeddings_model.embed_query(chunk.text)) for chunk in chunks]
