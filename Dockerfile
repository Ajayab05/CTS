# ---------- Builder Stage ----------
FROM python:3.12-slim AS builder

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --upgrade pip

RUN pip install --prefix=/install --no-cache-dir -r requirements.txt

# ---------- Runtime Stage ----------
FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN groupadd -r flask && useradd -r -g flask flask

COPY --from=builder /install /usr/local

COPY . .

RUN chown -R flask:flask /app

USER flask

EXPOSE 5000

CMD ["gunicorn","-c","gunicorn.conf.py","app:app"]
