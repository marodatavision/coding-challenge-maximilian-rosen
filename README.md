# 🔍 RAG-PDF-Suchsystem mit LLM-Unterstützung

Dieses Projekt ist eine prototypische Implementierung einer Retrieval-Augmented-Generation-(RAG)-Anwendung, die es ermöglicht, strukturierte Anfragen gegen einen PDF-Korpus zu stellen. Als LLM kommt die OpenAI API zum Einsatz. Die Anwendung ist vollständig dockerisiert und sofort lauffähig.

---

## 🚀 Schnellstart mit Docker

### 🔧 Voraussetzungen
- Docker
- (Optional) Python 3.11+ & [Poetry](https://python-poetry.org) – nur bei lokalem Setup

---

### 🛠️ Setup

1. **Repository klonen**  
   ```bash
   git clone <repo-url>
   cd <repo-name>
   ```

2. **Umgebungsvariablen setzen**  
   Kopiere die Beispieldatei:
   ```bash
   cp .env.example .env -> linux
   copy .env.example .env -> windows
   ```
   Trage deinen OpenAI API Key in `.env` ein:

   ```env
   OPENAI_API_KEY=sk-...
   ```

3. **Docker starten**

   - **Produktivmodus (CLI-Nutzung):**
     ```bash
     docker compose run --rm rag-prod
     ```

     Beispielabfrage (voreingestellt in `docker-compose.yml`):
     ```text
     Was ist die Farbtemperatur von SIRIUS HRI 330W 2/CS 1/SKU?
     ```

   - **Testmodus:**
     ```bash
     docker compose run --rm rag-test
     ```

---

## 🧪 Beispielanfragen (Teil 2)

| Beispielanfrage                                                                 | Beschreibung                                          |
|----------------------------------------------------------------------------------|--------------------------------------------------------|
| Was ist die Farbtemperatur von SIRIUS HRI 330W 2/CS 1/SKU?                      | Technisches Attribut extrahieren                      |
| Welche Leuchten sind gut für die Ausstattung im Operationssaal geeignet?        | Semantische, kontextbasierte Suche                    |
| Gib mir alle Leuchtmittel mit ≥ 1000 Watt und > 400 Stunden Lebensdauer         | Kriterienbasierte Filterung                          |
| Welche Leuchte hat die primäre Erzeugnisnummer 4062172212311?                   | ID-basierte Suche (Produktdatenbank)                 |

---

## 🗂️ Projektstruktur

```
.
├── .env
├── .env.example
├── .gitignore
├── docker-compose.yml
├── Dockerfile
├── Dockerfile_poetry
├── gdrive_service_account.json.example
├── poetry.lock
├── pyproject.toml
├── README.md
├── tree_structur.txt
├── .pytest_cache/
│   ├── .gitignore
│   ├── CACHEDIR.TAG
│   ├── README.md
│   └── v/
│       └── cache/
├── app/
│   ├── config.py
│   ├── __init__.py
│   ├── adapters/
│   │   ├── io/
│   │   ├── llm/
│   │   └── vectorstore/
│   ├── core/
│   │   ├── interfaces/
│   │   └── models/
│   ├── entrypoints/
│   │   └── cli.py
│   ├── services/
│   └── __pycache__/
├── data/
│   └── pdfs/
│       ├── ZMP_1004795.pdf
│       ├── ZMP_1006242.pdf
│       ├── ZMP_1006707.pdf
│       └── ...
├── tests/
│   ├── adapters/
│   ├── core/
│   └── services/
```

---

## 📈 Skalierung (Antwort zu Teil 3)

Wenn das System auf **10.000+ PDFs** erweitert werden soll, sind folgende Schritte erforderlich:

| Bereich            | Maßnahme                                                                 |
|--------------------|--------------------------------------------------------------------------|
| **Retrieval**      | Einsatz einer Vektordatenbank wie **FAISS**, **Chroma**, **Weaviate**    |
| **Embedding**      | Vorab-Indexierung aller Chunks; Caching von Embeddings                   |
| **Performance**    | Asynchrone Verarbeitung, ggf. Batch-Indexierung & Task-Queues            |
| **Speicherung**    | Nutzung persistenter Backends (z. B. SQLite, FAISS mit On-Disk-Modus)    |
| **Antwortzeit**    | Einsatz von Memory-basierten Indexen + Parallelisierung                  |
| **Horizontale Skalierung** | Aufteilung in Microservices (z. B. PDF-Loader, Retriever, LLM-Caller)   |

---

## 📄 Lizenz und Hinweise

Dieses Projekt wurde im Rahmen einer technischen Challenge entwickelt und ist nicht für den produktiven Einsatz bestimmt. Der Zugriff auf OpenAI-Dienste erfordert einen gültigen API-Key.