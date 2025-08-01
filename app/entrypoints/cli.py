import os
import sys
from dotenv import load_dotenv

from app.config import settings
from services.document_loader import load_and_split
from services.embedding_service import embed_chunks
from services.query_service import QueryService
from adapters.vectorstore.faiss_retriever import FAISSRetriever
from adapters.llm.openai_client import OpenAIClient
from core.models.query import Query


def main():
    load_dotenv()

    if len(sys.argv) < 3:
        print("❗ Usage: python app/entrypoints/cli.py <pdf_folder> <deine frage>")
        sys.exit(1)

    pdf_folder = sys.argv[1]
    user_question = " ".join(sys.argv[2:])

    print(f"🔍 Lade Dokumente aus: {pdf_folder} ...")
    chunks = []
    for fname in os.listdir(pdf_folder):
        if fname.lower().endswith(".pdf"):
            chunks.extend(load_and_split(os.path.join(pdf_folder, fname)))

    print(f"📦 Erstelle Embeddings ...")
    embedded_chunks = embed_chunks(chunks)

    print(f"⚙️ Initialisiere Komponenten ...")
    retriever = FAISSRetriever(chunks=chunks)
    llm = OpenAIClient()
    query_service = QueryService(retriever, llm)

    print(f"💬 Sende Anfrage an das System ...")
    query = Query(text=user_question)
    answer = query_service.run(query)

    print("\n✅ Antwort:\n")
    print(answer.text)
    if answer.sources:
        print("\n🔗 Quellen:")
        for src in answer.sources:
            print(f"- {src}")


if __name__ == "__main__":
    main()
