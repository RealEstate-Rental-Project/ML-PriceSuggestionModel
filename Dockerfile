# Image Python légère
FROM python:3.10-slim

WORKDIR /app

# Installation des dépendances système
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Installation des dépendances Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copie du code source
COPY . .

# AJOUT CRUCIAL : Résolution des imports pour les dossiers daily/ et monthly/
ENV PYTHONPATH="${PYTHONPATH}:/app"

# Exposition du port standard FastAPI
EXPOSE 8000

# Lancement de l'application
CMD ["python", "main.py"]
