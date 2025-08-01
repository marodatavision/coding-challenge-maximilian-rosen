# Dockerfile für RAG App mit Testfunktionalität
FROM python:3.11-slim

# Systempakete für PDF-Verarbeitung & Build
RUN apt-get update && apt-get install -y \
    build-essential \
    libpoppler-cpp-dev \
    && rm -rf /var/lib/apt/lists/*

# Arbeitsverzeichnis
WORKDIR /app

# Abhängigkeiten
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Entwicklungs-Tools (z. B. pytest)
RUN pip install pytest

# Quellcode
COPY . .

# Default-Befehl: Tests ausführen
CMD ["pytest", "--maxfail=3", "--disable-warnings", "-q"]
