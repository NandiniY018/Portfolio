FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        gcc \
        default-libmysqlclient-dev \
        pkg-config \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/
# Convert UTF-16 requirements.txt if needed (sometimes powershell saves it that way)
RUN iconv -f UTF-16LE -t UTF-8 requirements.txt > requirements_utf8.txt || cp requirements.txt requirements_utf8.txt
RUN pip install --no-cache-dir -r requirements_utf8.txt
RUN pip install redis celery

COPY . /app/
