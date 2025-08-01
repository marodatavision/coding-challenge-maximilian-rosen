# Basisimage
FROM python:3.11-slim

# Systempakete installieren
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    git \
    libpoppler-cpp-dev \
    && rm -rf /var/lib/apt/lists/*

# Arbeitsverzeichnis
WORKDIR /app

# Poetry installieren
RUN curl -sSL https://install.python-poetry.org | python3 - \
    && ln -s /root/.local/bin/poetry /usr/local/bin/poetry

# Projektdateien kopieren (nur für Dependency-Auflösung)
COPY pyproject.toml poetry.lock ./

# Dependencies installieren (ohne Dev-Tools, wenn prod-Image)
RUN poetry install --no-root

# Quellcode kopieren
COPY . .

# Standardbefehl (Testmodus als default)
CMD ["poetry", "run", "pytest", "--maxfail=3", "--disable-warnings", "-q"]
