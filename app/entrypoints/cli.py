import sys
from dotenv import load_dotenv

from app.config import settings
from app.services.document_loader import load_and_split
from app.services.embedding_service import embed_chunks
from app.services.query_service import QueryService
from app.adapters.vectorstore.faiss_retriever import FAISSRetriever
from app.adapters.llm.openai_client import OpenAIClient
from app.core.models.query import Query

def main():
    load_dotenv()

    if len(sys.argv) < 2:
        print("❗ Usage: python app/entrypoints/cli.py <deine frage>")
        sys.exit(1)

    user_question = " ".join(sys.argv[1:])

    print(f"🔍 Lade und verarbeite Dokumente ...")
    chunks = load_and_split()

    if not chunks:
        print("❗ Es wurden keine Dokumente gefunden oder verarbeitet.")
        sys.exit(1)

    print(f"📦 Erstelle Embeddings ...")
    #embedded_chunks = embed_chunks(chunks)

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
