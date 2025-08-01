from app.core.models.document import Document
from app.core.models.document_chunk import DocumentChunk
from typing import List

def chunk_documents(documents: List[Document], chunk_size: int = 500) -> List[DocumentChunk]:
    chunks = []

    for doc in documents:
        text = doc.text
        metadata = doc.metadata

        # Einfache Split-Strategie: feste Zeichenzahl
        for i in range(0, len(text), chunk_size):
            chunk_text = text[i:i+chunk_size]
            chunk = DocumentChunk(text=chunk_text, metadata=metadata)
            chunks.append(chunk)

    return chunks
