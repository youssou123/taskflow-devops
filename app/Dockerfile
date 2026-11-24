# Étape 1 : Builder (installation des dépendances)
FROM python:3.12-slim AS builder
WORKDIR /build
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

# Étape 2 : Runtime (image finale légère)
FROM python:3.12-slim
RUN useradd -m appuser
WORKDIR /app

# On copie uniquement les paquets installés depuis l'étape 1
COPY --from=builder /root/.local /home/appuser/.local
COPY main.py .

ENV PATH=/home/appuser/.local/bin:$PATH
USER appuser
EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]