from app.core.models.document import Document
from pypdf import PdfReader
from pathlib import Path

def load_local_documents(path: str = "data/pdfs") -> list[Document]:
    documents = []
    for file in Path(path).rglob("*.pdf"):
        reader = PdfReader(str(file))
        text = "\n".join(page.extract_text() or "" for page in reader.pages)
        documents.append(Document(text=text, metadata={"source": str(file)}))
    return documents
