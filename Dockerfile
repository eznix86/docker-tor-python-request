FROM python:3.9

ENV PYTHONUNBUFFERED=1

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    netcat && \ 
    rm -rf /var/lib/apt/lists/*

WORKDIR /code
# Install dependencies:

COPY requirements.txt /code/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt