import sys
from services.document_loader import load_and_split
from services.embedding_service import embed_chunks
from services.query_service import answer_query
import os

def main():
    if len(sys.argv) < 3:
        print("Usage: python cli.py <pdf_folder> <query>")
        sys.exit(1)
    pdf_folder = sys.argv[1]
    query = " ".join(sys.argv[2:])
    chunks = []
    for fname in os.listdir(pdf_folder):
        if fname.lower().endswith(".pdf"):
            chunks.extend(load_and_split(os.path.join(pdf_folder, fname)))
    emb = embed_chunks(chunks)
    answer = answer_query(emb, query)
    print("Antwort:", answer)

if __name__ == "__main__":
    main()
