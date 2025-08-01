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

    print("\n🟢 Starte Chat. Gib 'exit' ein, um zu beenden.\n")

    while True:
        user_input = input("💬 Deine Frage: ").strip()
        if user_input.lower() in {"exit", "quit"}:
            print("👋 Bis zum nächsten Mal!")
            break

        if not user_input:
            continue

        query = Query(text=user_input)
        answer = query_service.run(query)

        print("\n✅ Antwort:\n")
        print(answer.text)

        if answer.sources:
            print("\n🔗 Quellen:")
            for src in answer.sources:
                print(f"- {src}")
        print("\n" + "-" * 60 + "\n")


if __name__ == "__main__":
    main()
