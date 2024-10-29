FROM python:3.12-slim

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    default-libmysqlclient-dev \
    pkg-config && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt 

COPY . .

EXPOSE 8501  

ENV PYTHONPATH=/app:/rdbms

CMD ["streamlit", "run", "app/app.py"]