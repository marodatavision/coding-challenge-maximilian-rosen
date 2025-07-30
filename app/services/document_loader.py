from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from core.models import DocumentChunk

def load_and_split(pdf_path: str):
    loader = PyPDFLoader(pdf_path)
    docs = loader.load()
    splitter = RecursiveCharacterTextSplitter(chunk_size=settings.chunk_size, chunk_overlap=settings.overlap)
    chunks = splitter.split_documents(docs)
    return [DocumentChunk(text=ch.page_content, metadata=ch.metadata) for ch in chunks]
