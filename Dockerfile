FROM python:3.9-slim-buster

ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    libjpeg-dev \
    libfreetype6-dev \
    libssl-dev \
    libxml2-dev \
    libxslt1-dev \
    libldap2-dev \
    libsasl2-dev \
    netcat

RUN mkdir /code
WORKDIR /code

COPY requirements.txt /code/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /code/DjangoREST/

WORKDIR /code/DjangoREST/pollsapi

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]