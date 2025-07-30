from langchain.embeddings import OpenAIEmbeddings
from core.models import DocumentChunk

embeddings_model = OpenAIEmbeddings(openai_api_key=settings.openai_api_key)

def embed_chunks(chunks: list[DocumentChunk]) -> list[tuple[DocumentChunk, list[float]]]:
    return [(chunk, embeddings_model.embed_query(chunk.text)) for chunk in chunks]
