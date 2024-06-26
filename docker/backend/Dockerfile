FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY src/requirements.txt .

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

COPY src/ .
COPY docker/backend/ /

RUN chmod +x /wsgi-entrypoint.sh
RUN chmod +x /celery.sh
