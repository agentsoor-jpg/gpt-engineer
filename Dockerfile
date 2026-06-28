FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y git curl && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip

RUN pip install gpt-engineer fastapi uvicorn python-multipart

COPY app.py /app/app.py

RUN mkdir -p /app/projects

EXPOSE 8000

CMD ["sh", "-c", "uvicorn app:app --host 0.0.0.0 --port ${PORT:-8000}"]
